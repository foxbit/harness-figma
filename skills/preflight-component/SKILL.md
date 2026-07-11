# Skill: Preflight Component

## Quando usar
Quando um componente precisa ser migrado do arquivo Legado para o
arquivo de Produção — disparado por um item `MIGRAR DO LEGADO` no plano
do `interpreter`, ou por priorização manual a partir de
`migration-backlog.md`. Ver `preflight/PREFLIGHT.md` para o processo
completo e a justificativa do modelo incremental (não big-bang).

## Resumo do procedimento
1. `preflight-planner` lê o componente no Legado como referência,
   propõe reconstrução (nunca duplicação) seguindo
   `COMPONENT_STANDARDS.md` e reaproveitando tokens já existentes
2. Aprovação humana — inclui avaliar riscos de drift visual apontados
   pelo planner
3. `preflight-builder` reconstrói no arquivo de Produção — na primeira
   execução do cliente, a criação do ARQUIVO é ação manual do humano
   (criar no Figma, abrir, rodar o plugin bridge, registrar o
   `File-key` no `PROJECT.md`); o agente cria só a estrutura de
   páginas
4. `documenter` (de produção) atualiza `Status: em revisão` →
   `Status: ativo`

Sempre roda ANTES do `builder` construir a tela que motivou a migração
— nunca durante. Nunca escreve no arquivo Legado.

Detalhes completos: `preflight/PREFLIGHT.md` e os arquivos
`.claude/agents/preflight-*.md`
