# Inventário de Onboarding — `_SANDBOX_TESTE` (mcp-test)

> **ATENÇÃO — ESTE É UM INVENTÁRIO PARCIAL DE TESTE DE FUMAÇA (SMOKE TEST).**
> Escopo reduzido deliberadamente para validar o processo do `onboard-scanner`
> — **NÃO é um onboarding real completo**. O arquivo Legado `mcp-test` tem
> **75 páginas no total**; este inventário cobre **apenas 2 páginas**:
> - `Componentes` (id `11:23284`)
> - `   ↳ ML-001 - Login e Acesso ✔️ ✔️✔️` (id `164:3568`), sub-página de
>   `Modulo 0: Inicio` (id `164:3569`)
>
> As outras 73 páginas (Biblioteca Digital, Editor de documento, Leitor
> Digital, Flashcards, Simulados, Guia de estudos, Drafts, jornadas
> PP2-24/PP-619 etc.) **não foram varridas** e não estão representadas aqui.
> Um onboarding real deve repetir este processo para as páginas restantes.

---

## 0. Confirmação de arquivo (regra de segurança)

- `get_metadata` retornou `fileName: "mcp-test"`.
- `PROJECT.md` de `_SANDBOX_TESTE` declara o Legado como `mcp-test`.
- **Confirmado**: arquivo aberto no Figma Desktop corresponde ao Legado
  declarado. Prosseguiu-se com a varredura (somente leitura).
- `pageCount` total do arquivo: **75** (lista completa de páginas obtida via
  `get_metadata`, não reproduzida aqui na íntegra — fora do escopo deste
  teste).

---

## 1. Página "Componentes" (id `11:23284`)

### 1.1 Tentativa via `get_local_components`

Erro retornado (verbatim):

```
in get_variantProperties: Component set for node has existing errors
```

Conforme processo documentado, isso é um **erro conhecido de dado
inconsistente no arquivo legado** (component set com variant properties
corrompidas), não falha de conexão MCP. O erro não identifica qual
component set específico está corrompido — a mensagem é genérica para
o arquivo inteiro. **Catalogação alternativa** foi feita via
`scan_nodes_by_types` (tipos `COMPONENT` e `COMPONENT_SET`), conforme
abaixo.

### 1.2 Catalogação alternativa via `scan_nodes_by_types`

Retornou **618 nós** do tipo `COMPONENT` ou `COMPONENT_SET` na página
Componentes. Listagem literal na ordem retornada pela ferramenta
(profundidade/ordem de documento — um `COMPONENT_SET` costuma ser seguido
na lista pelos seus `COMPONENT` variantes filhos, mas isso é uma
observação de padrão, não uma garantia estrutural verificada nó a nó;
nenhuma hierarquia foi inferida manualmente). Formato: `id — nome — tipo`.

