# Decisões — _SANDBOX_TESTE

<!-- Formato: ver CLAUDE.md, seção "Formato de memory/decisions.md".
Este projeto é o sandbox do harness; decisões aqui registradas que
afetam o MOTOR (não um cliente) são espelhadas nos docs universais. -->

## 2026-07-11 — Migração do MCP: figma-mcp-go → figma-console-mcp

- **Contexto**: o `figma-mcp-go` tinha duas limitações que paravam o
  fluxo (sem criar primeira instância; sem combinar variantes) e mais
  quatro dores confirmadas (estouro de payload, Auto Layout ilegível,
  checagem por `fileName` editável, reset de sizing). O
  `figma-console-mcp` (Southleft) foi avaliado por smoke test completo
  neste sandbox — 13 testes, ver `smoke-test-figma-console-mcp.md` na
  raiz.
- **Decisão**: migrar o harness inteiro (CLAUDE.md, 10 agentes, skills,
  README, templates) para o `figma-console-mcp`, registro em escopo de
  usuário (token fora do git). O `figma-mcp-go` permanece em
  `.mcp.json` apenas como fallback até a primeira jornada real
  completar no servidor novo.
- **Motivo**: gate do smoke test aprovado — as duas limitações
  eliminadas, 6 dos 8 erros conhecidos deixam de existir, leitura do
  Legado sem plugin (proteção estrutural), checagem de escrita por
  `fileKey` criptográfico.
- **Decisão associada — política do `figma_execute` ("A'")**: tools
  declarativas onde existirem; `figma_execute` permitido com a
  intenção do código descrita no plano aprovado; em agentes
  somente-leitura, apenas código de leitura (restrição de prompt —
  trade-off consciente vs. whitelist hard). A opção "A estrita" (só
  declarativas) foi INVIABILIZADA pelo teste: leitura de Auto
  Layout/boundVariables e gestão de páginas exigem código.
- **Restrição de reversão**: reverter exige nova rodada de smoke test
  e reescrita dos 10 agentes — não reverter sem registro novo aqui.
  Os 3 quirks do servidor novo (timeout≠falha, sync de tokens,
  nodeIds sem drill-down) estão documentados em `CLAUDE.md`; se algum
  se provar bloqueante em jornada real, reavaliar antes de reverter.
- **Aprovado por**: Angelo Rosa (sessão de 2026-07-11).

## 2026-07-11 — design.md como insumo estético obrigatório (absorve principles.md)

- **Contexto**: teste de reconstrução da jornada no sandbox produziu
  resultado estruturalmente correto mas esteticamente ruim
  (componentes genéricos/feios). Diagnóstico: o harness alimentava os
  builders com estrutura (tokens, standards, wireframe) mas nenhum
  documento de identidade visual. Avaliou-se usar o Google Stitch para
  gerar um design.md a partir de prints; descartado como pipeline —
  inferir valores de imagem quando o Figma legado dá os valores exatos
  via MCP seria downgrade de fidelidade e adicionaria passo manual
  externo não versionado.
- **Decisão**: criar `design-system/design.md` por projeto (formato
  inspirado no Stitch: identidade/tom, tema, regras de cor/tipografia/
  forma/espaçamento, anatomia dos componentes-chave, Do/Don'ts e telas
  canônicas), gerado internamente pelo onboarding — valores numéricos
  sempre da fonte autoral, seções perceptuais descritas sobre as telas
  canônicas selecionadas pelo scanner. Absorve e substitui o
  `principles.md`. Consumo obrigatório por interpreter,
  preflight-planner, builder, preflight-builder e validator, com regra
  de precedência: token exato > design.md > julgamento do modelo.
- **Motivo**: dar subsídio estético concreto e verificável (Do/Don'ts
  checáveis em screenshot + referência canônica na delegação) é o que
  impede o modelo de "inventar" estética genérica.
- **Restrição de reversão**: nenhuma técnica; se o formato se provar
  insuficiente após o teste de aceitação (regerar a jornada feia do
  sandbox com design.md preenchido e comparar), evoluir o template em
  vez de abandonar — registrar aqui.
- **Aprovado por**: Angelo Rosa (sessão de 2026-07-11).
