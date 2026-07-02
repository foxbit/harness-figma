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
   (`Categoria/Nome — Variante`)
3. Criar usando Auto Layout, sem valores hardcoded — vincular a tokens
   existentes em `design-system/tokens/*.md`
4. Se o componente contém outros componentes do design system, usar
   instâncias vinculadas, nunca cópias soltas
5. Após criar no Figma, o builder relata o que fez — o documenter então
   cria a entrada em `design-system/components/_draft/[nome].md`
   seguindo `_TEMPLATE.md` (estágio de rascunho, não oficial ainda)
6. Componente só é promovido para oficial após aprovação do validator na
   jornada inteira (ver ordem do fluxo em `CLAUDE.md`)

Detalhes de execução: `.claude/agents/builder.md`
Detalhes de documentação: `.claude/agents/documenter.md`
