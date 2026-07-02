# Migração de Telas — Fluxo Leve

Este documento cobre um caso específico dentro do fluxo normal de
Produção: quando uma jornada nova envolve uma tela que já existe no
mundo legado (ex: a Home), mas ainda não tem versão no arquivo de
Produção.

Isso NÃO é um quarto escopo separado — é uma variação do fluxo de
Produção descrito em `CLAUDE.md`, usando o print da tela legada como
referência em vez de (ou junto com) um wireframe novo do Miro.

---

## Quando isso se aplica

Você decide reconstruir uma tela legada no momento em que uma jornada
nova a envolve — não antes, não em lote. Ex: se a jornada "Checkout —
Nova Etapa de Pagamento" parte da Home, a Home é reconstruída agora e
passa a fazer parte do escopo atualizado (arquivo de Produção); a versão
antiga permanece apenas no arquivo Legado, como está.

## Como isso muda o insumo do interpreter

- **Wireframe de entrada**: pode ser o print/export da tela legada
  (quando a intenção é só preservar o comportamento atual), o wireframe
  novo do Miro (quando a jornada traz uma intenção de UX nova para
  aquela tela), ou os dois juntos (quando parte da tela muda e parte
  se preserva)
- **História do usuário**: pode ser mínima quando não há mudança de
  UX pretendida — algo como "preservar o comportamento atual da Home,
  sem alteração de fluxo" — mas ainda assim deve existir, para o
  `validator` ter contra o que comparar

## Como isso se conecta com MIGRAR DO LEGADO e preflight

Os *componentes* dentro da tela legada seguem exatamente a mecânica já
definida em `CLAUDE.md`: o `interpreter` classifica cada elemento, e
qualquer coisa marcada `MIGRAR DO LEGADO` passa por preflight antes do
`builder` seguir. A tela em si (o frame) segue a mecânica de "tela nova
em Telas Atuais" descrita em `CLAUDE.md`, já que — do ponto de vista do
arquivo de Produção — ela realmente é nova ali, mesmo que já existisse
há anos no Legado.

## Resultado esperado

Ao final: a tela passa a existir em `Telas Atuais` do arquivo de
Produção, construída com componentes do design system novo (alguns
reusados, alguns recém-migrados via preflight). A versão antiga
continua intacta no arquivo Legado, sem nenhuma alteração, servindo de
referência histórica até que não seja mais necessária.
