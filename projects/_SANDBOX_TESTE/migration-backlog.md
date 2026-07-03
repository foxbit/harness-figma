<!--
TESTE DE FUMAÇA — projeto _SANDBOX_TESTE, não é cliente real.
-->

# Migration Backlog — `_SANDBOX_TESTE` (mcp-test)

> **Baseado em inventário PARCIAL** (2 de 75 páginas do Legado — ver
> `onboarding-inventory.md`). Este backlog cobre apenas o que foi
> identificado nessas 2 páginas e resolvido pelas 25 decisões em
> `onboarding-decisions.md`. Um onboarding real deve gerar backlogs
> adicionais conforme as 73 páginas restantes forem varridas.
>
> Prioridade reflete o mesmo critério já usado pelo `onboard-analyst` em
> `onboarding-questions.md` (nº de ocorrências / impacto potencial em
> telas futuras / bloqueio de ferramenta), não uma nova reavaliação.

---

## P0 — Bloqueia ferramenta, não só reuso

### 1. Corrigir variante duplicada `Tipo=3 dias` no set "Card" (`749:23237`)
- **Decisão**: Q9 (negociada de verdade)
- **Justificativa de prioridade**: esta é a causa mais provável do erro
  `"Component set for node has existing errors"` que bloqueia
  `get_local_components` para a página "Componentes" **inteira** (618
  nós). Enquanto não corrigida, qualquer varredura futura via
  `get_local_components` continua exigindo o contorno via
  `scan_nodes_by_types`. Maior alavancagem de esforço de todo o backlog:
  uma correção pontual desbloqueia a ferramenta para os outros 617 nós.
- Documentado em: `design-system/components/card-recorrencia-e-status.md`
- Ação: investigação pontual no Figma Desktop (autorizada por Q9),
  depois preflight normal de reconstrução.

---

## P1 — Consolidações de alto impacto (usadas em muitos módulos)

### 2. Consolidar "Modal confirmação" (~16 ocorrências) em componente único
- **Decisão**: Q1 (negociada de verdade)
- **Justificativa de prioridade**: maior nº de duplicatas de nível
  superior do inventário; espalhado por simulados, flashcards,
  cronômetro e planos de estudo — qualquer jornada nova nesses módulos
  provavelmente precisa deste componente. Resolver uma vez evita
  recriar (ou pior, duplicar de novo) em cada jornada futura.
- Documentado em: `design-system/components/modal-de-confirmacao.md`
- Ação: preflight-planner deve inspecionar os 16 nós de origem
  (`get_node` individual, não feito nesta amostra) para confirmar que a
  variação de conteúdo cabe nas props propostas antes do
  preflight-builder reconstruir.

### 3. Consolidar "Modal Genérica" (9x), "Pop up" (7x) e "Toasty/Default" (7x)
- **Decisão**: Q6 (decisão-padrão de teste)
- **Justificativa de prioridade**: mesmo padrão de Q1, terceiro maior
  grupo de duplicatas por contagem agregada (23 nós ao todo). Overlay
  genérico e toast são primitivos usados por praticamente qualquer
  jornada — alto risco de bloqueio se não resolvidos antes de começar
  produção em qualquer módulo.
- Documentado em: `design-system/components/modal-generico.md` (só a
  família "Modal Genérica" tem arquivo próprio nesta amostra; "Pop up" e
  "Toasty" ainda precisam de documentação equivalente antes do
  preflight)
- Ação: preflight-planner deve tratar como 3 componentes distintos
  (Modal Genérica, Pop-up, Toast), cada um com seu próprio
  `design-system/components/[nome].md` antes da reconstrução.

### 4. Renomear e reestruturar "Container" (15+ usos distintos)
- **Decisão**: Q2 (decisão-padrão de teste)
- **Justificativa de prioridade**: segundo maior grupo por contagem
  bruta de nós (15+), mas BAIXO risco de consolidação equivocada porque
  a decisão já é "não consolidar, renomear cada um" — o esforço aqui é
  de nomenclatura, não de re-design, mais rápido de executar que P1.2/P1.3.
