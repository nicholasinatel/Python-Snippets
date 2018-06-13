# Máxima e Mínima
# Quebrar Problema em Problemas Menores
# Conceitos de Desenvolvimento de Software em Python
# Testes Automatizados Para Todo Código Escrito
# Refatoração - Eliminar Codigo Duplicado - Técnica Extrair Método
# Manter Parte Fixa do Código | Loop Para Parte Variável

#__________________________________________________________________________________________________
def MinMax(temperaturas):
    print("A menor temperatura do mês foi: ", minima(temperaturas), "C.")
    print("A maior temperatura do mês foi: ", maxima(temperaturas), "C.")

#__________________________________________________________________________________________________
# MAXIMA
def maxima(temps):
    max = temps[0] # Inicializa com o primeiro Valor Do Vetor Nesse Caso
    i = 0
    while i < len(temps):
        if temps[i] > max:
            max = temps[i]
        i += 1
    return max

#__________________________________________________________________________________________________
# MINIMA
def minima(temps):
    min = temps[0] # Inicializa com o primeiro Valor Do Vetor Nesse Caso
    i = 0
    while i < len(temps):
        if temps[i] < min:
            min = temps[i]
        i += 1
    return min

#__________________________________________________________________________________________________
# AUTOMATED TEST
# Exec - pytest 06_MaxMinDevSoft_Foda_Automated_Test.py
# Compilador Procura Automaticamente por funções começadas em "test_*"
def test_MaxMin():
    print("Início Bateria de Testes")

    InputTestArray = [[0], [0,0,0,0,0,0], [1,2,3,4,5,6,7,8,9], [20,30,15,25,20,100], [-15,-2,0,15]]
    
    OutputTestArray_max = [0, 0, 9 , 100, 15]
    OutputTestArray_min = [0, 0, 1 , 15, -15]

    for i in range(len(InputTestArray)):
        assert maxima(InputTestArray[i]) == OutputTestArray_max[i] 
        assert minima(InputTestArray[i]) == OutputTestArray_min[i]

    print("Final Bateria de Testes")

 