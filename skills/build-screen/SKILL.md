# Skill: Build Screen

## Quando usar
Após o plano do interpreter ser aprovado pelo humano, para construir UMA
tela específica da jornada via MCP no Figma.

## Resumo do procedimento
1. Confirmar o arquivo de destino: `currentFileKey` (via
   `figma_get_status`) deve corresponder ao `File-key` de Produção
   declarado no `PROJECT.md` (regra de segurança do `CLAUDE.md`)
2. Receber o trecho do plano referente a esta tela + o
   `journey-state.md` atualizado até aqui
3. Executar por elemento, conforme classificação do plano:
   - REUSO DIRETO → `figma_instantiate_component` (componentKey +
     nodeId de `figma_search_components` da MESMA sessão; funciona
     mesmo sem instância pré-existente; não usar parentId de frame
     com Auto Layout — ver erros conhecidos do `CLAUDE.md`)
   - NOVA VARIANTE → `figma_create_component_set` (100% via MCP, sem
     passo manual)
   - COMPONENTE NOVO → seguir skill `create-new-component`
3a. Após QUALQUER timeout de escrita: verificar o estado real no Figma
   antes de retentar — a operação pode ter sido aplicada (erro nº 1 do
   `CLAUDE.md`); retry cego duplica elementos
4. Em caso de falha parcial, parar e reportar o que já foi criado — não
   tentar recuperar sozinho
5. Ao concluir, relatar em texto o que foi construído — a sessão
   principal usa esse relato para atualizar `journey-state.md` antes da
   próxima tela

Detalhes completos: `.claude/agents/builder.md`
Regra de estado entre telas: `CLAUDE.md`, seção "Estado compartilhado
entre telas de uma mesma jornada"
