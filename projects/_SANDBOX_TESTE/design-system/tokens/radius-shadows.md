<!--
TESTE DE FUMAÇA — projeto _SANDBOX_TESTE. Confirmado ao vivo via
get_styles nesta sessão (arquivo Legado mcp-test).
-->

# Tokens — radius-shadows

O arquivo Legado `mcp-test` **não tem nenhum effect style nem grid
style definido** (`get_styles` retornou listas vazias para `effects` e
`grids`). Confirmado pela decisão Q19: sombras/efeitos usados nas telas
(se houver) são hardcoded, sem token/style associado. Corner radius
também não tem variável dedicada na única coleção do arquivo.

Valores de cornerRadius hardcoded observados na amostra `login.md`: 28
(Card), 16 (Content), 9999 (Input, Button — radius total/pill). Citados
só como insumo para o preflight, não são tokens.

| Nome do token | Uso pretendido | Observações |
|---|---|---|
| [PREENCHER — nenhum effect/grid style existe no Legado; a criar do zero no preflight] | [PREENCHER] | [PREENCHER] |
