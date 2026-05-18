#API: http://127.0.0.1:8000
#Swagger: http://127.0.0.1:8000/docs
#Redoc: http://127.0.0.1:8000/redoc

from fastapi import FastAPI

from routes.tarefas import router

app = FastAPI(
    title="To-Do API",
    description="API simples de gerenciamento de tarefas feita com FastAPI",
    version="1.0.0"
)

app.include_router(router)

# Rota inicial
@app.get("/")
def home():
    return {"mensagem": "API funcionando!"}