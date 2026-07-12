# Harness v2 — Storybook + Penpot com fonte única da verdade

Status: proposta discutida e com decisões ratificadas (2026-07-11) —
**refatoração NÃO iniciada**; aguarda "go" explícito do Angelo para a
Fase 1
Autor: sessão de 2026-07-11 (Angelo Rosa + Claude)
Local: `temp/` — ao iniciar a execução, promover para a raiz/docs e
registrar em `decisions.md`

---

## 1. Contexto e motivação

O harness v1 opera o Figma como banco de dados do design system:
componentes, tokens e telas vivem no arquivo Figma, e os agentes
constroem design **via API de plugin** (MCP), nó por nó.

A jornada de teste no sandbox (`_teste-interpreter`, 2026-07-11) expôs
os limites dessa arquitetura, mesmo após a migração para o
`figma-console-mcp`:

- **Lentidão estrutural**: uma tela exige dezenas de operações MCP
  granulares; o custo não é do servidor MCP, é da natureza da Plugin
  API.
- **Fragilidade**: timeout que executa mesmo assim (retry cego
  duplica), tool que reporta sucesso e perde o nó
  (`figma_arrange_component_set`, confirmado em 2026-07-11), sync de
  tokens que duplica coleções.
- **Estética**: o modelo desenha mal "por API" mesmo com o design.md —
  a distância entre a intenção e o resultado é grande quando cada
  decisão visual vira uma chamada de mutação.

Diagnóstico: o modelo é nativamente forte em **escrever código**
(HTML/CSS/React) e fraco em **operar ferramenta de design por API**.
A v2 realinha a arquitetura com essa realidade.

---

## 2. Visão

> O harness é o **DesignOps automatizado** do projeto: o designer
> desenha e decide, o dev revisa e consome, e os agentes catalogam,
> parametrizam, sincronizam, documentam e auditam — garantindo por
> construção que design e código nunca divergem.

Mudança de fundação:

| | v1 (atual) | v2 (proposta) |
|---|---|---|
| Fonte da verdade | arquivo Figma de Produção | **repositório git** (código + tokens) |
| Componentes | nós Figma documentados em .md | **código React + stories** (Storybook) |
| Tokens | variáveis Figma (espelhadas em JSON) | **JSON DTCG no git** (fonte), consumido por código e Penpot |
| Ferramenta de design | Figma (leitura e escrita via MCP) | **Penpot self-hosted** (espelho da biblioteca + estúdio do designer) |
| Documentação de componente | `design-system/components/*.md` | **Storybook autodocs/MDX** |
| Construção de tela pelo agente | mutações via Plugin API | **código** (story de página) + composição no Penpot via MCP |
| Entrega ao front | handoff (inspecionar Figma) | **pacote npm (GitHub Packages)** — o mesmo artefato que o designer vê |

O Storybook não é "alimentado" pela fonte — ele **é a fonte
renderizada** (stories são código). O Penpot é alimentado de verdade,
por um espelho regenerável. Uma verdade, um espelho — nunca duas
verdades sincronizadas.

---

## 3. Arquitetura

### 3.1 O repositório-fonte (um por cliente)

Criado a partir do template `ds-template` (mantido junto ao harness):

```
ds-<cliente>/
├── tokens/
│   └── tokens.json           # DTCG — A fonte de cor/espaço/raio/tipo
├── src/
│   ├── components/
│   │   ├── Button/
│   │   │   ├── Button.tsx
│   │   │   ├── Button.stories.tsx    # variantes = catálogo oficial
│   │   │   └── Button.mdx            # doc de uso (opcional, autodocs cobre o básico)
│   │   └── _draft/                   # componentes ainda não aprovados
│   ├── screens/                      # stories de página (telas de jornada)
│   └── styles/                       # saída do Style Dictionary (gerado, não editado)
├── .storybook/
├── tests/visual/                     # baselines de screenshot (regressão visual)
├── style-dictionary.config.js        # tokens.json → CSS vars + preset Tailwind (+ Dart p/ Flutter)
├── package.json                      # publica @<org>/ds-<cliente> no GitHub Packages
└── mirror/                           # config do espelho → Penpot (team/file IDs)
```

- **Stack**: React 18 + Tailwind (tema gerado dos tokens) + Storybook +
  Style Dictionary. TypeScript.
- **Qualidade embutida** (o que o Figma nunca deu): type-check, lint,
  testes de interação, addon de acessibilidade, regressão visual
  (ver 3.6).
