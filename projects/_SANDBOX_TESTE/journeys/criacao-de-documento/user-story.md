## 📄 User Story: Criação de Documento na Biblioteca Digital

**Como** um estudante ou produtor de conteúdo da plataforma Ponto a Ponto,
**Quero** poder adicionar um novo documento a partir da Biblioteca Digital, definindo seu título e tipo,
**Para que** eu possa criar apostilas e materiais personalizados utilizando o editor interno.

---

## 🛠️ Critérios de Aceitação (Gherkin & Regras de Negócio)

### Cenário 1: Abertura do Modal de Criação

* **Dado que** estou na tela de "Biblioteca Digital",
* **Quando** eu clicar no card de ação "Adicionar novo documento" (primeiro item da listagem),
* **Então** o sistema deve abrir um modal centralizado sobrepondo a listagem com um efeito de *overlay* escuro no fundo.

### Cenário 2: Validação e Preenchimento dos Campos

* **Dado que** o modal "Adicionar novo documento" está aberto,
* **Então** os seguintes campos devem estar visíveis e seguir as regras:
* **Nome do documento (Input de Texto):** Obrigatório. Limite de 100 caracteres. Placeholder: *"Adicionar texto"*.
* **Tipo do documento (Select Dropdown):** Obrigatório. Deve listar categorias predefinidas (ex: Apostila, Exercício, Resumo). Placeholder: *"Selecionar"*.
* **Botão "Adicionar" (Primary CTA):** Deve permanecer desabilitado até que ambos os campos obrigatórios estejam validados e preenchidos.
* **Botão "Cancelar" (Secondary CTA):** Fecha o modal e retorna o usuário ao estado inicial da listagem sem salvar alterações.

### Cenário 3: Redirecionamento para o Editor após Criação bem-sucedida

* **Dado que** preenchi o nome como `"Apostila de Matemática"` e selecionei o tipo de documento,
* **Quando** eu clicar no botão "Adicionar",
* **Então** o sistema deve realizar a requisição na API para criar o registro do documento,
* **E** me redirecionar imediatamente para a tela do Editor de Texto/Composição, carregando o título do documento no cabeçalho e uma área em branco (canvas) pronta para edição.

---

## 💡 Notas Técnicas de Handoff & UX

* **Estados dos Botões:** O botão primário "Adicionar" deve usar o token de cor azul da marca em estado ativo, mudando visualmente para *hover* e mostrando um *loading spinner* interno durante a requisição assíncrona de criação para evitar cliques duplos.
* **Foco Inicial:** Ao abrir o modal, o foco do teclado (*autofocus*) deve ir automaticamente para o input "Nome do documento" para otimizar a velocidade de digitação do usuário.
