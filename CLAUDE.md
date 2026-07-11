# Harness de Design Determinístico — Regras Universais

Este arquivo define o processo que vale para QUALQUER projeto dentro de
`projects/`. Regras específicas de um cliente ficam no `PROJECT.md`
daquele projeto e têm precedência sobre este arquivo em caso de conflito
explícito (ex: convenção de nomenclatura diferente).

Este harness tem **três escopos de trabalho**, com ciclos de vida e
riscos diferentes:

| Escopo | Quando roda | Ação sobre o Figma | Documento de referência |
|---|---|---|---|
| **Onboarding** | Uma vez por cliente (ou raramente) | Só leitura | `onboarding/ONBOARDING.md` |
| **Preflight** | Sob demanda, incremental, disparado pela produção | Escreve no arquivo NOVO | `preflight/PREFLIGHT.md` |
| **Produção** | Dia a dia, a cada jornada/tela nova | Escreve no arquivo NOVO | Este arquivo |

Onboarding nunca escreve no Figma. Preflight e Produção só escrevem no
arquivo Figma novo/limpo — nunca no arquivo legado.

---

## Papéis (separação decisão vs. execução)

- **interpreter** — lê wireframe + história do usuário, propõe plano.
  Nunca escreve no Figma.
- **builder** — executa plano JÁ APROVADO via MCP. Nunca reinterpreta,
  nunca decide sozinho em caso de ambiguidade.
- **documenter** — documenta componentes em `_draft/` após a construção;
  promove para oficial somente após aprovação do validator.
- **auditor** — verifica consistência técnica (tokens, nomenclatura,
  duplicatas, sincronização com o Figma real). Só reporta.
- **validator** — compara o resultado construído contra a história do
  usuário, o wireframe original e a coerência entre telas da jornada.
  Só reporta, nunca corrige.

Agentes de onboarding (`onboard-scanner`, `onboard-analyst`,
`onboard-writer`) e de preflight (`preflight-planner`,
`preflight-builder`) seguem a mesma lógica de separação decisão/execução
— ver `onboarding/ONBOARDING.md` e `preflight/PREFLIGHT.md`.

Nenhum agente aciona outro diretamente. Toda a coordenação passa pela
sessão principal (você + Claude na conversa raiz), que decide quando
delegar e quando pedir aprovação humana.

---

## Economia de tokens — disciplina obrigatória

Cada subagente roda em contexto isolado e frio — não há cache de prompt
compartilhado entre chamadas a agentes diferentes, e mesmo chamadas
repetidas ao mesmo agente só se beneficiam de cache dentro da janela de
poucos minutos. Na prática, isso significa que o controle real de custo
não vem de configuração de infraestrutura (isso já é gerenciado pela
plataforma) — vem de disciplina de conteúdo, em dois pontos:

### Saída concisa (todos os agentes)
Tokens de saída custam mais que os de entrada. O relatório final de
qualquer agente deve:
- Reportar achados de forma direta — sem restatar o input recebido, sem
  introdução/conclusão decorativa
- Preferir listas compactas a prosa longa quando a informação é
  estruturada por natureza (IDs, valores, status)
- Citar só os campos relevantes de um retorno bruto de tool (ex: o hex
  de um fill), nunca colar de volta o JSON inteiro de uma resposta MCP
  no texto do relatório
- Isso não é licença para omitir raciocínio genuinamente necessário
  (ex: por que um candidato foi descartado) — conciso é sobre eliminar
  repetição e enfeite, não sobre cortar substância

### Pre-flight barato antes de agente caro (responsabilidade da sessão principal)
Antes de invocar um subagente para uma tarefa que pode ser um beco sem
saída óbvio, fazer uma checagem rápida e barata primeiro
(`figma_get_status`, `figma_list_open_files`, ou um `figma_execute` de
leitura pontual), em vez de descobrir o problema só depois de um
subagente inteiro já ter rodado. Exemplos já aplicados
nesta base: confirmar que o arquivo certo está aberto antes de rodar uma
varredura completa; confirmar que um node/página existe antes de propor
um plano de reconstrução em cima dele.

---

## Dois arquivos Figma por projeto — legado e produção

Cada projeto tem dois arquivos Figma distintos, declarados em
`PROJECT.md`:

- **Legado** — o arquivo antigo do cliente, mal estruturado. Somente
  leitura. Usado como referência visual pelo onboarding e pelo
  preflight. NUNCA recebe escrita de nenhum agente.
