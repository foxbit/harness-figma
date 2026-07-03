<!--
TESTE DE FUMAÇA — projeto _SANDBOX_TESTE. Confirmado ao vivo via
get_styles nesta sessão (arquivo Legado mcp-test).
-->

# Tokens — typography

O arquivo Legado `mcp-test` **não tem nenhum text style definido**
(`get_styles` retornou lista vazia para `text`). Confirmado pela decisão
Q19 (negociada de verdade): tipografia usada nas telas é hardcoded, sem
token/style associado, e a criação de text styles é trabalho novo do
preflight — não uma migração, porque não existe equivalente no Legado.

Exemplo de valores hardcoded observados na amostra `login.md`: Nunito
SemiBold 24 (título), Inter Medium 14 (labels), Inter Regular 16
(valores de input), Inter Regular 14 (hint text). Estes NÃO são tokens
— são citados aqui só como insumo para o preflight definir a escala
tipográfica real.

| Nome do token | Uso pretendido | Observações |
|---|---|---|
| [PREENCHER — nenhum text style existe no Legado; a criar do zero no preflight] | [PREENCHER] | [PREENCHER] |
