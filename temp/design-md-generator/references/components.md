# Referência de Componentes Básicos para o DESIGN.md

Este documento serve como referência de como os componentes básicos devem ser estruturados e descritos no arquivo `design.md`.

## Estrutura de Componentes no YAML

No YAML front matter, os componentes devem ser descritos usando referências aos tokens de cores, tipografia, arredondamento e espaçamento definidos anteriormente.

```yaml
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "10px 18px"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    borderColor: "{colors.hairline}"
    borderWidth: "1px"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "10px 18px"
  card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    borderWidth: "1px"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
  input-field:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    borderWidth: "1px"
    rounded: "{rounded.md}"
    padding: "10px 14px"
    typography: "{typography.body-md}"
  chip:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.secondary}"
    rounded: "{rounded.full}"
    padding: "6px 12px"
    typography: "{typography.caption}"
```

## Diretrizes de Estilo por Componente

### 1. Botões (Buttons)
- **Botão Primário**: Deve usar a cor de marca principal (`{colors.primary}`) como fundo para atrair a atenção do usuário. O texto deve ter alto contraste (`{colors.on-primary}`).
- **Botão Secundário**: Deve ser sutil, usando fundo transparente, borda fina em `{colors.hairline}` e texto na cor `{colors.primary}` ou `{colors.secondary}`.
- **Botão Terciário (Link)**: Fundo transparente, sem bordas, texto na cor `{colors.primary}` ou `{colors.secondary}`. Usado para ações de menor importância.

### 2. Cards
- **Estrutura**: Containers que agrupam informações relacionadas.
- **Estilo**: Devem usar a cor `{colors.surface-card}` como fundo. Em designs flat ou minimalistas, use bordas finas de 1px em `{colors.hairline}`. Em designs tradicionais, pode-se usar uma sombra extremamente suave.
- **Padding**: Deve usar o token `{spacing.lg}` ou `{spacing.md}` para garantir espaçamento interno confortável.

### 3. Campos de Entrada (Inputs)
- **Estados**: Devem prever estados visualmente distintos (padrão, focado, com erro, desabilitado).
- **Estilo**: Fundo na cor `{colors.canvas}` ou `{colors.neutral}`, borda fina em `{colors.hairline}` e cantos arredondados usando `{rounded.md}` ou `{rounded.sm}`.
- **Foco**: Ao receber foco, a borda deve mudar para `{colors.primary}` ou usar um anel de foco sutil.

### 4. Chips e Badges
- **Uso**: Usados para tags, categorias, status ou filtros rápidos.
- **Estilo**: Cantos totalmente arredondados usando `{rounded.full}` (estilo pílula). Fundo na cor `{colors.neutral}` e texto sutil na cor `{colors.secondary}`.

### 5. Listas (Lists)
- **Estrutura**: Itens empilhados verticalmente.
- **Estilo**: Itens individuais separados por uma linha fina em `{colors.hairline}`. Padding vertical consistente usando `{spacing.sm}` ou `{spacing.md}`.
