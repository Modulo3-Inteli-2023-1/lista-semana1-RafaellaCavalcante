#  Se achar necessario, faça import de outras bibliotecas
# Rafaella Bianca Cavalcante
# Crie a função que será avaliada no exercício aqui
def multiplas_operacoes(x, y): #função com parâmetros x e y.
    if y == 0: #se y for 0
        divisao = 0 #o resultado da divisão vai ser 0
    else: #caso contrário, vai realizar uma operação de divisão
        divisao = x/y
    soma = x + y #operação de soma
    subtracao = x - y #operação de subtração
    multiplicacao = x * y #operação de multiplicação
    return {soma, subtracao, multiplicacao, divisao} #vai retornar o resultado de cada operação

# Teste a sua função aqui (caso ache necessário)