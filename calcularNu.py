import scipy.stats as stats
import math


def calcularNu(a):
    resultado = a**2
    resultado = resultado + 1
    resultado = math.sqrt(resultado)
    resultado = resultado + a
    resultado = resultado ** 2
    resultado = resultado * 2/9
    return resultado

# Ejemplo de uso
a = 8.7009
nu = calcularNu(a)
print("Valor de Nu:", nu)