# Skill: Build Screen

## Quando usar
Após o plano do interpreter ser aprovado pelo humano, para construir UMA
tela específica da jornada via MCP no Figma.

## Resumo do procedimento
1. Confirmar file-key de destino contra `PROJECT.md` (regra de
   segurança do `CLAUDE.md`)
2. Receber o trecho do plano referente a esta tela + o
   `journey-state.md` atualizado até aqui
3. Executar por elemento, conforme classificação do plano:
   - REUSO DIRETO → instanciar componente existente
   - NOVA VARIANTE → criar variante dentro do componente pai
   - COMPONENTE NOVO → seguir skill `create-new-component`
4. Em caso de falha parcial, parar e reportar o que já foi criado — não
   tentar recuperar sozinho
5. Ao concluir, relatar em texto o que foi construído — a sessão
   principal usa esse relato para atualizar `journey-state.md` antes da
   próxima tela

Detalhes completos: `.claude/agents/builder.md`
Regra de estado entre telas: `CLAUDE.md`, seção "Estado compartilhado
entre telas de uma mesma jornada"
