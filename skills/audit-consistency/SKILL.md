# Skill: Audit Consistency

## Quando usar
No início de cada sessão de trabalho em um projeto (checagem leve de
sincronização), ou sob demanda quando há suspeita de divergência entre o
Figma real e o `design-system/` documentado.

## Resumo do procedimento
1. Listar componentes reais no Figma via MCP
2. Comparar contra `design-system/components/*.md` oficial (ignorar
   `_draft/` — ainda não promovidos)
3. Reportar componentes não catalogados e entradas `.md` órfãs
4. Checar consistência técnica contra `COMPONENT_STANDARDS.md`: tokens
   hardcoded, nomenclatura, Auto Layout, instâncias vs. cópias,
   possíveis duplicatas

Este processo é somente leitura — nunca corrige automaticamente.

Detalhes completos: `.claude/agents/auditor.md`
