#  Se achar necessario, faça import de outras bibliotecas
# Rafaella Bianca Cavalcante





# Crie a função que será avaliada no exercício aqui
def tem_duplicados(lista): #define função com parâmetro lista
    percorridos = [] #lista que começa vazia
    for item in lista: #percorre cada item na lista
        if item in percorridos: #se o item está na lista percorridos, retorna true
            return True
        percorridos.append(item) #adiciona o item a lista percorridos
    return False #retorna falso





# Teste a sua função aqui (caso ache necessário)











