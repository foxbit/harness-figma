# Skill: Onboard Project

## Quando usar
Início de um cliente novo — antes de qualquer trabalho de produção ou
preflight ser possível. Ver `onboarding/ONBOARDING.md` para o processo
completo.

## Resumo do procedimento
1. `onboard-scanner` varre o arquivo Legado inteiro, produz inventário
   bruto sem julgamento
2. `onboard-analyst` cruza o inventário, identifica suspeitas de
   duplicata/inconsistência, formula perguntas objetivas
3. Negociação com o humano, uma pergunta por vez, respostas registradas
4. `onboard-writer` gera `design-system/tokens/*.md` e
   `design-system/components/*.md` (com `Status: em revisão`) +
   `migration-backlog.md`

Nenhuma escrita no Figma acontece neste processo — onboarding é
puramente leitura + documentação.

Detalhes completos: `onboarding/ONBOARDING.md` e os arquivos
`.claude/agents/onboard-*.md`
