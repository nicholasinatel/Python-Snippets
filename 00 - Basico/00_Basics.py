# This is how you comment in Python
# There are two ways of running this program:
# 1. Run
#     python3 Basics.py
# then enter two numbers and press ctrl-d/ctrl-z
# 2. Save two numbers to a file -- say, dataset.txt.
# Then run
#     python3 Basics.py < dataset.txt

import sys
import math

#-----------Conversor de Temperatura----------------------
# param - void
# return - void
#tempFahrenheit = (tempCelsius * 9 / 5) + 32
#tempCelsius = (tempFahrenheit - 32) * (5 / 9)
def temp_calc():
    print("Entre qual tipo de temperatura quer calcular: ")
    print("1 - Celsius ")
    print("2 - Fahrenheit ")

    seletor = input("Digite: ") # input sempre devolve uma string

    if int(seletor) == 1: 
        tempFahrenheit = input("Entre com a temperatura em Fahrenheit: ")
        tempCelsius = float( (float(tempFahrenheit) - 32) / (9 / 5) )
        print(tempCelsius, "C Celsius")
    elif int(seletor) == 2:
        tempCelsius = input("Entre com a temperatura em Celsius: ")
        tempFahrenheit = float( float(tempCelsius) * (1.8) + 32 )
        print(tempFahrenheit, "F Fahrenheit")

    menu()

#-----------Conversor de Segundos/Minutos/Horas-------------
# param - void
# return - void
def time_calc():
    print("Conversor de Segundos/Minutos/Horas")
    print("1 - Converter Segundos")
    print("2 - Converter Minutos")
    print("3 - Converter Horas")

    seletor = input("Opção: ")

    if int(seletor) == 1:
        segundos_str = input("Entre Numero de Segundos Para Conversão")
        minutos = int(segundos_str) / 60
        horas = minutos / 60
        print(minutos, "minuto(s)", horas, "hora(s)")
    elif int(seletor) == 2:
        minutos_str = input("Entre Numero de Minutos Para Conversao")
        segundos = int(minutos_str) * 60
        horas = segundos / 3600
        print(segundos, "segundo(s)", horas, "hora(s)")
    elif int(seletor) == 3:
        horas_str = input("Entre Número de Horas Para Conversão")
        segundos = int(horas_str) * 3600
        minutos = int(horas_str) * 60
        print(segundos, "segundo(s)", minutos, "minuto(s)")
    menu()

#---------------------Valores Booleanos--------------------
# and &&
# or ||
# not !
#----------------------Precedência de Operadores-------------
#Nível----Categoria---------Operadores
#  7      Exponenciação     **
#  6      Multiplicação     *,/,//,%
#  5      Adição            +,-
#  4      Relacional        ==,!=.<=,>
#  3      Lógico            not
#  2      Lógico            and
#  1      Lógico            or

#----------Raízes de Fução Polinomial do Segundo Grau--------
# ax^2 + bx + c = 0
# Raiz Quadradao Precisa Ser Maior Que Zero - Sugerido B < 0
# Bhaskara
def bhaskara():
    A = float(input("Entre com A: "))
    B = float(input("Entre com B: "))
    C = float(input("Entre com C: "))

    delta = B**2 - ( 4 * A * C)

    if delta < 0:
        print("Este algoritmo Só calcula Raízes Reais")
    elif delta > 0:
        print("delta = ", delta)
        X1 = ( - B + math.sqrt(delta) ) / (2*A) 
        X2 = ( - B - math.sqrt(delta) ) / (2*A)
        print("Raízes: ", X1, " e ", X2)
    elif delta == 0:
        X = -B / (2*A)
        print("Raiz", X)
    menu()

#-----------------------Repetições--------------------------
# while - Soma De Numeros Digitados
def soma_while():
    print("Digite uma Sequencia de Valores terminada por zero.")
    soma = 0;

    valor = 1;
    while valor != 0:
        valor = int(input("Digite um Valor a ser somado: "))
        soma += valor

    print("Soma dos valores = ", soma)
    menu()

#----Calculador da Soma dos Digitos de Um Numero Inteiro----
def soma_inteiros():
    numero_str = input("Entre com o numero Inteiro: ")
    soma = 0
    tamanho = len(numero_str)
    numero = int(numero_str)
    print("numero = ", numero, "tamanho = ", tamanho)
    i = 0

    while i < tamanho:
        x = numero % 10;
        print(x, "numero x")
        numero = numero // 10; # // Divisão Inteira
        soma += x 
        i += 1

    print("Soma = ", soma)
    menu()
#-----------------------------------------------------------

#----------------Flag Indicador de Passagem-----------------
#Desafio - Dado um numero, necessario dizer se ele tem 2 digitos adjacentes iguais
#213215 Nao tem digitos adjacentes iguais
#3142254 Tem Digitos Adjacentes Iguais
def flag():
    numero_str = input("Entre com um numero para analisar se tem 2 digitos adjacentes iguais: ")

    numero = int(numero_str)
    tamanho = len(numero_str)
    print(tamanho)
    i = 0

    while i < tamanho:
        print("numero = ", numero)
        x = numero % 10;
        print(x)
        numero = numero // 10
        y = numero % 10;
        print(y)
        if x == y :
            print("2 digitos iguais")
            i += 1
        elif x != y :
            i += 1
    menu()

#-------------Coeficiente Binomial------------------------------------------------
def binomial_input():
    n = int(input("Entre com N: "))
    k = int(input("Entre com K: "))
    if n >= k and k >= 0 :
        binomial_calc(n,k)
    else :
        print("Erro - Condicao Necessaria Para Realizar o Calculo n >= k >= 0")
        binomial_input()

def binomial_calc(x,y):
    b_coe = math.factorial(x) / (math.factorial(y) * math.factorial(x-y))
    print(b_coe)
    menu()

#-----------------------------------------------------------
# Menuzao!
def menu():
    print("_______________________________________________________________________________")
    print("_Pack de Programas Utilities")
    print("_A-Conversao de Temperatura")
    print("_B-Conversao de Segundos/Minutos/Horas")
    print("_C-Raizes de Fução Polinomial do Segundo Grau")
    print("_D-Soma De Numeros Digitados")
    print("_E-Calculador da Soma dos Digitos de Um Numero Inteiro")
    print("_F-Flag Indicador de Passagem")
    print("_G-Coeficiente Binomial")

    seletor = input("Opção...: ")
    if seletor == 'A' :
        temp_calc()
    elif seletor == 'B':
        time_calc()
    elif seletor == 'C':
        bhaskara()
    elif seletor == 'D':
        soma_while()
    elif seletor == 'E':
        soma_inteiros()
    elif seletor == 'F':
        flag()
    elif seletor =='G' :
        binomial_input()
    else :
        menu()

#------MAIN--------
Numero = 5.5
Texto = "Isto é uma String"
NString = str(Numero) #Conversao De Types - int to string

print(Texto, int(Numero), "Assim também rola String")
print(len(Texto))
print("Isto eh um numero convertido em String", NString)
menu()


