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

Antes de qualquer operação de escrita no Figma, confirmar que o
`file-key` do node de destino corresponde ao `file-key de produção`
declarado no `PROJECT.md` do projeto atualmente carregado. Se não
corresponder — incluindo se o destino for o file-key do legado — PARAR
e alertar. Nunca escrever no arquivo legado, em nenhuma circunstância.

A conta Figma é corporativa única (múltiplos clientes dentro dela). O
isolamento entre clientes é feito por esta verificação de configuração,
não por token separado.

---

## Estrutura de páginas do arquivo de Produção

O arquivo de Produção de cada cliente segue esta estrutura de páginas
(criada pelo preflight ao gerar o arquivo novo):

```
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

## Conexão MCP com o Figma (ambiente Linux)

Este harness usa o servidor MCP `figma-console-mcp`
(https://github.com/southleft/figma-console-mcp), não o MCP oficial do
Figma, por compatibilidade com Linux. Detalhes de setup: ver
`README.md`.

Ponto crítico de arquitetura: escrita no Figma (usada por `builder` e
`preflight-builder`) depende do plugin "Desktop Bridge" rodando dentro
do Figma Desktop app, que não tem build oficial para Linux. Agentes
somente-leitura (`interpreter`, `auditor`, `validator`,
`onboard-scanner`, `onboard-analyst`) funcionam via modo Remote SSE,
sem essa dependência. Ver `README.md` para as opções de contorno
(VM Windows, Wine, máquina física ocasional).

`[PREENCHER]` — nomes reais das tools MCP expostas pela conexão real
devem substituir os placeholders `figma_*` usados nos arquivos
`.claude/agents/*.md`.

---

## Fora de escopo deste harness (v1) — não implementar sem revisão

- Rollback automatizado de operações no Figma
- Múltiplos aprovadores / fluxo de aprovação por cliente
- Responsividade / breakpoints como processo funcional
- Conexão MCP direta com Miro (wireframes chegam como PDF/imagem)
- Portabilidade automática de assets entre arquivo legado e arquivo de
  produção — `[VALIDAR]` na prática, ver `onboarding/ONBOARDING.md`
