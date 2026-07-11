# Skill: Build Screen

## Quando usar
Após o plano do interpreter ser aprovado pelo humano, para construir UMA
tela específica da jornada via MCP no Figma.

## Resumo do procedimento
1. Confirmar o arquivo de destino: `fileName` (via `get_metadata`)
   deve corresponder ao arquivo de Produção declarado no `PROJECT.md`
   (regra de segurança do `CLAUDE.md` — este MCP não expõe file-key)
2. Receber o trecho do plano referente a esta tela + o
   `journey-state.md` atualizado até aqui
3. Executar por elemento, conforme classificação do plano:
   - REUSO DIRETO → `clone_node` de uma instância JÁ EXISTENTE do
     componente (não há tool de "criar instância"; se for o primeiro
     uso real do componente, parar e reportar)
   - NOVA VARIANTE → parar e reportar: combinação de variantes exige
     passo manual do humano no Figma (sem `combineAsVariants` neste
     MCP)
   - COMPONENTE NOVO → seguir skill `create-new-component`
4. Em caso de falha parcial, parar e reportar o que já foi criado — não
   tentar recuperar sozinho
5. Ao concluir, relatar em texto o que foi construído — a sessão
   principal usa esse relato para atualizar `journey-state.md` antes da
   próxima tela

Detalhes completos: `.claude/agents/builder.md`
Regra de estado entre telas: `CLAUDE.md`, seção "Estado compartilhado
entre telas de uma mesma jornada"
