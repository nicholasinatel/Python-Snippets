# Feito Sem Biblioteca Para Testes
def fatorial(n):
    fat = 1
    if n < 0:
        return 0
    while(n > 1) :
        fat = fat * n
        n -= 1
    return fat

def numeroBinomial(n,k):
    print(fatorial(n) / (fatorial(n - k) * fatorial(k)))

# Teste Automatizado - Ou Varios Testes Com Nomes Diferentes
def test_fatorial():
    assert fatorial(0) == 1
    assert fatorial(1) == 1
    assert fatorial(-10) == 0
    assert fatorial(4) == 24
    assert fatorial(5) == 120

def test_fatorial1():
    assert fatorial(1) == 1

def test_fatoriaNegativo():
    assert fatorial(-10) == 0


# Resumo:
# Casos em que o programa pode falhar
# Tipos diferentes de entrada que exercitam caminhos diferentes no programa
# Casos diferentes do código
# Escreva testes automatizados para todos esses casos