```
154:27732 — Atualizações — COMPONENT
207:4606 — Pagina demo — COMPONENT
231:17017 — Acessar e navegar no material — COMPONENT
337:20275 — Tela de anotações — COMPONENT
356:25838 — Início — COMPONENT
356:26652 — Leitor — COMPONENT
369:42560 — Modulo do curso — COMPONENT
36:5932 — Editior de documento — COMPONENT
16:9509 — Gestão de conteúdo — COMPONENT
336:24016 — Editior de documento — COMPONENT
1139:19380 — Realizacao do simulado — COMPONENT
856:21071 — Dashboard - Simulados — COMPONENT
870:14979 — Listagem meus simulados — COMPONENT
881:1367 — Criaçao do simulado — COMPONENT
1148:34071 — Histórico de simulados — COMPONENT
1268:51048 — Tela principal/Gerenciamento e cadastro de metas — COMPONENT
1278:69874 — Tela principal / Planos de estudo (aluno) — COMPONENT
1309:26531 — Visualizar registros de estudo (aluno) — COMPONENT
1381:75386 — Cronometro de estudos — COMPONENT
1411:50943 — Visualizar plano de estudos (aluno) — COMPONENT
1487:40649 — Container / Calendário — COMPONENT
1487:39867 — Container / Calendário — COMPONENT
52:41474 — Editor / Menu de ferramentas — COMPONENT_SET
45:38312 — Tiopo=Estilos — COMPONENT
52:41475 — Tiopo=Notas — COMPONENT
52:41563 — Tiopo=âncoras — COMPONENT
91:195457 — Tiopo=Ajustes — COMPONENT
811:61233 — Tiopo=Índice — COMPONENT
74:2167 — Bloco de texto — COMPONENT_SET
74:2109 — Fundo linha=Linhas — COMPONENT
75:77393 — Fundo linha=Selecionado — COMPONENT
74:2168 — Fundo linha=Texto neutro — COMPONENT
74:2212 — Fundo linha=Estilizado — COMPONENT
74:2266 — Parágrafo com estilização — COMPONENT
52:42281 — Editor / Menu de ferramentas / Item — COMPONENT_SET
45:40499 — Tipo=Nota do editor — COMPONENT
91:195702 — Tipo=Ajustes — COMPONENT
52:42282 — Tipo=Ancora — COMPONENT
29:29969 — Cabeçalho — COMPONENT_SET
29:29970 — Tipo=Editor — COMPONENT
11:23728 — Tipo=Default — COMPONENT
88:186989 — Poistit — COMPONENT
74:2095 — Bloco texto/On — COMPONENT
29:34046 — Dropdown — COMPONENT_SET
29:34045 — State=Idle — COMPONENT
29:34047 — State=Selected — COMPONENT
74:2126 — Barra de tipo — COMPONENT
82:150793 — Barra de tipo — COMPONENT_SET
74:2121 — Icone=Nota — COMPONENT
82:150794 — Icone=âncora — COMPONENT
84:185709 — Icone=Registrar — COMPONENT
41:8973 — Menu items — COMPONENT
82:184249 — Status de alteraçòes — COMPONENT_SET
82:184248 — Status=Ok — COMPONENT
82:184250 — Status=Pendentes — COMPONENT
137:39452 — Gemini_Generated_Image_4mhu8d4mhu8d4mhu-Photoroom 1 — COMPONENT
25:28782 — Menu lateral — COMPONENT_SET
137:33512 — Btn Menu=Atualizacoes, Usuario=Editor, Estado=Expandido — COMPONENT
137:38329 — Btn Menu=Inicio, Usuario=Editor, Estado=Expandido — COMPONENT
356:24153 — Btn Menu=Inicio, Usuario=Estudante, Estado=Expandido — COMPONENT
25:28783 — Btn Menu=Inicio, Usuario=Editor, Estado=Retraído — COMPONENT
356:24427 — Btn Menu=Inicio, Usuario=Estudante, Estado=Retraído — COMPONENT
1206:11708 — Btn Menu=Inicio, Usuario=Estudante, Estado=Retraído — COMPONENT
1206:11562 — Menu lateral/Inicio/Estudante/Expandido — COMPONENT
36:6550 — Modal Genérica — COMPONENT
45:7418 — Modal de informações — COMPONENT
45:22153 — Modal confirmação — COMPONENT
11:23947 — Table — COMPONENT
29:34761 — menu-bar — COMPONENT
150:139687 — Atualizações / Linha — COMPONENT
19:1868 — _Tag radio button — COMPONENT_SET
19:1869 — Checked=False, Size=sm, State=Default — COMPONENT
19:1870 — Checked=False, Size=sm, State=Disbaled — COMPONENT
19:1871 — Checked=False, Size=sm, State=Focused — COMPONENT
19:1872 — Checked=False, Size=sm, State=Hover — COMPONENT
19:1873 — Checked=True, Size=sm, State=Default — COMPONENT
19:1875 — Checked=True, Size=sm, State=Disbaled — COMPONENT
19:1877 — Checked=True, Size=sm, State=Focused — COMPONENT
19:1879 — Checked=True, Size=sm, State=Hover — COMPONENT
19:1881 — Checked=False, Size=md, State=Default — COMPONENT
19:1882 — Checked=False, Size=lg, State=Default — COMPONENT
19:1883 — Checked=False, Size=md, State=Disbaled — COMPONENT
19:1884 — Checked=False, Size=lg, State=Disbaled — COMPONENT
19:1885 — Checked=False, Size=md, State=Focused — COMPONENT
19:1886 — Checked=False, Size=lg, State=Focused — COMPONENT
19:1887 — Checked=False, Size=md, State=Hover — COMPONENT
19:1888 — Checked=False, Size=lg, State=Hover — COMPONENT
19:1889 — Checked=True, Size=md, State=Default — COMPONENT
19:1891 — Checked=True, Size=lg, State=Default — COMPONENT
19:1893 — Checked=True, Size=md, State=Disbaled — COMPONENT
19:1895 — Checked=True, Size=lg, State=Disbaled — COMPONENT
19:1897 — Checked=True, Size=md, State=Focused — COMPONENT
19:1899 — Checked=True, Size=lg, State=Focused — COMPONENT
19:1901 — Checked=True, Size=md, State=Hover — COMPONENT
19:1903 — Checked=True, Size=lg, State=Hover — COMPONENT
19:1905 — _Tag checkbox — COMPONENT_SET
19:1906 — Checked=False, Size=sm, State=Default — COMPONENT
19:1907 — Checked=False, Size=sm, State=Disbaled — COMPONENT
19:1908 — Checked=False, Size=sm, State=Focused — COMPONENT
19:1909 — Checked=False, Size=sm, State=Hover — COMPONENT
19:1910 — Checked=True, Size=sm, State=Default — COMPONENT
19:1912 — Checked=True, Size=sm, State=Disbaled — COMPONENT
19:1914 — Checked=True, Size=sm, State=Focused — COMPONENT
19:1916 — Checked=True, Size=sm, State=Hover — COMPONENT
19:1918 — Checked=False, Size=md, State=Default — COMPONENT
19:1919 — Checked=False, Size=lg, State=Default — COMPONENT
19:1920 — Checked=False, Size=md, State=Disbaled — COMPONENT
19:1921 — Checked=False, Size=lg, State=Disbaled — COMPONENT
19:1922 — Checked=False, Size=md, State=Focused — COMPONENT
19:1923 — Checked=False, Size=lg, State=Focused — COMPONENT
19:1924 — Checked=False, Size=md, State=Hover — COMPONENT
19:1925 — Checked=False, Size=lg, State=Hover — COMPONENT
19:1926 — Checked=True, Size=md, State=Default — COMPONENT
19:1928 — Checked=True, Size=lg, State=Default — COMPONENT
19:1930 — Checked=True, Size=md, State=Disbaled — COMPONENT
19:1932 — Checked=True, Size=lg, State=Disbaled — COMPONENT
19:1934 — Checked=True, Size=md, State=Focused — COMPONENT
19:1936 — Checked=True, Size=lg, State=Focused — COMPONENT
19:1938 — Checked=True, Size=md, State=Hover — COMPONENT
19:1940 — Checked=True, Size=lg, State=Hover — COMPONENT
19:1942 — _Toggle base — COMPONENT_SET
19:1943 — Pressed=True, Size=md, State=Focus — COMPONENT
19:1945 — Pressed=True, Size=sm, State=Focus — COMPONENT
19:1947 — Pressed=True, Size=md, State=Hover — COMPONENT
19:1949 — Pressed=True, Size=sm, State=Hover — COMPONENT
19:1951 — Pressed=True, Size=md, State=Default — COMPONENT
19:1953 — Pressed=True, Size=sm, State=Default — COMPONENT
19:1955 — Pressed=True, Size=md, State=Disabled — COMPONENT
19:1957 — Pressed=True, Size=sm, State=Disabled — COMPONENT
19:1959 — Pressed=False, Size=md, State=Focus — COMPONENT
19:1961 — Pressed=False, Size=sm, State=Focus — COMPONENT
19:1963 — Pressed=False, Size=md, State=Hover — COMPONENT
19:1965 — Pressed=False, Size=sm, State=Hover — COMPONENT
19:1967 — Pressed=False, Size=md, State=Default — COMPONENT
19:1969 — Pressed=False, Size=sm, State=Default — COMPONENT
19:1971 — Pressed=False, Size=md, State=Disabled — COMPONENT
19:1973 — Pressed=False, Size=sm, State=Disabled — COMPONENT
36:31864 — Apagar estilo — COMPONENT
19:2025 — Cabecalho — COMPONENT_SET
19:2026 — Tipo=Desabilitado — COMPONENT
19:2039 — Tipo=Indice — COMPONENT
19:2052 — Tipo=Anotacoes — COMPONENT
19:2065 — Tipo=Tipo4 — COMPONENT
45:38212 — Tab — COMPONENT_SET
45:38211 — Status=Selected — COMPONENT
45:38213 — Status=Idle — COMPONENT
196:3760 — Pop up — COMPONENT
203:3460 — Chip — COMPONENT_SET
203:3459 — Tipo=Apostila — COMPONENT
203:3461 — Tipo=Material de apoio — COMPONENT
203:3465 — Tipo=Plano de estudo — COMPONENT
231:13353 — Tipo=Versao atualizada — COMPONENT
203:3482 — Chip — COMPONENT_SET
203:3481 — Tipo=Rascunho — COMPONENT
203:3483 — Tipo=Publicado — COMPONENT
203:23220 — Header ADM — COMPONENT
203:23300 — Card — COMPONENT_SET
203:23299 — Tipo=Material de apoio — COMPONENT
203:23301 — Tipo=Apostila — COMPONENT
203:23326 — Tipo=Plano de estudo — COMPONENT
696:39293 — Tipo=Add documento — COMPONENT
227:12506 — Header aluno — COMPONENT
231:15774 — Progresso — COMPONENT_SET
231:15773 — Progresso=80% — COMPONENT
231:15775 — Progresso=90% — COMPONENT
231:15780 — Progresso=70% — COMPONENT
231:15785 — Progresso=30% — COMPONENT
231:15790 — Progresso=10% — COMPONENT
231:15843 — Progresso=Concluido — COMPONENT
1429:97203 — Progresso=0% — COMPONENT
231:15923 — Card curso — COMPONENT_SET
231:16537 — Cor=Verde — COMPONENT
369:37592 — Cor=Azul — COMPONENT
369:37613 — Cor=Laranja — COMPONENT
369:38349 — Cor=Roxo — COMPONENT
268:4585 — Indice/Modal de anotação — COMPONENT
277:7713 — Indice/Modal de edição da anotação — COMPONENT
277:3542 — Modal — COMPONENT_SET
277:3541 — Grifado=Default — COMPONENT
277:3543 — Grifado=Azul — COMPONENT
277:3588 — Grifado=Verde — COMPONENT
277:3633 — Grifado=Amarelo — COMPONENT
277:3678 — Grifado=Vermelho — COMPONENT
277:14009 — Modal confirmação — COMPONENT
278:16558 — Modal confirmação — COMPONENT
317:8299 — Pop up — COMPONENT
319:10411 — Modal Genérica — COMPONENT
319:17221 — Breadcrumb — COMPONENT_SET
319:17220 — Property 1=Default — COMPONENT
319:17222 — Property 1=Variant2 — COMPONENT
319:17237 — Property 1=Variant3 — COMPONENT
324:19820 — Buttons/Button — COMPONENT
336:11255 — Pop up — COMPONENT
337:4958 — Modal de acoes — COMPONENT
337:18650 — Card — COMPONENT_SET
337:18649 — Tipo=Aberto — COMPONENT
337:18651 — Tipo=Fechado — COMPONENT
369:41791 — Etapa — COMPONENT
242:19929 — Cards / paginas — COMPONENT_SET
242:19928 — Status=Default — COMPONENT
356:24534 — Menu / Footer / Ilustração — COMPONENT_SET
356:24538 — Imagem=Coruja — COMPONENT
356:24533 — Imagem=Apostilas — COMPONENT
356:24543 — Imagem=Atualização — COMPONENT
654:13980 — Imagem=Flashcards — COMPONENT
696:7324 — Imagem=Livros fechados — COMPONENT
356:24508 — Menu / Footer — COMPONENT
356:26398 — Indice leitor — COMPONENT_SET
356:26356 — Status=Aberto — COMPONENT
356:26399 — Status=Fechado — COMPONENT
356:27313 — _Nav item base — COMPONENT_SET
356:27312 — Status=Selecionado, Device=Desktop — COMPONENT
356:27314 — Status=Idle, Device=Desktop — COMPONENT
356:27362 — Status=Selecionado, Device=Mobile — COMPONENT
356:27370 — Status=Idle, Device=Mobile — COMPONENT
356:28822 — Menu — COMPONENT_SET
356:28821 — Usuário=Editor — COMPONENT
356:28823 — Usuário=Aluno — COMPONENT
237:18927 — Banner — COMPONENT
398:45324 — Leitor — COMPONENT_SET
356:26511 — Aba=Indice, Dispositivo=Desktop — COMPONENT
398:45330 — Aba=Comentários, Dispositivo=Desktop — COMPONENT
2615:19006 — Aba=Marcadores, Dispositivo=Desktop — COMPONENT
398:45536 — Aba=Atualizações, Dispositivo=Desktop — COMPONENT
811:62883 — Aba=Busca, Dispositivo=Desktop — COMPONENT
429:59775 — Aba=Aba4, Dispositivo=Mobile — COMPONENT
404:66704 — Buttons — COMPONENT_SET
404:66703 — Tipo=Concluir — COMPONENT
404:66705 — Tipo=Concluido — COMPONENT
429:60405 — Avatar Flutuante — COMPONENT
542:12398 — Modal de informações — COMPONENT
152:7349 — Pagination (V2) — COMPONENT
630:37370 — Pop up — COMPONENT
653:42914 — Modal confirmação — COMPONENT
663:39509 — Toasty — COMPONENT_SET
45:7821 — Tipo=Success — COMPONENT
663:39510 — Tipo=Warning — COMPONENT
663:39518 — Tipo=Error — COMPONENT
679:46553 — Pop up — COMPONENT
679:46706 — Modal Genérica — COMPONENT
696:41247 — Biblioteca Digital / Header — COMPONENT
792:47607 — Busca — COMPONENT
764:56874 — Leitor — COMPONENT
764:56722 — Leitor/Tab — COMPONENT
786:28598 — Apostilas — COMPONENT
799:51724 — Pop up — COMPONENT
870:17495 — Menu items — COMPONENT
1210:55221 — Modal Genérica — COMPONENT
1487:103792 — Modal de exclusao — COMPONENT
2620:33907 — marcador item — COMPONENT
570:31032 — Tabs — COMPONENT
653:14781 — Tabs — COMPONENT
555:29269 — flashcard-dashboard-kpi — COMPONENT_SET
555:29268 — Tipo=Vencer — COMPONENT
555:29270 — Tipo=Total — COMPONENT
555:29277 — Tipo=Indice — COMPONENT
572:31060 — Chip — COMPONENT_SET
572:31059 — Tipo=Facil — COMPONENT
572:31061 — Tipo=Médio — COMPONENT
572:31063 — Tipo=Difícil — COMPONENT
823:32236 — Tipo=Arquivado — COMPONENT
572:36615 — Modal de informações — COMPONENT
603:8316 — Numero — COMPONENT
603:8323 — CaretDown — COMPONENT_SET
603:8322 — Tipo=Fechado — COMPONENT
603:8324 — Tipo=Aberto — COMPONENT
603:11204 — Card — COMPONENT_SET
603:11203 — Tipo=Dificil — COMPONENT
603:11205 — Tipo=Medio — COMPONENT
603:11213 — Tipo=Facil — COMPONENT
603:11726 — Tipo=Arquivado — COMPONENT
603:11264 — Card — COMPONENT_SET
603:11263 — Tipo=Aberto — COMPONENT
603:11265 — Tipo=Fechado — COMPONENT
635:41008 — Modal de edicao/ usuario — COMPONENT
649:33392 — Card adm — COMPONENT_SET
649:33391 — Tipo=Dificil — COMPONENT
649:33393 — Tipo=Medio — COMPONENT
649:33407 — Tipo=Facil — COMPONENT
649:33421 — Tipo=Arquivado — COMPONENT
653:12709 — Card — COMPONENT_SET
653:11400 — Tipo=Facil — COMPONENT
653:12710 — Tipo=Medio — COMPONENT
653:12720 — Tipo=Dificil — COMPONENT
653:13676 — Card / Admin — COMPONENT_SET
653:11399 — Admin=Facil — COMPONENT
653:13677 — Admin=Medio — COMPONENT
653:13687 — Admin=Dificil — COMPONENT
653:40108 — Modal de edicao/ admin — COMPONENT
653:45128 — Container — COMPONENT
572:35161 — Visualização geral - Flashcards — COMPONENT
630:37106 — Visualização e organização- Meus flashcards — COMPONENT
653:45163 — Visualização geral - sem flashcards — COMPONENT
786:28647 — Pagina demo / sem documentos — COMPONENT
714:36005 — Flashcard page / KPIs — COMPONENT
682:55617 — Card frente — COMPONENT
682:55630 — Card verso — COMPONENT
736:27724 — Logomark — COMPONENT_SET
736:27723 — Tipo=Logo — COMPONENT
736:27725 — Tipo=Text — COMPONENT
759:35501 — Tipo=Lixo — COMPONENT
823:31999 — Flashcard Card Base — COMPONENT_SET
823:31998 — Tipo=Mobile — COMPONENT
823:32000 — Tipo=Desktop — COMPONENT
823:32122 — Flashcard — COMPONENT_SET
823:32121 — Cor=Verde — COMPONENT
823:32123 — Cor=Laranja — COMPONENT
823:32139 — Cor=Vermelho — COMPONENT
823:32159 — Cor=Cinza — COMPONENT
697:1087 — Tabs — COMPONENT
694:14785 — Cabeçalho — COMPONENT
694:14783 — Header — COMPONENT
697:1402 — Mobile/Tela visao geral — COMPONENT
721:20182 — Mobile/Tela visao geral — COMPONENT
700:15205 — Card frente — COMPONENT
721:20414 — Modal de edicao/ usuario — COMPONENT
736:25585 — Card verso — COMPONENT
749:13781 — Modal de edicao/ usuario — COMPONENT
749:24146 — Mobile/Tela visao geral — COMPONENT
759:38184 — Toasty/Default — COMPONENT
762:39540 — Modal confirmação — COMPONENT
762:39819 — Toasty/Default — COMPONENT
764:55522 — Buttons — COMPONENT
764:58948 — Acessar e navegar no material / Mobile — COMPONENT
764:58949 — Acessar e navegar no material / Mobile — COMPONENT
771:60639 — Acessar e navegar no material / Mobile — COMPONENT
764:59990 — Indice/Modal de anotação — COMPONENT
764:60292 — Indice/Modal de anotação — COMPONENT
771:61141 — Indice/Modal de edição da anotação — COMPONENT
771:60942 — Acessar e navegar no material / Mobile — COMPONENT
771:61693 — Modal confirmação — COMPONENT
795:50907 — Mobile/Tela visao geral — COMPONENT
803:38247 — Acessar e navegar no material / Mobile — COMPONENT
810:56389 — Acessar e navegar no material / Mobile — COMPONENT
749:23237 — Card — COMPONENT_SET
749:21941 — Tipo=diaria — COMPONENT
749:23238 — Tipo=3 dias — COMPONENT
749:23252 — Tipo=Semanal — COMPONENT
749:23825 — Tipo=Arquivados — COMPONENT
749:23344 — Tipo=Aberto — COMPONENT
749:23462 — Tipo=3 dias — COMPONENT
749:23517 — Tipo=Facil — COMPONENT
749:22127 — Cabecalho — COMPONENT
749:21965 — Card mobile — COMPONENT_SET
749:21964 — Tipo=Medio — COMPONENT
749:21966 — Tipo=Dificil — COMPONENT
749:22079 — Tipo=Facil — COMPONENT
749:22132 — CaretDown — COMPONENT_SET
749:22131 — Tipo=Fechado — COMPONENT
749:22133 — Tipo=Aberto — COMPONENT
1377:37146 — Modal confirmação — COMPONENT
1381:181136 — Mobile/Tela visao geral — COMPONENT
1381:181376 — Mobile/ plano de estudos — COMPONENT
1435:46572 — Mobile/Adicionar plano de estudo — COMPONENT
1448:15711 — Mobile/Adicionar plano de estudo — COMPONENT
1448:68042 — Mobile/Adicionar plano de estudo — COMPONENT
1448:97268 — Modal confirmação — COMPONENT
1587:37578 — Modal Registrar tempo de estudo — COMPONENT_SET
1587:37577 — Tipo=Via cronometro — COMPONENT
1587:38033 — Tipo=Registro manual — COMPONENT
2113:6638 — Mobile/Tela visao geral — COMPONENT
2061:21670 — Mobile/Tela visao geral — COMPONENT
856:14537 — Gemini_Generated_Image_9hoo3q9hoo3q9hoo 1 — COMPONENT_SET
856:14536 — Tipo=1 — COMPONENT
856:14552 — Tipo=2 — COMPONENT
856:14558 — Tipo=3 — COMPONENT
856:14607 — container 3 — COMPONENT
856:14576 — Container 2 — COMPONENT
856:14535 — Container 1 — COMPONENT
865:2321 — Chip — COMPONENT_SET
865:2320 — tipo=numero — COMPONENT
865:2322 — tipo=vazio — COMPONENT
865:2326 — tipo=novo — COMPONENT
865:8755 — Card — COMPONENT_SET
865:8587 — Tipo=Novo — COMPONENT
865:8756 — Tipo=pp — COMPONENT
865:8785 — Tipo=Realizado — COMPONENT
921:6954 — Modal confirmação — COMPONENT
874:16321 — Container — COMPONENT_SET
874:16320 — Tipo=Fechado — COMPONENT
874:16322 — Tipo=Aberto — COMPONENT
874:16479 — Container — COMPONENT
881:11246 — Modal confirmação — COMPONENT
896:54618 — Gemini_Generated_Image_kso7mjkso7mjkso7 1 — COMPONENT_SET
896:54617 — Tipo=Star — COMPONENT
896:54630 — Tipo=ampulheta — COMPONENT
896:54657 — Tipo=ampulheta — COMPONENT
896:54663 — Tipo=time — COMPONENT
896:54698 — Container — COMPONENT_SET
896:54697 — Tipo=Star — COMPONENT
896:54699 — Tipo=Time — COMPONENT
896:54709 — Tipo=ampulheta — COMPONENT
910:2880 — Setas — COMPONENT_SET
910:2875 — Tipo=Fechado — COMPONENT
910:2881 — Tipo=Aberto — COMPONENT
910:2935 — Barra de progresso — COMPONENT_SET
910:2934 — Tipo=4/5 — COMPONENT
910:2936 — Tipo=1/2 — COMPONENT
910:2938 — Tipo=3/5 — COMPONENT
1429:134581 — Tipo=concluida — COMPONENT
910:2940 — Tipo=2/3 — COMPONENT
910:2969 — Container — COMPONENT_SET
910:2956 — Tipo=Aberto — COMPONENT
910:3183 — Chip — COMPONENT_SET
910:3182 — Tipo=Errou — COMPONENT
910:3184 — Tipo=Acertou — COMPONENT
910:3678 — Container — COMPONENT_SET
910:3677 — Tipo=Aberto — COMPONENT
910:4443 — Tipo=Fechado — COMPONENT
910:4992 — Container — COMPONENT_SET
910:4991 — Tipo=Aberto — COMPONENT
910:4993 — Tipo=Fechado — COMPONENT
940:24119 — Modal — COMPONENT
952:1886 — Pop up — COMPONENT
969:26421 — Container — COMPONENT_SET
969:26418 — Tipo=Maior — COMPONENT
969:26422 — Tipo=Menor — COMPONENT
971:27687 — Container — COMPONENT_SET
971:27686 — Tipo=Maior — COMPONENT
971:27688 — Tipo=Menor — COMPONENT
1078:13498 — Bolinha — COMPONENT_SET
1078:13499 — Tipo=Fill — COMPONENT
1139:11336 — Tipo=Empty — COMPONENT
1078:15699 — Modal confirmação — COMPONENT
1081:14348 — Modal confirmação — COMPONENT
1139:16287 — Lista bolinhas — COMPONENT
1278:69165 — Card/plano — COMPONENT
1280:74426 — Modal Genérica — COMPONENT
1285:76108 — Modal — COMPONENT
1284:75988 — Container — COMPONENT
1280:74925 — Tag — COMPONENT_SET
1280:74924 — Tipo=Nao preenchido — COMPONENT
1280:74926 — Tipo=Preenchido — COMPONENT
1280:75085 — Modal — COMPONENT
1285:77231 — Menu items — COMPONENT
1288:20223 — _Calendar event — COMPONENT_SET
1288:20222 — Tipo=Verde — COMPONENT
1288:20224 — Tipo=Roxo — COMPONENT
1288:20234 — Tipo=azul — COMPONENT
1289:1245 — Calendar — COMPONENT_SET
1289:1244 — Tipo=Mes — COMPONENT
1289:1246 — Tipo=Semana — COMPONENT
1289:2080 — Tipo=Dia — COMPONENT
1647:28498 — Calendar - Title — COMPONENT
1296:2544 — Buttons — COMPONENT_SET
1296:2543 — Tipo=Mes — COMPONENT
1296:2545 — Tipo=Semana — COMPONENT
1296:2565 — Tipo=Dia — COMPONENT
1297:17977 — Chip — COMPONENT_SET
1297:17976 — Tipo=Nao preenchido — COMPONENT
1297:17978 — Tipo=Preenchido — COMPONENT
1309:11219 — Chip — COMPONENT_SET
1309:11218 — Tipo=Verde — COMPONENT
1309:11220 — Tipo=Vermelho — COMPONENT
1309:11286 — Container — COMPONENT_SET
1309:11285 — Tipo=Meta atingida — COMPONENT
1309:11287 — Tipo=Não atingida — COMPONENT
1344:16745 — Button — COMPONENT_SET
1344:16744 — Tipo=Cronometro — COMPONENT
1344:16746 — Tipo=Manualmente — COMPONENT
1344:23409 — Modal Genérica — COMPONENT
1370:4466 — Container — COMPONENT_SET
1370:4465 — Tipo=Descansar — COMPONENT
1370:4467 — Tipo=Estudar — COMPONENT
1375:31078 — Modal — COMPONENT
1376:34761 — Modal confirmação — COMPONENT
1381:104151 — Container — COMPONENT_SET
1381:104150 — Tipo=Rodando — COMPONENT
1381:105006 — Tipo=Tipo3 — COMPONENT
1381:104152 — Tipo=Parado — COMPONENT
1381:105015 — Tipo=Tipo4 — COMPONENT
1381:74493 — container — COMPONENT_SET
1381:74492 — Tipo=Cronometro — COMPONENT
1381:74494 — Tipo=Estudar — COMPONENT
1470:48236 — Tipo=Descansar — COMPONENT
1393:197956 — Modal — COMPONENT
1393:197683 — Modal Genérica — COMPONENT
1393:198208 — Modal — COMPONENT
1393:199031 — Modal — COMPONENT
1404:24705 — Toasty/Default — COMPONENT
1411:72565 — Container — COMPONENT_SET
1411:72564 — Tipo=Cronometro — COMPONENT
1411:72566 — Tipo=Pomodoro — COMPONENT
1421:12313 — Modal confirmação — COMPONENT
1421:56137 — Modal confirmação — COMPONENT
1297:18419 — Container — COMPONENT_SET
1297:18418 — Tipo=Aberto — COMPONENT
1297:18420 — Tipo=Fechado — COMPONENT
1435:46063 — Tipo=Mobile — COMPONENT
1435:46290 — Tipo=mobile — COMPONENT
1404:31624 — Chip — COMPONENT_SET
1404:31623 — Property 1=Default — COMPONENT
1404:31627 — Property 1=Variant3 — COMPONENT
1404:31629 — Property 1=Variant4 — COMPONENT
1407:31681 — Card — COMPONENT_SET
1407:31680 — Tipo=Apostila — COMPONENT
1435:45886 — Tipo=Mobile — COMPONENT
1435:45896 — Tipo=Mobil — COMPONENT
1435:45911 — Tipo=Mobile — COMPONENT
1407:36330 — Tipo=Simulado — COMPONENT
1407:36343 — Tipo=Flashcard — COMPONENT
1421:73260 — Modal de exclusao — COMPONENT
1429:101707 — Container / Calendário — COMPONENT
1429:130489 — Toasty/Default — COMPONENT
1429:138766 — Toasty/Default — COMPONENT
1435:46770 — Modal — COMPONENT
1438:80012 — Modal confirmação — COMPONENT
1448:67866 — Container — COMPONENT_SET
1448:67865 — Tipo=verde — COMPONENT
1448:67867 — Tipo=Vermelho — COMPONENT
1448:72386 — Modal Genérica — COMPONENT
1449:107772 — container — COMPONENT
1449:122633 — Modal Genérica — COMPONENT
1450:134730 — Modal confirmação — COMPONENT
1470:48502 — Container — COMPONENT
1470:48294 — Container — COMPONENT_SET
1470:48293 — Tipo=DESCANSAR — COMPONENT
1470:48295 — Tipo=ESTUDAR — COMPONENT
1485:24750 — Período de estudo não definido clique para configurar — COMPONENT_SET
1485:24749 — Tipo=Default — COMPONENT
1485:24766 — Tipo=Variant2 — COMPONENT
1516:15310 — Play — COMPONENT
1516:15322 — Pause — COMPONENT
1516:15323 — Stop — COMPONENT
1516:15325 — Cronômetro / Botões de ação / Botões — COMPONENT_SET
1516:15324 — State=Play — COMPONENT
1535:32569 — State=State Primary — COMPONENT
1516:15326 — State=Pause — COMPONENT
1516:15335 — State=Stop Secondary — COMPONENT
1535:32871 — Cronometro / Corpo Timer — COMPONENT
1516:15440 — Cronômetro / Ilustração — COMPONENT_SET
1516:15439 — Tipo=Relaxar — COMPONENT
1516:15443 — Tipo=Estudar — COMPONENT
1535:35464 — Tipo=Pomodoro — COMPONENT
1522:21918 — Tipo=Cronômetro — COMPONENT
1535:32546 — Cronômetro / Botões de ação — COMPONENT_SET
1535:32545 — Estágio=Iniciar — COMPONENT
1535:32547 — Estágio=Pausar Cancelar — COMPONENT
1535:32958 — Cronômetro — COMPONENT_SET
1516:15378 — Tipo=Cronometro simples, Estado=Idle — COMPONENT
1535:35485 — Tipo=Pomodoro, Estado=Active — COMPONENT
1608:22198 — Tipo=Pomodoro, Estado=Idle — COMPONENT
1608:22226 — Tipo=Pomodoro, Estado=Idle — COMPONENT
1535:35562 — Tipo=Pomodoro, Estado=Estudar — COMPONENT
1608:22250 — Tipo=Pomodoro, Estado=Estudar — COMPONENT
1535:35591 — Tipo=Pomodoro, Estado=Descansar — COMPONENT
1535:32990 — Tipo=Cronometro simples, Estado=Active — COMPONENT
1535:33020 — Cronometro / Icon — COMPONENT
1535:52057 — Modal Registrar tempo de estudo — COMPONENT_SET
1344:16773 — Tipo=Via Cronometro — COMPONENT
1535:52058 — Tipo=Registro Manual — COMPONENT
1587:32344 — Toasty/Default — COMPONENT
1587:71415 — Toasty/Default — COMPONENT
1632:61820 — Cronômetro — COMPONENT_SET
1632:61819 — Tipo=Pausar — COMPONENT
1632:61833 — Tipo=Cancelar — COMPONENT
1632:61827 — Tipo=Parar — COMPONENT
1632:62062 — Chip — COMPONENT_SET
1632:62061 — Tipo=Estudar — COMPONENT
1632:62063 — Tipo=Descansar — COMPONENT
1669:38650 — Tipo=Cronometro — COMPONENT
1646:19710 — Calendar - Nav — COMPONENT_SET
1646:19709 — Tipo=Mês — COMPONENT
1646:19711 — Tipo=Semana — COMPONENT
1646:19743 — Tipo=Dia — COMPONENT
1651:63584 — Colapsado — COMPONENT_SET
1651:63585 — Tipo=Descansar — COMPONENT
1669:38632 — Tipo=Pomodoro — COMPONENT
1712:54926 — Tipo=Cronometro — COMPONENT
1712:54944 — Tipo=Finalizar — COMPONENT
1711:54822 — Tipo=Estudar — COMPONENT
1711:54844 — Tipo=Finalizar — COMPONENT
1701:38968 — Colapsado — COMPONENT_SET
1696:38945 — Mobile=Pomodoro — COMPONENT
1710:39579 — Mobile=Cronometro — COMPONENT
1710:39680 — Mobile=Conometro finalizado — COMPONENT
1711:39760 — Mobile=Retornar — COMPONENT
1701:38969 — Mobile=Estudar — COMPONENT
1701:38992 — Mobile=Finalizar — COMPONENT
1701:39021 — Mobile=Descansar — COMPONENT
1701:39010 — ArrowUDownLeft — COMPONENT
1701:39017 — CheckFat — COMPONENT
1701:39043 — X — COMPONENT
19:1716 — Logo secundaria — COMPONENT
164:3570 — Login — COMPONENT
1752:5160 — Modal — COMPONENT
1945:30392 — NotePencil — COMPONENT
```

