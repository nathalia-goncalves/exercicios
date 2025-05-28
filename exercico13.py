import json
import os

agenda = "agenda_cabeleleiro.json"

def carregar_dados():
    if os.path.exists(agenda):
        with open (agenda, "r", encoding= "utf-8") as arq_json:
            return json.load(arq_json)
    else:
        return[]
    
def obter_dados():
    nome_cliente = input("Informe o Nome do Cliente")
    servico_cliente = input("Informe o Servico Desejado")
    data_cliente = int(input("Informe a Data agendada"))
    horario_cliente = int(input("Informe o Horario agendado"))
    observacoes_cliente  = input("Informe as Observacoes do cliente se houver")

    agenda = {
        "nome_cliente": nome_cliente,
        "servico_cliente": servico_cliente,
        "data_cliente": data_cliente,
        "horario_cliente": horario_cliente,
        "observacoes_cliente" : observacoes_cliente
    }

    return agenda

def cadastrar_agendamento(receber_dados):
    db_agendamento = carregar_dados()
    db_agendamento.append(receber_dados)

    with open(agenda,"w", encoding="utf-8") as arq_json:
        json.dump(db_agendamento, arq_json, indent=4, ensure_ascii= False)



def mostrar_agendamentos(receber_agendamentos):
    print(receber_agendamentos)
    if receber_agendamentos:
        for agenda in receber_agendamentos:
            print(f"""
                  Nome do Cliente:{agenda["nome_cliente"]})
                  Servico Desejado:{agenda["servico_cliente"]})
                  Data do Cliente:{agenda["data_cliente"]})
                  Horario do Cliente:{agenda["cliente"]})
                  Observacoes do Cliente:{agenda["nome_cliente"]})
            """)
    else:
        print("Nenhum agendamento cadastrado no momento.")

def iniciar_sistema():
    db_agendamento = carregar_dados()
    while True:

        print("")
        print("="*80)
        print("Opcao 1 - Mostrar Agenda Completa")
        print("Opcao 2- Cadastrar um novo Agendamento")
        print("Opcao 3- Sair do Sistema")
        print("="*80)

        opcao = input("Escolha uma das opções do Menu.")

        if opcao == "1":
            mostrar_agendamentos(db_agendamento)
        elif opcao == "2":
            cadastrar_agendamento(obter_dados())
        elif opcao == "3": 
            print("Sistema Finalizado com Sucesso")
            break
        else:
            print("Opção Inválida, escolha uma das opções do menu.")
iniciar_sistema()


    



    
    
    