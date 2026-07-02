# Arquitetura do Harness Figma + Claude Code — Documento Didático

Este documento explica, de forma consolidada, como e por que o harness
de design determinístico foi estruturado. O objetivo é servir de
referência de leitura — não é o manual operacional (esse é o
`README.md` do projeto), é o "porquê por trás de cada decisão".

---

## 1. O problema que este harness resolve

Design systems reais, com o tempo, acumulam inconsistência: componentes
duplicados, nomenclatura solta, tokens usados de forma diferente em
lugares parecidos. Quando se tenta automatizar a criação de telas com
IA sobre uma base assim, dois riscos aparecem:

1. **Alucinação de componente** — o modelo "acha" que um elemento é
   parecido o suficiente com outro e o reusa errado, ou pior, cria um
   componente novo quando já existia um equivalente.
2. **Perda de coerência entre telas** — numa jornada de várias telas
   conectadas, cada tela pode resolver o mesmo tipo de elemento de um
   jeito diferente, porque não há memória entre as construções.

O harness existe para transformar essas decisões — que hoje vivem
implícitas na cabeça de quem desenha — em um **processo explícito,
auditável e repetível**.

---

## 2. Separação fundamental: motor vs. conteúdo

A primeira decisão estrutural foi separar o que é **igual para
qualquer cliente** do que é **específico de cada projeto**.

```
figma-harness/
├── CLAUDE.md          ← motor: regras universais de processo
├── .claude/agents/     ← motor: os 5 subagentes especializados
├── skills/             ← motor: procedimentos reutilizáveis
└── projects/
    └── cliente-x/       ← conteúdo: design system, memória, jornadas
```

Por que isso importa: se você aprende algo que melhora o *processo* de
interpretar wireframes, isso vira uma melhoria no `interpreter.md`
compartilhado — todo cliente se beneficia. Se você aprende algo sobre o
design system de um cliente específico, isso fica isolado dentro da
pasta daquele projeto e nunca vaza para outro cliente.

Essa separação é o que permite operar múltiplos clientes com o mesmo
harness sem misturar contexto entre eles.

---

## 3. Por que multi-agentes, e não um agente genérico fazendo tudo

A tentação inicial seria ter um único agente fazendo "leia o wireframe
e construa a tela". O problema é que isso mistura duas responsabilidades
que precisam ser separáveis: **decidir** o que construir e **executar**
a construção.

Se o mesmo agente decide e executa na mesma respiração, não existe
ponto de checagem no meio — um erro de interpretação vira
automaticamente um erro de execução, sem chance de você revisar antes.

Por isso o harness usa 5 agentes com escopo de acesso restrito:

| Agente | Decide ou executa? | Acesso |
|---|---|---|
| **interpreter** | Decide o quê construir | Só leitura |
| **builder** | Executa o que foi decidido | Escrita no Figma |
| **documenter** | Registra o que foi construído | Escrita em arquivos `.md` |
| **auditor** | Verifica consistência técnica | Só leitura |
| **validator** | Verifica se o resultado cumpre o objetivo | Só leitura |

Uma regra importante do Claude Code reforça essa separação de forma
técnica, não só organizacional: **subagentes não conseguem confirmar
prompts de aprovação interativos**. Isso significa que qualquer
ferramenta de escrita usada por um subagente é tratada como ação que
precisa ser explicitamente permitida com antecedência — não pode haver
uma aprovação "no meio do caminho". Essa restrição técnica é, na
prática, o que valida a separação decisão/execução: o `interpreter` (só
leitura) nunca esbarra nesse problema; o `builder` (escrita) é
desenhado desde o início sabendo que vai operar sem parar para pedir
confirmação no meio.

Outro detalhe técnico que molda o desenho: **subagentes não conversam
entre si diretamente**. Cada um reporta apenas ao agente principal (a
sessão onde você está conversando). Por isso o fluxo nunca é
"interpreter aciona builder" — é sempre "interpreter reporta para você
→ você aprova → você aciona builder".

---

## 4. O fluxo completo de uma jornada

Uma jornada é uma sequência de telas conectadas (ex: carrinho → endereço
→ confirmação), sempre acompanhada de uma história do usuário que
explica o objetivo por trás dela.

