import json
import os 

veiculos = "veiculos.json"

def carregar_dados():
    if os.path.exists(veiculos):
        with open(veiculos,"r", encoding= "utf-8") as arq_json:
            return json.load()
    else:
        return[]
    
def obter_dados():
    marca_veiculo = input("Informe a Marca do Veiculo")
    modelo_veiculo = input("Informe o Modelo do Veiculo")
    ano_fabricacao_veiculo = int(input("Informe o Ano de Fabricacao"))
    cor_veiculo = input("Informe a Cor do Veiculo")

    veiculo = {
       " marca_veiculo": marca_veiculo,
       "modelo_veiculo": modelo_veiculo,
       "ano_fabricacao_veiculo": ano_fabricacao_veiculo,
       "cor_veiculo": cor_veiculo
    }

def cadastrar_veiculo(receber_dados):
    db_veiculos = carregar_dados
    db_veiculos.append(receber_dados)

    with open(veiculos,"w" , encoding= "utf-8") as arq_json:
        json.dump(veiculos, arq_json, ident=4, ensure_ascii= False)



def mostrar_veiculos(veiculos):
    if veiculos:
        for veiculo in veiculos:
            print(f"""
        Marca do Veiculo:{veiculo["marca_veiculo"]}
        Modelo do Veiculo:{veiculo["modelo_veiculo"]}
        Ano de Fabricacao do Veiculo:{veiculo["ano_fabricacao_veiculo"]}
        Cor do Veiculo:{veiculo["cor_veiculo"]}
       """)
    else:
        print("Nenhum veiculo cadastrado no momento.")

def iniciar_sistema():
    db_veiculos = carregar_dados
    while True:

        print("")
        print("="*80)
        print("Opcao 1 - Exibir os Veiculos")
        print("Opcao 2- Cadastrar um novo Veiculo")
        print("Opcao 3- Sistema Finalizado com Sucesso")
        print("="*80)

        opcao = input("Escolha uma das opções do Menu.")

        if opcao == "1":
            mostrar_veiculos(db_veiculos)
        elif opcao == "2":
            cadastrar_veiculo(obter_dados())
        elif opcao == "3": 
            print("Sistema Finalizado com Sucesso")
            break
        else:
            print("Opção Inválida, escolha uma das opções do menu.")
iniciar_sistema()
       
        
        

    

                  
    


