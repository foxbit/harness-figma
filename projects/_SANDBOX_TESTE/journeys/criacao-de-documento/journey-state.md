# journey-state — Criação de Documento na Biblioteca Digital

## Plano aprovado (interpreter, 2026-07-03)
Todos os elementos das Telas 1-2 classificados MIGRAR DO LEGADO:
1. Card de ação "Adicionar novo documento" — gatilho, Tela 1 (dashboard Biblioteca Digital)
2. Container do modal (overlay + card) — "Modal de edição", categoria não coberta por `modal-generico.md` nem `modal-de-confirmacao.md`
3. Input de texto "Nome do documento" — possível NOVA VARIANTE (contador/limite 100 caracteres), a confirmar no preflight
4. Select dropdown "Tipo do documento"
5. Botão primário "Adicionar" — `Buttons/Button` (`324:19820`), possível NOVA VARIANTE (loading spinner)
6. Botão secundário "Cancelar" — mesmo `Buttons/Button` (`324:19820`), variante link — **mesmo componente-base do item 5, não tratar como componente distinto**

Item 7 (tela do Editor, destino do redirect no Cenário 3) — escopo aprovado: Módulo 2 completo (MC-001), tratado como **Fase B separada**, com seu próprio `interpreter` antes de qualquer preflight (não veio como wireframe nesta rodada).

## Sequenciamento aprovado pelo humano
- Fase A (agora): preflight em lote para os 5 componentes acima (itens 1-6, com 5 e 6 compartilhando base) → builder monta Telas 1 e 2 → validator
- Fase B (depois): interpreter dedicado para a tela do Editor (Legado `8:38`, página "MC-001") → preflight → builder

## Preflight-planner (2026-07-03) — decisões aprovadas

- **Item 1 reclassificado**: "Card de ação Adicionar novo documento" não tem nó de origem 1:1 no Legado (não é migração real) — reclassificado de MIGRAR DO LEGADO para **COMPONENTE NOVO informado pelo Legado** (reaproveita footprint do `Card` de grid + padrão ícone/texto do botão "Criar" do empty-state `786:28599`).
- **color.primary** = `#003d76` sólido (não o Gradiente/Verde) — aprovado.
- **radius.full** = `9999` (não `100`) — aprovado, normaliza pill de botões e inputs no mesmo valor.
- **Buttons/Button**: formalizar eixo `Size=lg/sm` (10/16 e 8/12 padding respectivamente) em vez de escolher um único tamanho — aprovado.
- Overlay/backdrop do modal: construção nova, sem precedente confirmado no Legado.
- Buttons/Button: combinar variantes em component set exige passo manual do humano no Figma (limitação do MCP, `combineAsVariants` não suportado) — `preflight-builder` constrói cada variante avulsa e para antes da combinação.
- Tokens novos propostos (a registrar oficialmente pelo `documenter` só depois do `validator` aprovar): `color.primary` #003d76, `color.primary-emphasis` #00386b, `color.on-primary` #ffffff, `color.surface` #ffffff, `color.on-surface` #000000, `color.on-surface-muted` #535862, `color.hairline` #d5d7da, `radius.lg` 16, `radius.md` 8, `radius.full` 9999, `spacing.sm`/`spacing.md`/`spacing.lg`, `typography.heading-md` (Nunito Bold 20), `typography.caption` (Nunito Regular 14).

## Preflight-builder (2026-07-03) — construção
Todos os 6 itens construídos na página `Componentes — Harness (validados)` (`4005:14444`), arquivo `mcp-test`:
- Coleção de tokens `Design Tokens` (`VariableCollectionId:4011:49847`) com todos os valores aprovados + `state/disabled-opacity`=0.4 (novo, não estava na lista original — registrar no documenter)
- `Buttons/Button` — 5 variantes avulsas: Primary/lg/default (`4011:49869`), Primary/sm/default (`4011:49870`), Primary/lg/disabled (`4011:49871`), Primary/lg/loading (`4011:49872`, spinner é círculo estático, não animado — decisão pendente), Link/default (`4011:49873`)
- Input/Text com contador — `4011:49882` (placeholder "Digite o nome do documento" em `#717680` hardcoded, fora da lista de tokens aprovada — sinalizar para o documenter)
- Select/Dropdown "Tipo do documento" — REUSO DIRETO real, clonado de `734:25248` → `4011:49883` (avulso, texto corrigido) e `4011:49906` (dentro do Modal, texto corrigido)
- Modal de edição — Container `4011:49923`: overlay novo `4011:49899`, Select ok, mas os slots de Input/Text e os 2 Buttons (Cancelar/Adicionar) estão VAZIOS — sem tool de "criar instância" no MCP, precisam de ação manual do humano (arrastar do Assets panel)
- Card de ação "Adicionar novo documento" — `4011:49929`, corrigido para 347×187 (era 82 de altura, bug do `create_component` já documentado no CLAUDE.md #8). Radius/dimensão do Card de conteúdo original CONFIRMADOS via `search_nodes` nesta sessão: 347×187 real (bate com o assumido)

### Achado de plataforma (registrar em memória)
Editar a lista `tools:` de um agente `.md` não tem efeito em invocações do mesmo tipo dentro da MESMA sessão do Claude Code — definição parece carregada uma vez por sessão. Corrigido aplicando as 2 correções mecânicas (resize + set_text) diretamente na sessão principal, por decisão explícita do humano, como exceção pontual à separação de papéis (não uma decisão de design, só destravar um bug já aprovado).

## Ícones reais aplicados (sessão principal, 2026-07-03)
- Fechar (✕) no Cabeçalho do Modal (`4011:49901`): clonado o vetor real `635:40913` ("x (1) 1", do modal de edição de flashcard) → `4011:51566`. Placeholder de texto `4011:49905` removido.
- Plus no Card de ação (`4011:49925`): clonado a instância real `I786:28599;786:28586;3466:411727` ("plus", do empty-state "Criar") → `4011:51568`, centralizado (14,14) no círculo de 48×48. Placeholder de texto `4011:49928` removido.
- Achado de plataforma: `clone_node`/`move_nodes` usam coordenadas relativas ao node pai (não canvas absoluto, apesar da descrição do tool dizer "absolute" para `move_nodes`) — confirmado empiricamente ao posicionar o ícone plus.
- Decisão do usuário: loading spinner mantido como círculo estático por ora (não é problema de estrutura Figma, é comportamento de código/protótipo).

## Pendências (ação humana direta no Figma, não delegável a agente)
1. Combinar as 5 variantes de `Buttons/Button` em um único component set (`combineAsVariants`, sem tool no MCP)
2. Arrastar 3 instâncias para dentro do Modal: Input/Text (`4011:49882`), Link (`4011:49873`), Primary/lg (`4011:49869`) — nos slots vazios rotulados dentro de `4011:49923`

## Estado da construção
6 componentes construídos, 5 correções técnicas + 2 ícones reais aplicados. Falta: as 2 pendências manuais acima antes do `builder` poder montar as Telas 1 e 2 usando estes componentes como instâncias reais.
