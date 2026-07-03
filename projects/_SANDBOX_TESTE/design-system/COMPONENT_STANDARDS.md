<!--
[PREENCHER] Este documento é genérico. Revise cada seção contra as
convenções que já existem nos arquivos Figma reais deste cliente — se a
empresa já usa um padrão de nomenclatura diferente, ajuste aqui em vez de
forçar o padrão abaixo sobre um projeto legado.
-->

# Padrões de Criação de Componentes — [Nome do Cliente]

## Nomenclatura
- Formato: `Categoria/Nome — Variante` (ex: `Card/Product — featured`)
- Nunca usar sufixos ambíguos (`v2`, `New`, `Copy`, `Old`)
- Nome deve descrever FUNÇÃO, não aparência (`Card/Product`, não
  `Card/Blue`)

[PREENCHER — se o cliente já tem convenção própria, documentar aqui e
remover/ajustar a regra acima]

## Uso de variantes (Figma variants) vs. componentes separados
- Se a diferença é de ESTADO (hover, disabled, selecionado, com/sem
  desconto) → variante do mesmo componente
- Se a diferença é de COMPOSIÇÃO (elementos internos diferentes, não só
  estado) → avaliar se é componente novo ou componente composto
- Nunca duplicar um componente inteiro só para mudar uma cor ou texto

## Uso de tokens (obrigatório)
- Nenhum valor de cor, espaçamento, raio ou tipografia pode ser
  hardcoded dentro de um componente — sempre vinculado a variável do
  Figma
- Componente com valor hardcoded é bloqueado para promoção (verificado
  pelo auditor) até correção

## Componentes aninhados
- Se um componente contém outro (ex: Card contém Button), o componente
  interno deve ser uma INSTÂNCIA vinculada ao componente original —
  nunca uma cópia solta
- Isso é o que garante que a extração via MCP reconheça a composição
  corretamente

## Auto Layout (obrigatório)
- Todo componente deve usar Auto Layout — isso é o que permite extração
  estrutural confiável via MCP; componentes com posicionamento livre
  (absolute) geram contexto ambíguo para o modelo

## Responsividade / breakpoints
<!-- Fora de escopo funcional por ora (ver CLAUDE.md, seção "Fora de
escopo"). Campo mantido para não exigir migração de estrutura depois. -->
- Breakpoints documentados: `[nenhum ainda | mobile | tablet | desktop]`

## Documentação mínima obrigatória por componente
Todo componente publicado no design system PRECISA ter, antes de ser
considerado disponível para uso pelo harness:
1. Entrada correspondente em `design-system/components/[nome].md`
   seguindo `_TEMPLATE.md`, com todos os campos preenchidos
   (não genéricos)
2. Pelo menos uma variante marcada como "default"
3. Descrição preenchida no próprio Figma (usada como fallback textual)

## Critério de "pronto para o harness"
Um componente só entra na lista que o interpreter consulta se passar
neste checklist. Componentes legados sem essa documentação ficam
marcados como "não catalogado" pelo auditor e são tratados como se não
existissem até serem documentados.
