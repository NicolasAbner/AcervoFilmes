arquivo_db = "Streamberry.txt"

import os


#FUNÇÃO PARA ARMAZENAR DADOS NO BANCO TXT
def gravaDado(dado):
    
    linha = ""
    for item in dado.values():
        linha = linha + str(item) + ";"
    
    linha =  "\n" + linha
    
    
    arquivo = open(arquivo_db, "a")
    arquivo.write(linha)
    arquivo.close()
    

#FUNÇÃO PARA BUSCAR DADOS NO BANCO TXT    
def buscaDado():
    
    arquivo = open(arquivo_db, "w")
    arquivo.close()

    arquivo = open(arquivo_db, "r")
    conteudo = arquivo.readlines()
    arquivo.close()
    
    result = []
    
    for linha in conteudo:
        if linha != "\n" :
            valores = linha.split(";")
            filme = {
                "id":valores[0], 
                 "nome":valores[1], 
                 "genero":valores[2], 
                 "ano":valores[3], 
                 "avaliacao":valores[4]
            }
            
            result.append(filme)
    
    return result
 
#FUNÇÃO PARA REESCREVER DADOS NO BANCO TXT   
def apagaDado():
    os.remove(arquivo_db)
    