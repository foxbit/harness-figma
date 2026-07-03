#!/usr/bin/env python3
import sys
import json
import os

def build_design_md(data):
    brand_name = data.get("brand_name", "Minha Marca")
    description = data.get("description", "Um sistema de design moderno e consistente.")
    theme = data.get("theme", "Minimalism")
    icon_set = data.get("icon_set", "Phosphor Icons")
    
    # Cores
    colors = data.get("colors", {})
    primary_color = colors.get("primary", "#000000")
    secondary_color = colors.get("secondary", "#666666")
    tertiary_color = colors.get("tertiary", "#FF0000")
    neutral_color = colors.get("neutral", "#F5F5F5")
    canvas_color = colors.get("canvas", "#FFFFFF")
    surface_color = colors.get("surface", "#FFFFFF")
    hairline_color = colors.get("hairline", "#E5E5E5")
    on_primary = colors.get("on_primary", "#FFFFFF")
    
    # Fontes
    fonts = data.get("fonts", {})
    heading_font = fonts.get("heading", "Inter")
    body_font = fonts.get("body", "Inter")
    
    # Tom e Voz
    tone_voice = data.get("tone_voice", {})
    personality = tone_voice.get("personality", "Profissional, direto e confiável.")
    audience = tone_voice.get("audience", "Profissionais e desenvolvedores.")
    emotion = tone_voice.get("emotion", "Confiança, clareza e eficiência.")
    
    # Shapes e Spacing
    rounded = data.get("rounded", {"sm": "4px", "md": "8px", "lg": "12px", "full": "9999px"})
    spacing = data.get("spacing", {"xs": "4px", "sm": "8px", "md": "16px", "lg": "24px", "xl": "32px"})
    
    # Do's and Don'ts
    dos = data.get("dos", ["Manter consistência visual.", "Usar espaçamento semântico."])
    donts = data.get("donts", ["Usar cores fora da paleta.", "Misturar múltiplos estilos de ícones."])

    # Montando o YAML Front Matter
    md = f"""---
version: alpha
name: {brand_name}
description: {description}
colors:
  primary: "{primary_color}"
  secondary: "{secondary_color}"
  tertiary: "{tertiary_color}"
  neutral: "{neutral_color}"
  canvas: "{canvas_color}"
  surface-card: "{surface_color}"
  hairline: "{hairline_color}"
  on-primary: "{on_primary}"
typography:
  display-lg:
    fontFamily: "'{heading_font}', sans-serif"
    fontSize: "48px"
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: "-0.02em"
  display-md:
    fontFamily: "'{heading_font}', sans-serif"
    fontSize: "36px"
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: "-0.01em"
  heading-lg:
    fontFamily: "'{heading_font}', sans-serif"
    fontSize: "24px"
    fontWeight: 600
    lineHeight: 1.3
  heading-md:
    fontFamily: "'{heading_font}', sans-serif"
    fontSize: "20px"
    fontWeight: 600
    lineHeight: 1.4
  body-lg:
    fontFamily: "'{body_font}', sans-serif"
    fontSize: "18px"
    fontWeight: 400
    lineHeight: 1.5
  body-md:
    fontFamily: "'{body_font}', sans-serif"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: 1.6
  label-caps:
    fontFamily: "'{body_font}', sans-serif"
    fontSize: "12px"
    fontWeight: 500
    lineHeight: 1
    letterSpacing: "0.1em"
  caption:
    fontFamily: "'{body_font}', sans-serif"
    fontSize: "12px"
    fontWeight: 400
    lineHeight: 1.4
rounded:
  sm: "{rounded.get('sm', '4px')}"
  md: "{rounded.get('md', '8px')}"
  lg: "{rounded.get('lg', '12px')}"
  full: "{rounded.get('full', '9999px')}"
spacing:
  xs: "{spacing.get('xs', '4px')}"
  sm: "{spacing.get('sm', '8px')}"
  md: "{spacing.get('md', '16px')}"
  lg: "{spacing.get('lg', '24px')}"
  xl: "{spacing.get('xl', '32px')}"
components:
  button-primary:
    backgroundColor: "{{colors.primary}}"
    textColor: "{{colors.on-primary}}"
    typography: "{{typography.body-md}}"
    rounded: "{{rounded.md}}"
    padding: "10px 18px"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{{colors.primary}}"
    borderColor: "{{colors.hairline}}"
    borderWidth: "1px"
    typography: "{{typography.body-md}}"
    rounded: "{{rounded.md}}"
    padding: "10px 18px"
  card:
    backgroundColor: "{{colors.surface-card}}"
    borderColor: "{{colors.hairline}}"
    borderWidth: "1px"
    rounded: "{{rounded.lg}}"
    padding: "{spacing.get('lg', '24px')}"
  input-field:
    backgroundColor: "{{colors.canvas}}"
    borderColor: "{{colors.hairline}}"
    borderWidth: "1px"
    rounded: "{{rounded.md}}"
    padding: "10px 14px"
    typography: "{{typography.body-md}}"
  chip:
    backgroundColor: "{{colors.neutral}}"
    textColor: "{{colors.secondary}}"
    rounded: "{{rounded.full}}"
    padding: "6px 12px"
    typography: "{{typography.caption}}"
---

# DESIGN.md - {brand_name}

Este documento define as diretrizes de design, tom, voz e tokens de estilo para a marca **{brand_name}**. Ele serve como a única fonte de verdade para garantir a consistência visual e de comunicação em todas as interfaces e pontos de contato da marca.

## Overview

O estilo visual da marca **{brand_name}** é profundamente enraizado no tema **{theme}**. A interface busca transmitir sentimentos de **{emotion}** para o público-alvo de **{audience}**.

A personalidade da marca é definida como:
> "{personality}"

### Características Chave:
- **Tema de Design**: {theme}
- **Estilo de Ícones**: {icon_set}
- **Fontes Principais**: {heading_font} (Títulos) e {body_font} (Corpo)
- **Abordagem de Cores**: Foco no contraste entre a cor principal ({primary_color}) e tons neutros, usando a cor terciária ({tertiary_color}) para interações críticas.

## Colors

As cores abaixo definem a identidade visual da marca. Cada cor possui uma função específica no sistema.

### Brand & Accent
- **Primary ({primary_color})**: Usada para elementos de destaque, cabeçalhos principais e CTAs primários.
- **Secondary ({secondary_color})**: Usada para textos secundários, ícones de apoio e elementos utilitários.
- **Tertiary ({tertiary_color})**: Usada exclusivamente para estados ativos, interações críticas e destaques importantes.

### Surface & Canvas
- **Canvas ({canvas_color})**: A cor de fundo de todas as páginas, oferecendo uma base limpa.
- **Surface Card ({surface_color})**: Usada para fundos de componentes como cards, modais e containers.
- **Neutral ({neutral_color})**: Tons de cinza ou neutros para fundos secundários e áreas de baixo contraste.

### Borders & Lines
- **Hairline ({hairline_color})**: Usada para bordas finas de 1px, divisores e linhas de separação de componentes.

## Typography

Nossa estratégia tipográfica utiliza a fonte **{heading_font}** para títulos para estabelecer uma presença marcante, e **{body_font}** para o corpo do texto, garantindo excelente legibilidade.

| Token | Font Family | Size | Weight | Line Height | Letter Spacing |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `display-lg` | {heading_font} | 48px | 600 | 1.1 | -0.02em |
| `display-md` | {heading_font} | 36px | 600 | 1.2 | -0.01em |
| `heading-lg` | {heading_font} | 24px | 600 | 1.3 | Normal |
| `heading-md` | {heading_font} | 20px | 600 | 1.4 | Normal |
| `body-lg` | {body_font} | 18px | 400 | 1.5 | Normal |
| `body-md` | {body_font} | 16px | 400 | 1.6 | Normal |
| `label-caps` | {body_font} | 12px | 500 | 1.0 | 0.1em |
| `caption` | {body_font} | 12px | 400 | 1.4 | Normal |

## Layout & Spacing

O sistema de espaçamento é baseado em uma escala lógica para manter o ritmo vertical e horizontal consistente.

- **xs ({spacing.get('xs', '4px')})**: Micro-espaçamentos, margens internas de ícones.
- **sm ({spacing.get('sm', '8px')})**: Espaçamento entre elementos relacionados (labels e inputs).
- **md ({spacing.get('md', '16px')})**: Espaçamento padrão entre componentes em um grupo.
- **lg ({spacing.get('lg', '24px')})**: Padding interno de cards e containers principais.
- **xl ({spacing.get('xl', '32px')})**: Margens grandes e espaçamento entre seções.

## Shapes

Nossa linguagem de formas segue o tema **{theme}**. Os cantos arredondados são aplicados de forma consistente usando a escala abaixo:

- **sm ({rounded.get('sm', '4px')})**: Usado para pequenos elementos como checkboxes, tags e tooltips.
- **md ({rounded.get('md', '8px')})**: Usado para botões, inputs e pequenos cards.
- **lg ({rounded.get('lg', '12px')})**: Usado para cards principais, modais e containers de conteúdo.
- **full ({rounded.get('full', '9999px')})**: Usado para avatares, chips e botões pílula.

## Elevation & Depth

A profundidade visual é alcançada de forma sutil, priorizando o contraste de cores e linhas de separação em vez de sombras pesadas, alinhando-se com a estética do tema **{theme}**.

- **Camadas de Tons**: O background principal usa `{canvas_color}`, enquanto elementos flutuantes ou em destaque usam `{surface_color}` com bordas de 1px em `{hairline_color}`.
- **Sombras**: Quando necessárias, as sombras devem ser extremamente suaves, usando opacidades baixas (ex: `box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05)`).

## Components

Estes são os componentes básicos do nosso sistema, construídos inteiramente a partir de referências aos tokens declarados.

### Buttons
- **Primary Button**: Utiliza `{colors.primary}` como fundo e `{colors.on-primary}` para o texto. Possui arredondamento `{rounded.md}`.
- **Secondary Button**: Fundo transparente com borda de 1px em `{colors.hairline}` e texto na cor `{colors.primary}`.

### Cards
- **Standard Card**: Fundo `{colors.surface-card}`, borda de 1px em `{colors.hairline}`, cantos arredondados `{rounded.lg}` e padding interno de `{spacing.lg}`.

### Inputs
- **Text Input**: Fundo `{colors.canvas}`, borda de 1px em `{colors.hairline}`, cantos arredondados `{rounded.md}` e padding interno de `10px 14px`.

### Chips & Badges
- **Status Chip**: Fundo `{colors.neutral}`, texto na cor `{colors.secondary}`, cantos totalmente arredondados `{rounded.full}` e padding de `6px 12px`.

## Do's and Don'ts

Diretrizes práticas para aplicação do sistema de design no dia a dia.

### Do's
"""
    for do in dos:
        md += f"- **Sim**: {do}\n"
        
    md += "\n### Don'ts\n"
    for dont in donts:
        md += f"- **Não**: {dont}\n"
        
    md += """
## References
1. [Stitch Official Documentation](https://stitch.withgoogle.com/docs/design-md/overview/) - Especificação oficial do formato DESIGN.md
2. [Google Fonts](https://fonts.google.com/) - Repositório de fontes gratuitas utilizadas no projeto
3. [Phosphor Icons](https://phosphoricons.com/) - Biblioteca de ícones de referência
"""
    return md

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 generate_design_md.py <caminho_dados_json>")
        sys.exit(1)
        
    json_path = sys.argv[1]
    if not os.path.exists(json_path):
        print(f"Arquivo não encontrado: {json_path}")
        sys.exit(1)
        
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    md_content = build_design_md(data)
    
    output_path = data.get("output_path", "design.md")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(md_content)
        
    print(f"DESIGN.md gerado com sucesso em: {output_path}")