- **Publicação**: Storybook estático por cliente no servidor do Penpot
  (ver 3.4); pacote npm privado no GitHub Packages.

### 3.2 Os dois fluxos direcionais (e por que não colidem)

**Penpot → fonte (extração)**: o desenho do designer é *insumo*. Uma
tela desenhada à mão, com rascunhos de componentes novos, é lida pelos
agentes como um "wireframe rico" e transformada em plano → código.

**Fonte → Penpot (espelho)**: componente oficializado em código é
publicado na biblioteca Penpot, com variantes e tokens vinculados.

A não-colisão é garantida por **territórios com donos diferentes**
dentro do Penpot — a mesma separação que a v1 já pratica:

| Território no Penpot | Dono | Equivalente v1 |
|---|---|---|
| **Biblioteca oficial** (arquivo de assets) | o código (via espelho) — designer só consome | página "Components" |
| **Projetos de jornada** (arquivos de trabalho) | o designer — agentes leem | página "Jornadas" |
| **Telas vigentes** (arquivo/projeto "Atuais") | promoção pós-validação | página "🟢 Telas Atuais" |

Regra de ouro: **a biblioteca oficial nunca é editada à mão**. Mudança
de componente entra pelo pipeline (rascunho → código → espelho).
Componente novo nasce como rascunho no arquivo de trabalho, vira código
em `_draft/`, e após aprovação aparece na biblioteca oficial.

### 3.3 O espelho (a única peça técnica genuinamente nova)

Mecanismo determinístico (transpilador, não LLM):

1. Renderizar cada story em browser headless
2. Ler a árvore DOM + estilos computados
3. Emitir a estrutura equivalente no Penpot via MCP oficial / API:
   flex/grid layout do Penpot ≈ CSS 1:1; tokens vinculados por NOME
   (mesmo DTCG dos dois lados, nunca por valor)
4. Combinar as stories em componente Penpot com variantes nomeadas
   pelas props (`variant / size / state`)

Adaptações conhecidas (limitações de ferramenta de design, não do
Penpot): pseudo-estados (hover/focus) viram variantes explícitas;
breakpoints viram variantes de viewport ou só o tamanho base;
pseudo-elementos/animações são achatados em shapes estáticos.

Precedente que prova o mecanismo: story.to.design faz exatamente isso
com o Figma como alvo (mais difícil, Auto Layout ≠ CSS). Penpot como
alvo é mais simples (SVG + CSS nativos).

**Fallback garantido**: se variantes programáticas no Penpot se
provarem imaturas, o espelho degrada para frames SVG pixel-fiéis por
variante (Penpot importa SVG nativamente). Perde conforto, nunca perde
fidelidade.

Validação do espelho: screenshot da story vs. screenshot do componente
no Penpot — comparação automatizável pelo auditor.

### 3.4 Multi-projeto / multi-cliente e infraestrutura

Contexto ratificado (2026-07-11): somos uma **software house** — os
designers têm acesso a todos os projetos. A separação por cliente é
**organizacional**, não de acesso.

```
harness (ESTE repo — o motor, único)
├── CLAUDE.md, agentes, skills, ONBOARDING/PREFLIGHT
├── ds-template/                  # scaffold do repositório-fonte
└── projects/
    └── <cliente>/                # SÓ estado e configuração por cliente
        ├── PROJECT.md            # aponta: repo ds-<cliente>, team Penpot,
        │                         #   fileKey do legado Figma, Storybook URL
        ├── design-system/design.md
        ├── journeys/
        ├── memory/ (decisions, learnings)
        └── onboarding/
```

**Infraestrutura (decidida em 2026-07-11):**

- **Penpot self-hosted, instância ÚNICA**, com 1 team por cliente
  (organização, não isolamento). A proteção contra misturar clientes
  é estrutural no espelho: cada `ds-<cliente>` declara em `mirror/` o
  team Penpot de destino, e o mirror-sync **valida o par
  (repo ↔ team ID) antes de qualquer escrita** — herdeiro direto da
  checagem de fileKey da v1.
- **Storybooks publicados no MESMO servidor do Penpot**: arquivos
  estáticos, um diretório por cliente atrás do mesmo proxy/nginx, com
  autenticação (basic auth ou Cloudflare Access). Link compartilhável
  com o cliente mediante credencial. Zero SaaS adicional.
- **npm privado: GitHub Packages** (a empresa já usa GitHub) —
  pacotes privados na organização, sem infra extra, autenticação com
  os tokens que o time já tem.
