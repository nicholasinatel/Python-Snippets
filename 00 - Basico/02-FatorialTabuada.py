# Advanced

# Repetições Encaixadas
# Funcao Tabuada
def tabuada():
    linha = 1
    coluna = 1
    while linha <= 10:
        while coluna <= 10:
            print(linha * coluna, end = "\t") # end = " " ----- \t = tab 4 spaces
            coluna += 1
        linha += 1
        coluna = 1
        print(end = "\n") # Printa o New Line Passe o Mouse em cima do print pra sacar


# User Digita Sequencia de Numeros e Imprime Fatorial dos Numeros Digitados

def numInput():
    numero_str = input("Entre com Numero: ")
    length = len(numero_str)
    print("numero_str: ", numero_str, "length: ", length)
    fatorialIndividual(int(numero_str), length)


def fatorial(x):
    fat = 1
    if x <= 0:
        return 0
    while(x > 1):
        fat = fat * x
        x -= 1
    return fat

def fatorialIndividual(n, lenght):
    while(lenght >= 1):
        dig1 = n % 10
        fat1 = fatorial(dig1)
        print("Numero Digitado: ", dig1, "Fatorial Dele: ", fat1)
        n = n // 10
        lenght -= 1
        

# Criar Um Menu
#tabuada()

numInput()
