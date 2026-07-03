# Perguntas de Onboarding — `_SANDBOX_TESTE` (mcp-test)

> **TESTE DE FUMAÇA — baseado em inventário PARCIAL** (2 de 75 páginas do
> Legado: `Componentes` com 618 nós catalogados via `scan_nodes_by_types`,
> e `ML-001 - Login e Acesso`). Estas perguntas cobrem só o que está
> documentado em `onboarding-inventory.md`. Não representam um onboarding
> completo — quando as 73 páginas restantes forem varridas, novas rodadas
> de perguntas serão necessárias.
>
> Cada pergunta é objetiva e deve poder ser respondida rapidamente por um
> humano com acesso ao Figma. A negociação (uma pergunta por vez) e o
> registro das respostas acontecem na sessão principal, em
> `onboarding-decisions.md` — este documento só lista as suspeitas.

Prioridade: duplicatas/inconsistências com maior número de ocorrências
(maior impacto potencial em telas futuras) vêm primeiro.

---

## Prioridade 1 — Nomes genéricos duplicados em massa

Estes são os achados de maior impacto: o mesmo nome é usado para dezenas
de componentes de nível superior distintos, o que torna impossível
identificar "qual é o certo" por nome durante o preflight ou a produção.

**Q1.** `"Modal confirmação"` aparece como **~16 componentes de nível
superior distintos** (ex.: ids `45:22153`, `277:14009`, `278:16558`,
`653:42914`, `881:11246`, `921:6954`, `1078:15699`, `1081:14348`,
`1376:34761`, `1421:12313`, `1421:56137`, `1438:80012`, `1450:134730`,
`1377:37146`, `771:61693`, `762:39540`), espalhados por módulos diferentes
(simulados, flashcards, cronômetro, planos de estudo).
Devem ser consolidados em **um único componente parametrizável** (texto/
contexto via prop) no design system novo, ou cada módulo realmente precisa
de uma versão própria por regra de negócio (ex: ações de confirmação
diferentes)?

**Q2.** `"Container"` é usado como nome de **15+ COMPONENT/COMPONENT_SET
distintos** com propósitos visuais completamente diferentes (calendário,
timer/cronômetro, flashcard, admin, "Fechado/Aberto" genérico — ex.:
`653:45128`, `874:16479`, `910:2969`, `969:26421`, `971:27687`,
`1284:75988`, `1370:4466`, `1381:104151`, `1381:74493` — este último
grafado em minúsculo `"container"` —, `1411:72565`, `1448:67866`,
`1449:107772`, `1470:48502`, `1470:48294`). Cada um deve ganhar um nome
específico no design system novo (ex.: "Calendar Event Container",
"Cronômetro / Container Estado"), em vez de todos se chamarem
"Container"?

**Q3.** `"Card"` é usado como nome de **10+ COMPONENT_SETs distintos** em
contextos sem relação entre si (dificuldade de flashcard, status de plano
de estudo, admin, apostilas/simulados). Mesma pergunta de Q2: renomear
cada um com um nome que descreva o contexto, ou manter "Card" genérico e
diferenciar só por propriedades internas?

**Q4.** `"Chip"` aparece como **8 COMPONENT_SETs distintos** com propriedades
de variante diferentes entre si (dificuldade, status de rascunho/publicado,
tipo de material, progresso, cor) — ids `205:3460`, `210:...` (`203:3482`),
`314:...` (`572:31060`), `427:...` (`865:2321`), `461:...` (`910:3183`),
`506:...` (`1297:17977`), `509:...` (`1309:11219`), `548:...`
(`1404:31624`), `615:...` (`1632:62062`). São conceitualmente o mesmo
componente-base "Chip" com propriedades diferentes por tela (o que
sugeriria consolidar em UM component set único com todas as variantes), ou
são conceitos diferentes que devem virar componentes com nomes distintos?

