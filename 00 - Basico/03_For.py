# For

lista_frutas = ["Jabuticaba", "Cupuacu", "Acai"]

for fruta in lista_frutas:
    print("Eu curto " + fruta) # Poderia Ser * Multiplicao, Percorreria Cada Elemento e Entao Multiplicaria

for i in range(20): # (fim)
    print(i)

for i in range(3,7): # (inicio, fim)
    print(i)

for i in range(1,10,2): # (inicio, fim, passo)
    print(i)

# Substituicao De Listas - Exemplo

primos = [2,3,5,7]

for i in range(len(primos)):
    primos[i] = primos[i]**3

print(primos)