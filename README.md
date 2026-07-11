# Figma Design Harness — Claude Code

Harness de **design determinístico** para Figma: um processo explícito,
auditável e repetível para construir telas e design systems no Figma
usando Claude Code + subagentes especializados, conectados ao Figma via
MCP. Nada é construído sem um plano aprovado por humano; nenhuma decisão
de design fica implícita.

---

## O que este projeto é (e o problema que resolve)

Design systems reais, com o tempo, acumulam inconsistência: componentes
duplicados, nomenclatura solta, tokens usados de forma diferente em
lugares parecidos. Quando se tenta automatizar a criação de telas com
IA em cima de uma base assim, dois riscos aparecem:

1. **Alucinação de componente** — o modelo "acha" que um elemento é
   parecido o suficiente com outro e o reusa errado, ou cria um
   componente novo quando já existia um equivalente.
2. **Perda de coerência entre telas** — numa jornada de várias telas
   conectadas, cada tela pode resolver o mesmo tipo de elemento de um
   jeito diferente, porque não há memória entre as construções.

Este harness resolve isso com quatro princípios:

- **Separação decisão vs. execução** — quem decide o que construir
  (agentes de planejamento, só leitura) nunca é quem constrói (agentes
  de execução, escrita no Figma). Entre um e outro, sempre há um ponto
  de aprovação humana.
- **Classificação obrigatória antes de construir** — todo elemento de
  wireframe é classificado como REUSO DIRETO / NOVA VARIANTE /
  COMPONENTE NOVO / MIGRAR DO LEGADO, com os candidatos descartados
  listados no plano. É isso que impede duplicação silenciosa.
- **Legado intocável** — cada cliente tem dois arquivos Figma: o
  **Legado** (antigo, bagunçado, somente leitura, usado como
  referência) e o de **Produção** (novo, limpo, único destino de
  escrita). Nenhum agente escreve no Legado, nunca.
- **Memória em arquivos versionados** — decisões, aprendizados e o
  estado do design system vivem em `.md` no repositório, não na
  "lembrança" de uma conversa. Cada correção de hoje vira regra que
  evita o mesmo erro amanhã.

Leia `arquitetura-harness-figma.md` para o raciocínio completo por trás
de cada decisão de desenho. Este README é o guia operacional; as regras
universais de processo estão em `CLAUDE.md`.

---

## Casos de uso — "estou nesta situação, uso o quê?"

| Situação | Módulo / caminho |
|---|---|
| Cliente novo chegou com um Figma legado bagunçado, nunca mapeado | **Onboarding** (Fluxo 1) — uma vez por cliente |
| Vou desenhar uma jornada/tela nova a partir de wireframe + história do usuário | **Produção** (Fluxo 3) — o ciclo do dia a dia |
| A tela nova precisa de um componente que só existe no arquivo legado | **Preflight** (Fluxo 2) — disparado pelo plano do interpreter (`MIGRAR DO LEGADO`), antes da construção |
| Quero adiantar a migração de componentes prioritários do legado, sem esperar demanda | **Preflight** manual, a partir do `migration-backlog.md` |
| Uma jornada nova envolve reconstruir uma tela que já existe no legado (ex: a Home) | **Produção** com print da tela legada como wireframe — ver `migration/MIGRATION.md` |
| Suspeito que alguém do time do cliente mexeu no Figma por fora do harness | **`auditor`** — checagem de sincronização (recomendado no início de toda sessão) |
| Atendo vários clientes na mesma conta Figma corporativa | Um diretório por cliente em `projects/`, com `PROJECT.md` declarando os arquivos — o isolamento é por configuração |

---

## Os três módulos e seus 10 agentes

O harness é dividido em três módulos (escopos), com cadências e riscos
diferentes. Cada módulo tem seus próprios agentes, e todos seguem a
mesma regra: **nenhum agente aciona outro** — a coordenação passa sempre
pela sessão principal (você + Claude na conversa raiz), que decide
quando delegar e quando pedir aprovação humana.

### Módulo 1 — Onboarding (uma vez por cliente · só leitura no Figma)

Mapeia um Figma legado desconhecido e o transforma em documentação que
os outros módulos conseguem consultar. Roda no início de cada cliente
novo (ou, raramente, numa re-varredura se o legado mudou muito).

| Agente | Quando entra | O que faz | Nunca faz |
|---|---|---|---|
| `onboard-scanner` | 1º — legado nunca mapeado | Varre o arquivo Legado em duas passadas (visual barata → estrutural cirúrgica) e produz o inventário bruto | Julgar, decidir, escrever no Figma |
| `onboard-analyst` | 2º — inventário pronto | Cruza o inventário, identifica suspeitas de duplicata/inconsistência e formula perguntas objetivas para o humano | Decidir sozinho |
| `onboard-writer` | 3º — todas as perguntas respondidas | Gera `design-system/tokens/*.md` e `components/*.md` (`Status: em revisão`) + `migration-backlog.md` | Escrever no Figma; rodar com perguntas pendentes |

