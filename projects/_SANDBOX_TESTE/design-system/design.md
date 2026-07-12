<!--
Identidade visual do _SANDBOX_TESTE, extraída do arquivo `mcp-test`
(produto: "ponto a ponto — estudo planejado"). Valores numéricos lidos
da fonte autoral via MCP (variáveis, nós reais); seções perceptuais
descritas sobre as telas canônicas. Gerado em 2026-07-11; enriquecido
na mesma data com a seção "Páginas Componentizadas" (16:9160, página
Componentes — 22 telas do sistema inteiro).
-->

# Identidade Visual — ponto a ponto (sandbox `mcp-test`)

Status: aprovado
Fonte: arquivo Figma `mcp-test` (File-key `zLIBE0CQN1rQBUQxOswcef`) —
tokens reais + telas canônicas + seção "Páginas Componentizadas"
(`16:9160`, 22 telas)
Aprovado por: Angelo Rosa (2026-07-11)

## 1. Identidade e tom

Plataforma de estudo planejado (biblioteca digital, flashcards,
simulados, guia de estudos) para estudantes de concursos/provas.
Personalidade visual: **amigável, encorajadora, lúdica-profissional,
arredondada, leve**. Mascote (coruja 3D de óculos) e ilustrações 3D
aparecem em momentos de acolhimento (home, login, avisos, estados
vazios de página) — nunca dentro de conteúdo funcional denso
(formulários, tabelas, questões).

## 2. Tema visual

- Superfícies claras com **tint esverdeado sutil** no fundo de página
  (`#F8FBF6` medido) e degradê verde suave subindo do rodapé da
  sidebar; conteúdo em cards **brancos elevados** com sombra muito
  discreta (DROP_SHADOW blur 2, y 2)
- Formas **muito arredondadas**: botões, chips, badges e inputs de
  linha única são pill; cards usam `radius.lg` (16)
- Densidade **espaçosa**: respiro generoso entre blocos; até telas
  densas (tabelas, formulários longos) respiram
- Elementos decorativos: formas orgânicas verdes, caminhos tracejados
  navy — só em telas de acolhimento (home/login)
- Light mode apenas

## 3. Cor — papéis e regras de uso

Tokens semânticos (coleção "Design Tokens", valores reais):
`color.primary #003D76` · `color.primary-emphasis #00386B` ·
`color.on-primary #FFFFFF` · `color.surface #FFFFFF` ·
`color.on-surface #000000` · `color.on-surface-muted #535862` ·
`color.hairline #D5D7DA`

Valores autorais medidos nas telas (ainda NÃO tokenizados — ⚠️
LACUNAS a resolver em preflight, nunca hardcodar sem pendência):
- **Verde de ação (CTA)**: gradiente linear `#629737 → #356A0A`
  (sutil, quase sólido) — componente `Buttons/Button`
- **Azul de link**: `#0063CE` (Nunito Medium 14 — itens clicáveis de
  tabela/lista)
- **Cinza de apoio de tabela**: `#717680` (headers de coluna, badge
  neutro — distinto do `on-surface-muted #535862`; consolidar na
  tokenização)
- **Semáforo de status** (badges/chips): positivo `#2E9B41` sobre
  `#E8F7EC` com borda `#ABEFC6`; neutro `#717680` sobre `#F5F5F5` com
  borda `#D5D7DA`; (variações laranja/vermelho seguem o mesmo padrão
  suave nos chips de dificuldade)

Regras de uso:
- **Navy (`color.primary`) NÃO é cor de ação** — é texto enfático,
  títulos, navegação ativa (pill navy texto branco), timer, radios e
  steppers selecionados, dots de progresso
- **Ação/CTA é VERDE** (gradiente acima) com texto branco — inclui
  botões com ícone `+` ("Novo", "Adicionar")
- **Link é AZUL `#0063CE`** — nunca navy nem verde para texto clicável
  em listas
- **Vermelho** só para sair, excluir (ícone lixeira) e destrutivas
- Chips/badges: sempre o trio suave texto/fundo-tintado/borda — nunca
  fundo sólido saturado