- Ação: preflight-planner mapeia os 15+ ids para nomes específicos
  (tabela antigo→novo) antes de qualquer um deles ser migrado
  individualmente sob demanda.

### 5. Renomear "Card" (10+ component sets sem relação)
- **Decisão**: Q3 (decisão-padrão de teste)
- **Justificativa de prioridade**: mesma lógica de Q2 — renomear, não
  consolidar. Um exemplo já foi tratado com prioridade máxima (P0.1,
  por causa do bug de variante duplicada), os demais 9+ podem seguir
  ordem normal, priorizados conforme a jornada que os demandar primeiro.
- Ação: mapear os 10+ ids restantes para nomes específicos quando cada
  jornada que os usa entrar em preflight (não há urgência isolada como
  no caso do Card já tratado).

### 6. Consolidar "Chip" (8 component sets com variantes diferentes)
- **Decisão**: Q4 (decisão-padrão de teste)
- **Justificativa de prioridade**: consolidação real (não só
  renomeação), então tem o mesmo risco de Q1/Q6 de a variação de
  conteúdo não caber num único set — mas o volume (8 sets) é menor,
  prioridade abaixo de Q1/Q6.
- Ação: preflight-planner precisa levantar as variant properties reais
  dos 8 sets de origem (dificuldade, status rascunho/publicado, tipo de
  material, progresso, cor) antes de desenhar o set consolidado.

---

## P2 — Duplicação de telas completas (não componentes atômicos)

### 7. Confirmar "Mobile/Tela visao geral" (7x) como telas distintas
- **Decisão**: Q5 (decisão-padrão de teste — manter nomes específicos por módulo)
- **Justificativa de prioridade**: são telas inteiras, não componentes
  reutilizáveis — o risco de bloqueio de reuso é baixo (cada uma já vai
  ganhar nome próprio), mas o volume de trabalho de renomeação é
  relevante (7 telas) e deve ser feito antes de qualquer preflight nos
  módulos correspondentes (simulados, flashcards, planos de estudo,
  cronômetro), para não perpetuar o nome genérico.

### 8. Confirmar "Acessar e navegar no material / Mobile" (6x) como estados/variações
- **Decisão**: Q7 (decisão-padrão de teste)
- **Justificativa de prioridade**: bloqueia especificamente o módulo
  "Leitor Digital" mobile — priorizar se uma jornada de leitor mobile
  entrar em produção; caso contrário, pode esperar.

### 9. Consolidar "Editior de documento" (2x, mesmo nome, typo)
- **Decisão**: Q8 (decisão-padrão de teste — manter só 1 versão, corrigir typo)
- **Justificativa de prioridade**: menor volume (2 nós), correção
  simples (é duplicata por engano, não variação real) — baixo esforço,
  pode ser feito a qualquer momento antes do preflight do módulo
  "Editor de documento".

---

## P3 — Jornada de Login (pronta para preflight)

### 10. Reconstruir componente "Login" com variant `Persona=`
- **Decisão**: Q24 (negociada de verdade) + Q25 (decisão-padrão de teste, tradução)
- **Justificativa de prioridade**: única jornada completa já com
  estrutura interna 100% levantada nesta amostra (via `get_node` ao
  vivo) — pronta para preflight sem levantamento adicional, diferente
  dos demais itens deste backlog que ainda precisam de `get_node`
  individual. Prioridade alta por estar "pronta para executar", mesmo
  não sendo a de maior volume de duplicatas.
- Documentado em: `design-system/components/login.md`
- Ação: preflight-builder reconstrói com variant `Persona=` (Estudante/
  Gestor) e traduz hint texts/supporting text para PT-BR (Q25).

### 11. Reclassificar telas fora de escopo na página "ML-001 - Login e Acesso"
- **Decisão**: Q23 (decisão-padrão de teste)
- **Justificativa de prioridade**: baixa urgência isolada — só é
  bloqueante quando as páginas correspondentes (Biblioteca Digital,
  Início/Boas-vindas, Leitor Digital) forem de fato varridas pelo
  `onboard-scanner` nas 73 páginas restantes. Registrado aqui para não
  ser esquecido, não para execução imediata.