```
 wireframe (imagens/PDF do Miro)
        +
 história do usuário (texto)
        │
        ▼
┌───────────────┐
│  interpreter    │  Lê os dois insumos + o design-system atual.
│                 │  Para cada elemento de cada tela, decide:
│                 │  REUSO DIRETO / NOVA VARIANTE / COMPONENTE NOVO
└───────┬─────────┘
        │ plano estruturado
        ▼
   [ aprovação humana ]
        │
        ▼
┌───────────────┐
│    builder      │  Constrói UMA tela por vez, via MCP no Figma.
│  (por tela)     │  Recebe o estado das telas já construídas antes
│                 │  de cada nova tela, para manter consistência.
└───────┬─────────┘
        │ relatório do que foi construído
        ▼
  (repete para cada tela da jornada)
        │
        ▼
┌───────────────┐
│   validator     │  Só roda depois de TODAS as telas prontas.
│                 │  Compara o resultado final contra a história do
│                 │  usuário, o wireframe original, e verifica
│                 │  coerência entre as telas da jornada.
└───────┬─────────┘
        │ relatório de validação
        ▼
   [ aprovação humana ]
        │
        ▼
┌───────────────┐
│  documenter     │  Só agora promove componentes novos/variantes
│                 │  de rascunho para o design system oficial.
└─────────────────┘
```

### Por que o validator vem antes do documenter, e não depois do builder

Essa é uma decisão de ordem que parece pequena, mas evita um problema
sério: se o `documenter` registrasse um componente novo no design
system logo após o `builder` criá-lo — antes de qualquer validação
semântica — corre-se o risco de **oficializar um componente que nasceu
de uma interpretação errada do wireframe**. Uma vez oficial, esse
componente passaria a ser oferecido como opção de reuso em tarefas
futuras, propagando o erro.

Por isso existe um estágio intermediário: componentes novos entram
primeiro em `design-system/components/_draft/` (rascunho) — existem no
Figma e estão documentados, mas **não são oferecidos pelo interpreter
como opção de reuso** até serem promovidos para a pasta oficial, o que
só acontece depois da aprovação do validator.

---

## 5. Como a decisão de reuso é tomada

Esta é provavelmente a parte mais importante do harness — é o que
evita a duplicação de componentes que você já vê hoje nos projetos
legados.

Para cada elemento do wireframe, o `interpreter` avalia três camadas de
correspondência contra os componentes já documentados:

1. **Estrutural** — o elemento tem a mesma composição interna (mesmos
   sub-elementos, na mesma disposição) que um componente existente?
2. **Funcional** — tem o mesmo propósito dentro da jornada?
3. **Variante coberta** — a diferença encontrada (um estado, um
   conteúdo diferente) já existe como variante documentada, ou é nova?

O resultado dessa avaliação sempre cai em uma de três categorias, e o
`interpreter` é obrigado a listar quais componentes existentes foram
considerados e por que foram descartados — essa lista fica visível no
plano, para você aprovar ou corrigir antes de qualquer construção.

```
REUSO DIRETO         → usa o componente como está
NOVA VARIANTE         → mesmo componente, adiciona uma variante nova
COMPONENTE NOVO       → nenhuma correspondência real encontrada
```

Essa disciplina só funciona porque existe um **template fixo de
documentação de componente** (`_TEMPLATE.md`), com campos específicos
como "Quando NÃO usar" e "Componentes relacionados" — são exatamente
esses campos que o interpreter consulta para decidir se um candidato
serve ou não.

---

## 6. Por que cada componente precisa de um "manual de como foi feito"

Documentar o *que* um componente é (nome, variantes, tokens) não
basta — também é preciso garantir que ele foi *construído* de um jeito
que permite ao modelo (e ao MCP) reconhecê-lo de forma confiável. Por
isso existe o `COMPONENT_STANDARDS.md`, com regras como:

- Nomenclatura por função, não por aparência (`Card/Product`, nunca
  `Card/Blue`)
- Diferenças de estado viram **variantes** do mesmo componente, nunca
  componentes separados
- Nenhum valor de cor, espaçamento ou tipografia pode estar
  "hardcoded" — sempre vinculado a um token
- Componentes aninhados precisam ser instâncias vinculadas, nunca
  cópias soltas
- Uso obrigatório de Auto Layout — sem isso, a extração de estrutura
  via MCP fica ambígua

Esse documento é o que torna os componentes **legíveis** para o
harness. Sem ele, mesmo com boa documentação em `.md`, o Figma real
poderia estar construído de um jeito que o MCP não consegue interpretar
de forma confiável.

---

## 7. Mantendo a coerência dentro de uma jornada multi-tela