Entre o analyst e o writer existe uma etapa humana obrigatória: a
negociação das perguntas, uma por vez, registrada em
`onboarding-decisions.md`.

### Módulo 2 — Preflight (sob demanda, incremental · escreve no arquivo de Produção)

Migra componentes do legado para o arquivo de Produção, **um por vez,
quando uma demanda real precisa deles** — nunca em lote (big-bang). É
também o módulo que cria o arquivo de Produção na primeira execução de
um cliente. "Migrar" aqui significa **reconstruir do zero** seguindo
`COMPONENT_STANDARDS.md`, usando o legado só como referência visual —
nunca copiar a estrutura problemática.

| Agente | Quando entra | O que faz | Nunca faz |
|---|---|---|---|
| `preflight-planner` | Elemento marcado `MIGRAR DO LEGADO`, ou priorização manual do backlog | Lê o componente no Legado e propõe a reconstrução, destacando riscos de drift visual para a aprovação | Reconstruir, escrever no Figma |
| `preflight-builder` | Plano de reconstrução aprovado | Reconstrói no arquivo de Produção (cria o arquivo e a estrutura de páginas na 1ª vez do cliente) | Escrever no Legado; decidir migrar algo fora do aprovado |

Após a reconstrução, o `documenter` (do módulo de Produção) promove o
componente: `Status: em revisão` → `Status: ativo`.

### Módulo 3 — Produção (dia a dia · escreve no arquivo de Produção)

O ciclo recorrente: transformar wireframe + história do usuário em
telas construídas no Figma, com componentes reusados ou criados de
forma controlada.

| Agente | Quando entra | O que faz | Nunca faz |
|---|---|---|---|
| `interpreter` | Início de toda jornada/tela nova | Lê wireframe + user story + design system e propõe o plano, classificando cada elemento (reuso/variante/novo/migrar) com candidatos descartados visíveis | Escrever no Figma; decidir sozinho em ambiguidade |
| `builder` | Plano aprovado, uma invocação por tela | Executa exatamente o plano via MCP; recebe o `journey-state.md` atualizado para manter coerência entre telas | Reinterpretar o plano; continuar após falha parcial; escrever em arquivos do harness |
| `validator` | TODAS as telas da jornada prontas | Compara o resultado contra a história do usuário, o wireframe e a coerência entre telas; gera `validation-report.md` (usa Opus — julgamento semântico fino) | Corrigir ou modificar qualquer coisa |
| `documenter` | Jornada aprovada pelo validator + humano | Promove componentes `_draft/` → oficial e frames aprovados → página "Telas Atuais"; registra tokens novos | Documentar/promover antes da validação |
| `auditor` | Início de cada sessão de trabalho (ou sob suspeita) | Confere consistência técnica do arquivo de Produção contra o `design-system/` documentado: hardcoded, nomenclatura, duplicatas, drift de token | Corrigir automaticamente |

A ordem do fluxo de produção é fixa e existe por um motivo: o
`documenter` vem por último porque oficializar um componente antes da
validação semântica propagaria um erro de interpretação para todas as
jornadas futuras.

```
interpreter → [aprovação humana] → (preflight, se necessário) →
builder (por tela) → validator (jornada completa) →
[aprovação humana] → documenter
```

---

## Estrutura do repositório

```
figma-harness/
├── CLAUDE.md                  # regras universais — leia primeiro
├── arquitetura-harness-figma.md # o "porquê" de cada decisão de desenho
├── onboarding/ONBOARDING.md    # processo do módulo de onboarding
├── preflight/PREFLIGHT.md      # processo do módulo de preflight
├── migration/MIGRATION.md      # variação leve: migrar tela legada
├── mcp-figma/plugin/            # plugin figma-mcp-go já vendorizado
│   ├── manifest.json             # importar direto no Figma Desktop
│   └── dist/                     # code.js / index.html do plugin
├── .claude/agents/             # os 10 subagentes
│   ├── interpreter.md / builder.md / documenter.md / auditor.md /
│   │   validator.md                            ← produção
│   ├── onboard-scanner.md / onboard-analyst.md /
│   │   onboard-writer.md                        ← onboarding
│   └── preflight-planner.md / preflight-builder.md   ← preflight
├── skills/                     # procedimentos reutilizáveis
└── projects/
    └── [nome-do-cliente]/      # um diretório por cliente/projeto
        ├── PROJECT.md            # fileName exato: Legado e Produção
        ├── design-system/        # tokens + components documentados
        ├── memory/               # decisões, aprendizados, changelog
        └── journeys/             # uma pasta por jornada construída
```