- **Produção** — o arquivo novo, criado pelo preflight, já seguindo
  `COMPONENT_STANDARDS.md` desde o início. É o único destino de escrita
  do `builder` e do `preflight-builder`.

## Regra de segurança — escopo por projeto

Antes de qualquer operação de escrita no Figma, confirmar que o arquivo
de destino corresponde ao arquivo de **Produção** declarado no
`PROJECT.md` do projeto atualmente carregado. Se não corresponder —
incluindo se o destino for o arquivo do legado — PARAR e alertar. Nunca
escrever no arquivo legado, em nenhuma circunstância.

A conta Figma é corporativa única (múltiplos clientes dentro dela). O
isolamento entre clientes é feito por esta verificação de configuração,
não por token separado.

**Como verificar (MCP conectado: `figma-console-mcp`)**: a escrita vai
para o arquivo ativo no bridge do Figma Desktop, e o servidor expõe o
`fileKey` real desse arquivo (identificador criptográfico, não
editável) via `figma_get_status`/`figma_list_open_files`. A checagem
obrigatória antes de escrever é: `fileKey` do arquivo ativo ==
`File-key` de Produção declarado no `PROJECT.md`. Se não bater, PARAR.
Cada `PROJECT.md` deve declarar o `File-key` de Legado e de Produção
(o `fileName` continua registrado, mas apenas como informação humana —
a verificação é pelo key).

**Proteção estrutural do Legado**: o arquivo Legado é lido via REST
(por `fileUrl`/`fileKey`, sem plugin) — o plugin bridge NUNCA deve ser
rodado dentro do arquivo Legado. Sem bridge no Legado, escrita nele é
impossível por arquitetura, não só por regra.

---

## Estrutura de páginas do arquivo de Produção

O arquivo de Produção de cada cliente segue esta estrutura de páginas
(criada pelo preflight ao gerar o arquivo novo):

```
Foundations           ← tokens/variáveis e estilos base
Components            ← componentes oficiais do design system — é
                          AQUI que o preflight-builder reconstrói
                          componentes migrados do legado
Patterns              ← composições recorrentes de componentes
Docs                  ← documentação viva dentro do próprio Figma
Archive               ← componentes deprecated/aposentados
🟢 Telas Atuais       ← SEMPRE a versão vigente de cada tela, uma
                          página por tela, nome fixo (não muda por
                          história/jornada). É a fonte da verdade de
                          "como a tela está agora".
🗂️ Jornadas            ← uma página por jornada/história, cadeia de
                          telas em ordem, mais recente no topo.
                          Histórico de trabalho, não fonte de verdade.
```

### Mecânica de tela — duplicação, nunca componente/instância

Telas inteiras NUNCA são tratadas como componente/instância do Figma —
sempre como frame duplicado (cópia solta). Componente/instância é
reservado para elementos reais de design system (Button, Card, Header).

Ao construir uma tela que já existe em "Telas Atuais":
1. Duplicar o frame de "Telas Atuais" para a página da jornada atual em
   "Jornadas"
2. Trabalhar livremente na cópia — elementos internos (Button, Card
   etc.) continuam sendo instâncias vinculadas aos componentes do
   design system, só o frame da tela em si é cópia solta
3. NUNCA editar diretamente o frame em "Telas Atuais" durante a
   construção
4. Só após aprovação do validator, o frame aprovado é copiado/promovido
   para substituir a versão anterior em "Telas Atuais"

Ao construir uma tela nova (sem versão anterior em "Telas Atuais"):
1. Criar o frame direto na página da jornada atual em "Jornadas"
2. Só após aprovação do validator, promover para "Telas Atuais"

---

## Ordem obrigatória do fluxo — por que documenter vem por último

```
interpreter → aprovação humana → [ se houver MIGRAR DO LEGADO:
preflight primeiro ] → builder (por tela) → validator (jornada
completa) → aprovação humana → documenter (promove _draft/ → oficial e
promove frames para Telas Atuais)
```

O `documenter` NUNCA promove um componente para `design-system/
components/` oficial antes do `validator` aprovar a jornada. Durante a
construção, componentes novos ficam em
`design-system/components/_draft/` — existem no Figma, mas não são
oferecidos pelo `interpreter` como opção de reuso em outras tarefas até
serem promovidos.

