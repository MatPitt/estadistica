import scipy.stats as stats
import math

#import scipy.stats as stats

def calcular_A(R, nivel_confianza):
    # Calcular alfa
    alfa = 1 - nivel_confianza
    
    # Calcular el valor crítico Z
    z = stats.norm.ppf(1 - alfa / 2)
    print("Z ",z)   
    # Calcular el tamaño de la muestra
    numerador = z * (R ** (1/3) + 1 )
    print("Numerador ",numerador)
    denominador = 2 * (R ** (1/3) - 1 )
    print("Denominador ",denominador)
    return numerador/denominador

# Ejemplo de uso
R = 1.7662  # Rango
nivel_confianza = 0.90

A = calcular_A(R, nivel_confianza)
print("Valor de A: ", A)