- **Convenção de nomes — o slug do cliente é idêntico em tudo**:
  repo `ds-<cliente>` · pacote `@<org>/ds-<cliente>` · team Penpot
  `<cliente>` · pasta `projects/<cliente>/` · diretório do Storybook
  `/<cliente>`. O auditor verifica esse casamento automaticamente.
  (Sandbox: `ds-sandbox` / `@<org>/ds-sandbox` / team `sandbox`.)

**O harness continua único e versionado**: processo, agentes e
aprendizados de motor valem para todos; o que é do cliente vive no
`projects/<cliente>/` (como hoje) + no repo `ds-<cliente>` (novo).
**Onboarding não muda**: o legado do cliente continua sendo um arquivo
Figma, lido via REST por fileKey — a ferramenta de escrita nem fala
com o Figma.

### 3.5 Projetos Flutter (minoria)

Camadas de compatibilidade, da mais barata à mais cara:

1. **Tokens — universais desde o dia 1**: Style Dictionary emite Dart
   (`tokens.dart`) do mesmo `tokens.json`. Todo cliente Flutter herda
   a paridade de tokens de graça.
2. **Catálogo**: o equivalente do Storybook no ecossistema Flutter é o
   **Widgetbook** — mesmo papel (variantes navegáveis, docs, testes
   golden). O template Flutter usa Widgetbook no lugar do Storybook.
3. **Componentes**: não há reuso de código React→Flutter. Cliente
   Flutter tem `ds-<cliente>` em Dart, com o MESMO processo (agentes
   escrevem widgets + entradas de Widgetbook; portões idênticos).
4. **Espelho Penpot**: numa primeira fase, via fallback SVG (render
   golden → import); espelho estrutural fica fora de escopo até o
   fluxo React estar maduro.

Decisão de escopo: o harness v2 nasce React-first; Flutter entra como
**adapter** (template + prompts de builder em Dart) numa fase
posterior, sem mudar o processo.

### 3.6 Regressão visual (decidida em 2026-07-11)

**Storybook test-runner + Playwright, com baselines de screenshot
commitadas no repo** (`tests/visual/`). Motivos:

- Grátis e roda igual em CI e localmente — custo zero por cliente
  (Chromatic cobra por snapshot e multiplicaria custo por cliente)
- Os diffs ficam no git como arquivos — **consumíveis pelos agentes**,
  que é exatamente o insumo do validator/auditor v2
- Determinístico (screenshots de story são pixel-estáveis)

Reavaliar Chromatic apenas se o review visual por humanos virar
gargalo — a migração é aditiva, não muda a arquitetura.

---

## 4. Papéis dos agentes — remapeamento

| v1 | v2 | O que muda |
|---|---|---|
| interpreter | **interpreter** | Igual em essência. Classifica contra o catálogo do Storybook (`index.json` das stories) + biblioteca Penpot. Lê telas manuais do designer como "wireframe rico". |
| preflight-planner | **component-planner** | Propõe a especificação do componente (props, variantes, tokens novos) a partir do legado Figma (REST) ou do rascunho do designer. |
| preflight-builder / builder (componentes) | **component-builder** | Escreve `Componente.tsx` + story + tokens no JSON, em `_draft/`. Sai como PR. Guiado por design.md + screenshot de referência. |
| builder (telas) | **screen-builder** | Compõe a tela: story de página no Storybook E/OU composição no Penpot com instâncias da biblioteca. Substitui rascunhos por instâncias oficiais após promoção. |
| validator | **validator** | Mais forte: regressão visual sobre screenshots de story (pixel-estável) + história do usuário + design.md + coerência da jornada. |
| auditor | **auditor** | Audita as NOVAS fronteiras: git ↔ Storybook ↔ Penpot ↔ tokens; telas do designer (lint de conformidade: valor fora de token, componente destacado, cópia solta); casamento de slugs repo↔team↔pacote. |
| documenter | **documenter** | Cura MDX/autodocs; promove `_draft/` → oficial (move pasta + tag); dispara regeneração do espelho; mantém decisions.md. |
| onboard-scanner/analyst/writer | **inalterados** | Legado continua Figma via REST. O onboard-writer passa a gerar também o `tokens.json` DTCG inicial. |

Novo processo automatizado (não é agente de decisão): **mirror-sync** —
job determinístico que regenera a biblioteca Penpot a cada mudança na
fonte (CI ou invocação da sessão principal), validando o par
repo↔team antes de escrever.

