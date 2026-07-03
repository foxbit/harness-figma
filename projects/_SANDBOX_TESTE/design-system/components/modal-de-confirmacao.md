<!--
TESTE DE FUMAÇA — projeto _SANDBOX_TESTE. Cobertura AMOSTRAL, não os 618
nós do inventário completo. Ver design-system/components/README.md.
-->

# Modal de Confirmação

## Status
em revisão

## Identidade Figma
- Component key: não há um único componente-fonte no Legado — este é um
  ALVO de consolidação. Os ~16 componentes de nível superior distintos
  que hoje respondem por "Modal confirmação" no arquivo Legado `mcp-test`
  são: `45:22153`, `277:14009`, `278:16558`, `653:42914`, `881:11246`,
  `921:6954`, `1078:15699`, `1081:14348`, `1376:34761`, `1421:12313`,
  `1421:56137`, `1438:80012`, `1450:134730`, `1377:37146`, `771:61693`,
  `762:39540`. Confirmado contra o `onboarding-inventory.md` (Q1); não
  foi rodado `get_node` individual nos 16 nós neste smoke test (fora do
  escopo da amostra) — cada um precisa ser inspecionado pelo
  `preflight-planner` antes da reconstrução, para garantir que a
  variação real de conteúdo (texto de título/corpo/ação por módulo:
  simulados, flashcards, cronômetro, planos de estudo) caiba nas props
  do componente único.
- Localização: espalhados pela página "Componentes" (`11:23284`) do
  arquivo Legado `mcp-test`, sem agrupamento por seção/frame — cada
  instância foi criada solta dentro do módulo que a usa.
- Tipo: componente composto (overlay + card de conteúdo + par de botões
  de ação)

## Propósito
Confirmar com o usuário uma ação irreversível ou destrutiva (ex.:
excluir simulado, excluir plano de estudo, cancelar registro de
cronômetro) antes de executá-la, pausando o fluxo da tela até resposta
explícita.

## Estrutura (composição)
<!-- Estrutura inferida a partir do nome/padrão observado em modais de
confirmação similares no inventário (ex.: "Modal de exclusao",
`1421:73260`, `1487:103792`) — a estrutura interna exata de cada um dos
16 nós de origem não foi levantada nó a nó neste smoke test. O
preflight-planner deve confirmar via get_node antes de construir. -->
- Overlay/backdrop — obrigatório
- Container do modal (card, cornerRadius, fill sólido) — obrigatório
- Ícone de alerta (opcional, conforme o tipo de ação) — opcional
- Título (texto curto, ex.: "Excluir plano de estudo?") — obrigatório
- Corpo/mensagem (texto explicativo da consequência da ação) — obrigatório
- Botão secundário (Buttons/Button, instância) — texto "Cancelar" — obrigatório
- Botão primário/destrutivo (Buttons/Button, instância) — texto de confirmação (ex.: "Excluir", "Confirmar") — obrigatório

## Variantes existentes

| Nome da variante | Quando usar | Diferença estrutural |
|---|---|---|
| default | Confirmação neutra (ex.: "Concluir simulado?") | Botão primário sem ênfase destrutiva |
| destrutivo | Ação que apaga dado permanentemente (ex.: "Excluir plano de estudo?", "Excluir registro de estudo") | Botão primário em cor de alerta/destrutiva + ícone de alerta visível |

<!-- Esta tabela é uma PROPOSTA de consolidação baseada na decisão Q1,
não uma variante já existente e confirmada em algum dos 16 nós — o
preflight-planner deve validar se essa distinção (neutro vs. destrutivo)
de fato aparece nos 16 casos de origem antes de assumir como definitiva. -->

## Props / propriedades configuráveis

| Prop | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| Título | texto | sim | Pergunta curta de confirmação, varia por módulo |
| Mensagem | texto | sim | Explica a consequência da ação |
| Texto do botão primário | texto | sim | Ex.: "Confirmar", "Excluir", "Concluir" |
| Texto do botão secundário | texto | não (default "Cancelar") | Ação de saída sem executar |
| Tipo | enum (`default` / `destrutivo`) | sim | Controla ênfase visual do botão primário e presença do ícone de alerta |

## Tokens utilizados
<!-- Nenhum token sólido de cor está definido no arquivo Legado (ver
design-system/tokens/colors.md desta amostra — só 7 paint styles,
todos gradiente). Tokens abaixo são PROPOSTOS para criação no preflight,
não existem hoje como style/variable nomeada. -->
- Cor: token novo a criar no preflight (ex.: `color/surface/overlay`,
  `color/action/destructive`) — hoje cada um dos 16 nós usa fill sólido
  hardcoded, não levantado individualmente nesta amostra
- Espaçamento: token novo a criar no preflight (padding do card do modal)
- Tipografia: token novo a criar no preflight (título/corpo) — arquivo
  Legado não tem nenhum text style definido (`get_styles` retornou lista
  vazia de `text`)

## Quando usar
Sempre que uma ação do usuário for irreversível ou tiver consequência
relevante (excluir, cancelar processo em andamento, sobrescrever dado) e
precisar de confirmação explícita antes de executar.

## Quando NÃO usar
Não usar para avisos informativos sem ação de confirmação — isso é
"Modal Genérica" (ver `modal-generico.md`, decisão Q6) ou "Toasty"
(notificação temporária não-bloqueante). Não usar para formulários ou
edição de conteúdo — isso são os diversos "Modal de edição"/"Modal de
edicao" observados no inventário (ex.: `635:41008`, `653:40108`), fora
do escopo desta amostra.

## Componentes relacionados
- Similar, mas diferente: `Modal Genérica` (`modal-generico.md`) —
  diferença: Modal Genérica não tem necessariamente um par de ações de
  confirmação/cancelamento, pode ser só informativo
- Similar, mas diferente: `Pop up` (9 usos, Q6) e `Toasty` (7 usos, Q6)
  — mesma lógica de consolidação da Q1, mas não documentados como
  arquivo próprio nesta amostra (ver README.md da pasta)
- Compõe-se de: `Buttons/Button` (instância, já existente no Legado
  como `324:19820`)
- É composto dentro de: telas de simulados, flashcards, cronômetro e
  planos de estudo — todas ainda MIGRAR DO LEGADO (nenhuma reconstruída
  em Produção)

## Histórico
- Criado em: `2026-07-03` — contexto: `onboard-writer`, smoke test do
  onboarding em `_SANDBOX_TESTE`, com base na decisão Q1 registrada em
  `onboarding-decisions.md` (negociada de verdade com o humano, não
  decisão-padrão de teste)
- Última alteração: nenhuma desde a criação
