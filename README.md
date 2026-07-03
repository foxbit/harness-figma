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

`figma-mcp-go` (ver passo 2) não exige token de API — usa só o plugin
bridge dentro do Figma Desktop. O `.env.example` fica de referência
para credenciais que outras integrações do projeto venham a precisar.
**Nunca** commite `.env`.

### 2. Conectar o MCP do Figma — `figma-mcp-go`

Este harness usa https://github.com/vkhanhqui/figma-mcp-go — testado e
funcionando neste projeto (Node v20, Linux). Diferente de uma conexão
por token de API, este servidor só enxerga o Figma através de um
plugin rodando dentro do Figma Desktop, aberto no arquivo-alvo. Isso
significa que **leitura e escrita exigem Figma Desktop igualmente** —
não há um modo remoto/read-only que dispense o app, ao contrário do
que se imaginava antes de testar na prática.

```bash
claude mcp add -s project figma-mcp-go -- npx -y @vkhanhqui/figma-mcp-go@latest
```

Isso grava a configuração em `.mcp.json` (raiz do projeto, versionado).
Na primeira vez que o Claude Code for usado neste diretório depois
disso, ele vai pedir aprovação do servidor — rode `claude` numa sessão
interativa e aprove. Depois, `claude mcp list` deve mostrar
`figma-mcp-go ... ✔ Connected`.

**Plugin no Figma Desktop (obrigatório para qualquer operação, não só escrita):**
1. Baixe `plugin.zip` da [release mais recente](https://github.com/vkhanhqui/figma-mcp-go/releases)
2. Extraia — o `manifest.json` fica na raiz do zip extraído
3. No Figma Desktop: **Plugins → Development → Import plugin from manifest** → aponte para esse `manifest.json`
4. Abra o arquivo Figma que quiser usar e rode o plugin manualmente (**Plugins → Development → figma-mcp-go**) — plugins de desenvolvimento não iniciam sozinhos, é preciso rodar a cada sessão de trabalho
5. Figma Desktop não tem build oficial para Linux — escolha um caminho: VM Windows leve, Wine/CrossOver (não suportado oficialmente, risco de instabilidade), ou máquina física ocasional (Mac/Windows)

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
placeholder pendente de preenchimento nesta conexão.

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