### 1.3 Observações literais sobre a página Componentes

- Convivem no mesmo catálogo componentes de UI atômicos (`Chip`, `Card`,
  `_Toggle base`, `_Tag checkbox`, `_Tag radio button`, `Buttons/Button`,
  `Toasty`) e **telas inteiras nomeadas como `COMPONENT`** (ex.: `Login`
  `164:3570`, `Início` `356:25838`, `Acessar e navegar no material`
  `231:17017`, `Pagina demo` `207:4606`, `Realizacao do simulado`
  `1139:19380`, `Editior de documento` — aparece duas vezes com o mesmo
  nome, ids `36:5932` e `336:24016`). Isso é registrado literalmente, sem
  julgamento — cabe ao `onboard-analyst` decidir se isso é um padrão
  problemático.
- Nomes com grafia inconsistente observados literalmente: `"Tiopo=..."`
  (em vez de `"Tipo=..."`) nos component sets `Editor / Menu de
  ferramentas` (`52:41474`); `"Disbaled"` (em vez de `"Disabled"`) em
  `_Tag radio button` e `_Tag checkbox`; variantes de mesmo nome
  duplicadas dentro do mesmo set (`Card` `749:23237` tem duas entradas
  `Tipo=3 dias`, ids `749:23238` e `749:23462`).
