<!--
Esta skill é referenciada pelo .claude/agents/interpreter.md — o
conteúdo detalhado do processo já vive lá. Este arquivo existe para
documentar o procedimento de forma reutilizável/consultável fora do
contexto do agente (ex: se você quiser rodar esse raciocínio manualmente
numa sessão comum, sem invocar o subagente).
-->

# Skill: Interpret Wireframe

## Quando usar
Sempre que uma jornada nova (wireframe + user-story.md) precisar virar
um plano de construção. Ver `.claude/agents/interpreter.md` para o
processo completo e o formato de output esperado.

## Resumo do procedimento
1. Ler user-story.md + todas as imagens de wireframe/ em ordem
2. Para cada elemento de cada tela, classificar como REUSO DIRETO /
   NOVA VARIANTE / COMPONENTE NOVO / MIGRAR DO LEGADO contra
   design-system/components/*.md (nunca _draft/) E contra o que já foi
   documentado do legado (onboarding/preflight anteriores — nunca uma
   nova varredura ad-hoc)
3. Documentar candidatos descartados e motivo para cada classificação
4. Apontar elementos recorrentes entre telas da mesma jornada
5. Produzir plano estruturado para aprovação humana — se houver itens
   MIGRAR DO LEGADO, destacá-los no topo: eles exigem preflight ANTES
   do builder construir a tela

Detalhes completos: `.claude/agents/interpreter.md`
