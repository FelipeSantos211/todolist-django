# ✅ ToDo List - Django

Aplicação web de lista de tarefas desenvolvida com Django. Permite ao usuário criar, visualizar, atualizar e deletar tarefas de forma simples e eficiente.

## ✨ Funcionalidades

- ✅ Cadastro de tarefas
- 🔁 Atualização do status de tarefas (concluída ou não)
- 🗑️ Remoção de tarefas
- 📄 Listagem de tarefas por usuário
- 🔒 Autenticação de usuário

## 💻 Tecnologias utilizadas

- Python 3
- Django
- HTML5
- Tailwind
- SQLite (padrão do Django)
- Docker

## 🚀 Como rodar o projeto

### 🔧 Rodando localmente

1. Clone este repositório:
   ```bash
   git clone https://github.com/FelipeSantos211/todolist-django.git
   ```

2. Acesse o diretório do projeto:
   ```bash
   cd todolist-django
   ```

3. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

5. Execute as migrações:
   ```bash
   python manage.py migrate
   ```

6. Inicie o servidor:
   ```bash
   python manage.py runserver
   ```

7. Acesse a aplicação:
   Abra o navegador e vá até [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

### 🐳 Rodando com Docker

1. Certifique-se de que o Docker está instalado.

2. No diretório do projeto, execute:
   ```bash
   docker build -t todolist-django .
   ```

3. Em seguida, inicie o container:
   ```bash
   docker run -p 8000:8000 todolist-django
   ```

4. Acesse a aplicação no navegador:
   [http://localhost:8000](http://localhost:8000)

---

## 📁 Estrutura do projeto

```
todolist-django/
├── app/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── templates/
│   ├── tests.py
│   └── views.py
├── tasks/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── templates/
│   ├── tests.py
│   └── views.py
├── manage.py
├── requirements.txt
└── Dockerfile

```

## 🙋‍♂️ Autor

Feito com 💙 por [Felipe Santos](https://github.com/FelipeSantos211)

---

Sinta-se à vontade para contribuir com melhorias ou sugestões! 🚀
