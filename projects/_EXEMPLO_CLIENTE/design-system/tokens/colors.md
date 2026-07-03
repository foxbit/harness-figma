<!--
[PREENCHER] Formato adotado: W3C Design Tokens Community Group (DTCG) —
ver https://www.designtokens.org/TR/drafts/format/. Este .md é a versão
narrativa/tabular, pensada para leitura humana e de agente; o par
machine-readable fica em `colors.tokens.json` (mesma pasta), gerado a
partir deste mesmo conteúdo — nunca o contrário.

Duas camadas obrigatórias, nunca misturar:
1. PRIMITIVOS — valores brutos encontrados no Figma (via variável, se já
   existir, ou hardcoded no legado, se não existir formalmente). Nomeados
   por characterização do valor (ex: `blue-500`), não por papel de uso.
2. SEMÂNTICOS — papéis de uso (`primary`, `secondary` etc.), cada um
   referenciando um primitivo via `{color.primitive.nome}`. É isso que
   `interpreter`/`builder` consultam — NUNCA um primitivo diretamente.

Simplificação pragmática desta versão: `$value` de cor é uma string hex
(`"#RRGGBB"`), não o objeto estruturado `{colorSpace, components, hex}`
que a spec mais recente do DTCG define — a spec ainda está em draft
("não implemente esta versão"), e string hex é o que a maioria das
ferramentas reais (Style Dictionary, Tokens Studio) aceita hoje. Revisar
se a spec formal estabilizar.

Papéis semânticos mínimos esperados (adicionar mais se o cliente
precisar, nunca remover sem motivo): primary, secondary, tertiary,
neutral, canvas, surface, hairline, on-primary, success, warning, error.
-->

# Tokens — colors

## Primitivos

| Nome | `$type` | `$value` | `$description` |
|---|---|---|---|
| `color.primitive.[PREENCHER]` | `color` | `#[PREENCHER]` | [PREENCHER — de onde veio: variável do Figma / hardcoded no nó X] |

## Semânticos

| Nome | `$type` | `$value` (referência) | `$description` |
|---|---|---|---|
| `color.primary` | `color` | `{color.primitive.[PREENCHER]}` | Cor principal da marca — CTAs primários, destaques |
| `color.secondary` | `color` | `{color.primitive.[PREENCHER]}` | Textos secundários, ícones de apoio |
| `color.tertiary` | `color` | `{color.primitive.[PREENCHER]}` | Interações críticas, estados ativos |
| `color.neutral` | `color` | `{color.primitive.[PREENCHER]}` | Fundos secundários, áreas de baixo contraste |
| `color.canvas` | `color` | `{color.primitive.[PREENCHER]}` | Fundo de página |
| `color.surface` | `color` | `{color.primitive.[PREENCHER]}` | Fundo de cards, modais, containers |
| `color.hairline` | `color` | `{color.primitive.[PREENCHER]}` | Bordas finas de 1px, divisores |
| `color.on-primary` | `color` | `{color.primitive.[PREENCHER]}` | Texto sobre fundo primary (alto contraste) |
| `color.success` | `color` | `{color.primitive.[PREENCHER]}` | Estados de sucesso/confirmação |
| `color.warning` | `color` | `{color.primitive.[PREENCHER]}` | Estados de atenção |
| `color.error` | `color` | `{color.primitive.[PREENCHER]}` | Estados de erro/destrutivos |

## Histórico
- Criado em: `[PREENCHER]` — origem: `[onboarding | preflight — nome do componente]`
- Última alteração: `[PREENCHER]`
