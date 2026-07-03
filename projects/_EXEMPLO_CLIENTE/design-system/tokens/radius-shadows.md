<!--
[PREENCHER] Formato DTCG — ver colors.md para a explicação completa.
Dois tipos neste arquivo: `dimension` (radius) e o tipo composto
`shadow` (color + offsetX + offsetY + blur + spread). Mesma lógica
primitivo→semântico das demais.
-->

# Tokens — radius & shadows

## Radius

### Primitivos

| Nome | `$type` | `$value` | `$description` |
|---|---|---|---|
| `radius.primitive.[PREENCHER]` | `dimension` | `[PREENCHER — ex: "4px"]` | [PREENCHER] |

### Semânticos

| Nome | `$type` | `$value` (referência) | `$description` |
|---|---|---|---|
| `radius.sm` | `dimension` | `{radius.primitive.[PREENCHER]}` | Elementos pequenos: checkbox, tag, tooltip |
| `radius.md` | `dimension` | `{radius.primitive.[PREENCHER]}` | Botões, inputs, cards pequenos |
| `radius.lg` | `dimension` | `{radius.primitive.[PREENCHER]}` | Cards principais, modais, containers de conteúdo |
| `radius.full` | `dimension` | `{radius.primitive.[PREENCHER] — geralmente "9999px"}` | Avatares, chips, botões pílula |

## Shadows (tipo composto `shadow`)

| Nome | `$type` | `color` | `offsetX` | `offsetY` | `blur` | `spread` | `$description` |
|---|---|---|---|---|---|---|---|
| `shadow.elevation-1` | `shadow` | `{color.primitive.[PREENCHER]}` | `[PREENCHER]` | `[PREENCHER]` | `[PREENCHER]` | `[PREENCHER]` | Elevação sutil (card sobre canvas) |
| `shadow.elevation-2` | `shadow` | `{color.primitive.[PREENCHER]}` | `[PREENCHER]` | `[PREENCHER]` | `[PREENCHER]` | `[PREENCHER]` | Elevação de destaque (modal, popover) |

<!-- Se o legado não tiver NENHUM effect style/sombra definida (caso comum
em arquivos sem tokens formais), registrar aqui "nenhuma sombra
catalogada" em vez de inventar valores — mesma disciplina de nunca criar
conteúdo sem referência visual real. -->

## Histórico
- Criado em: `[PREENCHER]` — origem: `[onboarding | preflight — nome do componente]`
- Última alteração: `[PREENCHER]`
