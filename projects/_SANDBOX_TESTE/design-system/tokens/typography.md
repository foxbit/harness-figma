<!--
TESTE DE FUMAÇA — projeto _SANDBOX_TESTE. Confirmado ao vivo via
get_styles numa sessão anterior (arquivo Legado mcp-test). Migrado para
formato DTCG nesta sessão, sem perder nenhum achado original.
-->

# Tokens — typography

## Primitivos

**Nenhum catalogado.** O arquivo Legado `mcp-test` não tem nenhum text
style definido (`get_styles` retornou lista vazia para `text`).
Confirmado pela decisão Q19 (negociada de verdade): tipografia usada nas
telas é hardcoded, sem token/style associado. A criação de tokens de
tipografia é trabalho NOVO do preflight — não uma migração, porque não
existe equivalente no Legado.

Valores hardcoded observados na amostra `login.md` (referência para o
preflight definir a escala real, NÃO são tokens): Nunito SemiBold 24
(título), Inter Medium 14 (labels), Inter Regular 16 (valores de input),
Inter Regular 14 (hint text).

## Semânticos

**Pendente** — sem primitivo catalogado, não há o que referenciar ainda.
Quando o preflight criar os primeiros text styles/fontFamily, definir os
tiers semânticos seguindo a convenção de `_EXEMPLO_CLIENTE/tokens/typography.md`
(`display-lg`, `heading-lg/md`, `body-lg/md`, `label-caps`, `caption`).

## Histórico
- Criado em: `2026-07-03` — origem: `onboard-writer`, smoke test do onboarding, migrado para formato DTCG na mesma data
