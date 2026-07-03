<!--
TESTE DE FUMAÇA — projeto _SANDBOX_TESTE, não é cliente real.
-->

# Cobertura desta pasta — AMOSTRAL, NÃO COMPLETA

Este é um smoke test do `onboard-writer`. O inventário de origem
(`projects/_SANDBOX_TESTE/onboarding-inventory.md`) catalogou **618 nós**
do tipo `COMPONENT`/`COMPONENT_SET` na página "Componentes" do arquivo
Legado `mcp-test`, mais 5 instâncias de tela na página "ML-001 - Login e
Acesso" — mas esse inventário cobre só **2 das 75 páginas** do arquivo.

Esta pasta **não documenta os 618 nós um a um**. Por instrução explícita
do teste, foram escolhidos **4 componentes reais e distintos** como
amostra representativa, cobrindo diferentes tipos de decisão registrados
em `onboarding-decisions.md`:

| Arquivo | Decisão(ões) coberta(s) | O que representa |
|---|---|---|
| `modal-de-confirmacao.md` | Q1 (negociada de verdade) | Consolidação de ~16 componentes de nível superior duplicados em um único componente parametrizável |
| `modal-generico.md` | Q6 (decisão-padrão de teste) | Mesmo padrão de consolidação do Q1, aplicado à família "Modal Genérica" (9 duplicatas) — documentado à parte por ser um componente conceitualmente diferente de "Modal de Confirmação" |
| `card-planos-revisao.md` | Q9 (negociada de verdade) + Q3/Q18 (decisão-padrão de teste) | Componente com variante duplicada (`Tipo=3 dias` aparecendo 2x no mesmo set) que causava o erro de `get_local_components`; também exemplo do problema de nomenclatura genérica "Card" e de propriedade `Tipo=` sobrecarregada |
| `login.md` | Q24 (negociada de verdade) + Q25 (decisão-padrão de teste) | Componente com 2 instâncias de persona (Estudante/Gestor) e hint texts em inglês pendentes de tradução |

Todos os outros ~614 nós do inventário (Container, Chip, Toasty, Pop up,
Card curso, Progresso, Cronômetro, etc. — ver `onboarding-inventory.md`
seção 1.2) **não têm arquivo `.md` correspondente ainda**. Um onboarding
real, não-smoke-test, deve repetir este processo para cada componente
único remanescente (depois de aplicadas as decisões de consolidação
registradas), e para as 73 páginas do arquivo Legado ainda não varridas.

Todos os componentes desta pasta estão com `Status: em revisão` —
nenhum foi promovido a `ativo` (isso só acontece após preflight +
documenter, nunca durante onboarding).
