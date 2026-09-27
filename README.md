# 📒 Projeto Agenda

Aplicação web de uma agenda de contatos desenvolvida com **Python e Django**, criada como projeto prático de estudo e desenvolvimento.

O projeto permite cadastrar, visualizar, editar e excluir contatos, utilizando autenticação de usuários e persistência de dados em banco PostgreSQL.

## 🌐 Aplicação online

**[Acessar o Projeto Agenda](http://34.60.139.237/)**

> Aplicação hospedada em uma VM na Google Cloud.

## 🚀 Tecnologias utilizadas

* Python
* Django
* PostgreSQL
* HTML5
* CSS3
* Gunicorn
* Nginx
* Linux
* Git / GitHub
* Google Cloud

## ✨ Funcionalidades

* Cadastro e autenticação de usuários
* Cadastro de contatos
* Visualização de contatos
* Edição de contatos
* Exclusão de contatos
* Pesquisa de contatos
* Paginação
* Categorias de contatos
* Upload de imagens
* Arquivos estáticos com Django
* Interface responsiva

## 🏗️ Arquitetura

O projeto utiliza a arquitetura padrão do Django, separando responsabilidades entre:

* **Models** — estrutura e persistência dos dados
* **Views** — regras de negócio e processamento das requisições
* **Templates** — interface HTML
* **Forms** — entrada e validação de dados
* **URLs** — roteamento das páginas

## 🗄️ Banco de dados

Em produção, a aplicação utiliza **PostgreSQL**.

A comunicação entre Django e PostgreSQL é realizada através do driver `psycopg`.

## ☁️ Deploy

A aplicação foi configurada para produção em uma VM Linux na **Google Cloud**, utilizando:

```text
Internet
   ↓
Nginx
   ↓
Gunicorn
   ↓
Django
   ↓
PostgreSQL
```

O Gunicorn é executado como serviço do `systemd`, enquanto o Nginx atua como servidor web e proxy reverso.

Os arquivos estáticos são coletados pelo Django através do:

```bash
python manage.py collectstatic
```

## ⚙️ Executando localmente

Clone o repositório:

```bash
git clone git@github.com:ougwYT/projeto-agenda.git
cd projeto-agenda
```

Crie um ambiente virtual:

```bash
python -m venv venv
```

Ative o ambiente virtual no Linux:

```bash
source venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute as migrações:

```bash
python manage.py migrate
```

Colete os arquivos estáticos:

```bash
python manage.py collectstatic
```

Inicie o servidor de desenvolvimento:

```bash
python manage.py runserver
```

A aplicação estará disponível em:

```text
http://127.0.0.1:8000/
```

## 📁 Estrutura do projeto

```text
projeto-agenda/
├── base_static/
├── base_templates/
├── comandos/
├── contact/
├── project/
├── utils/
├── manage.py
├── requirements.txt
└── README.md
```

## 📚 Objetivo

Este projeto faz parte da minha jornada de aprendizado em **Python, Django e desenvolvimento web**, com foco não apenas na construção da aplicação, mas também em conceitos de banco de dados, autenticação, arquivos estáticos, Linux e implantação de aplicações em ambiente de produção.

## 👨‍💻 Autor

**Miguel Ferreira Sena**

* GitHub: [@ougwYT](https://github.com/ougwYT)
* Área de interesse: **Python Developer**

---

⭐ Projeto desenvolvido como parte da minha evolução prática em desenvolvimento web com Python e Django.
