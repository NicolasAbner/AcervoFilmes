import database
import sys
import json

#FUNÇÃO LIMPATELA
def limpaTela():
    print ("\n" * 130) 

#FUNÇÃO MENU
def menu():
    print("=====================")
    print("==== Streamberry ====")
    print("=====================")
    print("1- Cadastrar")
    print("2- Listar")
    print("3- Atualizar")
    print("4- Deletar")
    print("5- Pesquisar")
    print("6- Importar para JSON")
    print("7- Sair")
    
    opt = validaCampo("Informe a opção desejada", "int", 7)
    
    if opt == 1:
        cadastrar()
        menu()
    elif opt == 2:
        listar()
        menu()
    elif opt == 3:
        atualizar()
        menu()
    elif opt == 4:
        deletar()
        menu()
    elif opt == 5:
        pesquisar()
        menu()
    elif opt == 6:
        geraJson()
        menu()
    elif opt == 7:
        sys.exit()
    else:
        print("OPÇÃO INVÁLIDA! TENTE NOVAMENTE...")
        input()
        limpaTela()
        menu()

#FUNÇÃO PARA VALIDAR ENTRADA DO USUÁRIO
def validaCampo(mensagem, tipo, valorPadrao):
    
    result = input(f"{mensagem}:")
    
    if tipo == "int":
        try:
            result = int(result)
        except:
           result = valorPadrao 
           
    return result
    
#FUNÇÃO PARA CADASTRO DE FILME NA PLATAFORMA
def cadastrar():
    limpaTela()
    
    try:
        nextId = int(lista_filmes[-1].get('id')) + 1        
    except:
        nextId = 0
        
    filme = {
        "id":nextId,
        "nome":"",
        "genero":"",
        "ano":0,
        "avaliacao":0
    }
    
    print("==== CADASTRO DE FILME ====")
    novoFilme = validaCampo("Infome o nome", "string", "")
    for item in lista_filmes:
        if novoFilme in item.values():
            input("O FILME INFORMADO JÁ ESTÁ CADASTRADO!")
            menu()
        else:
            filme["nome"] = novoFilme
    filme["genero"] = validaCampo("Infome o gênero", "string", "")
    filme["ano"] = validaCampo("Infome o ano", "int", 1900)
    filme["avaliacao"] = validaCampo("Infome a avaliação", "int", 0)
    
    lista_filmes.append(filme)
    database.gravaDado(filme)
    input("Filme cadastrado com sucesso!")
    limpaTela()
    
#FUNÇÃO PARA LISTAGEM DE FILMES POR CAMPO    
def listar():
    limpaTela()
    print("==== LISTAGEM DE FILMES ====")
    print("1- Gênero")
    print("2- Ano de Lançamento")
    print("3- Avaliação")
    print("4- Todos")
    listagem = validaCampo("INFORME O MÉTODO DE LISTAGEM", "int", 0)

    if listagem == 1:
        listaGenero = validaCampo("Informe o Gênero", "str", " ")
        stts = metodoListar(listaGenero, "genero")
        if stts == False:
            print("Nenhum filme encontrado...")
        
    elif listagem == 2:
        listaAno = validaCampo("Informe o Ano", "int", 1900)
        stts = metodoListar(listaAno, "ano")
        if stts == False:
            print("Nenhum filme encontrado...")
        
    elif listagem == 3:
        listaAvaliacao = validaCampo("Informe A Avaliação", "int", 0)
        stts = metodoListar(listaAvaliacao, "avaliacao")
        if stts == False:
            print("Nenhum filme encontrado...")
        
    elif listagem == 4:
        for item in lista_filmes:
            print("------------")
            print("Id:", item.get("id", ''))
            print("Filme:", item.get("nome", ''))
            print("Gênero:", item.get("genero", ''))
            print("Ano de Lançamento:", item.get("ano", ''))
            print("Avaliação:", item.get("avaliacao", ''))
            print("------------")
    
    else:
        input("OPÇÃO INVÁLIDA! TENTE NOVAMENTE!")
        limpaTela()
        listar()
        
    
    input("Pressione qualquer tecla para retornar ao menu...")
    limpaTela()
    
#FUNÇÃO PARA PESQUISA POR MÉTODO    
def metodoListar(metodoListagem, modulo):
    limpaTela()
    print("==== LISTANDO FILMES ====")
    for item in lista_filmes:
        if str(metodoListagem) in item[modulo]:
            print("\n==========================================")
            print("Id:", item.get("id", ''))
            print("Filme:", item.get("nome", ''))
            print("Gênero:", item.get("genero", ''))
            print("Ano de Lançamento:", item.get("ano", ''))
            print("Avaliação:", item.get("avaliacao", ''))
            print("==========================================")
            
    return True
    
