# A Plataforma de Design — proposta descritiva

Documento de leitura: o que a plataforma é, como funciona e como cada
pessoa a utiliza. A especificação técnica correspondente está em
`arquitetura-harness-storybook-penpot.md`.

---

## O que é, em um parágrafo

Uma plataforma interna de design e desenvolvimento onde **o design
system de cada cliente existe uma única vez** — como código — e todo o
resto é gerado a partir dele: a biblioteca visual que o designer usa
no Penpot, o catálogo de documentação que o time consulta no
Storybook, e o pacote que o desenvolvedor instala para montar os
sites. Uma equipe de agentes de IA (o "harness") cuida do trabalho
operacional que mantém tudo isso alinhado: cataloga, parametriza,
documenta, audita e sincroniza. As pessoas fazem o que exige
julgamento — desenhar, decidir e aprovar.

---

## O problema que ela resolve

Hoje, todo projeto de design convive com **duas verdades**: o que está
desenhado na ferramenta de design e o que está implementado no código.
Elas nascem iguais e divergem com o tempo — o designer ajusta um botão
no arquivo, o dev corrige um espaçamento no código, e seis meses
depois ninguém sabe qual dos dois é o oficial. Manter as duas verdades
sincronizadas é trabalho manual, caro e ingrato (é a função inteira
chamada "DesignOps", que times grandes contratam gente para fazer).

Além disso, aprendemos na prática (harness v1) que fazer a IA
*desenhar dentro da ferramenta de design*, operando a API dela, é
lento e frágil. A IA é excelente escrevendo código de interface — é
nisso que ela deve ser usada.

A plataforma resolve os dois problemas com uma decisão de arquitetura:
**só existe uma verdade, e ela é o código.** Tudo o mais é vista ou
espelho dessa verdade — e espelho não diverge, porque é regenerado.

---

## As peças, e para que serve cada uma

### 1. A Fonte (repositório git, um por cliente)

O coração. Um repositório de código para cada cliente contendo:

- **Os tokens** — as decisões de identidade visual em formato aberto
  (cores, espaçamentos, raios, tipografia). Um arquivo só, padrão
  W3C, que alimenta todos os outros lugares.
- **Os componentes** — Button, Card, Input... escritos em React, cada
  um com suas variantes declaradas.
- **As telas** — as telas das jornadas, compostas a partir dos
  componentes.

Ninguém "abre" a fonte para trabalhar no dia a dia (exceto o dev).
Ela é o registro oficial do qual as três vistas abaixo derivam.

### 2. O Catálogo (Storybook)

Um site interno, um por cliente, gerado automaticamente da fonte. Nele
qualquer pessoa — designer, dev, PM, o próprio cliente — navega pelos
componentes reais: vê cada variante funcionando, lê a documentação de
uso, testa estados (desabilitado, carregando, com erro). É a
documentação que **não mente**, porque não é escrita à parte — é o
próprio componente renderizado.

