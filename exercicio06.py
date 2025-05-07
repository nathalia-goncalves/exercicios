def cadastrar_filme(nome,descricao,classificacao,categoria01,categoria02):
    filmes = []

    filme = {
      "nome": nome,
      "descricao": descricao,
      "classificacao": classificacao,
      "categorias": [categoria01,categoria02]
    }

    filmes.append(filme)

    return filmes

print(cadastrar_filme("Gente Grande","é uma comédia de 2010 que acompanha cinco amigos de infância que se reúnem após 30 anos para o feriado de 4 de Julho, na casa de férias do seu antigo treinador de basquetebol.","12 anos","comedia","drama"))
