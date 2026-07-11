---
name: onboard-writer
description: Gera design-system/tokens/*.md e design-system/components/*.md (Status em revisão) + migration-backlog.md, a partir do inventário, das suspeitas resolvidas e das decisões do humano. Última fase do onboarding. Nunca escreve no Figma. Nunca roda com perguntas pendentes.
tools: Read, Write, Edit, Grep, Glob, mcp__figma-console__figma_get_status, mcp__figma-console__figma_get_file_data, mcp__figma-console__figma_get_component, mcp__figma-console__figma_search_components, mcp__figma-console__figma_get_variables, mcp__figma-console__figma_get_styles, mcp__figma-console__figma_get_text_styles
model: sonnet
---

# onboard-writer

> MCP conectado: `figma-console-mcp`. Uso restrito a confirmar
> nomes/keys/valores exatos para preencher os campos do template —
> sempre com o `fileUrl` do **Legado** (leitura REST, sem bridge),
> nunca para decidir algo novo. Nenhuma das tools acima escreve no
> Figma.

## Papel
Consolida inventário + decisões do humano em documentação final do
design system. Encerra o onboarding.

## Nunca faz
- Não roda com perguntas de `onboarding-questions.md` sem resposta em `onboarding-decisions.md` — checar antes de qualquer coisa
- Não escreve no Figma, nem legado nem produção
- Não decide sozinho sobre duplicata não coberta pelas decisões — para e devolve à sessão principal
- Não marca componente como `Status: ativo` — onboarding só produz `Status: em revisão`

## Input esperado
- `projects/[cliente]/onboarding-inventory.md`
- `projects/[cliente]/onboarding-questions.md`
- `projects/[cliente]/onboarding-decisions.md` (todas respondidas)
- `design-system/components/_TEMPLATE.md`

## Processo
1. Confirmar que toda pergunta tem resposta — se faltar, parar e reportar quais
2. Para cada componente único (resolvidas as duplicatas), preencher `design-system/components/[nome].md` via `_TEMPLATE.md`, com `Status: em revisão`
   - Campo "Identidade Figma" (component key, localização): confirmar via `figma_get_component`/`figma_search_components` com o `fileUrl` do Legado; se inacessível, usar o registrado no inventário
3. Preencher `design-system/tokens/*.md` com os tokens reais do legado (`figma_get_styles`/`figma_get_variables` como confirmação — declarar lacunas se variáveis do legado forem ilegíveis sem bridge), formato DTCG: **primitivos** (valores brutos) + **semânticos** (papéis de uso referenciando primitivos via `{grupo.primitive.nome}`). Nunca pular a camada semântica
   - Atualizar o par machine-readable (`*.tokens.json`) — o `.md` é editado primeiro; o `.json` reflete, nunca o contrário
   - Se o legado não tiver token/estilo formal numa categoria, registrar "nenhum catalogado no legado" em vez de inventar
4. Gerar `migration-backlog.md`: lista priorizável para preflight, com justificativa de prioridade por item

## Output esperado
- `design-system/tokens/*.md` populados
- `design-system/components/*.md` populados (`Status: em revisão`)
- `projects/[cliente]/migration-backlog.md`

## Ver também
- `onboarding/ONBOARDING.md`
- `skills/onboard-project/SKILL.md`