#FUNÇÃO PARA ATUALIZAÇÃO DE CADASTRO
def atualizar():
    print("==== ATUALIZA CADASTRO ====")
    att = validaCampo("Informe o ID do filme que deseja atualizar", "int", -1)
    index = encontraIndex(att)
    if index > -1:
        filmes_att = lista_filmes[index]
        print("==== ATUALIZAÇÃO DE FILME -", filmes_att["nome"], "====")
        filmes_att["nome"] = validaCampo("Infome o nome", "string", "")
        filmes_att["genero"] = validaCampo("Infome o gênero", "string", "")
        filmes_att["ano"] = validaCampo("Infome o ano", "int", 1900)
        filmes_att["avaliacao"] = validaCampo("Infome a avaliação", "int", 0)
        
        lista_filmes[index] = filmes_att
        database.apagaDado()
        for item in lista_filmes:
            database.gravaDado(item)
        
        input("Filme atualizado com sucesso! \nPressione qualquer tecla para retornar ao menu...")
        
    else:
        input("ID INVÁLIDO! TENTE NOVAMENTE!")
        limpaTela()
        menu()
        
    
    limpaTela()
        
 
#FUNÇÃO PARA DELETAR CADASTRO DE FILME        
def deletar():
    print("=== DELETA CADASTRO ===")
    delete = validaCampo("Informe o ID do filme que deseja deletar", "int", -1)
    index = encontraIndex(delete)
    if index < 0:
        input("FILME NÃO ENCONTRADO. TENTE NOVAMENTE!")
        limpaTela()
        menu()
    print("Deseja realmente deletar o filme:", lista_filmes[index]["nome"], "?")
    print("1- Prosseguir")
    print("2- Retornar ao Menu")
    escolha = input()
    
    if int(escolha) == 2:
        limpaTela()
        menu()
        
    elif int(escolha) < 1 and int(escolha) > 2:
        input("OPÇÃO INVÁLIDA! Retornando ao Menu principal...")
        
    else:
        print("Deletando...")
    
    if index > -1:
        lista_filmes.pop(index)
        database.apagaDado()
        for item in lista_filmes:
            database.gravaDado(item)
        input("Cadastro deletado com sucesso! \nPrecione qualquer tecla para voltar ao menu...")
    else:
        print("ID INVÁLIDO! TENTE NOVAMENTE!")
        limpaTela()
        menu()
        
    limpaTela()
    
#FUNÇÃO PARA ENCONTRAR INDEX REFERENTE À EXCLUSÃO
def encontraIndex(ident):
    count = 0
    result = -1
    for valores in lista_filmes:
        if int(valores.get("id")) == int(ident):
            result = count
            break

        count = count + 1
         
    return result


#FUNÇÃO PARA PESQUISA ESPECÍFICA POR CAMPO
def pesquisar():
    limpaTela()
    print("==== PESQUISA DE FILME ====")
    print("1- Filme")
    print("2- Gênero")
    print("3- Ano de Lançamento")
    print("4- Avaliação")
    search = validaCampo("Informe o campo que deseja pesquisar", "int", " ")
    
    if search == 1:
        pesquisa = "nome"
    elif search == 2:
        pesquisa = "genero"
    elif search == 3:
        pesquisa = "ano"
    elif search == 4:
        pesquisa = "avaliacao"
    else:
        input("OPÇÃO INVÁLIDA!")
        menu()
        
    limpaTela()
    print("==== PESQUISA DE FILME ====")
    searchEsp = validaCampo("INFORME O QUE DESEJA PESQUISAR", "str", " ")
    print("Pressione qualquer tecla para visualizar o resultado da pesquisa...")
    input()
    encontrou = 0
    for item in lista_filmes:
        if searchEsp in item[pesquisa]:
            print("\n==========================================")
            print("Id:", item.get("id", ''))
            print("Filme:", item.get("nome", ''))
            print("Gênero:", item.get("genero", ''))
            print("Ano de Lançamento:", item.get("ano", ''))
            print("Avaliação:", item.get("avaliacao", ''))
            print("==========================================\n")
            encontrou = 1
        
    if encontrou != 1:
        print("NENHUM FILME ENCONTRADO...\n")
    
    input("Precione qualquer tecla para voltar ao menu principal...")
    limpaTela()
    
#FUNÇÃO PARA SERIALIZAÇÃO EM JSON    
def geraJson():
    
    with open('lista_filmes.json', 'w') as file:
        json.dump(lista_filmes, file)
    print("Serialização realizada com sucesso!")
    input("Pressione qualquer tecla para voltar ao menu principal...")
    limpaTela()
    
#INÍCIO DO CÓDIGO/VARIÁVEIS GLOBAIS.
filme = {}
lista_filmes = database.buscaDado()   

menu()