- Fundos de página: branco ou `#F8FBF6`; header de tabela `#F5F5F5`

## 4. Tipografia — hierarquia real

Família única: **Nunito** (nenhum text style formal catalogado no
arquivo — ⚠️ LACUNA a resolver em preflight futuro).

| Papel | Família | Peso | Tamanho | Uso observado |
|---|---|---|---|---|
| Título de página | Nunito | Bold | 30 | "Criar novo simulado" — navy |
| Título de seção/card | Nunito | Bold/Medium | 20 | "Informações Básicas", "Questão 06" — navy |
| Timer/valor destaque | Nunito | Bold | ~30–40 | navy |
| Botão / nav | Nunito | Bold ou Medium | 16 | branco sobre navy/verde |
| Corpo | Nunito | Regular/Medium | 14–16 | `on-surface`/`-muted` |
| Link em lista | Nunito | Medium | 14 | `#0063CE` |
| Label de input / header de coluna | Nunito | Regular/Medium | 12–14 | cinza muted, acima do campo |

## 5. Forma — raios, bordas e sombras

- Botões: **pill** (`radius.full`), altura 44 (toolbar) a 52 (destaque)
- Chips/badges: **pill** (radius 16 medido no badge) com borda 1px
- Inputs de linha única e busca: **pill** com borda `color.hairline`;
  textarea: radius ~12
- Cards e containers: `radius.lg` (16); tabela vive DENTRO de um card
- Empty state: container de **borda tracejada** radius ~12, ícone +
  texto muted centrados
- Sombra: um único nível discreto (blur 2, y 2); nunca empilhada
- Separadores e linhas de tabela: `color.hairline` 1px

## 6. Espaçamento e layout

- Escala: `spacing.md` 16 · `spacing.lg` 24 (padding de card ≥ 16;
  respiro entre blocos ≥ 24)
- Desktop: sidebar branca à esquerda (~260px, itens em pill navy
  quando ativos; versão COLAPSADA só-ícones com ativo em quadrado navy
  arredondado); toolbar de página = título à esquerda + busca pill +
  ações à direita (outline "Filtros" + verde "Novo")
- Formulários: TODO o formulário dentro de UM card branco, com títulos
  de seção navy internos; labels acima dos campos; rodapé de ações
  centrado no card ("Cancelar" texto navy + primária verde pill)
- Tabelas/listagens: card branco radius 16 > header de colunas
  `#F5F5F5` texto `#717680` > linhas brancas com hairline; nome do
  item como link azul; ações por linha à direita (ícones + kebab);
  paginação centrada abaixo (números, ativo em círculo navy)
- Mobile: menu em drawer branco; ação principal em largura quase total
- Estado desabilitado: `state.disabled-opacity` 0.4

## 7. Anatomia dos componentes-chave

### Buttons/Button (existe como componente no arquivo)
- Pill com gradiente verde, texto Nunito 16 branco; variante com
  ícone `+` à esquerda; secundária = outline/texto navy; "Cancelar" é
  SEMPRE texto sem fundo
- Regra de ouro: UMA primária verde por bloco; nunca navy como fundo
  de ação

### Card de indicador/KPI
- Card branco radius 16, sombra sutil, ícone 3D à esquerda, rótulo
  Nunito Medium 20 navy, valor Bold grande (navy ou verde)
- Regra de ouro: valor sempre maior que o rótulo; máx. 3 por linha

### Chip / Badge de status
- Pill, trio suave (texto/fundo/borda na cor do status — valores em §3)
- Regra de ouro: cor comunica categoria; rótulo textual obrigatório

### Tabela/listagem
- Sempre dentro de card; header `#F5F5F5`; nome-link azul `#0063CE`;
  badge de status por linha; kebab de ações; paginação círculo navy
- Regra de ouro: tabela nunca "solta" na página, nunca zebra striping

### Formulário
- Um card único com seções tituladas em navy; labels muted acima;
  inputs pill/rounded com hairline; steppers (– valor +) com valor em
  pill navy (ativo) ou cinza (zero); empty state tracejado
