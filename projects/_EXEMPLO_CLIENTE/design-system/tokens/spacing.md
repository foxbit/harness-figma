<!--
[PREENCHER] Formato DTCG — ver colors.md para a explicação completa.
`$type: dimension`. Simplificação pragmática: `$value` como string
("16px"), não o objeto {value, unit} da spec mais recente — mesma
justificativa de colors.md (spec em draft, string é o que a maioria das
ferramentas aceita hoje).

Primitivos = escala bruta encontrada no legado (ex: grid de 4px ou 8px,
o que o cliente realmente usa — não impor 8px se o legado usa 4px).
Semânticos = papéis de uso (xs/sm/md/lg/xl), cada um referenciando um
degrau da escala primitiva.
-->

# Tokens — spacing

## Primitivos (escala bruta)

| Nome | `$type` | `$value` | `$description` |
|---|---|---|---|
| `spacing.primitive.[PREENCHER — ex: 100]` | `dimension` | `[PREENCHER — ex: "4px"]` | [PREENCHER] |

## Semânticos

| Nome | `$type` | `$value` (referência) | `$description` |
|---|---|---|---|
| `spacing.xs` | `dimension` | `{spacing.primitive.[PREENCHER]}` | Micro-espaçamentos, margem interna de ícone |
| `spacing.sm` | `dimension` | `{spacing.primitive.[PREENCHER]}` | Espaçamento entre elementos relacionados (label + input) |
| `spacing.md` | `dimension` | `{spacing.primitive.[PREENCHER]}` | Espaçamento padrão entre componentes de um grupo |
| `spacing.lg` | `dimension` | `{spacing.primitive.[PREENCHER]}` | Padding interno de cards/containers principais |
| `spacing.xl` | `dimension` | `{spacing.primitive.[PREENCHER]}` | Margens grandes, espaçamento entre seções |

## Histórico
- Criado em: `[PREENCHER]` — origem: `[onboarding | preflight — nome do componente]`
- Última alteração: `[PREENCHER]`
