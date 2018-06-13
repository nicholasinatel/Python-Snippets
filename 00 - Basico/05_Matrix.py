# Programa Para Gerenciar Notas De Alunos
# Matrizes
# Listas De Listas

# Estrutura de Dados Bidimensional com Linhas e Colunas
A = [[1,2,3],
     [4,5,6],
     [7,8,9]]
#__________________________________________________________________________________________________
# Função Para Criar uma Matriz Identidade com Input Da Ordem Da Matriz
def identidade(ordem):
    matriz = []
    i = 0
    j = 0
    for i in range(ordem) :
        # Cria Linha i
        linha = [] # lista vazia Zera Em Toda Nova Iteração De Linha
        for j in range(ordem):
            if i == j:
                linha.append(1)
            else :
                linha.append(0)

        #Adiciona Linha a Matriz
        matriz.append(linha)

    return matriz
#__________________________________________________________________________________________________
# Printar Matriz QUADRADA No Formato Para Ser Humano Entender
def oracle(matrix, ordem):
    for i in range(ordem):
        for j in range(ordem):
            print(matrix[i][j], end=" ") # end=" " Para Que A Proxima String Não Pule Uma Linha
        print("\t") # Pula Uma Linha
#__________________________________________________________________________________________________
def leMatriz():
    lin = int(input("Digite Numero De Linhas Da MAtriz: "))
    col = int(input("Digite o Numero de Colunas Da MAtriz: "))
    matrixInfo = [criaMatriz(lin, col), lin, col]
    return matrixInfo #RETORNA VETOR COM UMA MATRIZ, NUMERO DE LINHAS E NUMERO DE COLUNAS
#__________________________________________________________________________________________________
def criaMatriz(lin, col):
    matrix = []
    for i in range(lin):
        buffer = [] # Zera o Buffer a A Cada Nova Linha
        for j in range(col):
            buffer.append(int(input("Entre com um Valor Da MATRIZ: ")))

        matrix.append(buffer) # Acrescenta Buffer(Linha) A Matriz
    
    return matrix 
#__________________________________________________________________________________________________
# Execução Prinicpal Do Código
# Matriz Identidade
ordem = int(input("Entre com a Ordem da Matriz Identidade: "))
matriz = identidade(ordem) # Recebe Matriz Identidade
oracle(matriz, ordem) # Printa Matriz Identidade
#__________________________________________________________________________________________________
matrizInfo = leMatriz() #Retorno Do Vetor Com Informacoes Da Matriz Digitada
matriz = matrizInfo[0] #Extrair A Matriz Do Vetor Por Usabilidade
# Printar A Matriz que pode ser Não Quadrada que foi digitada previamente
for i in range(matrizInfo[1]):
    for j in range(matrizInfo[2]):
        print(matriz[i][j], end=" ")
    print("\t")
