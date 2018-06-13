# Exercicio de Numeros Primos
# https://www.youtube.com/watch?v=Wcug8mjU8Sg

def primo(numero):
    # numero = int(input("Entre com o número: "))
    if (numero <= 1):
        print("Não é um número primo: ", numero)
        primo()
    
    n = 2
    soma = 0
    while n <= numero:
        teste = numero % n
        if (teste == 0):
            soma += 1
        n += 1
    
    if soma == 1:
        # print(numero, "Primo")
        return True
    elif soma > 1:
        # print(numero, "Não é Primo")
        return False

limite = int(input("Limite Maximo: "))

n = 2
while n < limite:
    if primo(n):
        print(n, end=", ")
    n += 1
