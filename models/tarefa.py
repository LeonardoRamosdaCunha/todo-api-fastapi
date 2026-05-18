from pydantic import BaseModel

# Modelo da tarefa
class Tarefa(BaseModel):
    titulo: str