# Skill: Onboard Project

## Quando usar
Início de um cliente novo — antes de qualquer trabalho de produção ou
preflight ser possível. Ver `onboarding/ONBOARDING.md` para o processo
completo.

## Resumo do procedimento
1. `onboard-scanner` varre o arquivo Legado inteiro, produz inventário
   bruto sem julgamento — em duas passadas (visual/screenshot primeiro
   para pesquisa barata, consulta estrutural pontual depois só nos
   candidatos sinalizados; nunca dump de árvore/catálogo inteiro de uma
   vez, ver `onboard-scanner.md`). A leitura do Legado é via REST por
   `fileUrl`/`File-key` — NÃO exige Figma Desktop e o plugin bridge
   nunca roda no Legado
2. `onboard-analyst` cruza o inventário, identifica suspeitas de
   duplicata/inconsistência, formula perguntas objetivas
3. Negociação com o humano, uma pergunta por vez, respostas registradas
4. `onboard-writer` gera `design-system/tokens/*.md`,
   `design-system/components/*.md` (com `Status: em revisão`),
   `design-system/design.md` (identidade visual: valores exatos da
   fonte autoral + Do/Don'ts descritos sobre as telas canônicas que o
   scanner selecionou) + `migration-backlog.md`

Nenhuma escrita no Figma acontece neste processo — onboarding é
puramente leitura + documentação.

Detalhes completos: `onboarding/ONBOARDING.md` e os arquivos
`.claude/agents/onboard-*.md`
