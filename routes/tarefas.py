from fastapi import APIRouter, HTTPException

from models.tarefa import Tarefa

from services.tarefas_service import (
    ler_tarefas,
    salvar_tarefas,
    gerar_novo_id
)

router = APIRouter()

# Listar tarefas
@router.get("/tarefas")
def listar_tarefas():

    tarefas = ler_tarefas()

    return tarefas


# Listar tarefas concluídas
@router.get("/tarefas/concluidas")
def listar_tarefas_concluidas():

    tarefas = ler_tarefas()

    tarefas_concluidas = []

    for tarefa in tarefas:

        if tarefa["concluida"] == True:
            tarefas_concluidas.append(tarefa)

    return tarefas_concluidas


# Buscar tarefa
@router.get("/tarefas/{tarefa_id}")
def buscar_tarefa(tarefa_id: int):

    tarefas = ler_tarefas()

    for tarefa in tarefas:

        if tarefa["id"] == tarefa_id:
            return tarefa

    raise HTTPException(
        status_code=404,
        detail="Tarefa não encontrada"
    )


# Criar tarefa
@router.post("/tarefas")
def criar_tarefa(tarefa: Tarefa):

    tarefas = ler_tarefas()

    nova_tarefa = {
        "id":  gerar_novo_id(), #(Melhoria: deveria funcionar assim) Cria uma lista dos IDs, pega o maior, soma 1 para criar o próximo
        "titulo": tarefa.titulo,
        "concluida": False
    }

    tarefas.append(nova_tarefa)

    salvar_tarefas(tarefas)

    return {
        "mensagem": "Tarefa criada com sucesso",
        "tarefa": nova_tarefa
    }


# Concluir tarefa
@router.put("/tarefas/{tarefa_id}")
def concluir_tarefa(tarefa_id: int):

    tarefas = ler_tarefas()

    for tarefa in tarefas:

        if tarefa["id"] == tarefa_id:

            tarefa["concluida"] = True

            salvar_tarefas(tarefas)

            return {
                "mensagem": "Tarefa concluída com sucesso",
                "tarefa": tarefa
            }

    raise HTTPException(
        status_code=404,
        detail="Tarefa não encontrada"
    )


# Deletar tarefa
@router.delete("/tarefas/{tarefa_id}")
def deletar_tarefa(tarefa_id: int):

    tarefas = ler_tarefas()

    for tarefa in tarefas:

        if tarefa["id"] == tarefa_id:

            tarefas.remove(tarefa)

            salvar_tarefas(tarefas)

            return {
                "mensagem": "Tarefa deletada com sucesso"
            }

    raise HTTPException(
        status_code=404,
        detail="Tarefa não encontrada"
    )