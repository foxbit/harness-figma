<!--
TEMPLATE — copie este arquivo para components/[nome-do-componente].md
(ou components/_draft/[nome].md se ainda não promovido) e preencha todos
os campos. Não deixe campos genéricos ou vazios — o interpreter e o
auditor dependem de conteúdo específico para funcionar bem.
-->

# [Nome do Componente]

## Status
<!--
- em revisão → documentado pelo onboarding, ainda NÃO existe no
  arquivo de Produção. interpreter NÃO oferece como reuso direto —
  trata como candidato a MIGRAR DO LEGADO.
- ativo → já reconstruído no arquivo de Produção (via preflight ou
  criado direto em produção) e promovido pelo documenter. Disponível
  para reuso direto.
- deprecated → existiu como ativo, foi substituído. Nunca oferecido
  como reuso, mas mantido documentado para não quebrar referências
  antigas.
-->
[PREENCHER]

## Identidade Figma
- Component key: `[PREENCHER — chave do componente principal no Figma]`
- Localização: `[PREENCHER — página/frame no arquivo Figma]`
- Tipo: `[PREENCHER — componente simples | componente composto]`

## Propósito
<!-- Uma frase objetiva: para que serve, em que contexto de jornada
aparece. NÃO descrever aparência aqui — isso é o Figma que mostra. -->
[PREENCHER]

## Estrutura (composição)
<!-- Lista dos elementos internos, na ordem em que aparecem. Se este
componente contém outros componentes do design system, referenciar
explicitamente. -->
- [Elemento 1] — obrigatório | opcional
- [Elemento 2] — obrigatório | opcional

## Variantes existentes

| Nome da variante | Quando usar | Diferença estrutural |
|---|---|---|
| default | [PREENCHER] | [PREENCHER] |

## Props / propriedades configuráveis

| Prop | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| [PREENCHER] | texto/imagem/booleano/etc | sim/não | [PREENCHER] |

## Tokens utilizados
<!-- Nomes SEMÂNTICOS de tokens (formato DTCG, ver design-system/tokens/),
nunca valores hex/px soltos e nunca o nome do primitivo bruto — ex:
"color.primary", não "#1A1C1E" nem "color.primitive.blue-500". Se algum
valor deste componente ainda não tem token semântico correspondente,
registrar isso explicitamente como pendência (não inventar um token só
para preencher o campo). -->
- Cor: `[PREENCHER — ex: color.surface]`
- Espaçamento: `[PREENCHER — ex: spacing.lg]`
- Raio: `[PREENCHER — ex: radius.md]`
- Tipografia: `[PREENCHER — ex: typography.body-md]`

## Quando usar
[PREENCHER — critério objetivo de aplicabilidade]

## Quando NÃO usar
<!-- Campo mais importante para evitar duplicação futura. Seja
específico: cite componentes parecidos que NÃO são este. -->
[PREENCHER]

## Componentes relacionados
- Similar, mas diferente: `[nome]` — diferença: `[PREENCHER]`
- Compõe-se de: `[lista de sub-componentes, se houver]`
- É composto dentro de: `[lista de componentes que usam este]`

## Histórico
- Criado em: `[data]` — contexto: `[jornada/tarefa que originou]`
- Última alteração: `[data]` — `[o que mudou]`
