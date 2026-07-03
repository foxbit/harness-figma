---
name: design-md-generator
description: Gera arquivos DESIGN.md completos no padrão oficial do Google Stitch, baseando-se na análise de sites/arquivos e perguntas interativas sobre a marca, tom, voz, temas e componentes.
---

# Design MD Generator

Este skill guia você na criação de um arquivo `design.md` completo e estruturado de acordo com a especificação oficial do Google Stitch, otimizado para ser consumido por agentes de IA como o Claude.

O fluxo de trabalho consiste em analisar os assets da marca (site ou arquivo de style guide), fazer perguntas interativas estruturadas e gerar o documento final.

## Fluxo de Trabalho

### Passo 1: Análise Inicial da Marca
Solicite ao usuário o link do site da marca ou o caminho de um arquivo de style guide local. Execute o script de análise para extrair os tokens iniciais de cores e fontes:

```bash
python3 /home/ubuntu/skills/design-md-generator/scripts/analyze_brand.py <url_ou_caminho_arquivo>
```

O script retornará um JSON contendo as cores extraídas (hex) e fontes identificadas. Guarde esses dados para as etapas seguintes.

### Passo 2: Perguntas Guiadas e Interativas
Apresente ao usuário as opções de personalização com base nas informações coletadas e nas listas pré-estabelecidas do sistema. Faça as perguntas em blocos lógicos para não sobrecarregar o usuário.

#### Bloco A: Identidade e Tema
1. **Nome da Marca**: Confirmar o nome da marca.
2. **Descrição**: Uma breve descrição do produto ou serviço.
3. **Tema de Design**: Apresentar a lista de temas e solicitar a escolha de um:
   - *Glassmorphism*: Transparência e efeito de vidro fosco.
   - *Neumorphism*: Soft UI com sombras suaves e relevo.
   - *Skeuomorphism*: Imitação de objetos e texturas do mundo real.
   - *Flat Design*: Bidimensional puro, simples e geométrico.
   - *Minimalism*: Foco extremo no essencial, uso generoso de whitespace.
   - *Maximalism*: Cores vibrantes, composições densas e tipografia ousada.
   - *Brutalism / Neobrutalism*: Grids visíveis, bordas pretas grossas, sombras duras.
   - *Retro Futurism*: Estética anos 80/90 com gradientes neon.
   - *Swiss Style*: Grids precisos, layouts assimétricos, foco absoluto na ordem.
   - *Art Deco*: Padrões geométricos ricos, simetria e elegância clássica.

#### Bloco B: Tipografia e Ícones
1. **Fonte para Títulos (Headings)**: Apresentar opções do Google Fonts:
   - *Geist*: Moderna, limpa e geométrica.
   - *Instrument Serif*: Elegante, clássica e editorial.
   - *Plus Jakarta Sans*: Amigável e com excelente presença.
   - *Syne*: Artística e expressiva em tamanhos grandes.
   - *Montserrat*: Geométrica forte e confiável.
2. **Fonte para o Corpo (Body)**: Apresentar opções do Google Fonts:
   - *Inter*: O padrão ouro para legibilidade em telas.
   - *Plus Jakarta Sans*: Moderna e amigável.
   - *DM Sans*: Neutra e limpa em qualquer resolução.
   - *Manrope*: Contemporânea, equilibra técnica com calor humano.
   - *Roboto*: Clássica, neutra e confiável.
3. **Set de Ícones**: Apresentar os sets mais populares:
   - *Phosphor Icons*: Amigável, geométrico e muito consistente (recomendado).
   - *Tabler Icons*: Neutro, focado em stroke-based design.
   - *Heroicons*: Extremamente limpo, otimizado para Tailwind CSS.
   - *Feather Icons / Lucide Icons*: Minimalista, elegante e preciso.
   - *Material Icons*: Padrão do Google, extremamente completo.
   - *Remix Icon*: Neutro e elegante, com versões outline e solid.

