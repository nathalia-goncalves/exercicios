from exercicio04 import calcular_media

def cadastrar_aluno(nome,email,serie,nota01,nota02,nota03):
    alunos = []

    aluno = {
        "nome": nome,
        "email": email,
        "serie": serie,
        "notas": [nota01,nota02,nota03]
    }

    alunos.append(aluno)
    media = alunos(aluno["nota"])
    return alunos

print(cadastrar_aluno("Nathalia", "abc@abc.com", "serie 2B", 8,7,9))