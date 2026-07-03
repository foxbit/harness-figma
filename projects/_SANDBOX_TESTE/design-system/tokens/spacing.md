<!--
TESTE DE FUMAÇA — projeto _SANDBOX_TESTE. Confirmado ao vivo via
get_variable_defs numa sessão anterior (arquivo Legado mcp-test).
Migrado para formato DTCG nesta sessão, sem perder nenhum achado
original.
-->

# Tokens — spacing

## Primitivos

**Nenhum catalogado.** A única coleção de variáveis do arquivo Legado
(`Variable collection`, `Mode 1`) não contém nenhuma variável de
espaçamento — as 11 variáveis existentes são todas de cor ou string de
conteúdo (ver `colors.md`). Não há token de spacing a migrar; a criação
de uma escala de espaçamento é trabalho NOVO do preflight (mesma lógica
da decisão Q19, por analogia — nenhum equivalente existe no Legado).

Valores de padding hardcoded observados na amostra `login.md` (referência
para o preflight, NÃO são tokens): 72/41/60/41 (Card), 24 uniforme
(Content), 10/20/20/10 (Input).

## Semânticos

**Pendente** — sem primitivo catalogado. Quando o preflight definir a
escala real, nomear os semânticos seguindo `_EXEMPLO_CLIENTE/tokens/spacing.md`
(`xs`/`sm`/`md`/`lg`/`xl`).

## Histórico
- Criado em: `2026-07-03` — origem: `onboard-writer`, smoke test do onboarding, migrado para formato DTCG na mesma data
