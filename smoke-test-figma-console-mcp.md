# Smoke Test — figma-console-mcp (candidato a substituir figma-mcp-go)

Avaliação prática do servidor MCP `figma-console-mcp` (Southleft,
https://github.com/southleft/figma-console-mcp) contra as limitações e
erros conhecidos do `figma-mcp-go` documentados em `CLAUDE.md`.

- **Executado em**: 2026-07-11 · servidor/plugin v1.35.0 · Node 24 ·
  Windows 11 · Figma Desktop
- **Arquivo-alvo**: `mcp-test` (fileKey `zLIBE0CQN1rQBUQxOswcef`),
  sandbox do projeto `_SANDBOX_TESTE`
- **Artefatos do teste**: Section `_smoke-console-mcp` na página
  `Draft` (mantida como evidência — componentes `Smoke/*`, tela
  `Tela/Smoke-Login`, coleção de variáveis `smoke-tokens`)

## ✅ VEREDITO: GATE DE MIGRAÇÃO APROVADO

T1, T2, T3, T5, T7, T9 e T10 (obrigatórios) = ✅. T4, T8 e T11 = ⚠️
com caminho viável via `figma_execute`. Nenhum critério de "não
migrar" foi acionado. Ressalvas operacionais importantes no final.

---

## 1. Pré-requisitos

1. Figma Desktop instalado (Windows — roda nativo) e logado na conta
   corporativa
2. Node 18+ disponível (`node --version`)
3. **Personal Access Token do Figma** — criar em
   https://www.figma.com/developers/api#access-tokens
   (Figma → Settings → Security → Personal access tokens):
   - Scopes (todos só leitura, exceto comments): **File content
     (Read)**, **File versions (Read)**, **Variables (Read)**,
     **Comments (Read/write)**
   - O token começa com `figd_` — a escrita no canvas NÃO passa pelo
     token (passa pelo plugin bridge)

## 2. Instalação (coexiste com o figma-mcp-go — não remover o atual)

### 2.1 Registrar o servidor MCP no Claude Code

```bash
claude mcp add figma-console -s user \
  -e FIGMA_ACCESS_TOKEN=figd_SEU_TOKEN_AQUI \
  -e ENABLE_MCP_APPS=true \
  -- npx -y figma-console-mcp@latest
```

> ⚠️ **Usar `-s user` (ou `-s local`), NUNCA `-s project`**: o registro
> de projeto grava em `.mcp.json`, que é versionado — o token iria
> parar no git.

> Nota da instalação real: a primeira checagem de saúde pode falhar
> ("Failed to connect") porque o download inicial do `npx` estoura o
> timeout — com o pacote em cache, conecta normalmente.

### 2.2 Instalar o plugin Desktop Bridge no Figma

1. O servidor materializa o plugin em
   `C:\Users\<usuario>\.figma-console-mcp\plugin\manifest.json` na
   primeira execução
2. Figma Desktop: **Plugins → Development → Import plugin from
   manifest...** → apontar para esse arquivo
3. Abrir o arquivo-alvo e rodar o plugin — conecta via WebSocket
   (portas 9223–9232, com fallback automático de porta)
4. Plugin de desenvolvimento precisa ser rodado a cada sessão

### 2.3 Sanidade

`figma_get_status` com `probe: true` → bridge conectado, arquivo e
fileKey reportados (latência do probe no teste: 4ms).

---

## 3. Roteiro de testes — RESULTADOS

### T0 — Inventário de tools

Resultado: ✅ — 117 tools expostas; todos os nomes usados no roteiro
existem. Bridge conectado, probe 4ms. `figma_get_status` já expõe
`currentFileKey` real (identificador criptográfico, não editável).

---

### T1 — Criar a PRIMEIRA instância de um componente
**Cobre**: limitação nº 1 do figma-mcp-go

Resultado: ✅ — componente `Smoke/Botao` criado com zero instâncias;
`figma_instantiate_component` (componentKey + nodeId) criou instância
`type: INSTANCE` vinculada ao mãe correto. **Limitação nº 1
eliminada.** Ressalva: com `parentId` apontando para frame com Auto
Layout a tool deu timeout (ver achado crítico em T12); com Section
como pai funcionou de primeira. Fallback via `figma_execute`
(`comp.createInstance()`) sempre funciona.

---

### T2 — Combinar componentes em variantes
**Cobre**: limitação nº 2 do figma-mcp-go

Resultado: ✅ — os DOIS modos funcionaram sem passo manual:
- Combinar existentes: `Smoke/Chip` (2 variantes, property
  `state=default|selected` correta no set)
- Matriz de base: `Smoke/Tag` com eixos `size×tone` → 4 variantes,
  base preservado como primeira variante, `autoArrange` gerou grid
  rotulado. **Limitação nº 2 eliminada.**

---

### T3 — Auto Layout na criação + conversão sem reset de sizing
**Cobre**: erro nº 8 do figma-mcp-go

Resultado: ✅ — frame 200×90 `FIXED/FIXED` convertido com
`figma.createComponentFromNode()`; releitura no MESMO bloco:
`200×90`, `FIXED/FIXED`, `layoutMode/itemSpacing` intactos. O reset
para "hug" não se reproduz pelo caminho de código direto — e mesmo se
ocorresse, verificação+correção acontecem na mesma operação.

---

### T4 — Leitura de Auto Layout (incl. sizing modes)
**Cobre**: erro nº 6 do figma-mcp-go

Resultado: ⚠️ aprovado com ressalva — os formatos de leitura padrão
NÃO expõem Auto Layout nesta versão: `figma_get_component`
`reconstruction` retornou stub raso (dimensões erradas 50×50),
`metadata` sem layout, `figma_get_file_data` idem. PORÉM via
`figma_execute` TODAS as propriedades são legíveis de forma
determinística: `layoutMode`, `itemSpacing`, paddings E os sizing
modes (`layoutSizingHorizontal/Vertical`) — que hoje são
"não verificáveis" no figma-mcp-go. O auditor passa a verificar 100%
da regra de Auto Layout, mas pelo caminho de código.

---

### T5 — Variáveis: criar, vincular (fill E não-fill), IDs, deletar
**Cobre**: erro nº 7 do figma-mcp-go + capacidade de binding

Resultado: ✅ — tudo funcionou:
- Coleção `smoke-tokens` + variáveis COLOR e FLOAT criadas
- IDs no mesmo formato prefixado do MCP atual
  (`VariableID:4016:22174`), mas documentados no schema das tools;
  round-trip sem erro em bind e delete
- Binding fill via `figma_set_fills` + `variableId` (declarativo) ✅
- Binding padding/itemSpacing via `figma_execute` +
  `setBoundVariable` ✅ (valor real do nó atualizado pelo token)
- `figma_delete_variable` e `figma_delete_variable_collection` ✅

---

### T6 — Export/import de tokens em DTCG

Resultado: ⚠️ aprovado com ressalva séria —
- Export DTCG (escopo `file`): ✅ estruturalmente compatível com os
  `*.tokens.json` do harness (`$type`/`$value`, grupos aninhados,
  FLOAT→`dimension`, metadata de round-trip em `$extensions`)
- Import diff-aware: ✅ mecânica correta (dry-run, merge preservou os
  25 tokens só-do-Figma, valores aplicados certos)
- **RESSALVA**: o pipeline de export/import usa snapshot próprio que
  NÃO enxerga coleções criadas na mesma sessão via
  `create_variable_collection` — `scope: collection` retornou vazio e
  o import **duplicou a coleção** `smoke-tokens` em vez de casar pelo
  nome (nem `refreshCache` do `figma_get_variables` resolve).
  **Regra prática**: escolher UMA via por coleção — ou nasce via
  `figma_import_tokens` (e o sync é confiável), ou nasce via
  `create_variable*` (e export/import não devem ser usados nela na
  mesma sessão). Duplicata foi deletada na limpeza do teste.

---

### T7 — Payload controlado em página densa
**Cobre**: erros nº 4 e 5 do figma-mcp-go (312k chars na tela de login)

Resultado: ✅ — a mesma seção de login (`164:3664`, 598 nós) foi
navegada em 2 chamadas de ~1–2KB cada: inventário raso da página →
contagem + leitura rasa de um frame específico → drill sob demanda.
Nunca chegou perto de estourar. Nota: o parâmetro `nodeIds` de
`figma_get_file_data` tem quirk (retorna a árvore de páginas em vez de
mergulhar no nó pedido) — o caminho preferido para leitura cirúrgica é
`figma_execute` com serialização rasa controlada.

---

### T8 — Gestão de páginas (criar, navegar, deletar — incl. a ativa)
**Cobre**: erro nº 3 do figma-mcp-go

Resultado: ✅ com ressalva conhecida —
- Navegar entre páginas (`setCurrentPageAsync`): ✅
- Deletar página NÃO-ativa: ✅
- Deletar página ATIVA: mesmo erro de plataforma de hoje (`Removing
  this node is not allowed`) — é comportamento do Figma, não do MCP;
  contorno idêntico (navegar antes), agora executável no MESMO bloco
  de código
- Criar página: bloqueado no sandbox pelo plano Starter do arquivo
  ("only 3 pages") — restrição de plano Figma, não do MCP; não afeta
  clientes em plano pago

---

### T9 — Screenshot e export de imagem
**Cobre**: dependência do `validator` e `onboard-scanner`

Resultado: ✅ — dois caminhos funcionais:
- `figma_capture_screenshot`: estado RUNTIME via plugin, imagem inline
  legível (validou visualmente todos os artefatos T1–T5, incluindo a
  cor do token no fill)
- `figma_get_component_image`: via REST, URL válida por 30 dias

---

### T10 — Leitura por fileKey SEM plugin

Resultado: ✅ com nota — `figma_get_status`/`figma_list_open_files`
expõem `fileKey` criptográfico do alvo de escrita (a checagem de
segurança do harness deixa de depender de `fileName` editável).
Transporte REST comprovado (shape da API REST no `get_file_data`, URL
S3 no export de imagem), `fileUrl` aceito nas tools de leitura. Teste
definitivo com um segundo arquivo nunca-bridged fica pendente para
quando houver um Legado real de cliente.

---

### T11 — boundVariables na leitura

Resultado: ⚠️ aprovado com ressalva — mesmo padrão do T4: ausente nos
formatos de leitura padrão, mas 100% legível via `figma_execute`
(`node.boundVariables` retornou fill e paddings vinculados com os IDs
corretos). A checagem hardcoded-vs-token do auditor é viável, pelo
caminho de código.

---

### T12 — Fluxo builder em miniatura (integração)

Resultado: ✅ com ACHADO CRÍTICO —
- Fluxo completo OK: tela com Auto Layout vertical → instância
  vinculada dentro dela → `itemSpacing` vinculado a token (valor do nó
  passou a 24, dirigido pela variável) → `figma_rename_node` →
  releitura estrutural → screenshot de confirmação
- **ACHADO CRÍTICO — timeout com efeito colateral**: as duas chamadas
  de `figma_instantiate_component` que reportaram "timed out after
  15000ms" na verdade EXECUTARAM (as instâncias apareceram na tela).
  Timeout de WebSocket ≠ falha limpa. **Consequência para o harness**:
  o protocolo de falha parcial do builder deve, após QUALQUER timeout,
  verificar o estado real no Figma antes de retentar — retentar às
  cegas duplica elementos (foi exatamente o que aconteceu no teste).

---

## 4. Gate de decisão — APLICADO

| Critério | Status |
|---|---|
| T1, T2, T3, T5, T7, T9, T10 todos ✅ | ✅ cumprido |
| T4, T8, T11 ✅ ou ⚠️ com caminho viável | ✅ cumprido (via `figma_execute`) |
| Nenhum eliminatório falhou | ✅ |

**Decisão do gate: APTO A MIGRAR**, condicionado às políticas abaixo.

## 5. Ressalvas operacionais para o plano de migração

1. **`figma_execute` é indispensável** (não opcional): leitura de Auto
   Layout/sizing/boundVariables, criação com controle fino e gestão de
   páginas dependem dele. A política recomendada no item 6 (opção A
   estrita, "só tools declarativas") é INVIÁVEL — adotar variante:
   tools declarativas onde existirem + `figma_execute` com código
   fazendo parte do plano aprovado.
2. **Timeout ≠ falha** (T12): todo agente de escrita deve verificar
   estado após timeout antes de retentar. Incluir no builder.md /
   preflight-builder.md na migração.
3. **Tokens: uma via por coleção** (T6): não misturar
   `create_variable*` com export/import na mesma coleção/sessão —
   risco de coleção duplicada.
4. **Leitura cirúrgica via código** (T7): não confiar no `nodeIds` de
   `figma_get_file_data`; padrão de duas passadas (raso → drill)
   continua valendo, agora via `figma_execute`.
5. `figma_instantiate_component` com `parentId` de frame Auto Layout:
   usar Section/página como destino e mover depois, ou instanciar via
   código direto no pai.

## 6. Decisão de política do `figma_execute` (registrar antes da migração)

- ~~**A (conservadora)**: builder usa só tools declarativas~~ —
  inviabilizada pelo teste (ver ressalva 1)
- **A' (recomendada)**: tools declarativas onde existirem;
  `figma_execute` permitido com o código incluído no plano aprovado
  pelo humano; proibido improvisar código fora do plano
- **B (flexível)**: builder escreve código livremente dentro do plano
  aprovado

Registrar a escolha em `memory/decisions.md` do primeiro projeto que
usar o servidor novo.
