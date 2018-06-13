# Maxima e Minima
# Quebrar Problema em Problemas Menores
# Conceitos de Desenvolvimento de Software em Python
# Testes Automatizados Para Todo Codigo Escrito
# Refatoracao - Eliminar Codigo Duplicado - Tecnica Extrair Metodo

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

def testa_maxima():
    print("Inicio Teste Maxima") # Codigo Duplicado Demais Usar Tecnica de Extrair Metodo
    teste_pontual_maxima([0], 0) # Valor Para Calculo / Valor Esperado Como Resultado
    teste_pontual_maxima([0,0,0,0,0,0], 0)
    teste_pontual_maxima([1,2,3,4,5,6,7,8,9], 9)
    teste_pontual_maxima([20,30,15,25,20,100], 100)
    teste_pontual_maxima([-15,-2,0,15], 15)
    print("Final Teste Maxima")
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

def testa_minima():
    print("Inicio Teste Minima") # Codigo Duplicado Demais Usar Tecnica de Extrair Metodo
    teste_pontual_minima([0], 0) # Valor Para Calculo / Valor Esperado Como Resultado
    teste_pontual_minima([0,0,0,0,0,0], 0)
    teste_pontual_minima([1,2,3,4,5,6,7,8,9], 1)
    teste_pontual_minima([20,30,15,25,20,100], 15)
    teste_pontual_minima([-15,-2,0,15], -15)
    print("Final Teste Minima")

# Extrair Método - Consiste em:
# Manter o que é Fixo e Passar Por Parâmetro Aquilo que é Variável
#   temp = [0]                                   #---> Fixo - Varia Conteudo do Vetor
#   if minima(temp) != 0:                        #---> Fixo - Varia Conteudo Da Condicao
#       print("Valor Errado Para Array: ", temp) #---> Fixo
#   temp = [0,0,0,0,0,0]
#   if minima(temp) != 0:
#       print("Valor Errado Para Array: ", temp)
  
def teste_pontual_minima(temp, valor_esperado): # Extrair Método Aplicado
    valor_calculado = minima(temp)

    if valor_calculado  != valor_esperado:
        print("Valor Errado Para Array: ", temp)
        print("Valor Esperado Para Array: ", valor_esperado)

def teste_pontual_maxima(temp, valor_esperado): # Extrair Método Aplicado
    valor_calculado = maxima(temp)

    if valor_calculado  != valor_esperado:
        print("Valor Errado Para Array: ", temp)
        print("Valor Esperado Para Array: ", valor_esperado)
#__________________________________________________________________________________________________
