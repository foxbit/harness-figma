<!--
TESTE DE FUMAÇA — projeto _SANDBOX_TESTE. Fonte: onboarding-inventory.md
(seção 2) + confirmação ao vivo via get_styles/get_variable_defs numa
sessão anterior (arquivo Legado mcp-test ainda acessível). Cobertura:
TODOS os paint styles e variáveis existentes no arquivo (só 7 + 11,
arquivo inteiro, não amostral — diferente de components/, que é
amostral).

MIGRAÇÃO PARA DTCG (nesta sessão): o conteúdo abaixo já existia em
formato tabular solto; foi reorganizado na convenção primitivo→semântico
descrita em `colors.md` do `_EXEMPLO_CLIENTE`, sem perder nenhum achado
original. Camada SEMÂNTICA fica deliberadamente pendente — onboarding só
cataloga o que existe (primitivos), a atribuição de papel semântico
(`color.primary` etc.) é decisão do preflight ao reconstruir cada
componente, não do onboarding.

IMPORTANTE: o arquivo Legado não tem nenhum paint style SÓLIDO, nenhum
text style, nenhum effect style e nenhum grid style (get_styles retornou
listas vazias para effects/grids/text). As tabelas abaixo já refletem as
decisões Q20/Q21/Q22 aplicadas (renomeação, descarte, escala de
opacidade) — não são o retorno bruto do Legado.
-->

# Tokens — colors

## Primitivos

### 1. Paint styles — gradientes de fundo (7 no total, confirmado ao vivo)

Todos são `GRADIENT_LINEAR`. Não existe nenhum paint style sólido no
Legado — cores sólidas usadas em componentes (ex.: `#213975`, `#f8f8f8`
vistos em `Login`) são hardcoded, sem style associado. Confirmado (Q19):
criação de tokens sólidos é trabalho novo do preflight, não migração.

| Nome (`color.primitive.*`) | `$type` | `$value` (stops, confirmado ao vivo) | `$description` |
|---|---|---|---|
| `color.primitive.gradiente-verde-claro` | `color` | `#FFFFFF` → `#57AC13` | Fundo decorativo de tela (ex.: telas de boas-vindas). Nome Figma: `Verde Claro` |
| `color.primitive.gradiente-verde` | `color` | `#629737` → `#356A0A` | Fundo de card/seção com ênfase verde. Nome Figma: `Gradiente/Verde` |
| `color.primitive.gradiente-azul` | `color` | `#363F72` → `#16299C` | Fundo de card/seção com ênfase azul. Nome Figma: `Gradiente/Azul` |
| `color.primitive.card-bg-vermelho` | `color` | `#FFC0BC` → `#FFFFFF` | Fundo de card de categoria "vermelho" (dificuldade/status de alerta). Nome Figma: `Card Background/Vermelho` |
| `color.primitive.card-bg-laranja` | `color` | `#FFC493` → `#FFFFFF` | Fundo de card de categoria "laranja". Nome Figma: `Card Background/Laranja` |
| `color.primitive.card-bg-verde` | `color` | `#CFFFD2` → `#FFFFFF` | Fundo de card de categoria "verde". Nome Figma: `Card Background/Verde` |
| `color.primitive.card-bg-cinza` | `color` | `#E6E6E6` → `#FFFFFF` | Fundo de card neutro/arquivado. Nome Figma: `Card Background/Cinza` |

### 2. Variáveis de cor — após aplicação de Q20/Q21/Q22

Coleção original no Legado: `Variable collection`, um único modo
(`Mode 1`). 11 variáveis no total, sendo 3 STRING (não são tokens de
cor — ver seção "Descartados") e 8 COLOR.

| Nome (`color.primitive.*`) | `$type` | `$value` | Nome original no Legado | `$description` |
|---|---|---|---|---|
| `color.primitive.verde-claro-50` | `color` | `#D0F8AB` @ 50% alpha | `Estilos de formatação/Verde Claro 50` | Fundo/destaque verde claro, opacidade reduzida. Par completo com o token abaixo |
| `color.primitive.verde-claro-100` | `color` | `#D0F8AB` | `Estilos de formatação/Verde Claro 100` | Fundo/destaque verde claro, opaco |
| `color.primitive.azul-claro-50` | `color` | `#D1E9FF` @ 50% alpha | `Estilos de formatação/Azul Claro 50` | Fundo/destaque azul claro, opacidade reduzida. Par completo |
| `color.primitive.azul-claro-100` | `color` | `#D1E9FF` | `Estilos de formatação/Azul Claro 100` | Fundo/destaque azul claro, opaco |
| `color.primitive.verde-escuro-100` | `color` | `#2FA836` | `Estilos de formatação/Verde escuro 100` | Texto/ícone em verde escuro (contraste sobre fundo claro). **Gap Q22**: sem par `50`, criar no preflight |
| `color.primitive.amarelo` | `color` | `#FFF050` | `Estilos de formatação/Amarelo` | Destaque/grifo amarelo (marca-texto). **Gap Q22**: sem nenhuma variante de opacidade, criar `50`/`100` no preflight |
| `color.primitive.ancora` | `color` | `#E0CBFB` | `Estilos de formatação/Âncora` | Destaque de âncora/link no editor. **Gap Q22**: idem, criar no preflight |
| `color.primitive.sem-registro` | `color` | `#FFCACA` | `" Sem registro"` (espaço em branco líder, literal no Legado) | Indicador visual de "sem registro"/dado ausente. Renomeado por decisão Q21. **Gap Q22**: sem variantes de opacidade |
| `color.primitive.verde-muito-claro` | `color` | `#FAFFF6` | `Green light` | Fundo muito sutil com leve tom esverdeado — uso exato não confirmado com produto (nome original em inglês, ver Q21). Renomeado por decisão Q21. **Gap Q22**: sem variantes de opacidade |

## Semânticos

**Pendente** — onboarding cataloga primitivos; a atribuição de papel
semântico (`color.primary`, `color.surface` etc., referenciando os
primitivos acima) é decisão do `preflight-planner`/`preflight-builder`
ao reconstruir cada componente que os utiliza, não do `onboard-writer`.
Nenhum primitivo acima deve ser usado direto em componente (ver
`COMPONENT_STANDARDS.md`) — precisa passar por um semântico primeiro.

## Descartados (decisão Q20)

Estas 3 variáveis STRING foram identificadas como resíduo de
conteúdo/teste, não tokens de design, e por decisão Q20 são descartadas
do design system novo (não recriar no preflight):

| Nome original | Tipo | Valor | Motivo do descarte |
|---|---|---|---|
| `Title` | STRING | `"Gestão de conteúdo"` | Conteúdo de página/texto solto, não token |
| `String` | STRING | `"String value"` | Placeholder de plugin/template não substituído |
| `Pergunta` | STRING | Enunciado completo de questão de prova | Conteúdo de exemplo, não token de design |

## Escala de opacidade — status por cor base (decisão Q22)

| Cor base | Tem `50`? | Tem `100`? | Ação |
|---|---|---|---|
| Verde Claro | sim | sim | completo |
| Azul Claro | sim | sim | completo |
| Verde escuro | não | sim | criar `50` no preflight |
| Amarelo | não | não | criar `50` e `100` no preflight |
| Âncora | não | não | criar `50` e `100` no preflight |
| Sem registro | não | sim (implícito, valor único) | criar `50` no preflight |
| Verde Muito Claro | não | sim (implícito, valor único) | criar `50` no preflight |

## Histórico
- Criado em: `2026-07-03` — origem: `onboard-writer`, smoke test do onboarding, migrado para formato DTCG na mesma data