- Múltiplos nós com nome genérico `Container`, `Card`, `Modal`, `Modal
  confirmação`, `Modal Genérica`, `Pop up`, `Chip`, `Tabs`, `Toasty/Default`
  se repetem várias vezes com ids diferentes ao longo da página — não
  foi feita nenhuma tentativa de deduplicar ou apontar qual é "a"
  versão correta; ficam listados como estão.
- Nome de component set contendo caractere de quebra de linha literal
  (` `): `"Período de estudo não definido clique para
  configurar"` (id `1485:24750`).

---

## 2. Estilos e variáveis (arquivo inteiro)

### 2.1 `get_styles` — Paint styles

Total: **7 paint styles**. Todos são gradientes lineares — **nenhum
paint style sólido**, **nenhum text style**, **nenhum effect style**,
**nenhum grid style** definido no arquivo.

| Nome | Tipo | Stops (RGB aprox.) |
|---|---|---|
| `Verde Claro` | GRADIENT_LINEAR | branco (#fff) → verde escuro (~#00ab12) |
| `Gradiente/Verde` | GRADIENT_LINEAR | verde médio (~#629737) → verde escuro (~#356a0a) |
| `Gradiente/Azul` | GRADIENT_LINEAR | azul escuro (~#36406e) → azul mais escuro (~#162a9c aprox.) |
| `Card Background/Vermelho` | GRADIENT_LINEAR | rosa claro (~#ffc0bc) → branco |
| `Card Background/Laranja` | GRADIENT_LINEAR | pêssego claro (~#ffc493) → branco |
| `Card Background/Verde` | GRADIENT_LINEAR | verde claro (~#cffcd0) → branco |
| `Card Background/Cinza` | GRADIENT_LINEAR | cinza claro (~#e7e7e7) → branco |

### 2.2 `get_variable_defs` — Variáveis

Uma única coleção: **"Variable collection"**, um modo apenas (`Mode 1`).

| Nome da variável | Tipo | Valor (Mode 1) |
|---|---|---|
| `Title` | STRING | `Gestão de conteúdo` |
| `Estilos de formatação/Verde Claro 50` | COLOR | rgba ~ (208,247,171,0.5) |
| `Estilos de formatação/Verde Claro 100` | COLOR | rgb ~ (208,248,171) |
| `Estilos de formatação/Azul Claro 50` | COLOR | rgba ~ (209,233,255,0.5) |
| `Estilos de formatação/Verde escuro 100` | COLOR | rgb ~ (47,168,54) |
| `Estilos de formatação/Azul Claro 100` | COLOR | rgb ~ (209,233,255) |
| `Estilos de formatação/Amarelo` | COLOR | rgb ~ (255,240,80) |
| `Estilos de formatação/Âncora` | COLOR | rgb ~ (224,203,251) |
| ` Sem registro` (nome com espaço inicial, literal) | COLOR | rgb ~ (255,202,202) |
| `String` | STRING | `String value` (placeholder não substituído) |
| `Pergunta` | STRING | `Explique o teorema de Pitágoras e como ele é aplicado na engenharia civil hoje em dia.` |
| `Green light` | COLOR | rgb ~ (250,255,247) |

Observação literal: nome de variável `" Sem registro"` tem espaço em
branco antes do nome — registrado exatamente como retornado pela API.

---

## 3. Página "Modulo 0: Inicio" (id `164:3569`)

`get_document` nesta página retornou `children: []` — a página em si
não contém nenhum nó diretamente. Todo o conteúdo relevante está na
sub-página listada abaixo dela na árvore de páginas do Figma (indentada
com `↳` no nome, convenção usada neste arquivo legado para simular
hierarquia dentro da lista plana de páginas).

## 4. Sub-página "   ↳ ML-001 - Login e Acesso ✔️ ✔️✔️" (id `164:3568`)

`get_document` nesta página excedeu o limite de tokens (308 675
caracteres) — página com conteúdo grande. Estrutura foi levantada via
`scan_nodes_by_types` (tipo `FRAME`, 229 nós retornados) + `get_nodes_info`
pontual nos nós de nível mais alto + `scan_text_nodes` nas instâncias de
login.

### 4.1 Frames/instâncias de nível superior encontrados na página

A página contém **5 instâncias soltas de nível superior** (não um único
frame de tela), cada uma instância de um componente da página
Componentes:

| id da instância | nome (instance) | componente de origem (Componentes) |
|---|---|---|
| `164:3571` | Login | `164:3570` — "Login" |
| `310:6788` | Login | `164:3570` — "Login" |
| `207:5135` | Pagina demo | `207:4606` — "Pagina demo" |
| `356:25839` | Início | `356:25838` — "Início" |
| `369:38658` | Acessar e navegar no material | `231:17017` — "Acessar e navegar no material" |

**Observação literal**: a página nomeada "ML-001 - Login e Acesso" não
contém somente telas de login — contém também instâncias completas de
"Pagina demo" (parece um dashboard/biblioteca com listagem "Apostilas"
repetida 3x, paginação e menu lateral), "Início" (tela de boas-vindas
pós-login, com balão de fala e ilustração) e "Acessar e navegar no
material" (tela de leitor/dashboard de cursos com barra de progresso,
nome que corresponde ao módulo "Leitor Digital", não a "Login e
Acesso"). Isso é registrado como está encontrado, sem julgar se é erro
de organização do arquivo legado — cabe ao `onboard-analyst`.

### 4.2 Estrutura interna da instância "Login" (via componente-fonte `164:3570`)

Hierarquia observada (nomes de nó, tipo):

```
Login (COMPONENT, 164:3570)
├─ Blur (ELLIPSE) x3 — elementos decorativos de fundo, posicionamento livre (x/y absolutos)
├─ Fundo (VECTOR)
├─ Blur (ELLIPSE) x2
├─ Imagem (RECTANGLE)
├─ Ellipse 6, Ellipse 7, Ellipse 9 (ELLIPSE) — decorativos
├─ Vector 2 (VECTOR)
├─ Imagem (RECTANGLE)
├─ Card (FRAME) — padding 72/41/60/41, cornerRadius 28, fill #fffffff2
│  ├─ Topo (FRAME)
│  │  ├─ Logo secundaria (INSTANCE de componente 19:1716)
│  │  └─ "Bem-vindo ao portal do\nestudante!" (TEXT, Nunito SemiBold 24)
│  └─ Content (FRAME) — padding 24 em todos os lados, cornerRadius 16, fill #f8f8f8
│     ├─ Form (FRAME)
│     │  └─ Input field (INSTANCE) — campo "E-mail"
│     │     ├─ Label wrapper (FRAME) → "E-mail" + "*" (asterisco obrigatório)
│     │     └─ Input (FRAME, padding 10/20/20/10, cornerRadius 9999, stroke #d5d7da)
│     │        ├─ Content → placeholder "seu@email.com"
│     │        └─ Help icon (INSTANCE) → help-circle (INSTANCE aninhada)
│     │     └─ Hint text → "This is a hint text to help user." (texto em inglês, não traduzido)
│     ├─ Input field (FRAME) — campo "Senha" (mesma estrutura do campo e-mail)
│     │  └─ placeholder mascarado "••••••••"
│     ├─ Row (FRAME)
│     │  ├─ Checkbox (INSTANCE) → "_Checkbox base" (INSTANCE aninhada) + texto "Lembrar" / "Save my login details for next time." (inglês)
│     │  └─ Buttons/Button (INSTANCE) → link "Esqueceu a senha"
│     └─ Button (FRAME)
│        └─ Buttons/Button (INSTANCE) → texto "Acessar" (Nunito Bold 16)
├─ Blur (ELLIPSE)
├─ Imagem (RECTANGLE)
└─ Vector (VECTOR)
```

### 4.3 Campos de formulário identificados (texto literal)

| Campo | Label | Placeholder/valor | Obrigatório | Hint text |
|---|---|---|---|---|
| E-mail | "E-mail" | "seu@email.com" | sim (asterisco) | "This is a hint text to help user." (EN, não traduzido) |
| Senha | "Senha" | "••••••••" | sim (asterisco) | "This is a hint text to help user." (EN, não traduzido) |
| Checkbox | "Lembrar" | — | não | "Save my login details for next time." (EN, não traduzido) |

Título da tela (varia por instância, texto sobrescrito):
- Instância `164:3571`: **"Bem-vindo ao portal de\ngestão!"** — porém o
  nome interno do nó de texto continua `"Bem-vindo ao portal do
  estudante!"` (nome do nó não foi atualizado quando o texto foi
  sobrescrito — inconsistência literal entre nome do nó e conteúdo real).
- Instância `310:6788`: **"Bem-vindo ao portal do\nestudante!"** —
  aqui nome do nó e conteúdo coincidem.

Ações/links: "Esqueceu a senha" (link), "Acessar" (botão primário).

### 4.4 Auto Layout vs. posicionamento livre

A ferramenta MCP usada não expõe diretamente o campo `layoutMode` no
retorno de `get_node`/`get_nodes_info` (apenas `bounds`, `fills`,
`padding`, `strokes`, `cornerRadius`, dados de fonte). Não é possível
confirmar de forma determinística, só por inferência:

- Frames como `Card`, `Content`, `Input`, `Text padding` (dentro do
  botão) têm valores de `padding` não-zero e coerentes com o texto que
  envolvem — **indício de Auto Layout**, mas não confirmado
  explicitamente.
- Elementos decorativos de fundo (`Blur`/ELLIPSE, `Imagem`/RECTANGLE,
  `Vector`) têm coordenadas x/y absolutas e se sobrepõem livremente —
  **indício de posicionamento livre**, típico de arte de fundo.
- Registrado como limitação da varredura, não como conclusão definitiva
  — o `onboard-analyst` ou uma inspeção manual no Figma deve confirmar
  `layoutMode` se isso for relevante para a migração.

---

## 5. Lacunas conhecidas deste inventário parcial

- Apenas 2 das 75 páginas do arquivo foram varridas (ver aviso no topo).
- Não foi feito `scan_text_nodes` completo da página "Componentes"
  (618 nós de componente — custo desproporcional para um smoke test).
- Não foi possível confirmar `layoutMode` (Auto Layout) via MCP para
  nenhum nó — ver seção 4.4.
- O erro de `get_local_components` não identifica qual component set
  específico está corrompido; não foi feita tentativa de isolar o nó
  problemático nó a nó (fora de escopo deste teste).
- Efeitos (`effects`) e grids não foram encontrados no arquivo (listas
  vazias em `get_styles`), mas isso não foi cruzado manualmente contra
  o Figma para confirmar se de fato não há nenhum estilo desse tipo
  aplicado localmente sem virar "style" nomeado.