O que **sobrevive intacto** da v1: os 3 escopos, as 4 categorias
(REUSO DIRETO / NOVA VARIANTE / COMPONENTE NOVO / MIGRAR DO LEGADO),
os portões de aprovação humana, design.md (fica MAIS eficaz — alimenta
geração de código, terreno nativo do modelo), journey-state.md,
decisions.md, o ciclo `_draft → em revisão → ativo → deprecated`, a
coordenação centralizada na sessão principal.

O que **morre**: toda a camada de escrita no Figma (política do
`figma_execute`, quirks de timeout/sync, estrutura de páginas do
arquivo de Produção, checagem de fileKey para escrita, plugin bridge).
A leitura REST do Figma fica (onboarding/preflight de legado).

---

## 5. Fluxos operacionais

### Fluxo A — jornada por wireframe (gerada por agente)
1. Wireframe + user-story.md na pasta da jornada (como hoje)
2. interpreter → plano com as 4 categorias → **aprovação humana**
3. MIGRAR DO LEGADO / NOVO → component-planner → aprovação →
   component-builder (código em `_draft/` + PR) → **review do dev** →
   merge → mirror-sync publica na biblioteca Penpot
4. screen-builder compõe a(s) tela(s) — story de página + Penpot
5. validator (jornada completa) → **aprovação humana** → documenter
   promove (código sai de `_draft/`, tela vira vigente, espelho
   regenera)

### Fluxo B — jornada desenhada à mão pelo designer
1. Designer compõe a tela no Penpot: instâncias da biblioteca para o
   que existe, rascunho para o que falta, num projeto de jornada
2. Designer roda a cadeia: interpreter lê a tela como wireframe rico —
   separa instância (resolvido) / rascunho (categoria 2 ou 3) / valor
   fora de token (pendência)
3. Segue idêntico ao Fluxo A a partir do passo 3; ao final, os
   rascunhos da tela são substituídos pelas instâncias oficiais

### Fluxo C — manutenção pelo dev
1. Dev altera componente por PR normal (correção, refactor, prop nova)
2. CI: testes + regressão visual; se a story mudou visualmente,
   validator/auditor apontam impacto
3. Merge → mirror-sync → designers veem a mudança na biblioteca
4. Auditor reporta divergência semântica (ex: prop nova sem doc)

### Fluxo D — onboarding de cliente novo
1. Igual à v1 (scanner/analyst/writer sobre o legado Figma via REST)
2. Saídas novas: `tokens.json` DTCG inicial + repo `ds-<cliente>` do
   template + team no Penpot + design.md
3. migration-backlog prioriza o que virar componente em código

---

## 6. Documentação — o que vai para onde

| Conteúdo | v1 | v2 |
|---|---|---|
| Anatomia/variantes/uso de componente | `components/*.md` | **Storybook autodocs + MDX** (gerado do código + curadoria do documenter) |
| Status do ciclo de vida | campo `Status` no .md | pasta `_draft/` + tags de story; `deprecated` = tag + banner MDX |
| Identidade visual | `design.md` | **igual** (no `projects/<cliente>/`) — insumo dos builders de código |
| Decisões/learnings | `memory/*.md` | **igual** |
| Estado de jornada | `journey-state.md` | **igual** |
| Tokens | .md descritivo + variáveis Figma | **`tokens.json` DTCG** (a fonte) + visualização no Storybook |

---

## 7. Riscos e mitigações

| # | Risco | Impacto | Mitigação |
|---|---|---|---|
| 1 | Espelho código→Penpot com variantes desconfortáveis (recurso novo no Penpot) | experiência do designer | Validação dedicada na Fase 2 com critério de aceite do designer; fallback SVG pixel-fiel; plano B: Figma + story.to.design (pago) |
| 2 | Estabilidade do Penpot em arquivos grandes | operação diária | self-host (controle de versão do servidor); telas por projeto de jornada (arquivos pequenos); relatos 2026 indicam bugs em UIs complexas — medir no sandbox |
| 3 | Mudança cultural: designer deixa de ser dono da ferramenta-verdade | adoção | é a MESMA disciplina da v1 ("nunca editar Telas Atuais"), transposta; o Fluxo B mantém o desenho manual como cidadão de primeira classe |
| 4 | Custo de manter o transpilador do espelho | manutenção | peça determinística com testes próprios (story ↔ Penpot screenshot diff); escopo contido (subset de CSS que os componentes usam) |
| 5 | Clientes Flutter | cobertura | tokens universais desde o dia 1; adapter Dart/Widgetbook em fase posterior; não bloqueia o rollout React |
| 6 | Refatoração ampla do harness (CLAUDE.md ~60% Figma-write) | esforço | v1 continua operável durante a transição; v2 nasce no sandbox sem tocar cliente real; docs reescritos só na Fase 3 |

