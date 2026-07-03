<!-- Jornada de TESTE do harness (_SANDBOX_TESTE) — não é cliente real. -->

# História do Usuário — Registro de Produção Diária (app de obra)

## Persona
Operário/encarregado de obra civil (ex: rede de saneamento/tubulação),
usando o app em campo, pelo celular, durante o expediente.

## Objetivo
Selecionar a obra em que está trabalhando, ver o progresso da sua
produção no período atual (extensão executada vs. a executar) e
registrar a produção do dia. Secundariamente, poder ver e editar seus
próprios dados de perfil (idioma, senha).

## Contexto / gatilho
O operário chega na obra, abre o app, confirma que está na obra certa
(pode haver mais de uma obra ativa) e registra o quanto executou no dia
antes de encerrar o turno.

## Passos esperados
1. **Tela "Minha produção"**: usuário vê seu nome/cargo no topo, seleciona
   a obra num dropdown ("Belavista - Capão Raso"), vê o período vigente
   (De/Até), alterna entre métricas de produção (Extensão, Área,
   Profundidade média, PV) via abas, vê dois indicadores — "A executar"
   (924 m) e "Executado" (15 m) — e toca em "Registrar produção do dia"
2. Navegação por barra inferior fixa com 3 itens: "Minha produção"
   (ativa), "Histórico de registros", "Meus dados"
3. **Tela "Meus dados"** (acessada pela barra inferior): usuário vê/edita
   avatar, nome completo, cargo, e-mail e usuário (somente leitura),
   escolhe idioma de preferência (dropdown, ex: Português), e pode
   alterar a senha (campo senha atual + nova senha, botão "Salvar"
   desabilitado até haver alteração válida)

## Critérios de sucesso
- Usuário consegue trocar de obra sem perder contexto da tela
- Usuário entende visualmente quanto falta executar vs. quanto já
  executou, sem precisar calcular
- Botão "Registrar produção do dia" é a ação primária, sempre visível
  sem rolagem em tela de celular padrão
- Troca de idioma e alteração de senha na tela "Meus dados" são ações
  independentes uma da outra
- "Salvar" (Meus dados) só fica habilitado quando há alteração pendente

## Fora de escopo desta jornada
- Tela "Histórico de registros" (só aparece como item de navegação,
  sem wireframe correspondente nesta jornada)
- Fluxo de logout/troca de conta
- Qualquer tela de outra obra que não "Belavista - Capão Raso"
