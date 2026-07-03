<!--
TESTE DE FUMAÇA — projeto _SANDBOX_TESTE. Confirmado ao vivo via
get_styles numa sessão anterior (arquivo Legado mcp-test). Migrado para
formato DTCG nesta sessão, sem perder nenhum achado original.
-->

# Tokens — radius & shadows

## Primitivos

**Nenhum catalogado.** O arquivo Legado `mcp-test` não tem nenhum effect
style nem grid style definido (`get_styles` retornou listas vazias para
`effects` e `grids`). Confirmado pela decisão Q19: sombras/efeitos usados
nas telas (se houver) são hardcoded, sem token/style associado. Corner
radius também não tem variável dedicada na única coleção do arquivo.

Valores de cornerRadius hardcoded observados na amostra `login.md`
(referência para o preflight, NÃO são tokens): 28 (Card), 16 (Content),
9999 (Input, Button — radius total/pill).

## Semânticos

**Pendente** — sem primitivo catalogado. Quando o preflight definir os
valores reais, nomear seguindo `_EXEMPLO_CLIENTE/tokens/radius-shadows.md`
(`radius.sm/md/lg/full`, `shadow.elevation-1/2`).

## Histórico
- Criado em: `2026-07-03` — origem: `onboard-writer`, smoke test do onboarding, migrado para formato DTCG na mesma data
