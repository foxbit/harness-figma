# Skill: Create New Component

## Quando usar
Quando o plano aprovado classifica um elemento como COMPONENTE NOVO (não
nova variante — para isso ver a seção correspondente em
`.claude/agents/builder.md`).

## Checklist
1. Confirmar, antes de criar, que não há candidato real em
   `design-system/components/*.md` (oficial) — se restar dúvida, parar e
   perguntar em vez de criar
2. Nomear seguindo `design-system/COMPONENT_STANDARDS.md`
   (`Categoria/Nome — Variante`); estética (forma, tipografia,
   espaçamento) segue o `design-system/design.md` — precedência: token
   exato > design.md > julgamento do modelo
3. Criar usando Auto Layout com sizing modes explícitos (via
   `figma_execute`, com a intenção do código no plano aprovado —
   política A' do `CLAUDE.md`), sem valores hardcoded — vincular a
   tokens existentes: fill via `figma_set_fills` + `variableId`,
   demais propriedades via `setBoundVariable` no código. Converter em
   componente com `createComponentFromNode` e conferir
   tamanho/sizing no MESMO bloco
4. Se o componente contém outros componentes do design system, usar
   instâncias vinculadas (`figma_instantiate_component` ou
   `createInstance()` no código), nunca cópias soltas
5. Após criar no Figma, o builder relata o que fez — o documenter então
   cria a entrada em `design-system/components/_draft/[nome].md`
   seguindo `_TEMPLATE.md` (estágio de rascunho, não oficial ainda)
6. Componente só é promovido para oficial após aprovação do validator na
   jornada inteira (ver ordem do fluxo em `CLAUDE.md`)

Detalhes de execução: `.claude/agents/builder.md`
Detalhes de documentação: `.claude/agents/documenter.md`
