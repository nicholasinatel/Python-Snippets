# Objetos e Referencias Na Memoria
# Em Python Strings Sao Imutaveis
# Portanto a && b estao apontando para o mesmo bloco de memoria

a = "banana"
b = "banana"

test = a is b # Retorna True Por Estar Apontando para o mesmo bloco de memoria ja que strings sao imutaveis
print(test)

#__________________________________

d = [3,4,5]
c = [3,4,5]

test = d is c
print(test) # Nesse caso os objetos sao diferentes portanto retorna false
test = d == c
print(test) # o sinal == refere-se ao conteudo dos objetos portanto iguais e retorna TRUE

#______________________________________________
# Lista De Listas
origlist = [45, 76, 34, 55]
listaDelistas = [origlist] * 3
print(listaDelistas)

origlist[1] = 99 # Altera no objeto origlist

print(listaDelistas) # Alterou 3 objetos em listaDelistas pois apontam para o mesmo objeto de origlist