- Regra de ouro: rodapé centrado com "Cancelar" (texto) + primária
  (verde); "Salvar/primária" desabilitada até haver alteração válida

### Seleção (radio/dots de progresso)
- Radio: círculo; selecionado = navy preenchido com check branco
- Progresso de passos: dots — feito navy, atual navy com anel, pendente
  cinza claro

### Navegação (sidebar/tab)
- Item ativo: pill navy texto/ícone branco (expandida) ou quadrado
  navy arredondado (colapsada); inativos: texto navy sem fundo
- Regra de ouro: exatamente UM item ativo visível

## 8. Hierarquia de ações

- Máximo UMA ação primária (verde) visível por seção/tela
- Secundárias: outline ou texto navy; "Cancelar" sempre texto
- Destrutivas: vermelho (ícone/texto), sempre com confirmação
- Ação primária de tela mobile: sempre visível sem rolagem

## 9. Do / Don't — erros estéticos proibidos

- DO: fundo branco/`#F8FBF6`; cards brancos radius 16 com sombra
  sutil; botões pill verdes texto branco; títulos navy Nunito Bold;
  chips/badges pill com trio suave; links azuis `#0063CE`; empty
  states com borda tracejada
- DON'T: **NUNCA** cantos retos ou radius < 8 em botão/chip/card/input
- DON'T: **NUNCA** navy como fundo de botão de ação (ação é verde;
  navy é navegação/seleção/texto)
- DON'T: **NUNCA** chip/badge/status com fundo sólido saturado
- DON'T: **NUNCA** mais de um nível de sombra, nem sombra forte
  (blur > 8) em elemento de conteúdo
- DON'T: **NUNCA** tipografia que não seja Nunito
- DON'T: **NUNCA** cinza escuro/preto como fundo de área de conteúdo
- DON'T: **NUNCA** dois botões primários verdes lado a lado
- DON'T: **NUNCA** "Cancelar" como botão preenchido (é texto navy)
- DON'T: **NUNCA** tabela solta fora de card, nem zebra striping
- DON'T: **NUNCA** mascote/ilustração 3D dentro de formulário, tabela
  ou tela de operação

## 10. Referências canônicas

| Tela | nodeId | Onde | Por que é canônica |
|---|---|---|---|
| Login | `164:3571` | ↳ ML-001 | Marca, ilustração 3D, card sobre cena verde, CTA pill |
| Dashboard Flashcards | `2207:3041` | ↳ FC-001 | Sidebar, KPIs, chips, tabs, busca, paginação |
| Criação do simulado | `881:1367` | Páginas Componentizadas (`16:9160`) | O padrão de FORMULÁRIO completo: card único, seções, steppers, empty state, rodapé de ações |
| Gestão de conteúdo | `16:9509` | Páginas Componentizadas (`16:9160`) | O padrão de LISTAGEM: tabela em card, links azuis, badges, toolbar, paginação |
| Menu Mobile | `764:55556` | ↳ FC-001 | Padrão mobile: drawer branco, tipografia e navegação |

Catálogo completo: seção "Páginas Componentizadas" (`16:9160`, página
"Componentes") reúne as 22 telas do sistema como componentes — usar
como fonte de consulta para padrões não cobertos acima (leitor,
editor, calendário, cronômetro, histórico).

## 11. Acessibilidade específica do projeto

- Texto sobre verde e sobre navy: sempre branco
- Texto de apoio muted nunca abaixo de 14px (labels de 12px só em
  headers de coluna/microcopy)
- Não usar cor como único diferenciador em chips/badges (rótulo
  textual obrigatório)

## 12. Casos de exceção conhecidos

- Telas de gestão/portal usam a MESMA linguagem do app do aluno — não
  há tema separado de admin
- Ilustrações 3D e mascote: só em home/login, estados vazios de página
  e avisos — nunca em telas de operação
- Modo prova ("Realização do simulado"): sidebar colapsada e cabeçalho
  com timer — é a única tela onde o cabeçalho de usuário some