O Catálogo substitui os atuais arquivos `components/*.md`: a anatomia
e as variantes passam a ser geradas do código, e a curadoria (regras
de uso, do/don'ts) vive junto, mantida pelos agentes.

### 3. O Estúdio (Penpot, self-hosted)

A ferramenta de design — onde o designer passa o dia. Open source,
hospedada em servidor nosso, com todos os projetos acessíveis ao time
de design (somos uma software house; a separação por cliente é
organizacional, um espaço por cliente).

No Estúdio existem dois territórios com regras diferentes:

- **A biblioteca oficial** — os componentes do cliente, espelhados
  automaticamente da fonte, com as mesmas variantes e os mesmos
  tokens. O designer **usa** (arrasta instâncias, troca variantes,
  edita textos), mas não edita a biblioteca em si — ela pertence à
  fonte e é regenerada a cada mudança.
- **Os projetos de trabalho** — as telas das jornadas. Aqui o designer
  é dono: compõe livremente com as peças da biblioteca e, quando
  precisa de algo que não existe, **desenha à mão como rascunho**.
  Esse rascunho não é um problema — é o insumo mais rico que o
  pipeline pode receber.

### 4. O Pacote (npm via GitHub Packages)

O que o desenvolvedor de produto instala (`@org/ds-cliente`) para
montar os sites. Componentes prontos, tokens aplicados, testados.
Como o pacote e a biblioteca do designer vêm **do mesmo arquivo
fonte**, o que o dev monta é — por construção, não por disciplina —
idêntico ao que o designer desenhou.

### 5. Os Agentes (o harness — o DesignOps automatizado)

A equipe invisível que faz a plataforma funcionar. Cada um tem um
papel estreito e nenhum decide sozinho — decisões passam por aprovação
humana:

| Agente | O que faz |
|---|---|
| **interpreter** | Lê um wireframe ou uma tela desenhada e produz o plano: o que já existe (reusar), o que é variante nova, o que é componente novo, o que precisa migrar do legado |
| **component-planner** | Especifica um componente novo: propriedades, variantes, tokens necessários |
| **component-builder** | Escreve o componente em código, com a identidade visual do cliente (design.md), e abre a proposta para o dev revisar |
| **screen-builder** | Monta as telas das jornadas a partir dos componentes oficiais |
| **validator** | Confere a jornada pronta contra a história do usuário, o wireframe e a identidade visual — inclusive com comparação visual automática |
| **auditor** | O fiscal: aponta cor fora de token, componente destacado, biblioteca dessincronizada, nomenclatura errada |
| **documenter** | Mantém o Catálogo curado e promove componentes de rascunho a oficial |
| **onboard-*** (3 agentes) | Fazem a entrada de um cliente novo: varrem o Figma legado dele e produzem o inventário, os tokens iniciais e o documento de identidade visual |

E um processo automático (não é um agente que decide, é uma rotina):
o **espelho**, que regenera a biblioteca do Penpot toda vez que a
fonte muda — conferindo antes que está escrevendo no espaço do cliente
certo.

### 6. A memória (o que faz a plataforma ser "do projeto")

Cada cliente tem, além do código, os documentos que ensinam os agentes
a trabalhar do jeito daquele cliente:

- **design.md** — a identidade visual escrita: tom, regras de cor e
  forma, anatomia dos componentes-chave, o que nunca fazer. É o que
  impede a IA de gerar design genérico.
- **decisions.md / learnings** — por que as coisas são como são;
  decisões nunca são revertidas silenciosamente.
- **journey-state** — o andamento de cada jornada em construção.

---

## Como funciona no dia a dia — quatro cenários

### Cenário 1 — Uma jornada nova, a partir de wireframes

O PM entrega wireframes e a história do usuário. O interpreter analisa
e apresenta o plano: "a tela usa 6 componentes que já existem, 1
variante nova do Input e 1 componente novo (seletor de métricas)".
**Alguém aprova o plano** (portão humano). O component-builder escreve
o componente novo em código; o dev revisa a proposta em minutos (vê o
código e a imagem, aprova). A biblioteca do Penpot ganha o componente
automaticamente. O screen-builder monta as telas. O validator confere
tudo contra a história e a identidade visual. **Aprovação final**, e a
jornada está pronta — desenhada no Estúdio, documentada no Catálogo,
implementável pelo Pacote.

### Cenário 2 — O designer prefere desenhar à mão

O designer abre o Estúdio, cria as telas da jornada arrastando
instâncias da biblioteca, aplica tokens pelo painel — trabalho normal
de design, na ferramenta, sem IA no meio. Onde falta peça, rascunha à
mão. Ao terminar, aciona os agentes: o interpreter lê a tela pronta
como um "wireframe rico", identifica os rascunhos, e o resto segue
igual ao cenário 1 — os rascunhos viram componentes de verdade e são
substituídos na tela pelas instâncias oficiais. O designer nunca
precisou sair da ferramenta nem escrever uma linha de código.

### Cenário 3 — O dev corrige um componente

O dev encontra um bug de alinhamento no Button. Corrige no código,
abre a proposta de mudança. O sistema de testes acusa: "essa mudança
altera visualmente 3 variantes" — com as imagens do antes/depois. Se
está tudo certo, entra. A biblioteca do designer atualiza sozinha; as
telas que usam o Button refletem a correção. Ninguém precisou avisar
ninguém — a plataforma é o aviso.

### Cenário 4 — Chega um cliente novo

O cliente tem um Figma antigo e bagunçado. Os agentes de onboarding
varrem esse arquivo (só leitura — o legado nunca é tocado), inventariam
o que existe, extraem os valores reais de cor/tipografia/espaçamento e
produzem: o arquivo de tokens inicial, o design.md da identidade
visual, e um backlog do que migrar primeiro. Um repositório novo nasce
do template, um espaço novo abre no Penpot, e a migração acontece
componente a componente, com aprovação humana em cada lote — cada
componente migrado já nasce documentado, testado e espelhado.

---

## O que garante a qualidade

- **Portões humanos** — nenhum componente vira oficial e nenhuma tela
  vira vigente sem aprovação de gente. A IA propõe e executa; humanos
  decidem. (É a regra nº 1 do harness desde a v1.)
- **Identidade visual escrita** — o design.md dá aos agentes as regras
  estéticas do cliente; o validator compara o resultado contra elas.
- **Testes automáticos que o design nunca teve** — cada componente tem
  verificação de tipo, lint, teste de acessibilidade e **regressão
  visual** (screenshot de cada variante comparado ao anterior; nada
  muda visualmente sem ser notado).
- **Auditoria contínua** — o auditor varre as fronteiras (código ↔
  catálogo ↔ biblioteca ↔ tokens) e as telas dos designers, apontando
  desvios antes que virem dívida.
- **Rastreabilidade** — tudo é git: quem mudou, quando, por quê. As
  decisões têm registro e dono.

---

## Antes e depois

| | Hoje (v1) | Plataforma (v2) |
|---|---|---|
| Onde vive o design system | arquivo Figma + docs .md paralelos | código (uma fonte), com catálogo e biblioteca gerados |
| Design e código divergem? | risco permanente, auditoria manual | impossível por construção — espelho regenerado |
| IA constrói como? | operando a API do Figma (lento, frágil) | escrevendo código (rápido, forte) |
| Designer trabalha onde | Figma | Penpot (mesmo modelo mental, open source, nosso) |
| Dev recebe o quê | handoff para inspecionar e traduzir | pacote npm com os componentes prontos |
| Documentação | arquivos .md mantidos à mão | catálogo vivo gerado do código + curadoria |
| Custo de ferramenta | licenças Figma | zero licença (Penpot self-hosted, stack open source) |
| Cliente Flutter | fora do fluxo | tokens compartilhados desde o dia 1; adaptação completa em fase futura |

---

## O que a plataforma NÃO é

- **Não é um gerador automático de design.** A direção criativa, a
  pesquisa e a decisão de produto continuam humanas. O design.md — o
  gosto do cliente formalizado — é escrito com aprovação humana, e os
  agentes obedecem a ele.
- **Não tira o designer da ferramenta.** O desenho manual é cidadão de
  primeira classe (cenário 2); a IA é opcional em cada jornada.
- **Não abandona o Figma dos clientes.** O arquivo legado de cada
  cliente continua sendo lido (só leitura) como referência da
  migração. Só deixamos de *construir* lá.
- **Não está pronta.** Este documento descreve a proposta ratificada
  em 2026-07-11. A construção acontece por fases (fundação → espelho →
  reescrita do harness → teste de aceitação → primeiro cliente), cada
  uma com critério de saída e com início condicionado a "go" explícito.

---

## Resumo em uma imagem

```
                        ┌──────────────────────────┐
                        │   FONTE (git, por cliente)│
                        │   tokens + componentes    │
                        │   + telas, em código      │
                        └──────┬─────────┬──────────┘
             espelho automático│         │build
              ┌────────────────┘         └───────────────┐
              ▼                  ▼                        ▼
      ┌──────────────┐   ┌──────────────┐        ┌──────────────┐
      │   ESTÚDIO    │   │   CATÁLOGO   │        │    PACOTE    │
      │   (Penpot)   │   │  (Storybook) │        │    (npm)     │
      │   designer   │   │  todo o time │        │     dev      │
      └──────┬───────┘   └──────────────┘        └──────────────┘
             │ telas desenhadas / rascunhos (insumo)
             └────────────► AGENTES (harness) ──► propostas de código
                            interpreter · builders · validator
                            auditor · documenter — com portões
                            humanos em toda promoção
```

O designer desenha no Estúdio. O dev consome o Pacote e revisa
propostas. Os agentes mantêm o ciclo girando. E as três pontas nunca
divergem, porque todas nascem da mesma Fonte.
