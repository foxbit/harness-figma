# Journey State — _teste-interpreter (Registro de Produção Diária)

Reconstrução da jornada com o harness pós-migração (figma-console-mcp
+ design.md aprovado). Wireframe: `wireframe/tela-1.png` (2 telas
mobile). Plano do interpreter aprovado em 2026-07-11.

## Decisões humanas do plano (2026-07-11, Angelo Rosa)

- Plano aprovado como está; CTAs em VERDE por precedência do design.md
  (wireframe desenha azul — corrigido por regra §3/§9)
- Headers das 2 telas: **manter 2 distintos** (fiel ao wireframe), sem
  componente App Header unificado
- Documentação pendente (risco 1 do plano): formalizar **depois** da
  jornada, via documenter, junto com a promoção normal
- Card de indicador: builder deve REUTILIZAR o nó existente
  `4005:14450` como base (nunca recriar), corrigindo estética para
  design.md §7 (card branco radius 16, sombra sutil, label 20 navy)

## Sequência

1. [EM ANDAMENTO] Preflight: chips/abas de métrica (MIGRAR DO LEGADO)
2. [PENDENTE] Builder — Tela 1 "Minha produção" (ref. canônica:
   Dashboard Flashcards 2207:3041)
3. [PENDENTE] Builder — Tela 2 "Meus dados" (ref. canônica: Criação do
   simulado 881:1367 + Menu Mobile 764:55556)
4. [PENDENTE] Validator — jornada completa + comparação com o
   resultado antigo (feio) do teste anterior

## Telas construídas

(nenhuma ainda)

## Componentes novos criados nesta jornada

(nenhum ainda)

## Pendências de token acumuladas

(nenhuma ainda — atenção às lacunas já conhecidas do design.md §3:
verde de ação, azul de link e cinza de tabela não tokenizados)
