# 📘 **API de Gerenciamento Escolar — Flask MVC**

Uma API REST desenvolvida em **Flask**, estruturada no padrão **MVC**, com CRUD completo para **Professores**, **Turmas** e **Alunos**.
A persistência é feita com **SQLite + SQLAlchemy**, a documentação é gerada com **Swagger (Flasgger)** e toda a aplicação está preparada para rodar em **Docker**.

> Para criar uma turma é necessário existir ao menos um professor.
> Para criar um aluno é necessário existir ao menos uma turma.

---

## 🔧 **Tecnologias Utilizadas**

* **Flask**
* **Flask-SQLAlchemy**
* **Flasgger (Swagger UI)**
* **Pytest**
* **SQLite**
* **Docker**
* **Render** 
---

## 🗂️ **Arquitetura do Projeto (MVC)**

```
/projeto
│── app.py                 # Ponto de entrada da aplicação
│── requirements.txt       # Dependências do Python
│── Dockerfile             # Configuração do container
│
│── /model                 # Modelos do banco (SQLAlchemy)
│    ├── database.py
│    ├── professor.py
│    ├── turma.py
│    └── aluno.py
│
│── /controller            # Regras de negócio
│    ├── professor_controller.py
│    ├── turma_controller.py
│    └── aluno_controller.py
│
│── /routes                # Definição das rotas da API
│    professor_routes.py
│    ├── turma_routes.py
│    └── aluno_routes.py
│
│── /static                # Arquivos estáticos (Bootstrap)
│── /templates             # Templates HTML 
│── /tests
│   └── unit
│       └── test_academic_crud.py # Testes uniários
└── README.md              # Documentação
```

---

## 🚀 **Como Executar o Projeto**

### 🔹 1. Clonar o repositório

```bash
git clone https://github.com/DiogoJP202/flask-academic-crud.git
cd flask-academic-crud
```

---

### 🔹 2. Executar sem Docker (opcional)

#### Criar ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

#### Instalar dependências

```bash
pip install -r requirements.txt
```

#### Rodar o servidor

```bash
flask run
```

Acesse em:
👉 **[http://localhost:5000](http://localhost:5000)**

---

### 🔹 3. Executar com Docker 🐳

```bash
# Build da imagem
docker build -t flask-mvc-api .

# Executar o container
docker run -p 5000:5000 flask-mvc-api
```

Acesse em:
👉 **[http://localhost:5000](http://localhost:5000)**

---

## 📚 **Documentação da API (Swagger)**

Depois de iniciar a aplicação, abra:

👉 **[http://localhost:5000/apidocs](http://localhost:5000/apidocs)**

O Swagger lista todos os endpoints e permite testar a API diretamente pelo navegador.

---

## 📌 **Principais Endpoints**

### 👨‍🏫 Professores — `/professores`

* `GET /professores` → Lista todos
* `POST /professores` → Cria novo professor
* `PUT /professores/{id}` → Atualiza professor
* `DELETE /professores/{id}` → Remove professor

### 🏫 Turmas — `/turmas`

* `GET /turmas` → Lista todas
* `POST /turmas` → Cria nova turma
* `PUT /turmas/{id}` → Atualiza turma
* `DELETE /turmas/{id}` → Remove turma

### 👨‍🎓 Alunos — `/alunos`

* `GET /alunos` → Lista todos
* `POST /alunos` → Cria novo aluno
* `PUT /alunos/{id}` → Atualiza aluno
* `DELETE /alunos/{id}` → Remove aluno