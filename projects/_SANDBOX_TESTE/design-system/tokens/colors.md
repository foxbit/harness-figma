<!--
TESTE DE FUMAÇA — projeto _SANDBOX_TESTE. Fonte: onboarding-inventory.md
(seção 2) + confirmação ao vivo via get_styles/get_variable_defs nesta
sessão (arquivo Legado mcp-test ainda acessível). Cobertura: TODOS os
paint styles e variáveis existentes no arquivo (só 7 + 11, arquivo
inteiro, não amostral — diferente de components/, que é amostral).

IMPORTANTE: o arquivo Legado não tem nenhum paint style SÓLIDO, nenhum
text style, nenhum effect style e nenhum grid style (get_styles retornou
listas vazias para effects/grids/text). As tabelas abaixo já refletem as
decisões Q20/Q21/Q22 aplicadas (renomeação, descarte, escala de
opacidade) — não são o retorno bruto do Legado.
-->

# Tokens — colors

## 1. Paint styles — gradientes de fundo (7 no total, confirmado ao vivo)

Todos são `GRADIENT_LINEAR`. Não existe nenhum paint style sólido no
Legado — cores sólidas usadas em componentes (ex.: `#213975`, `#f8f8f8`
vistos em `Login`) são hardcoded, sem style associado. Confirmar via
`get_variable_defs`/`get_styles` que este é o cenário real (Q19: sim,
confirmado — criação de tokens sólidos é trabalho novo do preflight, não
migração).

| Nome do token (Figma) | Uso pretendido | Stops (hex, confirmado ao vivo) |
|---|---|---|
| `Verde Claro` | Fundo decorativo de tela (ex.: telas de boas-vindas) | `#FFFFFF` → `#57AC13` |
| `Gradiente/Verde` | Fundo de card/seção com ênfase verde | `#629737` → `#356A0A` |
| `Gradiente/Azul` | Fundo de card/seção com ênfase azul | `#363F72` → `#16299C` |
| `Card Background/Vermelho` | Fundo de card de categoria "vermelho" (ex.: dificuldade/status de alerta) | `#FFC0BC` → `#FFFFFF` |
| `Card Background/Laranja` | Fundo de card de categoria "laranja" | `#FFC493` → `#FFFFFF` |
| `Card Background/Verde` | Fundo de card de categoria "verde" | `#CFFFD2` → `#FFFFFF` |
| `Card Background/Cinza` | Fundo de card neutro/arquivado | `#E6E6E6` → `#FFFFFF` |

## 2. Variáveis de cor — após aplicação de Q20/Q21/Q22

Coleção original no Legado: `Variable collection`, um único modo
(`Mode 1`). 11 variáveis no total, sendo 3 STRING (não são tokens de
cor — ver seção 3) e 8 COLOR.

| Nome do token (proposto, pós-decisão) | Nome original no Legado | Uso pretendido | Valor (hex, confirmado ao vivo) | Observações |
|---|---|---|---|---|
| `Estilos de formatação/Verde Claro 50` | (mesmo) | Fundo/destaque verde claro, opacidade reduzida | `#D0F8AB` @ 50% alpha | Par completo com o token abaixo (escala 50/100 já existia) |
| `Estilos de formatação/Verde Claro 100` | (mesmo) | Fundo/destaque verde claro, opaco | `#D0F8AB` | — |
| `Estilos de formatação/Azul Claro 50` | (mesmo) | Fundo/destaque azul claro, opacidade reduzida | `#D1E9FF` @ 50% alpha | Par completo (escala 50/100 já existia) |
| `Estilos de formatação/Azul Claro 100` | (mesmo) | Fundo/destaque azul claro, opaco | `#D1E9FF` | — |
| `Estilos de formatação/Verde escuro 100` | (mesmo) | Texto/ícone em verde escuro (contraste sobre fundo claro) | `#2FA836` | **Gap Q22**: não tem par `50` — precisa ser criado no preflight para completar a escala padronizada |
| `Estilos de formatação/Amarelo` | (mesmo) | Destaque/grifo amarelo (marca-texto) | `#FFF050` | **Gap Q22**: não tem nenhuma variante de opacidade (`50`/`100`) — criar ambas no preflight |
| `Estilos de formatação/Âncora` | (mesmo) | Destaque de âncora/link no editor | `#E0CBFB` | **Gap Q22**: idem — sem variantes de opacidade, criar no preflight |
| `Estilos de formatação/Sem registro` | `" Sem registro"` (com espaço em branco antes do nome, literal no Legado) | Indicador visual de "sem registro"/dado ausente | `#FFCACA` | Renomeado por decisão Q21 — nome original tinha espaço em branco líder e não seguia o padrão `Estilos de formatação/[Nome]`. **Gap Q22**: sem variantes de opacidade, criar no preflight |
| `Estilos de formatação/Verde Muito Claro` | `Green light` | Fundo muito sutil (quase branco) com leve tom esverdeado — uso pretendido específico ainda não confirmado com time de produto (nome original em inglês sugere ter sido criado por dev externo, ver Q21) | `#FAFFF6` | Renomeado por decisão Q21 (único nome em inglês da coleção). Nome final `"Verde Muito Claro"` é PROPOSTA desta sessão para diferenciar de `Verde Claro` (que é bem mais saturado, `#D0F8AB`) — não confirmado com o cliente real (não aplicável neste smoke test). **Gap Q22**: sem variantes de opacidade, criar no preflight |

## 3. Variáveis descartadas (decisão Q20)

Estas 3 variáveis STRING foram identificadas como resíduo de
conteúdo/teste, não tokens de design, e por decisão Q20 são descartadas
do design system novo (não aparecem na tabela acima nem devem ser
recriadas no preflight):

| Nome original | Tipo | Valor | Motivo do descarte |
|---|---|---|---|
| `Title` | STRING | `"Gestão de conteúdo"` | Conteúdo de página/texto solto, não token |
| `String` | STRING | `"String value"` | Placeholder de plugin/template não substituído |
| `Pergunta` | STRING | Enunciado completo de questão de prova | Conteúdo de exemplo, não token de design |

## 4. Escala de opacidade — status por cor base (decisão Q22)

| Cor base | Tem `50`? | Tem `100`? | Ação |
|---|---|---|---|
| Verde Claro | sim | sim | completo |
| Azul Claro | sim | sim | completo |
| Verde escuro | não | sim | criar `50` no preflight |
| Amarelo | não | não | criar `50` e `100` no preflight |
| Âncora | não | não | criar `50` e `100` no preflight |
| Sem registro | não | sim (implícito, valor único) | criar `50` no preflight |
| Verde Muito Claro | não | sim (implícito, valor único) | criar `50` no preflight |