**Q5.** `"Mobile/Tela visao geral"` se repete **7 vezes** com ids
distintos (`697:1402`, `721:20182`, `749:24146`, `795:50907`,
`1381:181136`, `2113:6638`, `2061:21670`), aparentemente uma por módulo
(simulados, flashcards, planos de estudo, cronômetro). Confirmar: são 7
telas de fato distintas que devem manter nomes próprios e específicos no
design system novo (ex.: "Simulados / Mobile / Visão geral"), ou há
duplicação real por cópia indevida do mesmo nome?

**Q6.** `"Modal Genérica"` duplicado **9x** (`36:6550`, `319:10411`,
`679:46706`, `1210:55221`, `1280:74426`, `1344:23409`, `1393:197683`,
`1448:72386`, `1449:122633`), `"Pop up"` duplicado **7x** (`196:3760`,
`317:8299`, `336:11255`, `630:37370`, `679:46553`, `799:51724`,
`952:1886`) e `"Toasty/Default"` duplicado **7x** (`759:38184`,
`762:39819`, `1404:24705`, `1429:130489`, `1429:138766`, `1587:32344`,
`1587:71415`). Mesma linha de pergunta de Q1: consolidar em um componente
único reutilizável por tipo (modal genérico, pop-up, toast), ou manter
múltiplas versões por módulo?

**Q7.** `"Acessar e navegar no material / Mobile"` duplicado **6x**
(`764:58948`, `764:58949`, `771:60639`, `771:60942`, `803:38247`,
`810:56389`). Mesmo padrão de Q5 — são estados/variações reais da mesma
tela mobile do leitor, ou duplicação por engano?

**Q8.** `"Editior de documento"` (grafia com erro de digitação — falta o
"t" antes do "o" final está trocado: "Editior" em vez de "Editor")
aparece **2 vezes com o mesmo nome exato**, ids `36:5932` e `336:24016`.
São a mesma tela duplicada por engano, ou duas versões/estados diferentes
do editor que só não foram renomeados para diferenciá-los?

**Q9.** Dentro do **mesmo** component set `"Card"` (id `749:23237`),
existem **duas variantes com o mesmo valor de propriedade** `Tipo=3 dias`
(ids `749:23238` e `749:23462`). Esse tipo exato de inconsistência
(variantes duplicadas dentro de um set) é a causa mais provável do erro
`"Component set for node has existing errors"` que bloqueou
`get_local_components` para a página inteira. Autorizar investigação
pontual deste component set específico no Figma Desktop para
identificar/corrigir a variante duplicada antes do preflight?

---

## Prioridade 2 — Grafia e nomenclatura inconsistente (typos)

**Q10.** Grafia `"Tiopo="` (deveria ser `"Tipo="`) usada nas variant
properties do component set `"Editor / Menu de ferramentas"` (`52:41474`).
Corrigir para `"Tipo="` no design system novo?

**Q11.** Grafia `"Disbaled"` (deveria ser `"Disabled"`) usada como valor
de `State=` em `"_Tag radio button"` e `"_Tag checkbox"` (`19:1868`,
`19:1905`, dezenas de variantes filhas). Corrigir?

**Q12.** Acentuação inconsistente entre component sets diferentes para o
mesmo conceito de dificuldade: `"Médio"` (`572:31061`) vs. `"Medio"`
(`603:11205`, `649:33393`, `653:12710`); `"Difícil"` (`572:31063`) vs.
`"Dificil"` (`603:11203`, `649:33391`, `653:12720`). Qual grafia deve ser
adotada como padrão único no design system novo?

**Q13.** Capitalização/grafia inconsistente em variantes de card mobile,
todas no mesmo componente `"Card"` (`1407:31681`): `"Tipo=Mobile"`
(`1435:45886`, `1435:45911`), `"Tipo=Mobil"` (typo, `1435:45896`),
`"Tipo=mobile"` minúsculo (`1435:46290`), `"Tipo=Mobile"` (`1435:46063`).
Padronizar para uma única grafia ("Mobile", capitalizado)?