#### Bloco C: Cores e Tokens Visuais
Apresente as cores extraídas pelo script no Passo 1 e peça para o usuário confirmar ou ajustar os papéis semânticos:
1. **Primary**: Cor principal da marca (usada em CTAs e destaques).
2. **Secondary**: Cor secundária (textos secundários, ícones).
3. **Tertiary**: Cor de destaque crítico ou interações ativas.
4. **Neutral**: Tons neutros para fundos secundários.
5. **Canvas**: Cor de fundo principal da página.
6. **Surface**: Cor de fundo de cards e containers.
7. **Hairline**: Cor para divisores e bordas finas de 1px.
8. **On-Primary**: Cor do texto sobre o fundo primário (alto contraste).

#### Bloco D: Tom e Voz
Faça perguntas simples para estruturar a comunicação da marca:
1. **Personalidade**: Como a marca se descreve? (Ex: "Inovadora, técnica mas amigável").
2. **Público-Alvo**: Para quem o produto é feito? (Ex: "Desenvolvedores e designers").
3. **Sentimento/Emoção**: Qual sentimento a interface deve evocar? (Ex: "Confiança, clareza e eficiência").

#### Bloco E: Boas Práticas (Do's and Don'ts)
Peça ao usuário para citar 2 ou 3 regras práticas de "Pode" (Do's) e "Não Pode" (Don'ts) para o uso do design system.

### Passo 3: Geração do Arquivo DESIGN.md
Com todas as respostas coletadas, estruture os dados em um arquivo JSON temporário e execute o script de geração:

```bash
python3 /home/ubuntu/skills/design-md-generator/scripts/generate_design_md.py <caminho_dados_json>
```

O script criará o arquivo `design.md` final no caminho especificado (geralmente no diretório do projeto ou na home do usuário).

### Passo 4: Entrega do Arquivo
Apresente o arquivo `design.md` gerado ao usuário e explique como ele pode ser usado como contexto em prompts para o Claude ou outras ferramentas de IA.

## Exemplo de Estrutura do JSON de Entrada para Geração

```json
{
  "brand_name": "Acme Corp",
  "description": "Plataforma de automação inteligente para equipes de design.",
  "theme": "Minimalism",
  "icon_set": "Phosphor Icons",
  "colors": {
    "primary": "#1A1C1E",
    "secondary": "#6C7278",
    "tertiary": "#B8422E",
    "neutral": "#F7F5F2",
    "canvas": "#FFFFFF",
    "surface": "#FFFFFF",
    "hairline": "#E5E5E5",
    "on_primary": "#FFFFFF"
  },
  "fonts": {
    "heading": "Geist",
    "body": "Inter"
  },
  "tone_voice": {
    "personality": "Técnica, focada em performance mas extremamente amigável.",
    "audience": "Profissionais de tecnologia, designers e desenvolvedores.",
    "emotion": "Foco, produtividade e clareza absoluta."
  },
  "rounded": {
    "sm": "4px",
    "md": "8px",
    "lg": "12px",
    "full": "9999px"
  },
  "spacing": {
    "xs": "4px",
    "sm": "8px",
    "md": "16px",
    "lg": "24px",
    "xl": "32px"
  },
  "dos": [
    "Usar o espaçamento padrão de 8px para manter o ritmo visual.",
    "Garantir que todos os textos tenham contraste adequado com o fundo."
  ],
  "donts": [
    "Usar cores fora da paleta semântica definida.",
    "Misturar ícones de diferentes bibliotecas no mesmo fluxo."
  ],
  "output_path": "/home/ubuntu/design.md"
}
```

## Referências Úteis
- Consulte `/home/ubuntu/skills/design-md-generator/references/design_tokens_guide.md` para mais detalhes sobre os temas de design, ícones e fontes.
- Consulte `/home/ubuntu/skills/design-md-generator/references/components.md` para entender as definições padrão dos componentes básicos.
