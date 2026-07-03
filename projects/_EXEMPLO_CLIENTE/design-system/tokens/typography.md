<!--
[PREENCHER] Formato DTCG — ver colors.md para a explicação completa da
convenção adotada (primitivo vs. semântico, par com .tokens.json).

Primitivos aqui = famílias de fonte (`fontFamily`). Semânticos = tiers de
uso (`typography`, tipo composto DTCG: fontFamily + fontSize + fontWeight
+ lineHeight + letterSpacing), cada um referenciando um primitivo de
fonte. Tiers sugeridos abaixo (display/heading/body/label/caption) são
um ponto de partida razoável, não uma imposição — ajustar a quantidade
de tiers ao que o legado realmente usa, mas manter a nomenclatura
semântica (nunca nomear um tier "24px-bold").
-->

# Tokens — typography

## Primitivos (famílias de fonte)

| Nome | `$type` | `$value` | `$description` |
|---|---|---|---|
| `typography.primitive.font-heading` | `fontFamily` | `["[PREENCHER]", "sans-serif"]` | Fonte usada em títulos |
| `typography.primitive.font-body` | `fontFamily` | `["[PREENCHER]", "sans-serif"]` | Fonte usada em corpo de texto |

## Semânticos (tiers, tipo composto `typography`)

| Nome | `$type` | `fontFamily` | `fontSize` | `fontWeight` | `lineHeight` | `letterSpacing` | `$description` |
|---|---|---|---|---|---|---|---|
| `typography.display-lg` | `typography` | `{typography.primitive.font-heading}` | `[PREENCHER]` | `[PREENCHER]` | `[PREENCHER]` | `[PREENCHER]` | Maior destaque de título (hero, telas de abertura) |
| `typography.heading-lg` | `typography` | `{typography.primitive.font-heading}` | `[PREENCHER]` | `[PREENCHER]` | `[PREENCHER]` | `[PREENCHER]` | Título de seção principal |
| `typography.heading-md` | `typography` | `{typography.primitive.font-heading}` | `[PREENCHER]` | `[PREENCHER]` | `[PREENCHER]` | `[PREENCHER]` | Título de subseção |
| `typography.body-lg` | `typography` | `{typography.primitive.font-body}` | `[PREENCHER]` | `[PREENCHER]` | `[PREENCHER]` | `[PREENCHER]` | Corpo de texto em destaque |
| `typography.body-md` | `typography` | `{typography.primitive.font-body}` | `[PREENCHER]` | `[PREENCHER]` | `[PREENCHER]` | `[PREENCHER]` | Corpo de texto padrão |
| `typography.label-caps` | `typography` | `{typography.primitive.font-body}` | `[PREENCHER]` | `[PREENCHER]` | `[PREENCHER]` | `[PREENCHER]` | Rótulos curtos, geralmente caixa-alta |
| `typography.caption` | `typography` | `{typography.primitive.font-body}` | `[PREENCHER]` | `[PREENCHER]` | `[PREENCHER]` | `[PREENCHER]` | Texto de apoio, legendas, metadados |

## Histórico
- Criado em: `[PREENCHER]` — origem: `[onboarding | preflight — nome do componente]`
- Última alteração: `[PREENCHER]`
