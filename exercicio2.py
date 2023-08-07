#  Se achar necessario, faça import de outras bibliotecas
# Rafaella Bianca Cavalcante





# Crie a função que será avaliada no exercício aqui

def cumulativo(lista): #função com parâmetro lista
    listadois = [] #lista vazia
    anterior = 0 #variável que começa zerada
    for item in lista: #para cada item recebido na lista parâmetro
        listadois.append(item + anterior)  #adiciona 
        anterior += item
    return listadois


# Teste a sua função aqui (caso ache necessário)











