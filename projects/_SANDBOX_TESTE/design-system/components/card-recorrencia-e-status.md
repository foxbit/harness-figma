<!--
TESTE DE FUMAÇA — projeto _SANDBOX_TESTE. Cobertura AMOSTRAL, não os 618
nós do inventário completo. Ver design-system/components/README.md.
-->

# Card — Recorrência e Status (nome provisório)

<!-- Nome de arquivo/título é uma proposta de renomeação (decisão Q3):
o nome original no Legado é apenas "Card", igual a 10+ outros
component sets sem relação entre si. Este título específico descreve o
melhor entendimento possível do conteúdo observado nas variantes, mas
NÃO foi confirmado com o time de produto do cliente (neste smoke test
não há cliente real) — um onboarding real deveria validar este nome
antes de torná-lo definitivo. -->

## Status
em revisão

## Identidade Figma
- Component key: `749:23237` (component set "Card", confirmado ao vivo
  via `get_node` nesta sessão — arquivo Legado `mcp-test` ainda
  acessível)
- Localização: página "Componentes" (`11:23284`) do arquivo Legado
  `mcp-test`, próximo a outros nós com prefixo `749:*` (`749:22127`
  "Cabecalho", `749:21965` "Card mobile", `749:22132` "CaretDown") —
  sugere que este set pertence ao mesmo agrupamento/módulo que esses
  vizinhos, mas a página não tem organização por frame/seção que
  confirme isso estruturalmente.
- Tipo: componente composto (component set com 7 variantes filhas)

## Propósito
<!-- Propósito inferido pelos nomes de variante, não confirmado com
descrição no Figma (campo "Descrição preenchida no próprio Figma", que
COMPONENT_STANDARDS.md exige e este componente do Legado NÃO tem). -->
Exibir um item recorrente (aparentemente um plano/rotina de
estudo ou revisão) mostrando sua periodicidade (diária, a cada 3 dias,
semanal) e/ou seu status (arquivado, aberto), com pelo menos uma
variante adicional de dificuldade ("Facil") cuja relação com as demais
não é clara a partir do nome sozinho.

## Estrutura (composição)
<!-- get_node retornou uma árvore muito grande (61.004 caracteres) para
os 7 filhos deste set; a estrutura interna completa de cada variante
não foi lida por completo nesta amostra (custo desproporcional para um
smoke test) — apenas confirmada a existência e os nomes dos 7 nós
filhos via grep sobre o retorno bruto do MCP. -->
- Card (COMPONENT_SET, `749:23237`) — obrigatório
  - Conteúdo interno não detalhado nesta amostra — preflight-planner
    deve rodar `get_node` completo (ou em fatias) antes de reconstruir

## Variantes existentes

| Nome da variante (Legado, literal) | id | Quando usar | Observação |
|---|---|---|---|
| Tipo=diaria | `749:21941` | Item com recorrência diária | — |
| Tipo=3 dias | `749:23238` | Item com recorrência a cada 3 dias | **Duplicada** — ver abaixo |
| Tipo=3 dias | `749:23462` | Mesmo valor de propriedade que a linha acima | **Duplicada** — variante irmã com o mesmo `Tipo=3 dias` dentro do mesmo set. Confirmado ao vivo via `get_node` nesta sessão (ambos os ids `749:23238` e `749:23462` existem como filhos diretos de `749:23237`). Esta é a inconsistência apontada na Q9 como causa mais provável do erro `"Component set for node has existing errors"` que bloqueou `get_local_components` para a página inteira |
| Tipo=Semanal | `749:23252` | Item com recorrência semanal | — |
| Tipo=Arquivados | `749:23825` | Item arquivado (fora do fluxo ativo) | Mistura conceito de status com as demais variantes de periodicidade |
| Tipo=Aberto | `749:23344` | Item em aberto (fluxo ativo) | Idem — conceito de status, não periodicidade |
| Tipo=Facil | `749:23517` | Não confirmado | Não foi possível determinar, só pelo nome, por que uma variante de dificuldade está no mesmo set que periodicidade/status. Pode ser erro de organização do Legado (variante que deveria estar num set de dificuldade separado, ex.: o "Chip"/"Card" de dificuldade de flashcard visto em outros ids como `572:31060`) — **não decidido aqui**, sinalizado para o `preflight-planner` avaliar antes da reconstrução, por não haver pergunta/decisão registrada especificamente sobre isso em `onboarding-decisions.md`

## Props / propriedades configuráveis

| Prop | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| Tipo | enum | sim | Hoje mistura periodicidade (diaria/3 dias/Semanal), status (Arquivados/Aberto) e possivelmente dificuldade (Facil) numa única propriedade — ver observação de Q18 abaixo |

<!--
Decisão Q18 aplicada: o design system novo deve padronizar um nome de
propriedade único por conceito (sempre "Tipo=" para variação
visual/conteúdo, sempre "Estado=" para interação). Isso sugere que este
componente, ao ser reconstruído no preflight, provavelmente precisa ser
SEPARADO em propriedades distintas (ex.: "Periodicidade=" e "Estado=")
em vez de uma única "Tipo=" sobrecarregada — mas essa separação
estrutural específica não foi objeto de nenhuma pergunta Q1-Q25, então
não está decidida aqui. Fica registrada como candidato a pauta do
preflight-planner, não como decisão já tomada pelo onboard-writer.
-->

## Tokens utilizados
- Cor: nenhum token sólido definido no Legado (ver
  `design-system/tokens/colors.md` desta amostra) — a definir no
  preflight
- Espaçamento: não levantado nesta amostra (estrutura interna completa
  não lida)
- Tipografia: não levantado nesta amostra

## Quando usar
Quando a tela precisar exibir um item recorrente de estudo/revisão com
sua periodicidade e/ou status visível em formato de card. Critério de
aplicabilidade exato depende da resolução do problema de propriedade
sobrecarregada acima — não usar como referência definitiva sem
confirmação do preflight-planner.

## Quando NÃO usar
Não confundir com os demais 10+ component sets também chamados "Card"
no Legado (decisão Q3 — todos precisam de nome específico, este é só
um deles). Em particular, não confundir com o "Card" de dificuldade de
flashcard puro (ex.: `572:31060` "Chip" ou `653:12709` "Card" com
`Tipo=Facil/Medio/Dificil`), que é conceitualmente mais simples (só
dificuldade, sem periodicidade/status misturados).

## Componentes relacionados
- Similar, mas diferente: `749:21965` "Card mobile" (variantes
  Tipo=Medio/Dificil/Facil) — mesma família de dificuldade, mas versão
  mobile, sem as variantes de periodicidade/status deste componente
- Similar, mas diferente: outros 9+ component sets "Card" catalogados em
  `onboarding-inventory.md` (Q3), nenhum documentado nesta amostra
- É composto dentro de: não confirmado nesta amostra — nenhuma tela da
  página ML-001 (a única com estrutura de tela levantada em detalhe
  neste smoke test) referencia este componente

## Histórico
- Criado em: `2026-07-03` — contexto: `onboard-writer`, smoke test do
  onboarding em `_SANDBOX_TESTE`, com base nas decisões Q9 (negociada de
  verdade — autoriza investigação da variante duplicada antes do
  preflight) e Q3 (decisão-padrão de teste — renomear "Card" com nome
  específico de contexto). Confirmado ao vivo via `get_node` nesta
  sessão que a duplicata `Tipo=3 dias` (`749:23238` / `749:23462`) de
  fato existe no arquivo Legado atual.
- Última alteração: nenhuma desde a criação