**Q14.** Grafia `"Conometro"` (typo, faltando o "r" de "Cronometro") em
`"Mobile=Conometro finalizado"` (`1710:39680`). Corrigir?

**Q15.** Ao longo de toda a área de cronômetro/pomodoro, as grafias
`"Cronometro"` (sem acento) e `"Cronômetro"` (com acento) são usadas
alternadamente para o mesmo conceito, às vezes no mesmo component set
(ex.: `1535:32958` — set chamado `"Cronômetro"` com variante
`"Tipo=Cronometro simples, Estado=Idle"` sem acento). Definir grafia
oficial única para uso em todo o design system?

**Q16.** Componente `"Poistit"` (`88:186989`) — nome não corresponde a
nenhuma palavra reconhecível em português (parece termo de outro idioma,
possivelmente deixado por engano de um plugin/template). Confirmar com o
time do cliente se este componente ainda está em uso ou pode ser
descartado do escopo de migração.

**Q17.** Nome de component set contém quebra de linha literal:
`"Período de estudo não definido clique para\nconfigurar"`
(`1485:24750`). Renomear para um nome curto sem quebra de linha (ex.:
"Período de estudo — CTA configurar")?

---

## Prioridade 3 — Nomenclatura de variant properties

**Q18.** Diferentes component sets usam prefixos de propriedade
distintos para conceitos semanticamente parecidos de estado/variação:
`Tipo=`, `Status=`, `State=`, `Pressed=`, `Checked=`, `Usuario=`,
`Device=`, `Mobile=`, `Estágio=`, `Admin=` — e em pelo menos dois casos
(`Breadcrumb`, id `319:17221`, e `Chip`, id `1404:31624`) a propriedade
nunca foi renomeada e ainda usa o padrão default do Figma
(`Property 1=Default/Variant2/Variant3`). Além disso, o mesmo conceito
de dificuldade em cards de admin usa `Tipo=` em um set (`649:33392`) e
`Admin=` em outro (`653:13676`). O design system novo deve padronizar um
nome de propriedade único por conceito (ex.: sempre `Estado=` para
interação, sempre `Tipo=` para variação visual/conteúdo), com uma tabela
de mapeamento antigo → novo? Isso entra no escopo do preflight?

---

## Prioridade 4 — Tokens e estilos inconsistentes

**Q19.** O arquivo legado tem **apenas 7 paint styles, todos
`GRADIENT_LINEAR`** — nenhum paint style sólido, nenhum text style,
nenhum effect style definido. Confirmar que cores sólidas, tipografia e
sombras usadas nas telas são hardcoded (sem token/style associado), e que
a criação de tokens sólidos, text styles e effect styles é trabalho novo
do preflight (não uma "migração", porque não existe equivalente a
migrar no legado)?

**Q20.** Três variáveis na única coleção do arquivo não parecem tokens de
design: `Title` (STRING, valor `"Gestão de conteúdo"`), `String` (STRING,
valor placeholder `"String value"` não substituído) e `Pergunta` (STRING,
valor é o enunciado completo de uma questão de prova). Confirmar que
essas 3 variáveis são resíduo de conteúdo/teste e devem ser descartadas do
design system novo, ou se têm algum uso funcional real que precisa ser
preservado?

**Q21.** Duas variáveis de cor destoam do padrão de nomenclatura
`"Estilos de formatação/[Nome]"` usado pelas demais: `" Sem registro"`
(tem espaço em branco antes do nome) e `"Green light"` (em inglês, único
nome não-português da coleção). Renomear ambas para seguir o padrão
`"Estilos de formatação/[Nome]"` em português, ou são exceções
intencionais (ex.: `Green light` usado por um dev externo)?

**Q22.** A escala de opacidade das variáveis de cor está incompleta:
`Verde Claro` tem par `50`/`100`, `Azul Claro` tem par `50`/`100`, mas
`Verde escuro` só tem `100` (sem `50`), e `Amarelo`, `Âncora` e
`Green light` não têm nenhuma variante de opacidade. O design system novo
deve padronizar uma escala de opacidade (`50`/`100`) para todas as cores
base, ou manter só o que for necessário caso a caso?

