# To-Do API - FastAPI

API REST simples para gerenciamento de tarefas desenvolvida com Python e FastAPI.

## Funcionalidades

- Criar tarefas
- Listar tarefas
- Buscar tarefa por ID
- Listar tarefas concluídas
- Concluir tarefas
- Deletar tarefas

---

## Tecnologias utilizadas

- Python
- FastAPI
- Uvicorn
- Pydantic
- JSON
- Git/GitHub

---

## Estrutura do projeto

```bash
todo-api/
│
├── main.py
├── tarefas.json
├── ultimo_id.txt
├── requirements.txt
│
├── models/
│   └── tarefa.py
│
├── services/
│   └── tarefas_service.py
│
└── routes/
    └── tarefas.py
```

---

## Como executar o projeto

### Clonar o repositório

```bash
git clone https://github.com/LeonardoRamosdaCunha/todo-api-fastapi.git
```

---

### Entrar na pasta

```bash
cd todo-api-fastapi
```

---

### Criar ambiente virtual

```bash
python -m venv venv
```

---

### Ativar ambiente virtual

#### Windows PowerShell

```bash
.\venv\Scripts\Activate.ps1
```

#### CMD

```bash
venv\Scripts\activate
```

---

### Instalar dependências

```bash
pip install -r requirements.txt
```

---

### Rodar servidor

```bash
uvicorn main:app --reload
```

---

## Documentação da API

### Swagger

```txt
http://127.0.0.1:8000/docs
```

### Redoc

```txt
http://127.0.0.1:8000/redoc
```

---

## Objetivo do projeto

Projeto desenvolvido para prática de:

- desenvolvimento backend;
- APIs REST;
- FastAPI;
- organização de código;
- versionamento com Git/GitHub.

---

## Autor

Leonardo Ramos da Cunha
