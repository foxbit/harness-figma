# Skill: Audit Consistency

## Quando usar
No início de cada sessão de trabalho em um projeto (checagem leve de
sincronização), ou sob demanda quando há suspeita de divergência entre o
Figma real e o `design-system/` documentado.

## Resumo do procedimento
1. Listar componentes reais no Figma (`figma_search_components`)
2. Comparar contra `design-system/components/*.md` oficial (ignorar
   `_draft/` — ainda não promovidos)
3. Reportar componentes não catalogados e entradas `.md` órfãs
4. Checar consistência técnica contra `COMPONENT_STANDARDS.md`: tokens
   hardcoded vs. vinculados (`boundVariables` via `figma_execute` de
   leitura), nomenclatura, Auto Layout COMPLETO (layoutMode,
   itemSpacing, paddings e sizing modes — tudo verificável via
   código), instâncias vs. cópias, possíveis duplicatas, e drift de
   valor entre variáveis reais (`figma_get_variables` com
   `refreshCache: true`) e os `*.tokens.json`

Este processo é somente leitura — nunca corrige automaticamente.

Detalhes completos: `.claude/agents/auditor.md`