Tudo que é **motor** (regras, agentes, skills) é compartilhado entre
clientes; tudo que é **conteúdo** (design system, memória, jornadas)
fica isolado dentro de `projects/[cliente]/` e nunca vaza para outro
cliente.

Veja `projects/_EXEMPLO_CLIENTE/` como modelo para criar um projeto
novo, e `projects/_SANDBOX_TESTE/` como fixture já preenchida (smoke
test dos 10 agentes) para consulta.

---

## Setup inicial (uma vez por máquina/instalação)

### 1. Credenciais

```bash
cp .env.example .env
```

`figma-mcp-go` (ver passo 2) não exige token de API — usa só o plugin
bridge dentro do Figma Desktop. O `.env.example` fica de referência
para credenciais que outras integrações do projeto venham a precisar.
**Nunca** commite `.env`.

### 2. Conectar o MCP do Figma — `figma-mcp-go`

Este harness usa https://github.com/vkhanhqui/figma-mcp-go — testado e
funcionando neste projeto (Node v20; ambiente atual: Windows, também
já validado em Linux). Diferente de uma conexão por token de API, este
servidor só enxerga o Figma através de um plugin rodando dentro do
Figma Desktop, aberto no arquivo-alvo. Isso significa que **leitura e
escrita exigem Figma Desktop igualmente** — não há um modo
remoto/read-only que dispense o app, ao contrário do que se imaginava
antes de testar na prática.

```bash
claude mcp add -s project figma-mcp-go -- npx -y @vkhanhqui/figma-mcp-go@latest
```

Isso grava a configuração em `.mcp.json` (raiz do projeto, versionado).
Na primeira vez que o Claude Code for usado neste diretório depois
disso, ele vai pedir aprovação do servidor — rode `claude` numa sessão
interativa e aprove. Depois, `claude mcp list` deve mostrar
`figma-mcp-go ... ✔ Connected`.

