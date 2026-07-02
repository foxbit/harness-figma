# Onboarding — Processo de Varredura do Design System Legado

Este documento rege o escopo de **onboarding**: a análise inicial de um
projeto Figma legado, mal estruturado, para prepará-lo como insumo do
harness de produção. Roda uma vez por cliente (ou raramente, se o
legado mudar muito). Nunca escreve no Figma — produz apenas arquivos
`.md` de saída.

Ver `CLAUDE.md` para como este escopo se relaciona com Preflight e
Produção.

---

## Quando usar

- Início de um cliente novo, cujo Figma legado nunca foi mapeado pelo
  harness
- Re-varredura pontual, se o time do cliente mudou muita coisa no
  legado fora do harness (raro — normalmente a sincronização de rotina
  do `auditor` é suficiente para o arquivo de Produção; o legado, uma
  vez mapeado, tende a ser só consultado, não revarrido)

## As três fases (agentes correspondentes)

```
1. onboard-scanner    → inventário bruto, sem julgamento
2. onboard-analyst     → identifica suspeitas, formula perguntas
3. [ negociação com o humano, via ask_user_input, uma pergunta por vez ]
4. onboard-writer      → gera design-system/ final (Status: em revisão)
```

Nenhuma fase pula para a seguinte sem o output completo da anterior.
`onboard-writer` especificamente NUNCA roda com perguntas pendentes.

## Output final do onboarding

- `design-system/tokens/*.md` — populados
- `design-system/components/*.md` — populados, todos com
  `Status: em revisão` (ainda não existem no arquivo de Produção — isso
  é trabalho do preflight)
- `migration-backlog.md` — lista priorizável do que precisa passar por
  preflight

## O que o onboarding explicitamente NÃO faz

- Não escreve nada no Figma, nem legado nem produção
- Não decide sozinho sobre duplicatas — sempre pergunta
- Não reconstrói componentes — isso é escopo do preflight
- Não cria o arquivo de Produção — isso acontece na primeira execução
  do `preflight-builder`

## `[VALIDAR]` — Portabilidade de assets entre arquivos

Ícones, imagens e fontes usados pelos componentes legados precisam ser
trazidos junto na reconstrução (preflight), não só a estrutura. Ainda
não foi validado na prática se o MCP conectado consegue "ler referência
de um arquivo, criar/importar asset em outro arquivo" na mesma operação,
ou se isso exige passo manual. Validar assim que o preflight rodar pela
primeira vez com um componente que dependa de asset externo (ícone,
imagem).
