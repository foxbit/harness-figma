<!--
TESTE DE FUMAÇA — projeto _SANDBOX_TESTE. Cobertura AMOSTRAL, não os 618
nós do inventário completo. Ver design-system/components/README.md.
-->

# Login

## Status
em revisão

## Identidade Figma
- Component key: `164:3570` (componente-fonte "Login", confirmado ao
  vivo via `get_node` nesta sessão — arquivo Legado `mcp-test` ainda
  acessível). Instâncias na página ML-001: `164:3571` (persona Gestor)
  e `310:6788` (persona Estudante).
- Localização: página "Componentes" (`11:23284`) do arquivo Legado
  `mcp-test`, tela completa modelada como `COMPONENT` (não frame comum —
  padrão observado em outras "telas" do mesmo catálogo, ex.: "Início",
  "Pagina demo"). Instâncias usadas na sub-página
  `   ↳ ML-001 - Login e Acesso ✔️ ✔️✔️` (`164:3568`).
- Tipo: componente composto (tela inteira: fundo decorativo + card de
  formulário)

## Propósito
Tela de acesso do portal (login), com formulário de e-mail/senha,
usada tanto pela persona Estudante quanto pela persona Gestor/Admin —
diferenciadas pelo texto de boas-vindas exibido no topo do card.

## Estrutura (composição)
<!-- Confirmado ao vivo via get_node nesta sessão (componente-fonte
164:3570 completo). -->
- Blur (ELLIPSE) x3 + Fundo (VECTOR) + Blur (ELLIPSE) x2 + Imagem
  (RECTANGLE) + Ellipse 6/7/9 + Vector 2 + Imagem (RECTANGLE) —
  elementos decorativos de fundo, posicionamento livre (coordenadas
  x/y absolutas, sem Auto Layout confirmado) — opcional/decorativo
- Card (FRAME, padding 72/41/60/41, cornerRadius 28, fill `#fffffff2`) — obrigatório
  - Topo (FRAME)
    - Logo secundaria (INSTANCE, componente `19:1716`) — obrigatório
    - Título de boas-vindas (TEXT, Nunito SemiBold 24) — obrigatório,
      texto varia por persona (ver "Props" e "Variantes")
  - Content (FRAME, padding 24, cornerRadius 16, fill `#f8f8f8`)
    - Form (FRAME)
      - Input field "E-mail" (INSTANCE) — label "E-mail" + asterisco
        obrigatório + placeholder "seu@email.com" + hint text (EN, ver
        Q25) — obrigatório
      - Input field "Senha" (FRAME) — mesma estrutura, placeholder
        mascarado — obrigatório
      - Row (FRAME)
        - Checkbox "Lembrar" (INSTANCE, aninha `_Checkbox base`) +
          supporting text (EN, ver Q25) — obrigatório
        - Buttons/Button (INSTANCE) — link "Esqueceu a senha" — obrigatório
      - Button (FRAME)
        - Buttons/Button (INSTANCE) — texto "Acessar" (Nunito Bold 16) — obrigatório
- Blur (ELLIPSE) + Imagem (RECTANGLE) + Vector (VECTOR) — decorativo, opcional

## Variantes existentes

| Nome da variante | Quando usar | Diferença estrutural |
|---|---|---|
| Persona=Estudante | Acesso de aluno ao portal | Título "Bem-vindo ao portal do\nestudante!" (confirmado em `310:6788`, nome do nó e conteúdo coincidem) |
| Persona=Gestor | Acesso de gestor/admin ao portal | Título "Bem-vindo ao portal de\ngestão!" (confirmado em `164:3571` — **atenção**: o nome interno do nó de texto na instância ainda diz "Bem-vindo ao portal do estudante!", não foi atualizado quando o conteúdo foi sobrescrito; isso é uma inconsistência de nomenclatura interna a corrigir no preflight, não um problema de conteúdo) |

<!-- Variant property "Persona=" é uma proposta de estruturação
(decisão Q24) — no Legado essas duas instâncias não são variantes
formais de um component set, são duas instâncias soltas do mesmo
componente com texto sobrescrito manualmente. -->

## Props / propriedades configuráveis

| Prop | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| Persona | enum (`Estudante` / `Gestor`) | sim | Controla o texto de boas-vindas exibido no topo do card |
| E-mail (placeholder) | texto | não (default "seu@email.com") | Placeholder do campo de e-mail |
| Hint text E-mail | texto | sim | Ver decisão Q25 — traduzir para PT-BR (hoje "This is a hint text to help user.", em inglês) |
| Hint text Senha | texto | sim | Idem — mesma string em inglês hoje |
| Texto do checkbox "Lembrar" (supporting text) | texto | sim | Ver decisão Q25 — traduzir para PT-BR (hoje "Save my login details for next time.", em inglês) |

## Tokens utilizados
- Cor: nenhum token sólido/style nomeado confirmado para os valores
  usados neste componente (`#fffffff2` do Card, `#f8f8f8` do Content,
  `#d5d7da` do stroke do Input, `#213975` do texto de título) — todos
  hardcoded no Legado, sem style associado (`get_styles` só retorna
  paint styles gradiente, nenhum sólido)
- Espaçamento: hardcoded — padding 72/41/60/41 (Card), padding 24 todos
  os lados (Content), padding 10/20/20/10 (Input) — sem token nomeado
- Tipografia: hardcoded — Nunito SemiBold 24 (título), Inter Medium 14
  (labels), Inter Regular 16 (valores de input), Inter Regular 14 (hint
  text) — sem text style nomeado (arquivo Legado não tem nenhum text
  style definido)

## Quando usar
Tela de entrada do portal, para ambas as personas (Estudante e Gestor),
sempre que o usuário precisar autenticar com e-mail e senha.

## Quando NÃO usar
Não usar para telas de cadastro/registro (fora do escopo deste
componente — não catalogado nesta amostra). Não usar como base para
outros formulários de autenticação com campos diferentes (ex.: SSO,
recuperação de senha) sem nova avaliação — a estrutura aqui é fixa
para e-mail + senha + lembrar-me.

## Componentes relacionados
- Compõe-se de: `Logo secundaria` (`19:1716`), `Buttons/Button`
  (`324:19820`), `_Checkbox base` (instância aninhada em `Checkbox`),
  `help-circle` (instância aninhada em `Help icon`)
- É composto dentro de: nenhum componente maior — é ele mesmo uma tela
  completa
- Observação de escopo de página (Q23): a página onde as instâncias de
  Login vivem hoje (`164:3568`, "ML-001 - Login e Acesso") também
  contém instâncias soltas de outras telas sem relação com login
  ("Pagina demo", "Início", "Acessar e navegar no material") — por
  decisão Q23, quando o restante do arquivo Legado for varrido, essas
  telas devem ser reclassificadas e a jornada de Login no design system
  novo deve conter só as instâncias de "Login"

## Histórico
- Criado em: `2026-07-03` — contexto: `onboard-writer`, smoke test do
  onboarding em `_SANDBOX_TESTE`, com base nas decisões Q24 (negociada
  de verdade — confirma as 2 personas como variante `Persona=`
  intencional, ambas a migrar) e Q25 (decisão-padrão de teste —
  traduzir hint texts/supporting text para PT-BR na reconstrução).
  Estrutura confirmada ao vivo via `get_node` (`164:3570`) nesta sessão
  — arquivo Legado `mcp-test` ainda acessível.
- Última alteração: nenhuma desde a criação
