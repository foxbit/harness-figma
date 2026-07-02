# Figma Design Harness — Claude Code

Harness para operações determinísticas de design no Figma via MCP, com
Claude Code e subagentes especializados. Cobre três escopos de trabalho:

- **Onboarding** — varredura e documentação inicial de um Figma legado
  mal estruturado (uma vez por cliente, só leitura)
- **Preflight** — reconstrução incremental de componentes do legado num
  arquivo de Produção novo, seguindo boas práticas (sob demanda, com
  escrita no Figma)
- **Produção** — construção do dia a dia de telas/jornadas a partir de
  wireframe + história do usuário (o ciclo recorrente)

Leia `arquitetura-harness-figma.md` (se você tiver esse documento à
mão) para o raciocínio completo por trás de cada decisão. Este README é
só o operacional.

> ⚠️ Este repositório contém ESQUELETO + PLACEHOLDERS. Vários arquivos
> têm marcações `[PREENCHER]` e `[VALIDAR]` que precisam ser resolvidas
> antes do harness funcionar de ponta a ponta — especialmente os nomes
> reais das tools MCP e os dados de `projects/`.

---

## Estrutura

```
figma-harness/
├── CLAUDE.md                  # regras universais — leia primeiro
├── onboarding/ONBOARDING.md    # processo do escopo de onboarding
├── preflight/PREFLIGHT.md      # processo do escopo de preflight
├── migration/MIGRATION.md      # variação leve: migrar tela legada
├── .claude/agents/             # os 10 subagentes
│   ├── interpreter.md / builder.md / documenter.md / auditor.md /
│   │   validator.md                            ← produção
│   ├── onboard-scanner.md / onboard-analyst.md /
│   │   onboard-writer.md                        ← onboarding
│   └── preflight-planner.md / preflight-builder.md   ← preflight
├── skills/                     # procedimentos reutilizáveis
└── projects/
    └── [nome-do-cliente]/      # um diretório por cliente/projeto
        ├── PROJECT.md            # dois file-keys: Legado e Produção
        ├── design-system/
        ├── memory/
        └── journeys/
```

Veja `projects/_EXEMPLO_CLIENTE/` como modelo para criar um projeto
novo.

---

## Setup inicial (uma vez por máquina/instalação)

### 1. Credenciais

```bash
cp .env.example .env
```

Preencha `.env` — ver comentários no próprio arquivo. Há duas URLs
distintas de MCP: uma para leitura (Remote SSE) e outra para escrita.
**Nunca** commite `.env`.

### 2. Conectar o MCP do Figma — `figma-console-mcp`

Este harness usa https://github.com/southleft/figma-console-mcp em vez
do MCP oficial do Figma, por compatibilidade com Linux. Confirme
sempre a documentação atual do projeto antes de seguir, pois esse tipo
de setup muda com frequência.

**Importante entender antes de configurar**: esse MCP tem modos com
capacidades bem diferentes.

| Modo | O que exige | Cobre quais agentes |
|---|---|---|
| **Remote SSE** | Só o token, via OAuth — nenhum app instalado, funciona 100% no Linux | `interpreter`, `auditor`, `validator`, `onboard-scanner`, `onboard-analyst` (todos read-only) |
| **Local NPX / Cloud Mode** | Node.js + **Figma Desktop app rodando com o plugin "Desktop Bridge"** | `builder`, `preflight-builder` (escrita) |

**A limitação real**: Figma Desktop não tem build oficial para Linux —
nem este MCP nem o oficial do Figma escapam dessa exigência para
escrita. Três caminhos possíveis, escolha um quando for de fato usar
`builder`/`preflight-builder` (não é bloqueante para o resto):

- **VM Windows leve** rodando Figma Desktop + plugin, usando **Cloud
  Mode** para o Claude Code (no seu Linux) se conectar ao relay —
  não precisa que a VM e o Claude Code estejam na mesma máquina
- **Wine/CrossOver** rodando o Figma Desktop direto no Linux — não
  suportado oficialmente pelo Figma, risco de instabilidade
- **Máquina física ocasional** (Mac/Windows que você tenha acesso de
  vez em quando) só para as sessões em que for rodar `builder`/
  `preflight-builder`

Passos gerais de conexão (confirme na doc atual do projeto):
```bash
claude mcp add --transport sse figma-read [URL_REMOTE_SSE]
# Quando for configurar escrita, adicionar a conexão correspondente
# ao modo escolhido (Local NPX ou Cloud Mode)
```

**[PREENCHER]** — depois de conectado, rode uma consulta simples para
listar as tools expostas de fato, e substitua os placeholders
`mcp__figma__*` / `figma_*` usados em `.claude/agents/*.md` pelos nomes
reais.

### 3. Criar um novo projeto/cliente

```bash
cp -r projects/_EXEMPLO_CLIENTE projects/nome-do-cliente
```

Preencha, nesta ordem:
1. `projects/nome-do-cliente/PROJECT.md` — pelo menos o file-key do
   Legado (o de Produção fica vazio até o preflight criar o arquivo)
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

## Os 10 agentes

| Agente | Escopo | O que faz | Nunca faz |
|---|---|---|---|
| `onboard-scanner` | Onboarding | Varre o Legado, inventário bruto | Julgar, decidir, escrever no Figma |
| `onboard-analyst` | Onboarding | Identifica suspeitas, formula perguntas | Decidir sozinho |
| `onboard-writer` | Onboarding | Gera design-system/ (Status: em revisão) | Escrever no Figma |
| `preflight-planner` | Preflight | Propõe reconstrução de um componente | Reconstruir, escrever no Figma |
| `preflight-builder` | Preflight | Reconstrói no arquivo de Produção | Escrever no Legado |
| `interpreter` | Produção | Decide reuso/variante/novo/migrar, propõe plano | Escrever no Figma |
| `builder` | Produção | Executa o plano aprovado, por tela | Reinterpretar, decidir sozinho |
| `documenter` | Produção | Documenta e promove _draft/ → oficial | Documentar antes da validação |
| `auditor` | Produção | Consistência técnica do arquivo de Produção | Corrigir automaticamente |
| `validator` | Produção | Alinhamento semântico com a história do usuário | Modificar qualquer coisa |

---

## Estrutura de páginas do arquivo de Produção

```
Foundations / Components / Patterns / Docs / Archive   ← design system
🟢 Telas Atuais    ← versão vigente de cada tela, sempre
🗂️ Jornadas         ← histórico, uma página por jornada
```

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
