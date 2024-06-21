# Image Showcase

Um projeto de galeria de imagens moderno utilizando Flask e Bootstrap. Este projeto apresenta um carrossel de imagens e uma galeria, com uma interface elegante e responsiva.

## Índice

- [Image Showcase](#image-showcase)
  - [Índice](#índice)
  - [Introdução](#introdução)
  - [Funcionalidades](#funcionalidades)
  - [Instalação](#instalação)
  - [Como Usar](#como-usar)
  - [Estrutura do Projeto](#estrutura-do-projeto)
  - [Tecnologias Utilizadas](#tecnologias-utilizadas)
  - [Contribuição](#contribuição)
  - [Licença](#licença)

## Introdução

Este projeto é uma galeria de imagens que utiliza Flask como backend e Bootstrap para estilização e componentes front-end. O objetivo é fornecer uma interface simples e eficaz para visualizar uma coleção de imagens com um carrossel e uma galeria.

## Funcionalidades

- Carrossel de imagens com navegação automática e manual
- Galeria de imagens organizada com cartões
- Divisão estilizada entre o carrossel e a galeria
- Suporte a diferentes formatos de imagem (jpg, jpeg, png, gif)
- Ordenação de imagens baseada em datas extraídas dos nomes dos arquivos

## Instalação

Siga os passos abaixo para configurar e executar o projeto localmente.

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seu-usuario/galeria-moderna.git
   cd galeria-moderna
   ```

2. **Crie um ambiente virtual:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
   ```

3. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Execute a aplicação:**

   ```bash
   flask run
   ```

   A aplicação estará disponível em `http://127.0.0.1:5000`.

## Como Usar

1. **Adicionar Imagens:**

   Coloque suas imagens na pasta `static/images`. Certifique-se de que os nomes das imagens sigam o formato `AAAA.MM.DD_Nome.jpg` para a correta ordenação por data.

2. **Navegação:**

   - Utilize as setas de navegação no carrossel para ver as imagens.
   - Role para baixo para ver a galeria de imagens.

3. **Tela Cheia e Visibilidade:**

   O carrossel pausará quando a aba do navegador não estiver visível e retomará quando a aba voltar a ser ativa.

## Estrutura do Projeto

```
galeria-moderna/
├── static/
│   ├── css/
│   │   └── style.css
│   ├── images/
│   └── js/
│       └── script.js
├── templates/
│   └── index.html
├── app.py
├── requirements.txt
└── README.md
```

## Tecnologias Utilizadas

- [Flask](https://flask.palletsprojects.com/) - Framework web em Python
- [Bootstrap](https://getbootstrap.com/) - Framework front-end para desenvolvimento de interfaces responsivas
- [JavaScript](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript) - Para funcionalidades interativas
- [CSS](https://developer.mozilla.org/pt-BR/docs/Web/CSS) - Para estilização

## Contribuição

Contribuições são bem-vindas! Siga os passos abaixo para contribuir:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Faça um push para a branch (`git push origin feature/nova-feature`)
5. Crie um novo Pull Request

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
