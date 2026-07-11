<!--
[PREENCHER] Identidade visual do projeto — o documento que ensina os
agentes a construir COM A CARA deste cliente, não algo genérico.

Gerado pelo onboarding (onboard-writer) a partir do Figma legado real:
valores numéricos vêm SEMPRE da fonte autoral via MCP (tokens, styles,
nós — nunca estimados de imagem); as seções perceptuais (tom,
densidade, Do/Don't) são descritas olhando as telas canônicas e
validadas pelo humano. Nasce com Status: em revisão e só vale após
aprovação humana.

Consumidores: interpreter e preflight-planner (planos citam este doc),
builder e preflight-builder (crítica visual contra os Do/Don'ts e as
referências canônicas), validator (coerência estética da jornada).
Regra de precedência (ver CLAUDE.md): token exato > design.md >
julgamento do modelo.

Cliente sem Figma legado (só prints/site): mesmo template, preenchido
por inferência visual — marcar cada valor inferido com [INFERIDO], e
substituir pelo valor real assim que existir fonte autoral.
-->

# Identidade Visual — [Nome do Cliente]

Status: [em revisão | aprovado]
Fonte: [arquivo Figma legado (File-key) | inferido de prints/site]
Aprovado por: [PREENCHER]

## 1. Identidade e tom
<!-- O que o produto é, para quem, e 3–5 adjetivos de personalidade
visual (ex: "sóbrio, denso, institucional" vs. "leve, arredondado,
amigável"). É o filtro para toda decisão estética não coberta por
regra explícita. -->
[PREENCHER]

## 2. Tema visual
<!-- Densidade de informação (compacta/espaçada), superfícies (flat /
elevação com sombras / hairlines), light/dark, uso de cor (contida ou
expressiva). -->
[PREENCHER]

## 3. Cor — papéis e regras de uso
<!-- NÃO repetir a tabela de tokens (vive em tokens/colors.md) — aqui
entram as REGRAS: proporção (ex: primária só em CTAs e navegação
ativa), fundos permitidos, estados, contraste mínimo. Referenciar
sempre o token semântico (color.primary), nunca hex solto. -->
- [PREENCHER — ex: "color.primary aparece UMA vez por seção (CTA principal); nunca em texto corrido"]

## 4. Tipografia — hierarquia real
<!-- Escala REAL extraída do Figma: papel → família/peso/tamanho/
line-height. Papéis mínimos: display, título de seção, corpo, apoio/
caption, botão. -->
| Papel | Família | Peso | Tamanho | Line-height | Uso |
|---|---|---|---|---|---|
| [PREENCHER] | | | | | |

## 5. Forma — raios, bordas e sombras
<!-- Valores reais por CLASSE de elemento (não por componente):
ex. "cards: radius.lg; inputs e botões: radius.md; chips/avatares:
radius.full". Sombras: níveis existentes e quando cada um aparece. -->
[PREENCHER]

## 6. Espaçamento e layout
<!-- Escala em uso (ref. tokens/spacing.md), ritmo interno de
componentes vs. respiro entre seções, larguras de container/grid das
telas, alinhamentos dominantes. -->
[PREENCHER]

## 7. Anatomia dos componentes-chave
<!-- Para os 3–6 componentes centrais (ex: Button, Card, Input):
estrutura resumida, estados existentes, e a regra de ouro de cada um.
Detalhe completo vive em components/*.md — aqui é o resumo que o
builder consulta sem abrir tudo. -->
### [Componente]
- Anatomia: [PREENCHER]
- Estados: [PREENCHER]
- Regra de ouro: [PREENCHER]

## 8. Hierarquia de ações
<!-- Absorvido do antigo principles.md. Ex: nunca mais de uma ação
"primary" visível por seção; destrutivas sempre exigem confirmação. -->
[PREENCHER]

## 9. Do / Don't — erros estéticos proibidos
<!-- A seção mais importante para os builders: lista DURA do que nunca
fazer neste projeto. Ex: "NUNCA sombra em elemento dentro de card";
"NUNCA texto primário abaixo de 14px"; "NUNCA botão com hug vertical —
altura fixa 40px". Cada item deve ser verificável num screenshot. -->
- DO: [PREENCHER]
- DON'T: [PREENCHER]

## 10. Referências canônicas
<!-- As 3–5 telas que melhor representam a linguagem visual, escolhidas
pelo onboard-scanner e confirmadas pelo humano. Builders recebem UMA
delas como referência visual em cada delegação. -->
| Tela | nodeId | Página no Figma | Por que é canônica |
|---|---|---|---|
| [PREENCHER] | | | |

## 11. Acessibilidade específica do projeto
<!-- Absorvido do antigo principles.md. -->
[PREENCHER]

## 12. Casos de exceção conhecidos
<!-- Situações onde a regra geral não se aplica e por quê. -->
[PREENCHER]