**Plugin no Figma Desktop (obrigatório para qualquer operação, não só escrita):**
1. O plugin já vem vendorizado neste repo em `mcp-figma/plugin/` (não é
   preciso baixar `plugin.zip` da release manualmente) — só use a
   [release oficial](https://github.com/vkhanhqui/figma-mcp-go/releases)
   se quiser atualizar para uma versão mais nova do que a commitada
2. No Figma Desktop: **Plugins → Development → Import plugin from
   manifest** → aponte para `mcp-figma/plugin/manifest.json`
3. Abra o arquivo Figma que quiser usar e rode o plugin manualmente (**Plugins → Development → figma-mcp-go**) — plugins de desenvolvimento não iniciam sozinhos, é preciso rodar a cada sessão de trabalho
4. O Figma Desktop tem build oficial para Windows e macOS (ambiente atual: Windows, roda nativo). Em Linux não há build oficial — escolha um caminho: VM Windows leve, Wine/CrossOver (não suportado oficialmente, risco de instabilidade), ou máquina física ocasional (Mac/Windows)

**Troubleshooting conhecido — "Can't call X in read-only mode":**
Isso não é falta de permissão de conta nem problema do plugin — é o
Figma em **Dev Mode** (ícone `</>` no canto superior direito da aba,
atalho `Shift+D`). Em Dev Mode a própria Plugin API do Figma bloqueia
escrita, para qualquer plugin. Alterne para "Design mode" e tente de
novo.

**Duas limitações reais deste servidor**, já refletidas em
`CLAUDE.md` e nos agentes: não existe tool para criar a primeira
instância de um componente (só clonar uma instância já existente), e
não existe tool para combinar componentes em variantes — ambas exigem
um passo manual no Figma quando ocorrem. Não existe também exposição
de `file-key`: a checagem de "arquivo correto" usa `fileName` (nome de
exibição), então declare o nome exato de cada arquivo (Legado e
Produção) no `PROJECT.md` de cada cliente.

As 73 tools reais já estão nomeadas corretamente em
`.claude/agents/*.md` (prefixo `mcp__figma-mcp-go__*`) — não há mais
placeholder pendente de preenchimento nesta conexão. Os 10 agentes
foram validados de ponta a ponta em `projects/_SANDBOX_TESTE/`. O que
ainda vem com marcações `[PREENCHER]`/`[VALIDAR]` é o que é
inerentemente por-cliente: o `PROJECT.md` de cada projeto novo (copiado
de `_EXEMPLO_CLIENTE`) e alguns pontos listados em "Fora de escopo"
abaixo.

### 3. Criar um novo projeto/cliente

```bash
cp -r projects/_EXEMPLO_CLIENTE projects/nome-do-cliente
```

Preencha, nesta ordem:
1. `projects/nome-do-cliente/PROJECT.md` — pelo menos o `fileName`
   exato do Legado (é isso que os agentes conferem via `get_metadata`,
   não o file-key — ver seção 2 acima). O bloco de Produção fica vazio
   até o preflight criar o arquivo
2. Rode o onboarding (ver abaixo) antes de qualquer trabalho de
   produção

---

## Fluxo 1 — Onboarding (uma vez por cliente)

```
"Use o onboard-scanner no projeto nome-do-cliente"
  → gera onboarding-inventory.md

"Use o onboard-analyst"
  → gera onboarding-questions.md

[ responda as perguntas, uma de cada vez ]
  → respostas viram onboarding-decisions.md

"Use o onboard-writer"
  → gera design-system/tokens/*.md e components/*.md
    (Status: em revisão) + migration-backlog.md
```

Detalhes: `onboarding/ONBOARDING.md`

## Fluxo 2 — Preflight (sob demanda, incremental)

Normalmente disparado automaticamente pelo fluxo de produção (abaixo),
quando o `interpreter` marca um elemento como `MIGRAR DO LEGADO`. Pode
também ser rodado manualmente a partir do `migration-backlog.md`:

```
"Use o preflight-planner para o componente Button/Primary"
  → propõe plano de reconstrução

[ aprovação humana ]

"Use o preflight-builder com o plano aprovado"
  → reconstrói no arquivo de Produção (cria o arquivo na primeira vez)

"Use o documenter para promover Button/Primary"
  → Status: em revisão → ativo
```

Detalhes: `preflight/PREFLIGHT.md`

## Fluxo 3 — Produção (dia a dia)

1. Crie `projects/nome-do-cliente/journeys/nome-da-jornada/`
2. `user-story.md` com a história do usuário (template incluso)
3. `wireframe/` com as imagens exportadas do Miro (ou print de tela
   legada, se for uma migração — ver `migration/MIGRATION.md`)

```
"Use o interpreter para a jornada nome-da-jornada"
  → plano com classificação por elemento: REUSO DIRETO / NOVA
    VARIANTE / COMPONENTE NOVO / MIGRAR DO LEGADO

[ aprovação humana ]

[ se houver MIGRAR DO LEGADO: rodar Fluxo 2 para esses itens antes
  de prosseguir ]

"Use o builder para construir a tela 1"
  → repita por tela; builder recebe journey-state.md atualizado a
    cada nova tela (atualização é responsabilidade da sessão
    principal, não do builder)

"Use o validator para validar a jornada completa"
  → gera journeys/nome-da-jornada/validation-report.md

[ aprovação humana ]

"Use o documenter para promover os componentes desta jornada e as
telas para Telas Atuais"
```

Rode o `auditor` periodicamente (recomendado: início de cada sessão de
trabalho no projeto) para checar sincronização com o arquivo de
Produção real.

Detalhes: `CLAUDE.md`

### Formato de wireframe aceito hoje

PDF ou imagem exportada do Miro (ou de qualquer ferramenta), uma por
tela, em `wireframe/`. Conexão MCP direta ao Miro foi avaliada e
adiada conscientemente — ver `CLAUDE.md`, seção "Fora de escopo".

---

## Estrutura de páginas do arquivo de Produção

```
Foundations / Components / Patterns / Docs / Archive   ← design system
🟢 Telas Atuais    ← versão vigente de cada tela, sempre
🗂️ Jornadas         ← histórico, uma página por jornada
```

Os componentes reconstruídos pelo preflight vivem em **Components**.
Telas são sempre frames duplicados (cópia solta), nunca componente/
instância — isso é reservado para elementos reais do design system
(Button, Card etc.). Ver `CLAUDE.md` para a mecânica completa.

---

## Pontos que ficaram conscientemente fora de escopo (v1)

- Rollback automatizado de operações no Figma
- Múltiplos aprovadores / fluxo de aprovação por cliente
- Responsividade / breakpoints (campo previsto no template, sem
  processo ainda)
- Conexão MCP direta com Miro
- `[VALIDAR]` Portabilidade automática de assets (ícones, imagens)
  entre arquivo Legado e arquivo de Produção — confirmar na prática
  assim que o preflight rodar com um componente que dependa de asset

Se algum desses virar necessidade real, revisite o raciocínio antes de
implementar — várias dessas decisões têm trade-offs já discutidos.
