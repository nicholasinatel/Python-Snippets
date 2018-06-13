# testes automatizados
# https://docs.pytest.org
# Testes Manuais Ou Testes Automatizados
# https://www.youtube.com/watch?v=c_5UByqX6kE - testes automatizado Python

# https://www.youtube.com/watch?v=sx1Gm1gSrPk - Assert Python
# Python Assert Statement
# assert <condition>
# assert <condition>, <error message>
# IF <condition> is FALSE, raise an AssertionError Exception
# 2 Categoris of Errors: Recoverable Errors   (excep ) - User can take corrective action
#                        Unrecoverable Errors (assert) - Not enough info to fix or no alternative action is possible
# Use Assertions to write: preconditions | postconditions | invariants

# To run: Windows Console: pytest automated_test.y 
# if type only pytest| ele procura por todos os arquivos test_*.py && *_test.py
# Executa Dentro do arquivo fun��es e m�todos do tipo test_*
# Considera classes do Tipo Test*

# content of automated_test.py | pytest simlpes
def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 4


