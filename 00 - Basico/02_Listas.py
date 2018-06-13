# Listas/Array/Vetor
# https://www.youtube.com/watch?v=krVca97F13I
# playlist de musicas
# https://docs.python.org/3/
# https://www.youtube.com/watch?v=LrXapVI66so&t=1s
# https://docs.python.org/3/reference/index.html

def inicioListas():

    playlist_nicholas = ["I Scream", "Sex Style", "Maria Maria"]
    lista_numeros_primos = [2, 3, 5 , 7, 11]
    filme = ["John Wick", 2.11, 2016]

    print(playlist_nicholas[1])
    print(filme)

    print(playlist_nicholas)
    print(len(playlist_nicholas)) # Tamanho da Lista

    # Altera ao Final da lista ja existente .append(Elemento)
    playlist_nicholas.append("Bella Ciao") # .append method Concatena Apos Vetor
    print(playlist_nicholas)
    print(len(playlist_nicholas))

    cartoes_amarelos = []

    cartoes_amarelos.append("Luis Fabiano")
    cartoes_amarelos.append(1)

    print(cartoes_amarelos)

# Exercicio: Le Do Teclado Sequencia de Numeros Inteiros, Quando 0 Imprime Ordem Inversa
def invertVector():
    sequencia = []

    n = 1
    while n != 0:
        n = int(input("Entre com numero: "))
        sequencia.append(n)

    print(sequencia)

    n = len(sequencia) - 1
    while n > -1:
        print(sequencia[n])
        n -= 1
    
# Extracao De SubListas
def sublista():

    primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    print(primos[1:2]) # A partir da Posicao 1 Ate posicao 2, (2 - 1) elementos * Cria Nova Lista
    print(primos[2:7]) # A partir da Posicao 2 Ate posicao 7, (7 - 2) elementos * Cria Nova Lista

    print(primos[:12]) # A partir da Posicao 0 Ate 12
    print(primos[12:]) # A partir da Posicao 12 Ate a ultima

# Clonar listas
def cloneLista():
    lista1 = ["vermelho", "verde", "azul"]
    lista2 = lista1

    print(lista2,"_Lista 2")
    lista2[0] = "rosa"
    # Ambas as Variaveis APONTAM para o mesmo bloco de memoria !!!
    print(lista1,"Lista_1")
    # Para que isso nao aconteca eh Necessario CLONAR a lista!

    clone = lista2[:] # Clona Para Outro Endereco De Memoria

    # Pertinencia a Uma Lista - Se Determinado Elemento Pertence a uma lista
    if "rosa" in lista1:
        print("esta")

    if "vermelho" in lista1:
        print("tala")

    return clone

# Concatenacao De Listas _Gera Novas Listas Diferente do .append
def concatenaLista():
    listaA = [2,3,4]
    listaB = [5,4,6]
    listaC = listaA + listaB
    print(listaC)

    listaTriplicada = listaA * 3
    print(listaTriplicada)

# Remocao De Listas
def deleteLista():
    a = [1,2,3]
    del a[1]
    lista = ['a','b','c','d','e']
    del lista[1:5]

    print(a)
    print(lista)
# ---------------------------------MENU-------------------------------
def menu():
    print("Listas_____________________")
    print("Inicio_Digite: 0")
    print("Inverter Lista_Digite: 1")
    print("Extrair Sublista_Digite: 2")
    print("Clonar Listas_Digite: 3")
    print("Concatenacao de Listas_Digite: 4")
    print("Delete Lista_Digite: 5")

    select = int(input("_"))
    if select == 0:
        inicioListas()
        menu()
    elif select == 1:
        invertVector()
        menu()
    elif select == 2:
        sublista()
        menu()
    elif select == 3:
        clone = cloneLista()
        print(clone,"Printando Clone")
        menu()
    elif select == 4:
        concatenaLista()
        menu()
    elif select == 5:
        deleteLista()
        menu()

menu()