---

## Regra de decisão de componentização (núcleo do interpreter)

Para cada elemento identificado no wireframe, classificar em uma das
QUATRO categorias, sempre listando os candidatos existentes descartados
e o motivo:

1. **REUSO DIRETO** — componente existente (Status: ativo) cobre
   estrutura e função, sem alteração.
2. **NOVA VARIANTE** — componente existente cobre a função, mas a
   diferença encontrada não está documentada como variante.
3. **COMPONENTE NOVO** — nenhuma correspondência estrutural ou funcional
   real, nem no design system novo nem no legado.
4. **MIGRAR DO LEGADO** — o elemento existe e é resolvido no arquivo
   Figma legado, mas ainda não foi trazido para o design system novo.
   Precisa de preflight (reconstrução) ANTES do builder seguir com a
   tela — nunca durante a construção da tela.

Nunca classificar como "componente novo" sem antes ter avaliado
candidatos existentes contra `design-system/components/*.md` (oficial,
nunca `_draft/`) E contra o arquivo legado (via onboarding/preflight já
realizados anteriormente, não uma nova varredura ad-hoc). Essa
classificação faz parte do plano e é visível para aprovação humana antes
de qualquer ação.

### Mecânica de "MIGRAR DO LEGADO" — sempre antes, nunca durante

```
1. interpreter aponta no plano: elemento X = MIGRAR DO LEGADO
2. Humano aprova o plano (incluindo essa marcação)
3. ANTES de acionar o builder para a tela, aciona-se
   preflight-planner + preflight-builder só para os componentes
   marcados
4. Só então o builder constrói a tela — a essa altura, os componentes
   migrados já são REUSO DIRETO
```

O `builder` nunca aciona preflight sozinho e nunca decide migrar um
componente no meio da execução de uma tela — se encontrar algo não
migrado que o plano não previu, PARA e devolve à sessão principal (ver
regra de falha parcial abaixo).

---

## Onde vive o status de migração — não confundir com journey-state.md

Duas informações diferentes, dois lugares diferentes:

- **`journeys/[nome]/journey-state.md`** — memória de CURTO PRAZO,
  válida só durante a construção de UMA jornada específica. Registra o
  que já foi construído nas telas anteriores DESTA jornada, para telas
  seguintes da MESMA jornada manterem consistência entre si. Depois que
  a jornada termina, vira histórico — não é consultado por jornadas
  futuras.
- **`design-system/components/[nome].md` → campo `Status`** — memória
  de LONGO PRAZO, permanente. Registra se aquele componente já foi
  migrado do legado (`Status: ativo`) ou ainda não existe no sistema
  novo. É isso que QUALQUER jornada futura consulta para saber se pode
  classificar aquele elemento como REUSO DIRETO ou precisa acionar
  MIGRAR DO LEGADO.

Nunca registrar status de migração dentro de `journey-state.md` — essa
informação fica invisível para jornadas futuras não relacionadas.

---

## Estado compartilhado entre telas de uma mesma jornada

Cada invocação do `builder` roda em contexto isolado — não tem memória
automática do que foi construído em telas anteriores da mesma jornada.

Regra: **a sessão principal é responsável por atualizar
`journeys/[nome]/journey-state.md`** após cada tela ser construída, e por
incluir o conteúdo atual desse arquivo no prompt de delegação ao builder
da próxima tela. O builder NÃO escreve neste arquivo — sua permissão é
restrita a operações MCP no Figma.

---

## Falha parcial do builder / preflight-builder

Se uma operação MCP falhar no meio da execução, ou se um elemento
inesperado não migrado for encontrado fora do previsto no plano, o
agente PARA imediatamente, lista exatamente o que já foi criado com
sucesso até o ponto da falha, e devolve à sessão principal. Nunca tenta
continuar sozinho nem refazer do zero — decisão de como prosseguir é
humana.

---

## Pós-execução (obrigatório)

Depois de qualquer tarefa aprovada pelo humano, perguntar:
"Alguma decisão desta tarefa deveria virar regra permanente?"
Se sim, atualizar `memory/learnings.md` ou o `components/*.md` relevante
do projeto ativo antes de encerrar a sessão.

---

## Checagem de integridade do harness (início de sessão)

Antes de aceitar tarefas numa sessão nova, confirmar que o motor do
harness está íntegro nesta máquina:

