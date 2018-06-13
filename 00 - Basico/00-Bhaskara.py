# Algoritmo Com Teste Automatico Formula de Bhaskara

import math

def entradaDados(A,B,C):
    Delta = B**2 - 4*A*C

    if Delta < 0:
        print("Raiz Complexa Que o Algoritmo Nao Calcula")
        return False
    else :
        return calculaRaizes(A,B,C,Delta)

def calculaRaizes(A,B,C,Delta):
    if Delta > 0:
        X1 = ( -B + math.sqrt(Delta)) / (2 * A)
        X2 = ( -B - math.sqrt(Delta)) / (2 * A)
        X = {X1, X2}
        print(X)
        return X
    else :
        X = - B / (2 * A )
        print(X)
        return X

def test_bhaskara():
    assert entradaDados(1,1,1) == False
    assert entradaDados(1,-2,1) == 1
    assert entradaDados(1, -3, 2) == {2, 1}