Cada chamada ao `builder` roda de forma isolada — ele não tem memória
automática do que foi construído na tela anterior da mesma jornada.
Isso poderia gerar um problema real: o mesmo tipo de elemento sendo
resolvido de formas diferentes em telas diferentes da mesma jornada.

A solução é um arquivo vivo, `journey-state.md`, que funciona como a
"memória de curto prazo" da jornada:

```
1. builder constrói a tela 1 → relata o que fez em texto
2. você (ou a sessão principal) registra esse relato no journey-state.md
3. builder é chamado de novo para a tela 2, recebendo o journey-state.md
   atualizado como parte do contexto
4. repete até a última tela
```

Importante: quem escreve nesse arquivo é a **sessão principal**, não o
`builder` — isso mantém o builder com escopo mínimo (só ferramentas de
escrita no Figma), sem misturar responsabilidade de editar arquivos do
harness.

---

## 8. As duas camadas de verificação: auditor vs. validator

É fácil confundir os dois, mas eles verificam coisas fundamentalmente
diferentes:

| | Auditor | Validator |
|---|---|---|
| Pergunta que responde | "Está bem construído?" | "É a coisa certa?" |
| Compara contra | Padrões técnicos (`COMPONENT_STANDARDS.md`) | Objetivo da jornada (`user-story.md`) |
| Quando roda | Início de sessão / sob demanda | Só depois de TODA a jornada construída |
| Detecta | Tokens hardcoded, nomenclatura errada, duplicatas | Escopo faltando, escopo inflado, incoerência entre telas |
| Modelo usado | Sonnet (verificação mais mecânica) | Opus (julgamento semântico fino) |

A escolha de usar Opus especificamente no validator não é acidental —
é o único ponto do harness onde um erro de julgamento tem custo alto:
deixar passar uma tela que não cumpre o objetivo da jornada, ou não
perceber uma quebra de coerência entre duas telas conectadas, é o tipo
de erro sutil que exige mais capacidade de raciocínio para pegar.

---

## 9. Isolamento e segurança entre clientes

Como a conta Figma é corporativa única, com os projetos de cada cliente
organizados internamente dentro dela, o isolamento entre clientes **não
é feito por credencial separada** — é feito por configuração:

- Um único token de API vive no `.env` global
- Cada projeto tem um `PROJECT.md` declarando explicitamente o
  `file-key` do Figma daquele cliente
- Antes de qualquer operação de escrita, o `builder` confirma que o
  destino corresponde ao `file-key` declarado — se não corresponder,
  para e alerta, nunca prossegue

Isso significa que a proteção contra "escrever no projeto errado" é uma
regra de processo (verificação obrigatória antes de escrever), não uma
barreira técnica de permissão — o que é suficiente dado que há um único
token, mas exige disciplina de sempre declarar o `PROJECT.md` corretamente
antes de operar em um cliente novo.

Já `memory/` (decisões, aprendizados, changelog) é sempre isolada por
projeto — nunca compartilhada entre clientes, por razão de
confidencialidade.

---

## 10. Memória: por que arquivos, não "lembrança"

O Claude não retém nada entre sessões por padrão — cada nova conversa
começa do zero. Por isso, tudo que precisa persistir no harness vira
**arquivo versionado**, nunca contexto implícito de conversa:

