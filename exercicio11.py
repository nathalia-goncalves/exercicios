db_filmes = "db_filmes.json"
# filmes = []
import json
import os

filmes = "filme.json"

def carregar_filmes():
    if os.path.exists(filmes):
        with open(filmes,"r", encoding="utf-8") as arq_json:
            return json.load(arq_json)
    else:
        return[]

def obter_dados_filme():
    nome_filme = input("Informe o Nome do Filme: ")
    descricao_filme = input("Informe a Descricao do Filme: ")
    classificacao_filme = int(input("Informe a Classificacao do Filme: "))
    categoria_filme = input("Informe a Categoria do Filme: ")

    data_filme = {
        "nome_filme": nome_filme,
        "descricao_filme": descricao_filme,
        "classificacao_filme": classificacao_filme,
        "categoria_filme": categoria_filme,

    }

    return data_filme

def cadastrar_filme(dados_filme):
    filme = carregar_filmes()
    filme.append(dados_filme)

    with open(filmes, "w" , encoding="utf-8") as arq_json:
        json.dump(filme, arq_json, indent=4, ensure_ascii=False)



def mostrar_filmes(filmes):
    if filmes:
        for filme in filmes:
            print(f"""
                Nome do Filme: {filme["nome_filme"]}
                Descricao do Filme: {filme["descricao_filme"]}
                Classificacao do Filme: {filme["classificacao_filme"]}
                Categoria do Filme: {filme["categoria_filme"]}
                """)
    else:
        print("Não existe filmes cadastrado.")
            
def iniciar_sistema():
    db_filmes = carregar_filmes()
    while True:
        
        print("")
        print("="*80)
        print("Opcao 1 - Mostrar Lista de Filmes")
        print("Opcao 2 - Cadastrar Filmes")
        print("Opcao 3 - Sair do Sistema.")
        print("="*80)

        opcao = input("Escolha uma das opções do Menu: ")

        if opcao == "1":
            mostrar_filmes(db_filmes)
        elif opcao == "2":
            cadastrar_filme(obter_dados_filme())
        elif opcao == "3":
            print("Sistema Finalizado")
            break
        else:
            print("Opcao invalida, escolha uma das opções no menu.")

iniciar_sistema()









    