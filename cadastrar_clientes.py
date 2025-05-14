clientes = []

def obter_dados_cliente():
    nome_cliente = input("Informe o Nome Completo do Cliente")
    cpf_cliente = input("Informe o CPF Completo do Cliente")
    rg_cliente = input("Informe o  Numero de RG Completo do Cliente")
    data_de_nascimento_cliente = input("Informe a Data de Nascimento do Cliente")
    endereco_cliente = input("Informe o Endereço do Cliente")
    cidade_cliente = input("Informe a Cidade do Cliente")
    estado_cliente = input("Informe o Estado do Cliente")
    telefone_cliente = input("Informe o Numero de Telefone do Cliente")
    celular_cliente = input("Informe o Numero de Celular do Cliente")
    email_cliente = input("Informe o E-mail Completo do Cliente")

    return cadastrar_clientes(nome_cliente, cpf_cliente, rg_cliente, data_de_nascimento_cliente, endereco_cliente, cidade_cliente, estado_cliente, telefone_cliente, celular_cliente, email_cliente)

def cadastrar_clientes(nome,cpf,rg,data_de_nascimento,endereco,cidade,estado,telefone,celular,email):

    cliente = {
        "nome": nome,
        "cpf": cpf,
        "rg": rg,
        "data de nascimento": data_de_nascimento,
        "endereco": endereco,
        "cidade": cidade,
        "estado": estado,
        "telefone": telefone,
        "celular": celular,
        "email": email
    }

    clientes.append(cliente)

    return clientes

def mostrar_dados_clientes(dados_clientes):
    for cliente in dados_clientes:
        print(f"Nome do Cliente: {cliente["nome"]} | Cpf do Cliente:{cliente["cpf"]} | RG do cliente:{cliente["rg"]} | Data de Nascimento Cliente:{cliente["data de nascimento"]} | Endereço do Cliente:{cliente["endereco"]} | Cidade do Cliente:{cliente["cidade"]} | Estado do Cliente:{cliente["estado"]} | Telefone do Cliente:{cliente["telefone"]} | Celular do Cliente:{cliente["celular"]} | Emial do Cliente:{cliente["email"]} ")
        return

def iniciar_sistema():
    while True:
        print("="*80)
        print("Opcao 1 = Mostrar lista de Clientes Cadastrados.")
        print("Opcao 2 => Cadastar Clientes.")
        print("Opcao 3=> Sair do sistema.")
        print("="*80)

        opcao =  input ("Escolha uma das opções acima: ")

        if opcao == "1":
            mostrar_dados_clientes(clientes)
        elif opcao == "2":
            obter_dados_cliente()
        else: 
            print("Sistema finalizado.")
            break

        
iniciar_sistema()