---

## 8. Roadmap

> A execução **não foi iniciada** — cada fase começa somente com "go"
> explícito do Angelo.

- **Fase 0 — Decisão**: ✅ documento discutido e decisões ratificadas
  (2026-07-11). Pendente apenas: registrar em `decisions.md` quando a
  execução for autorizada.
- **Fase 1 — Fundação (sandbox)**: `ds-template` (Vite + Storybook +
  Style Dictionary + Tailwind); portar `tokens.json` do sandbox;
  reescrever os 5 componentes validados em código com stories.
  *Critério de saída*: Storybook publicado com os 5 componentes
  fiéis ao design.md.
- **Fase 2 — Espelho (MVP)**: transpilador story→Penpot para os 5
  componentes; **avaliação de conforto pelo designer** (critérios de
  aceite na seção 9). *Critério de saída*: designer compõe uma tela
  só com instâncias espelhadas, sem fricção bloqueante.
- **Fase 3 — Harness re-apontado**: reescrever CLAUDE.md, remapear
  agentes (component-planner/builder, screen-builder, auditor v2),
  atualizar ONBOARDING/PREFLIGHT/README. Inclui análise skill a skill
  do `design-system-ops` (base para auditor/documenter v2).
- **Fase 4 — Teste de aceitação**: a jornada `_teste-interpreter`
  inteira na v2 (Fluxos A e B), comparando tempo e qualidade com a
  experiência v1 no Figma.
- **Fase 5 — Rollout**: primeiro cliente real; aposentar escrita
  Figma; arquivar agentes v1.
- **Fase futura — adapter Flutter**: template Dart/Widgetbook +
  prompts de builder; tokens já estarão prontos.

---

## 9. Decisões ratificadas e pendências

**Decisões ratificadas por Angelo (2026-07-11):**
- Figma deixa de ser obrigatório como entregável
- Stack de componentes: **React + Tailwind** (Flutter = minoria, via
  adapter posterior)
- **Penpot** como ferramenta de design — preferido sobre Paper (alpha)
  e sobre permanecer no Figma (dor de escrita via API)
- **Penpot self-hosted em instância única** — software house,
  designers acessam todos os projetos; separação por cliente é
  organizacional (1 team/cliente)
- **Storybooks publicados no mesmo servidor do Penpot** (estáticos,
  atrás do mesmo proxy, com autenticação)
- **npm privado no GitHub Packages** (a empresa já usa GitHub)
- **Regressão visual: Storybook test-runner + Playwright com
  baselines no git** (decisão delegada ao Claude; racional na 3.6)
- **Convenção de nomes: slug único do cliente em tudo** (repo, pacote,
  team Penpot, pasta projects/, diretório do Storybook)
- Espelho **unidirecional** fonte→Penpot; desenho manual entra como
  insumo (extração), nunca como edição direta da biblioteca

**Pendências (não bloqueiam a decisão; pertencem às fases):**
1. Registrar a decisão v2 em `decisions.md` do motor — no momento do
   "go" da Fase 1
2. Análise skill a skill do `design-system-ops`
   (github.com/murphytrueman/design-system-ops) — na Fase 3; postura
   padrão: adotar o que mapear, sem criar dependência
3. Critérios de aceite do designer para a Fase 2 — proposta a validar
   com Angelo ao iniciar a fase: (a) trocar variante pelo painel do
   Penpot; (b) override de texto/ícone sem detach; (c) usar instância
   em tela com flex layout sem quebrar; (d) atualização do componente
   propaga às instâncias existentes; (e) tokens aplicáveis pelo
   painel; (f) espelho completo da biblioteca roda em minutos, não
   horas
4. Definir a org GitHub / slug `<org>` dos pacotes e o endereço do
   servidor Penpot+Storybook — no provisionamento da infra (Fase 1/2)
5. Destino da jornada `_teste-interpreter` em andamento na v1
   (preflight interrompido por falha do `figma_arrange_component_set`):
   congelar como está e usá-la como baseline de comparação na Fase 4