---

## P4 — Nomenclatura e grafia (baixo risco, alto volume de pequenas correções)

### 12. Corrigir typos e padronizar grafia
- **Decisões**: Q10 (`Tiopo=`→`Tipo=`), Q11 (`Disbaled`→`Disabled`), Q12
  (acentuação `Médio`/`Difícil`), Q13 (`Mobile` padronizado), Q14
  (`Conometro`→`Cronometro`), Q15 (acento `Cronômetro`), Q16 (`Poistit`
  — candidato a descarte, confirmar uso real antes), Q17 (nome com
  quebra de linha)
- **Justificativa de prioridade**: nenhuma dessas correções bloqueia
  nada isoladamente — são acertos cosméticos de nomenclatura a aplicar
  no momento em que cada componente específico entrar em preflight por
  outro motivo (não justificam uma rodada de preflight só para isso).

### 13. Padronizar prefixos de variant property (`Tipo=`/`Estado=`)
- **Decisão**: Q18 (decisão-padrão de teste)
- **Justificativa de prioridade**: transversal — afeta a tabela de
  mapeamento antigo→novo de praticamente todo componente com variantes
  no arquivo. Deve ser tratada como regra de processo do preflight
  (aplicada a cada componente conforme migrado), não como um item único
  de backlog a "resolver de uma vez".

---

## P5 — Tokens e estilos (trabalho novo, não migração)

### 14. Criar tokens sólidos de cor, text styles e effect styles
- **Decisões**: Q19 (negociada de verdade), Q20 (descarte de variáveis
  residuais), Q21 (renomeação de `" Sem registro"` e `"Green light"`),
  Q22 (completar escala de opacidade 50/100)
- **Justificativa de prioridade**: sem token/style sólido definido, todo
  componente migrado hoje traz valor hardcoded (ver
  `design-system/components/card-de-indicador.md`, já registrado como
  pendência antes de promover a "ativo"). Isso é trabalho estrutural que
  idealmente acontece antes ou em paralelo ao primeiro preflight de
  qualquer componente visual — não bloqueia individualmente, mas sua
  ausência já gerou dívida técnica registrada em pelo menos um
  componente de produção.
- Documentado em: `design-system/tokens/colors.md` (completo, 7 paint
  styles + 8 variáveis de cor pós-decisão), `typography.md`,
  `spacing.md`, `radius-shadows.md` (confirmado que não há styles
  equivalentes no Legado para nenhum desses três).

---

## Resumo

| Prioridade | Item | Decisão(ões) | Bloqueia o quê |
|---|---|---|---|
| P0 | Card `749:23237` — duplicata `Tipo=3 dias` | Q9 | `get_local_components` da página inteira (618 nós) |
| P1 | Modal confirmação (16x) | Q1 | Reuso em simulados/flashcards/cronômetro/planos |
| P1 | Modal Genérica/Pop-up/Toasty (23x) | Q6 | Reuso transversal (overlay/toast em qualquer jornada) |
| P1 | Container (15+) | Q2 | Nomenclatura, baixo risco de execução |
| P1 | Card (10+ restantes) | Q3 | Nomenclatura, baixo risco de execução |
| P1 | Chip (8) | Q4 | Reuso em telas de progresso/dificuldade/status |
| P2 | Mobile/Tela visao geral (7x) | Q5 | Nomenclatura de 7 telas específicas |
| P2 | Acessar e navegar no material/Mobile (6x) | Q7 | Módulo Leitor Digital mobile |
| P2 | Editior de documento (2x) | Q8 | Módulo Editor de documento |
| P3 | Login (persona) | Q24, Q25 | Jornada de Login — já pronta para preflight |
| P3 | Página ML-001 — telas fora de escopo | Q23 | Reclassificação futura (depende de varredura das 73 páginas restantes) |
| P4 | Typos/grafia | Q10-Q17 | Nenhum bloqueio isolado — aplicar junto de outros preflights |
| P4 | Padrão de variant property | Q18 | Regra transversal de processo |
| P5 | Tokens sólidos/text/effect styles | Q19-Q22 | Dívida técnica em todo componente visual migrado |