1. `.claude/agents/` contém os 10 arquivos de agente (interpreter,
   builder, documenter, auditor, validator, onboard-scanner,
   onboard-analyst, onboard-writer, preflight-planner,
   preflight-builder)
2. O servidor `figma-console` aparece como conectado (`claude mcp
   list`) — registro é de escopo de USUÁRIO (carrega token), então uma
   máquina nova precisa refazer o `claude mcp add -s user ...` do
   `README.md`; não há nada no repositório que o restaure

Motivação real: numa migração de máquina (Linux → Windows), a cópia do
projeto perdeu silenciosamente todos os arquivos ocultos — incluindo os
10 agentes — e isso só seria percebido ao tentar invocar um agente. Se
algo estiver faltando, PARAR e recuperar do repositório git antes de
qualquer trabalho.

---

## Sincronização com o Figma real

No início de cada sessão de trabalho em um projeto, rodar uma checagem
leve com o `auditor` comparando a lista de componentes do arquivo de
Produção com o `design-system/` documentado, antes de aceitar tarefas
novas. Isso evita divergência silenciosa quando alguém do time do
cliente cria/edita componentes fora do harness. Isso é sobre o arquivo
de Produção — não confundir com a varredura do arquivo Legado, que é
trabalho do onboarding.

---

## Formato de `memory/decisions.md`

Cada entrada deve conter: data, contexto, decisão, motivo, e restrição de
reversão (se houver) — incluir campo "aprovado por". Nunca reverter uma
decisão registrada sem validação explícita e nova entrada no log.

---

## Componentes deprecated

Componentes marcados `Status: deprecated` no seu `.md` nunca são
oferecidos pelo `interpreter` como opção de reuso, mas permanecem
documentados (não apagar) para não quebrar referências em telas antigas.

---

## Conexão MCP com o Figma