---

## Prioridade 5 — Estrutura de página e conteúdo (página ML-001)

**Q23.** A página `"ML-001 - Login e Acesso"` contém, além das 2
instâncias de `"Login"`, instâncias completas de telas de outros módulos:
`"Pagina demo"` (dashboard/biblioteca, `207:5135`), `"Início"` (boas-vindas
pós-login, `356:25839`) e `"Acessar e navegar no material"`
(leitor/dashboard de cursos, `369:38658`). Quando o restante das 73
páginas do arquivo for varrido, essas telas devem ser reclassificadas nas
páginas/jornadas correspondentes, e a jornada de Login no design system
novo deve conter só as 2 instâncias de `"Login"`?

**Q24.** As duas instâncias de `"Login"` têm textos de boas-vindas
diferentes por sobrescrita: `164:3571` exibe **"Bem-vindo ao portal de
gestão!"**, mas o nome interno do nó de texto ainda diz
`"Bem-vindo ao portal do estudante!"` (não foi atualizado); já `310:6788`
exibe e nomeia corretamente `"Bem-vindo ao portal do estudante!"`. São
duas variantes intencionais do mesmo componente de Login (persona
Estudante vs. persona Gestor/Admin, que deveriam virar uma variant
property `Persona=` no design system novo), ou `164:3571` é conteúdo de
teste esquecido/erro a ignorar na migração?

**Q25.** Hint texts e texto de checkbox no formulário de Login estão em
inglês, não traduzidos, enquanto o resto da tela está em português:
`"This is a hint text to help user."` (ambos campos E-mail e Senha) e
`"Save my login details for next time."` (checkbox "Lembrar"). Essas
strings devem ser traduzidas para PT-BR como parte da reconstrução no
design system novo, ou são placeholders que o time de produto do cliente
ainda vai substituir por copy real (fora do escopo do design system)?

---

## Observação geral — Auto Layout (não é uma pergunta por componente)

A conexão MCP usada nesta varredura não expõe o campo `layoutMode` em
nenhum nó consultado (nem via `get_node`, nem `get_nodes_info`). Para a
instância `Login` inspeccionada em detalhe, frames de conteúdo (`Card`,
`Content`, `Input`) têm `padding` não-zero coerente com Auto Layout, mas
isso é inferência, não confirmação. Elementos decorativos de fundo
(`Blur`/ELLIPSE, `Imagem`/RECTANGLE, `Vector`) têm coordenadas absolutas
sobrepostas, típico de posicionamento livre — também inferência.

Recomendação operacional: o **preflight**, ao reconstruir qualquer
componente migrado do legado (não só os catalogados aqui), deve validar
`layoutMode` manualmente no Figma Desktop antes de assumir a estrutura —
esta varredura não pode confirmar isso de forma determinística para
nenhum dos 618+ nós da página Componentes nem para os 229 frames da
página ML-001. Isso vale como alerta geral de processo, não como uma
pergunta por componente.

---

## Resumo de contagem (para priorização na negociação)

| Prioridade | Nº de perguntas | Tema |
|---|---|---|
| 1 | 9 (Q1–Q9) | Duplicatas de nome genérico em massa (maior impacto) |
| 2 | 8 (Q10–Q17) | Typos e grafia inconsistente |
| 3 | 1 (Q18) | Padrão de nome de variant property |
| 4 | 4 (Q19–Q22) | Tokens/estilos (paint styles, variáveis) |
| 5 | 3 (Q23–Q25) | Estrutura de página / conteúdo do login |
| — | 1 nota | Auto Layout não verificável (observação geral) |

Total: **25 perguntas objetivas** + 1 observação geral, baseadas
exclusivamente no inventário parcial (2/75 páginas). Um onboarding
completo deste cliente vai gerar rodadas adicionais de perguntas quando
as 73 páginas restantes forem varridas pelo `onboard-scanner`.
