from exercicio04 import calcular_media

alunos = []

def obter_dados_aluno():
    nome_aluno = input("Informe o Nome Completo do Aluno")
    email_aluno = input("Informe o Email Completo do Aluno")
    serie_aluno = input("Informe a Serie do Aluno")
    nota01 = int(input("Informe a Primeira Nota do Aluno"))
    nota02 = int(input("Informe a Segunda Nota do Aluno"))
    nota03 = int(input("Informe a Terceira Nota do Aluno"))

    return cadastrar_aluno(nome_aluno, serie_aluno, email_aluno, nota01, nota02, nota03)
    
def cadastrar_aluno(nome,email,serie,nota01,nota02,nota03):
   
    notas= [nota01,nota02,nota03]

    aluno = {
        "nome": nome,
        "email": email,
        "serie": serie,
        "notas": notas,
        "media": calcular_media(notas)
    }

    alunos.append(aluno)
   
    return alunos

def mostrar_dados_alunos(dados_alunos):
    for aluno in dados_alunos:
        print(f"Nome do aluno: {aluno["nome"]} | Email do aluno: {aluno["email"]} | Série do aluno: {aluno["serie"]} | Notas do aluno: {aluno["notas"]} | Média do alunos: {aluno["media"]} ")
    return

def iniciar_sistema():
    while True:
        print("="*80)
        print("Opcao 1 = Mostrar lista de Alunos Cadastrados.")
        print("Opcao 2 => Cadastar Alunos.")
        print("Opcao 3=> Sair do sistema.")
        print("="*80)

        opcao =  input ("Escolha uma das opções acima: ")

        if opcao == "1":
            mostrar_dados_alunos(alunos)
        elif opcao == "2":
            obter_dados_aluno()
        else: 
            print("Sistema finalizado.")
            break
    
        
iniciar_sistema()
