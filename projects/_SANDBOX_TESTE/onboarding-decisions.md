<!--
TESTE DE FUMAÇA — projeto _SANDBOX_TESTE, não é cliente real.

As 4 primeiras decisões (Q1, Q9, Q19, Q24) foram negociadas de verdade,
uma pergunta por vez, com o humano, testando o mecanismo real de
negociação do onboarding. As demais (Q2-Q8, Q10-Q18, Q20-Q23, Q25) são
DECISÕES-PADRÃO DE TESTE, preenchidas pela sessão principal só para
permitir que o onboard-writer rode sem bloqueio de perguntas pendentes
— não representam deliberação real de um cliente/time de produto.
-->

# Decisões de Onboarding — `_SANDBOX_TESTE` (mcp-test)

## Q1 — "Modal confirmação" (~16 duplicatas) — NEGOCIADA DE VERDADE
**Decisão**: Consolidar num único componente parametrizável (texto/contexto via prop), reusado por todos os módulos.

## Q2 — "Container" (15+ usos distintos) — decisão-padrão de teste
**Decisão**: Cada um recebe nome específico do contexto (ex.: "Calendar Event Container", "Cronômetro / Container Estado"), nunca "Container" genérico.

## Q3 — "Card" (10+ component sets sem relação) — decisão-padrão de teste
**Decisão**: Renomear cada um com nome que descreva o contexto (dificuldade de flashcard, status de plano de estudo, admin, apostilas/simulados).

## Q4 — "Chip" (8 component sets com variantes diferentes) — decisão-padrão de teste
**Decisão**: Mesmo componente-base "Chip" — consolidar em um único component set com todas as variantes observadas.

## Q5 — "Mobile/Tela visao geral" (7x) — decisão-padrão de teste
**Decisão**: São 7 telas de fato distintas (uma por módulo) — manter nomes próprios e específicos no design system novo (ex.: "Simulados / Mobile / Visão geral").

## Q6 — "Modal Genérica"/"Pop up"/"Toasty/Default" (7-9x cada) — decisão-padrão de teste
**Decisão**: Consolidar em um componente único reutilizável por tipo (modal genérico, pop-up, toast), mesma linha do Q1.

## Q7 — "Acessar e navegar no material / Mobile" (6x) — decisão-padrão de teste
**Decisão**: São estados/variações reais da mesma tela mobile do leitor — tratar como variantes de um componente, não duplicação por engano.

## Q8 — "Editior de documento" (2x, typo, mesmo nome exato) — decisão-padrão de teste
**Decisão**: Duplicata por engano — manter só uma versão no design system novo, corrigindo o typo para "Editor de documento".

## Q9 — Variante duplicada `Tipo=3 dias` no set "Card" (749:23237) — NEGOCIADA DE VERDADE
**Decisão**: Sim, autorizar investigação pontual no Figma Desktop para corrigir antes do preflight reconstruir este componente.

## Q10 — "Tiopo=" (typo) — decisão-padrão de teste
**Decisão**: Corrigir para "Tipo=" no design system novo.

## Q11 — "Disbaled" (typo) — decisão-padrão de teste
**Decisão**: Corrigir para "Disabled".

## Q12 — "Médio"/"Medio", "Difícil"/"Dificil" (acentuação) — decisão-padrão de teste
**Decisão**: Padronizar com acentuação correta — "Médio" e "Difícil" — em todo o design system novo.

## Q13 — "Mobile"/"Mobil"/"mobile" (grafia) — decisão-padrão de teste
**Decisão**: Padronizar para "Mobile" (capitalizado, sem erro).

## Q14 — "Conometro" (typo) — decisão-padrão de teste
**Decisão**: Corrigir para "Cronometro" (ver Q15 para acentuação final).

## Q15 — "Cronometro"/"Cronômetro" (acentuação) — decisão-padrão de teste
**Decisão**: Padronizar com acento — "Cronômetro" — em todo o design system novo.

## Q16 — "Poistit" (nome não reconhecível) — decisão-padrão de teste
**Decisão**: Marcar como candidato a descarte do escopo de migração — não confirmado uso real (numa decisão de cliente real, isso exigiria confirmação explícita do time de produto antes de descartar).

## Q17 — Nome com quebra de linha literal — decisão-padrão de teste
**Decisão**: Renomear para "Período de estudo — CTA configurar" (sem quebra de linha).

## Q18 — Prefixos de variant property inconsistentes (Tipo=/Status=/State=/Admin=/etc.) — decisão-padrão de teste
**Decisão**: Padronizar um nome de propriedade único por conceito (sempre "Estado=" para interação, sempre "Tipo=" para variação visual/conteúdo), com tabela de mapeamento antigo → novo. Isso entra no escopo do preflight.

## Q19 — Ausência de tokens sólidos (só 7 paint styles gradiente) — NEGOCIADA DE VERDADE
**Decisão**: Confirmado — são tokens novos, trabalho do preflight, sem equivalente a migrar do legado.

## Q20 — Variáveis suspeitas (`Title`, `String`, `Pergunta`) — decisão-padrão de teste
**Decisão**: Resíduo de conteúdo/teste — descartar do design system novo.

## Q21 — Variáveis fora do padrão (`" Sem registro"`, `"Green light"`) — decisão-padrão de teste
**Decisão**: Renomear ambas para seguir o padrão `"Estilos de formatação/[Nome]"` em português.

## Q22 — Escala de opacidade incompleta — decisão-padrão de teste
**Decisão**: Padronizar escala `50`/`100` para todas as cores base do design system novo.

## Q23 — Página ML-001 com telas de outros módulos misturadas — decisão-padrão de teste
**Decisão**: Sim — quando as 73 páginas restantes forem varridas, reclassificar essas telas nas páginas/jornadas correspondentes; a jornada de Login no design system novo deve conter só as instâncias de "Login".

## Q24 — Duas personas de Login (portal de gestão vs. portal do estudante) — NEGOCIADA DE VERDADE
**Decisão**: São duas personas reais (Estudante/Gestor) — devem virar variant property `Persona=` no design system novo, ambas migradas.

## Q25 — Hint texts em inglês não traduzidos — decisão-padrão de teste
**Decisão**: Traduzir para PT-BR como parte da reconstrução no design system novo.
