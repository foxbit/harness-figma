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
| `onboard-writer` | 3º — todas as perguntas respondidas | Gera `design-system/tokens/*.md`, `components/*.md` (`Status: em revisão`), `design.md` (identidade visual) + `migration-backlog.md` | Escrever no Figma; rodar com perguntas pendentes |

Entre o analyst e o writer existe uma etapa humana obrigatória: a
negociação das perguntas, uma por vez, registrada em
`onboarding-decisions.md`.

### Módulo 2 — Preflight (sob demanda, incremental · escreve no arquivo de Produção)

Migra componentes do legado para o arquivo de Produção, **um por vez,
quando uma demanda real precisa deles** — nunca em lote (big-bang). É
também o módulo em que o arquivo de Produção nasce, na primeira
execução de um cliente (a criação do ARQUIVO em si é manual — o agente
cria a estrutura de páginas). "Migrar" aqui significa **reconstruir do zero** seguindo
`COMPONENT_STANDARDS.md`, usando o legado só como referência visual —
nunca copiar a estrutura problemática.

| Agente | Quando entra | O que faz | Nunca faz |
|---|---|---|---|
| `preflight-planner` | Elemento marcado `MIGRAR DO LEGADO`, ou priorização manual do backlog | Lê o componente no Legado e propõe a reconstrução, destacando riscos de drift visual para a aprovação | Reconstruir, escrever no Figma |
| `preflight-builder` | Plano de reconstrução aprovado | Reconstrói no arquivo de Produção (cria a estrutura de páginas na 1ª vez do cliente; único agente que cria variáveis/tokens) | Escrever no Legado; decidir migrar algo fora do aprovado |

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
| `validator` | TODAS as telas da jornada prontas | Compara o resultado contra a história do usuário, o wireframe, a coerência entre telas e a identidade visual (`design.md`); gera `validation-report.md` (usa Opus — julgamento semântico fino) | Corrigir ou modificar qualquer coisa |
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
├── mcp-figma/plugin/            # LEGADO: plugin do figma-mcp-go
│   │                              (MCP anterior — remover após a 1ª
│   │                              jornada real no servidor novo)
├── .claude/agents/             # os 10 subagentes
│   ├── interpreter.md / builder.md / documenter.md / auditor.md /
│   │   validator.md                            ← produção
│   ├── onboard-scanner.md / onboard-analyst.md /
│   │   onboard-writer.md                        ← onboarding
│   └── preflight-planner.md / preflight-builder.md   ← preflight
├── skills/                     # procedimentos reutilizáveis
└── projects/
    └── [nome-do-cliente]/      # um diretório por cliente/projeto
        ├── PROJECT.md            # File-key de Legado e de Produção
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

### 1. Personal Access Token do Figma

Crie um token em Figma → Settings → Security → Personal access tokens
(descrição sugerida: `Figma Console MCP`), com os scopes: **File
content (Read)**, **File versions (Read)**, **Variables (Read)**,
**Comments (Read/write)**. O token (`figd_...`) alimenta só a LEITURA
via REST — a escrita no canvas passa pelo plugin bridge, por isso os
scopes são de leitura. Copie na hora: não é exibido de novo. O
`.env.example` segue de referência para outras integrações; **nunca**
commite `.env` nem o token.

### 2. Conectar o MCP do Figma — `figma-console-mcp`

Este harness usa https://github.com/southleft/figma-console-mcp
(substituiu o `figma-mcp-go` em 2026-07-11, após smoke test completo —
ver `smoke-test-figma-console-mcp.md`). Arquitetura híbrida:
**leitura via REST** por `fileUrl`/`fileKey`, sem Figma Desktop — é
assim que o arquivo Legado é lido, sem nunca receber plugin — e
**escrita via plugin Desktop Bridge** rodando no arquivo-alvo.

```bash
claude mcp add figma-console -s user \
  -e FIGMA_ACCESS_TOKEN=figd_SEU_TOKEN_AQUI \
  -e ENABLE_MCP_APPS=true \
  -- npx -y figma-console-mcp@latest
```

> ⚠️ **Escopo `-s user` (ou `-s local`), NUNCA `-s project`** — o
> registro carrega o token, e `-s project` gravaria em `.mcp.json`,
> que é versionado. Consequência: cada máquina nova precisa refazer
> este comando; nada no repositório restaura o registro.

A primeira checagem (`claude mcp list`) pode falhar enquanto o `npx`
baixa o pacote — com o cache aquecido, mostra
`figma-console ... ✔ Connected`.

**Plugin Desktop Bridge (obrigatório para ESCRITA; leitura dispensa):**
1. O servidor materializa o plugin em
   `~/.figma-console-mcp/plugin/manifest.json` na primeira execução
2. Figma Desktop: **Plugins → Development → Import plugin from
   manifest** → aponte para esse arquivo
3. Abra o arquivo de **Produção** e rode o plugin (**Plugins →
   Development → Figma Desktop Bridge**) — conecta sozinho via
   WebSocket (portas 9223–9232). Plugins de desenvolvimento precisam
   ser rodados a cada sessão de trabalho
4. **NUNCA rode o plugin no arquivo Legado** — é a ausência do bridge
   que torna escrita no Legado impossível por arquitetura (ver
   `CLAUDE.md`, regra de segurança)
5. Figma Desktop: build oficial para Windows (ambiente atual, nativo)
   e macOS. Em Linux só a escrita exige contorno (VM/Wine) — a leitura
   via REST funciona em qualquer OS

**Troubleshooting — "Can't call X in read-only mode":** a aba do Figma
está em **Dev Mode** (ícone `</>`, atalho `Shift+D`) — a Plugin API
bloqueia escrita nesse estado, para qualquer plugin. Alterne para
Design mode.

As capacidades e quirks confirmados do servidor (timeout ≠ falha, sync
de tokens, leitura de Auto Layout via `figma_execute` etc.) estão em
`CLAUDE.md`, seção "Conexão MCP com o Figma". Os 10 agentes usam o
prefixo `mcp__figma-console__*`, migrados com base no smoke test em
`projects/_SANDBOX_TESTE/`. O que ainda vem com marcações
`[PREENCHER]`/`[VALIDAR]` é o que é inerentemente por-cliente: o
`PROJECT.md` de cada projeto novo (copiado de `_EXEMPLO_CLIENTE`) e
alguns pontos listados em "Fora de escopo" abaixo.

> Nota de transição: o servidor anterior (`figma-mcp-go`) permanece
> registrado em `.mcp.json`, e o plugin dele vendorizado em
> `mcp-figma/plugin/`, apenas como fallback — nenhum agente o usa
> mais. Remover ambos quando a primeira jornada real completar no
> servidor novo.

### 3. Criar um novo projeto/cliente

```bash
cp -r projects/_EXEMPLO_CLIENTE projects/nome-do-cliente
```

Preencha, nesta ordem:
1. `projects/nome-do-cliente/PROJECT.md` — pelo menos o **File-key**
   do Legado (basta o link do arquivo — o key está na URL). É por ele
   que os agentes leem o Legado via REST e que a regra de segurança
   verifica o alvo de escrita. O bloco de Produção fica vazio até o
   arquivo ser criado no primeiro preflight (criação do arquivo é
   manual — o agente cria só a estrutura de páginas)
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
  → gera design-system/tokens/*.md, components/*.md
    (Status: em revisão), design.md (identidade visual do projeto)
    + migration-backlog.md
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
  → reconstrói no arquivo de Produção (na 1ª vez: você cria o arquivo
    manualmente e roda o plugin nele; o agente cria as páginas)

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
