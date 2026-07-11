<!--
[PREENCHER] Copie esta pasta inteira (projects/_EXEMPLO_CLIENTE) para
projects/[nome-real-do-cliente] e preencha os campos abaixo. Este
arquivo é o ponto de entrada de qualquer sessão de trabalho neste
projeto — os agentes de leitura usam o File-key do Legado para ler via
REST, e builder/preflight-builder/documenter confirmam o File-key de
Produção (via figma_get_status) antes de qualquer escrita.
-->

# Projeto: [Nome do Cliente]

## Figma — Legado
<!-- Arquivo antigo, mal estruturado. SOMENTE LEITURA — nenhum agente
escreve aqui, nunca. Usado como referência visual pelo onboarding e
pelo preflight. -->
- File-key: `[PREENCHER]`
  <!-- Campo crítico: identificador real do arquivo (está na URL:
  figma.com/design/<FILE-KEY>/...). É por ele que os agentes leem o
  Legado via REST — sem Figma Desktop e sem plugin. O plugin bridge
  NUNCA deve ser rodado neste arquivo (ver CLAUDE.md, "Regra de
  segurança"). -->
- Nome do arquivo (`fileName`, informativo para humanos): `[PREENCHER]`
- Team / Projeto no Figma: `[PREENCHER]`
- Link direto: `[PREENCHER]`

## Figma — Produção
<!-- Arquivo novo, criado pelo preflight na primeira reconstrução.
Único destino de escrita do builder e do preflight-builder. Fica vazio
até a primeira execução do preflight para este cliente. -->
- File-key: `[PREENCHER — vazio até o arquivo ser criado no 1º preflight]`
  <!-- Campo crítico: é contra ele que builder/preflight-builder/
  documenter confirmam o alvo de escrita (currentFileKey via
  figma_get_status) antes de qualquer operação. Registrar assim que o
  arquivo for criado (o key está na URL). -->
- Nome do arquivo (`fileName`, informativo): `[PREENCHER — vazio até o arquivo existir]`
- Team / Projeto no Figma: `[PREENCHER]`
- Link direto: `[PREENCHER]`

## Status de migração
<!-- Comunicação para humanos (você e o time do cliente) sobre onde
está a fonte da verdade de cada tela/jornada. Atualizar conforme telas
são migradas — ver migration/MIGRATION.md. -->
- Arquivo de Produção é fonte de verdade para: `[PREENCHER — lista de
  telas/jornadas já migradas, ex: "Home, Checkout"]`
- Arquivo Legado ainda é referência para: `[PREENCHER — o resto]`

## Particularidades deste cliente
<!-- Regras específicas que sobrepõem ou complementam o CLAUDE.md
universal. Exemplos de coisas que costumam entrar aqui: -->
- [PREENCHER — ex: "Não usar cor destrutiva em nenhum CTA (exigência de marca)"]
- [PREENCHER — ex: "Tokens de espaçamento seguem escala de 4px, não 8px"]
- [PREENCHER — ex: "Convenção de nomenclatura própria: ver COMPONENT_STANDARDS.md"]

## Aprovador(es)
<!-- Ver CLAUDE.md — hoje o harness assume um único aprovador humano.
Campo mantido para rastreabilidade futura mesmo que hoje seja sempre a
mesma pessoa. -->
- Nome: `[PREENCHER]`

## Contexto de negócio
<!-- Breve, só o suficiente para o interpreter/validator entenderem tom
e prioridade do produto. -->
[PREENCHER]
