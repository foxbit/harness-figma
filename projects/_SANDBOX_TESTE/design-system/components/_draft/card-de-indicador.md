# Card de indicador

## Status
em revisão

## Identidade Figma
- Component key: `4003:445436` (componente principal); instâncias: `4003:445445` ("Card 1"), `4003:445450` ("Card 2")
- Localização: arquivo `mcp-test`, página "_TESTE-Jornada-registro-producao" (id `4003:445430`)
- Tipo: componente composto (agrupa um sub-frame "Text Group" com dois textos + um placeholder de ícone)

## Propósito
Exibir um indicador numérico curto (label + valor) dentro de um card compacto, usado na Tela 1 "Minha produção" para mostrar métricas de produção (ex: distância a executar / já executada).

## Estrutura (composição)
- Card de indicador (COMPONENT, Auto Layout horizontal, padding 16/16/16/16, gap 12, 200x90px) — obrigatório
- Icon Placeholder (retângulo 40x40, corner radius 6, fundo `#CCCCCC`) — obrigatório na estrutura atual, mas é placeholder: precisa ser substituído pelo ícone ilustrativo final do wireframe antes de promover a componente ativo
- Text Group (frame filho, Auto Layout vertical, gap 4) — obrigatório
  - Label (texto 12px, cor `#666666`) — obrigatório
  - Valor (texto 24px Bold, cor `#1A1A1A`) — obrigatório

## Variantes existentes

| Nome da variante | Quando usar | Diferença estrutural |
|---|---|---|
| default | Único caso construído até agora: par de cards lado a lado mostrando duas métricas da mesma tela (itens 5 e 6 do wireframe) | Nenhuma — mesma estrutura-base, muda apenas o conteúdo de Label/Valor |

## Props / propriedades configuráveis

| Prop | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| Label | texto | sim | Texto curto identificando a métrica (ex: "A executar", "Executado") |
| Valor | texto | sim | Valor numérico com unidade, destacado em bold (ex: "924 m", "15 m") |
| Ícone | imagem | sim (hoje é placeholder) | Ilustração representando a métrica; atualmente um retângulo cinza `#CCCCCC` sem ilustração final |

## Tokens utilizados
<!-- Nenhum token formal está registrado ainda em design-system/tokens/ deste
projeto (arquivos colors.md, spacing.md, typography.md, radius-shadows.md
estão todos com [PREENCHER] vazio) — valores abaixo foram aplicados direto
no Figma pelo builder, sem token nomeado associado. Isto deve ser resolvido
antes de promover este componente a "ativo". -->
- Cor: sem token — valores hardcoded `#F0F0F0` (fundo do card), `#666666` (Label), `#1A1A1A` (Valor), `#CCCCCC` (Icon Placeholder)
- Espaçamento: sem token — padding 16px (todos os lados), gap 12px (entre ícone e Text Group), gap 4px (entre Label e Valor), aplicados como valores soltos no Auto Layout
- Tipografia: sem token — 12px (Label), 24px Bold (Valor), aplicados como valores soltos

## Quando usar
Para exibir uma métrica numérica isolada (rótulo curto + valor destacado) em telas de acompanhamento/produção, quando duas ou mais métricas relacionadas precisam aparecer lado a lado em formato de card compacto (200x90px).

## Quando NÃO usar
Não usar para cards com múltiplas linhas de texto, ações (botões) ou navegação — este componente é somente leitura/exibição de indicador. Não confundir com um possível "Card" genérico do design system (nenhum registrado ainda neste projeto) que aceite conteúdo livre — o "Card de indicador" tem estrutura fixa (ícone + label + valor) e não deve ser generalizado para outros usos sem nova avaliação.

## Componentes relacionados
- Similar, mas diferente: nenhum componente equivalente encontrado no design-system oficial (`design-system/components/`, nenhum arquivo além do `_TEMPLATE.md` existia antes deste draft) nem em `onboarding-inventory.md` do arquivo legado — por isso foi classificado como COMPONENTE NOVO pelo interpreter, não MIGRAR DO LEGADO
- Compõe-se de: Text Group (sub-frame interno, não é um componente do design system à parte) + Icon Placeholder (retângulo placeholder, não é o componente de ícone final)
- É composto dentro de: nenhum componente maior até o momento — usado diretamente na Tela 1 "Minha produção"

## Histórico
- Criado em: `2026-07-02` — contexto: jornada `_teste-interpreter`, Tela 1 "Minha produção" do wireframe `exemplo-wireframe.pdf`, itens 5 e 6, identificado pelo `interpreter` como recorrência estrutural (mesmo componente-base, valores diferentes) e classificado como COMPONENTE NOVO. Construído pelo `builder` no arquivo `mcp-test`, página "_TESTE-Jornada-registro-producao"; duas instâncias criadas ("Card 1" com Label "A executar"/Valor "924 m", "Card 2" clone de "Card 1" com Label "Executado"/Valor "15 m")
</content>
