<!--
TESTE DE FUMAÇA — projeto _SANDBOX_TESTE. Cobertura AMOSTRAL, não os 618
nós do inventário completo. Ver design-system/components/README.md.
-->

# Modal Genérico

## Status
em revisão

## Identidade Figma
- Component key: alvo de consolidação, sem componente-fonte único no
  Legado. Os 9 componentes de nível superior distintos hoje nomeados
  `"Modal Genérica"` no arquivo Legado `mcp-test` são: `36:6550`,
  `319:10411`, `679:46706`, `1210:55221`, `1280:74426`, `1344:23409`,
  `1393:197683`, `1448:72386`, `1449:122633`. Confirmado contra
  `onboarding-inventory.md` (Q6); `get_node` individual nos 9 nós não
  foi rodado neste smoke test (fora do escopo da amostra).
- Localização: espalhados pela página "Componentes" (`11:23284`) do
  arquivo Legado `mcp-test`, um por módulo (editor de documento,
  breadcrumb, cronômetro, planos de estudo, etc.).
- Tipo: componente composto (overlay + card de conteúdo livre, sem
  padrão fixo de ação)

## Propósito
Exibir conteúdo informativo em overlay modal quando nenhum dos padrões
mais específicos já catalogados (Modal de Confirmação, Modal de edição)
se aplica — ex.: exibir detalhe expandido de um item, mensagem de
sistema, ou conteúdo auxiliar que precisa de foco temporário da tela.

## Estrutura (composição)
<!-- Estrutura inferida por nome/padrão, não levantada nó a nó nos 9
componentes de origem nesta amostra — preflight-planner deve confirmar
via get_node antes de construir. -->
- Overlay/backdrop — obrigatório
- Container do modal (card, cornerRadius, fill sólido) — obrigatório
- Botão de fechar (X, canto superior) — obrigatório
- Slot de conteúdo (título + corpo livre, varia por módulo) — obrigatório
- Ações (0, 1 ou 2 botões, opcional conforme contexto) — opcional

## Variantes existentes

| Nome da variante | Quando usar | Diferença estrutural |
|---|---|---|
| default | Conteúdo informativo simples, sem ação obrigatória | Só botão de fechar |
| com-acao | Conteúdo que precisa de uma ação única (ex.: "Entendi", "Ver mais") | Adiciona um botão primário |

<!-- Proposta de consolidação baseada na decisão Q6, não confirmada nos
9 nós de origem individualmente. -->

## Props / propriedades configuráveis

| Prop | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| Título | texto | não | Título do conteúdo exibido, se houver |
| Conteúdo | texto/composição livre | sim | Corpo do modal, varia por contexto de uso |
| Mostrar ação | booleano | não (default falso) | Controla se o botão de ação única aparece |
| Texto da ação | texto | não | Só relevante se "Mostrar ação" = verdadeiro |

## Tokens utilizados
<!-- Nenhum token sólido definido no Legado (ver colors.md desta
amostra). Tokens abaixo são propostos para criação no preflight. -->
- Cor: token novo a criar no preflight (ex.: `color/surface/overlay`,
  compartilhado com `Modal de Confirmação`)
- Espaçamento: token novo a criar no preflight
- Tipografia: token novo a criar no preflight — arquivo Legado não tem
  nenhum text style definido

## Quando usar
Para exibir conteúdo em overlay que não se encaixa no padrão de
confirmação de ação destrutiva (isso é `Modal de Confirmação`) nem no
padrão de edição/formulário (isso são os diversos "Modal de edição"
observados no inventário).

## Quando NÃO usar
Não usar quando a intenção é confirmar uma ação irreversível — usar
`Modal de Confirmação` (`modal-de-confirmacao.md`). Não usar para
notificação temporária não-bloqueante — isso é "Toasty" (7 duplicatas,
mesma decisão Q6, não documentado como arquivo próprio nesta amostra).
Não usar para conteúdo de formulário com múltiplos campos — isso são os
diversos "Modal de edição"/"Modal de edicao" do inventário.

## Componentes relacionados
- Similar, mas diferente: `Modal de Confirmação`
  (`modal-de-confirmacao.md`) — diferença: sempre tem par de ações
  cancelar/confirmar, este nem sempre tem ação
- Similar, mas diferente: `Pop up` (7 usos) e `Toasty` (7 usos) — mesma
  decisão de consolidação Q6, não documentados nesta amostra (ver
  README.md da pasta)
- Compõe-se de: `Buttons/Button` (instância), ícone de fechar (a
  confirmar componente de origem no preflight)
- É composto dentro de: telas de editor de documento, planos de estudo,
  cronômetro — todas ainda MIGRAR DO LEGADO

## Histórico
- Criado em: `2026-07-03` — contexto: `onboard-writer`, smoke test do
  onboarding em `_SANDBOX_TESTE`, com base na decisão Q6 registrada em
  `onboarding-decisions.md` (decisão-padrão de teste, não negociada de
  verdade com o humano — numa execução real de cliente, isso exigiria
  negociação como Q1)
- Última alteração: nenhuma desde a criação