Este harness usa o servidor MCP `figma-console-mcp`
(https://github.com/southleft/figma-console-mcp), registrado em
**escopo de usuário** (nunca de projeto — o registro carrega o token):

```bash
claude mcp add figma-console -s user \
  -e FIGMA_ACCESS_TOKEN=figd_... -e ENABLE_MCP_APPS=true \
  -- npx -y figma-console-mcp@latest
```

Detalhes de setup (token, plugin Desktop Bridge): ver `README.md`.
Histórico: substituiu o `figma-mcp-go` em 2026-07-11, após smoke test
completo — ver `smoke-test-figma-console-mcp.md` para as evidências.

Arquitetura híbrida — o ponto mais importante:
- **Leitura** vai por REST com o token, endereçada por
  `fileUrl`/`fileKey` — NÃO exige Figma Desktop nem plugin. É assim
  que o Legado é lido (o bridge nunca roda nele).
- **Escrita** (e leitura de estado runtime via `figma_execute`) exige
  o plugin "Figma Desktop Bridge" rodando no arquivo-alvo no Figma
  Desktop (Windows/macOS; plugin de desenvolvimento precisa ser rodado
  manualmente a cada sessão de trabalho).

**Dev Mode bloqueia toda escrita.** Se uma operação de escrita falhar
com "Can't call X in read-only mode", a aba do Figma provavelmente
está em Dev Mode (ícone `</>`, atalho `Shift+D`) — a Plugin API
bloqueia escrita nesse estado. Alternar para Design mode resolve.

### Política do `figma_execute` (decisão registrada — "A'")

`figma_execute` roda código Plugin API arbitrário e é indispensável
(leitura de Auto Layout/`boundVariables`, gestão de páginas e criação
com controle fino dependem dele). Regras:

1. Usar tools declarativas sempre que existirem
   (`figma_instantiate_component`, `figma_create_component_set`,
   `figma_set_fills`, `figma_rename_node`, etc.)
2. `figma_execute` em agente de ESCRITA: permitido, com a intenção do
   código descrita no plano aprovado — nunca improvisar mutações fora
   do plano
3. `figma_execute` em agente SOMENTE-LEITURA (`interpreter`,
   `auditor`, `validator`, `onboard-scanner`, `preflight-planner`):
   permitido APENAS com código de leitura — nenhuma chamada que mute o
   documento (`create*`, `remove`, atribuições a propriedades,
   `setBoundVariable` etc.). Isso é uma restrição de prompt, não de
   ferramenta — trade-off consciente aceito na migração: a garantia
   "hard" de whitelist não cobre o que acontece dentro do código.
4. Usar as variantes assíncronas da Plugin API
   (`getNodeByIdAsync`, `getInstancesAsync`, `setCurrentPageAsync`,
   `loadAllPagesAsync`) — as síncronas falham com `documentAccess:
   dynamic-page`. Carregar fontes (`loadFontAsync`) antes de criar
   texto.

### Capacidades que deixaram de ser limitação (vs. figma-mcp-go)

- Criar a PRIMEIRA instância de um componente:
  `figma_instantiate_component` (passar `componentKey` E `nodeId`)
- Combinar componentes em variantes: `figma_create_component_set`
  (modo matriz a partir de base, ou combinar existentes)
- Ler `layoutMode`/`itemSpacing`/paddings/sizing modes e
  `boundVariables`: via `figma_execute` (leitura determinística
  completa — a checagem de Auto Layout do `auditor` é 100% verificável)
- Payload em páginas densas: leitura em duas passadas via
  `figma_execute` (inventário raso → drill pontual); nunca serializar
  árvore inteira
- `fileKey` real exposto (`figma_get_status`) — base da regra de
  segurança

### Erros e quirks conhecidos (confirmados no smoke test de 2026-07-11)

1. **Timeout ≠ falha limpa.** Uma tool que reporta "timed out" pode
   ter EXECUTADO no Figma (confirmado: `figma_instantiate_component`
   aplicou a operação 2× apesar de reportar timeout). Após QUALQUER
   timeout de escrita: verificar o estado real no Figma antes de
   retentar — retry cego duplica elementos. Isso integra o protocolo
   de falha parcial do builder/preflight-builder.
2. **Sync de tokens não vê coleções criadas na mesma sessão.**
   `figma_export_tokens` com `scope: collection` pode vir vazio e
   `figma_import_tokens` pode DUPLICAR uma coleção recém-criada via
   `figma_create_variable*` (nem `refreshCache` resolve). Regra: cada
   coleção nasce por UMA via — ou por `figma_import_tokens` (DTCG), ou
   por `create_variable*` — sem misturar export/import na mesma sessão
   em que a coleção foi criada. `figma_get_variables` (com
   `refreshCache: true`) enxerga tudo e é a leitura confiável.
3. **`figma_get_file_data` com `nodeIds` não faz drill-down** (retorna
   a árvore de páginas em vez do nó pedido). Leitura cirúrgica de nós:
   `figma_execute` com serialização rasa controlada.
4. **Formatos de leitura padrão não expõem Auto Layout nem
   `boundVariables`** (`figma_get_component` `reconstruction` retorna
   stub raso com dimensões erradas; `metadata` não traz layout). Usar
   `figma_execute` para essas propriedades.
5. **`figma_instantiate_component` com `parentId` de frame com Auto
   Layout pode dar timeout** (e ainda assim executar — ver quirk 1).
   Preferir Section/página como destino e mover depois, ou
   `comp.createInstance()` via `figma_execute` direto no pai.
6. **Deletar a página ativa continua bloqueado pelo Figma**
   (`Removing this node is not allowed`) — comportamento de
   plataforma. Navegar para outra página antes, no mesmo bloco de
   código (`setCurrentPageAsync` → `remove()`).
7. **Criação de página é limitada pelo PLANO do arquivo** (Starter: 3
   páginas). Não é erro do MCP — mas o `preflight-builder` deve
   reportar esse erro como restrição de plano, não como falha.
8. **Primeira conexão pode falhar** ("Failed to connect") pelo
   download inicial do `npx` estourar o timeout do health check — com
   cache aquecido conecta normal. O bridge usa fallback de porta
   (9223–9232) automaticamente.

IDs de variável/coleção continuam no formato prefixado
(`VariableID:4016:22174`, `VariableCollectionId:4016:22173`) — usar
sempre exatamente como retornados, nunca truncar o prefixo.

---

## Fora de escopo deste harness (v1) — não implementar sem revisão

- Rollback automatizado de operações no Figma
- Múltiplos aprovadores / fluxo de aprovação por cliente
- Responsividade / breakpoints como processo funcional
- Conexão MCP direta com Miro (wireframes chegam como PDF/imagem)
- Portabilidade automática de assets entre arquivo legado e arquivo de
  produção — `[VALIDAR]` na prática, ver `onboarding/ONBOARDING.md`
