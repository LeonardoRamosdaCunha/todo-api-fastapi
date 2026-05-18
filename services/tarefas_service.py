import json

ARQUIVO_ULTIMO_ID = "ultimo_id.txt"
ARQUIVO_TAREFAS = "tarefas.json"

# Função para ler tarefas
def ler_tarefas():
    with open(ARQUIVO_TAREFAS, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)
    
# Função para salvar tarefas
def salvar_tarefas(tarefas):
    with open(ARQUIVO_TAREFAS, "w", encoding="utf-8") as arquivo:
        json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)
        #dump: salva no arquivo;
        #ident=4: formata;
        #ensure_ascii=False: permite acentos corretamente

def gerar_novo_id():

    try:
        with open(ARQUIVO_ULTIMO_ID, "r") as arquivo:
            ultimo_id = int(arquivo.read())
    except:
        ultimo_id = 0

    novo_id = ultimo_id + 1

    with open(ARQUIVO_ULTIMO_ID, "w") as arquivo:
        arquivo.write(str(novo_id))

    return novo_id