- `memory/decisions.md` — registra decisões não-óbvias (ex: "usar
  variante ghost, não destructive, por pedido do cliente") para não
  repetir a mesma correção em sessões futuras
- `memory/learnings.md` — padrões que se repetem e merecem virar regra
  permanente
- `memory/component-changelog.md` — histórico cronológico de criação e
  alteração de componentes oficiais

Isso transforma cada correção feita hoje em uma regra que evita o mesmo
erro amanhã, em vez de depender de alguém lembrar manualmente.

---

## 11. O que foi deixado conscientemente fora do escopo (v1)

Nem toda lacuna identificada precisa ser resolvida agora. Algumas
decisões foram adiadas de propósito, com o trade-off já registrado:

- **Onboarding de design systems legados e desorganizados** — tratado
  como projeto totalmente separado, com processo próprio de varredura
  e negociação iterativa com o humano, porque tem cadência e risco
  muito diferentes do uso do dia a dia do harness.
- **Rollback automatizado no Figma** — reversão é manual via histórico
  nativo do Figma; o estágio rascunho/oficial já reduz bastante a
  necessidade disso.
- **Múltiplos aprovadores** — por ora, um único humano aprova; o campo
  já existe nos registros para facilitar expansão futura sem
  retrabalho de formato.
- **Responsividade / breakpoints** — campo já previsto no template de
  componente, mas sem processo funcional até haver um caso real que
  exija.
- **Conexão MCP direta com ferramentas de wireframe (Miro)** — por
  ora, wireframes chegam como PDF/imagem exportada, decisão tomada por
  simplicidade; pode ser revisitada se a fricção de reexportar se
  tornar um problema real no uso.

---

## 12. Resumo mental de uma frase por peça

- **CLAUDE.md** — as regras do jogo, válidas para qualquer projeto
- **interpreter** — decide o quê construir, nunca constrói
- **builder** — constrói exatamente o que foi decidido, uma tela por vez
- **documenter** — registra, em dois estágios (rascunho → oficial)
- **auditor** — confere se está tecnicamente correto
- **validator** — confere se é semanticamente a coisa certa
- **journey-state.md** — a memória de curto prazo entre telas de uma jornada
- **memory/** — a memória de longo prazo de um projeto
- **_draft/ → oficial** — o portão que impede erro de interpretação virar parte permanente do design system

---

## Adendo — Onboarding, Preflight e Migração de Legado

As seções acima descrevem o harness de **Produção**. Depois desse
desenho inicial, foram adicionados mais dois escopos para lidar com
projetos Figma legados, mal estruturados: **Onboarding** e
**Preflight**. Ver `CLAUDE.md`, `onboarding/ONBOARDING.md` e
`preflight/PREFLIGHT.md` para o processo completo — aqui vai só o
raciocínio.

### Três escopos, três riscos diferentes

| Escopo | Cadência | Escreve no Figma? |
|---|---|---|
| Onboarding | Uma vez por cliente | Nunca |
| Preflight | Sob demanda, incremental | Sim, só no arquivo novo |
| Produção | Dia a dia | Sim, só no arquivo novo |

O onboarding não podia virar "mais um agente" dentro do ciclo de
produção porque opera num padrão incompatível: varre o arquivo inteiro,
negocia com você em várias rodadas, e roda raramente — bem diferente do
ciclo rápido "plano → aprovação → execução pontual" da produção.

### Dois arquivos Figma — Legado e Produção

O legado nunca é editado. Um arquivo novo, criado pelo preflight, nasce
já limpo e é o único destino de escrita do harness dali em diante. Isso
evita "consertar em cima do estrago" — decisão explicitamente preferida
a reformar o arquivo antigo no lugar.

### Migração incremental, não big-bang

Reconstruir todo o legado de uma vez arriscaria gastar esforço em
componentes que nunca mais seriam usados. Em vez disso, cada componente
só é reconstruído (preflight) quando uma jornada de produção real
precisa dele — o `interpreter` sinaliza isso com uma quarta categoria
de classificação, `MIGRAR DO LEGADO`, além das três originais (reuso
direto, nova variante, componente novo).

### Duas memórias que não podem se confundir

- `journey-state.md` — memória de curto prazo, vale só durante UMA
  jornada, para as telas dela se manterem coerentes entre si
- Campo `Status` em `components/[nome].md` — memória de longo prazo,
  permanente, é o que qualquer jornada FUTURA consulta para saber se
  um componente já foi migrado

Colocar status de migração dentro do `journey-state.md` o tornaria
invisível para jornadas futuras não relacionadas — por isso vive no
componente, não na jornada.

### Telas são cópias, não instâncias

Componente/instância do Figma existe para elementos que se repetem
(Button, Card) — não para telas inteiras, que são por definição únicas.
Telas são sempre frames duplicados. O arquivo de Produção tem duas
páginas fixas: `Telas Atuais` (fonte de verdade do estado vigente de
cada tela) e `Jornadas` (histórico cronológico de trabalho, uma página
por demanda — o modelo que já era usado antes de existir este harness).

### A limitação real do Linux

O harness usa `figma-console-mcp` em vez do MCP oficial do Figma. Isso
resolve leitura completamente (modo Remote SSE, sem nenhuma dependência
de app desktop) — cobre `interpreter`, `auditor`, `validator` e os
agentes de onboarding. Mas **nenhum MCP disponível hoje remove a
exigência do Figma Desktop app para escrita** — que não tem build
oficial para Linux. Por isso `builder` e `preflight-builder` dependem
de uma VM Windows, Wine, ou acesso ocasional a uma máquina Mac/Windows.
