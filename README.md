# 📂 Agregador de Editais

![GIF do Projeto em Ação](link_para_seu_gif_aqui.gif)
*(Dica: Grave um GIF rápido da tela mostrando o site funcionando. Ferramentas como LICEcap ou ScreenToGif são ótimas para isso)*

---

## 📜 Descrição

Este Agregador de Editais é uma aplicação web desenvolvida em Python que automatiza a busca e centralização de editais e chamadas de pesquisa. O projeto consome dados de sites de agências de fomento (atualmente a FAPESB) através de web scraping, armazena as informações em um banco de dados e as exibe em uma interface amigável, permitindo a filtragem e a marcação de editais favoritos.

Este projeto foi criado como uma peça de portfólio para demonstrar habilidades em desenvolvimento web, automação e infraestrutura.

---

## 🚀 Funcionalidades

**Automação:** Um scraper (robô) roda periodicamente para buscar novos editais e atualizar a base de dados.
**Centralização:** Agrega editais de diversas fontes em um único lugar.
**Interface Amigável:** Exibe os editais de forma clara e organizada.
**Filtragem:** Permite filtrar os resultados por agência de fomento.
**Favoritos:** O usuário pode marcar e desmarcar editais de seu interesse.

---

## 🛠️ Tecnologias Utilizadas

**Backend:** Python, Flask
**Coleta de Dados:** Requests, Beautiful Soup
**Banco de Dados:** SQLAlchemy, SQLite (em desenvolvimento)
**Automação:** APScheduler
**Frontend:** HTML, CSS, Bootstrap, JavaScript
**Infraestrutura:** Docker (para deploy)

---

## ⚙️ Como Rodar o Projeto Localmente

Siga os passos abaixo para executar o projeto na sua máquina:

```cmd
# 1. Clone o repositório
git clone [https://github.com/seu-usuario/agregador_editais.git](https://github.com/seu-usuario/agregador_editais.git)

# 2. Navegue até a pasta do projeto
cd agregador_editais

# 3. Crie e ative o ambiente virtual
python -m venv venv
# No Windows: venv\Scripts\activate
# No macOS/Linux: source venv/bin/activate

# 4. Instale as dependências
pip install -r requirements.txt

# 5. Execute o scraper uma vez para popular o banco
python test_scraper.py

# 6. Inicie a aplicação
python run.py

# 7. Abra seu navegador e acesse (http://127.0.0.1:5000/)
```

---

## 🧠 Desafios e Aprendizados

Um dos maiores desafios deste projeto foi o desenvolvimento do scraper. Entender como encontrar os editais da melhor forma, o que exigiu um processo contínuo de "engenharia reversa" e adaptação do código. Além disso, lidar com erros de certificado SSL (e contorná-los de forma pragmática para o ambiente de desenvolvimento) foi uma experiência de aprendizado valiosa sobre as complexidades das requisições web.


---

## 🔗 Link para o Projeto Online

Você pode acessar a versão ao vivo do projeto em: `[Link do seu projeto no Render.com ou Heroku]`