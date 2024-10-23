import scipy.stats as stats
import math

def calcular_varianza(numeros):
    if len(numeros) == 0:
        return 0
    
    media = sum(numeros) / len(numeros)
    varianza = sum((x - media) ** 2 for x in numeros) / (len(numeros) - 1)
    
    return varianza

# Ejemplo de uso
numeros = [25.4,25.1,24.9,25.2,25]

def calcular_desvio_estandar(numeros):
    if len(numeros) == 0:
        return 0
    
    media = sum(numeros) / len(numeros)
    varianza = sum((x - media) ** 2 for x in numeros) / (len(numeros) - 1)  # Dividir por (n-1) para muestra
    desvio_estandar = math.sqrt(varianza)
    
    return desvio_estandar

def calcularPromedio(numeros):
    if len(numeros) == 0:
        return 0
    return sum(numeros) / len(numeros)


def calcular_intervalo_confianza_varianza(N, nivel_confianza, desvio_estandar):
    # Grados de libertad
    df = N - 1
    
    # Valor de alfa
    alfa = 1 - nivel_confianza
    
    # Valores críticos de chi-cuadrado
    chi2_inf = stats.chi2.ppf(alfa / 2, df)
    print("Chi2_inf ",chi2_inf)
    chi2_sup = stats.chi2.ppf(1 - alfa / 2, df)
    print("Chi2_sup ",chi2_sup)
    
    # Calcular la varianza
    varianza = desvio_estandar ** 2
    
    # Calcular los límites del intervalo de confianza
    limite_inferior = (df * varianza) / chi2_sup
    limite_superior = (df * varianza) / chi2_inf
    
    print("Intervalo de Desvio Estandar: ", math.sqrt(limite_inferior),  math.sqrt(limite_superior))
    return limite_inferior, limite_superior

# Ejemplo de uso
print("Desvio Estandar ",calcular_desvio_estandar(numeros))  # Salida: 0.277
print("Varianza ",calcular_varianza(numeros))  # Salida: 2.0
print("Promedio ",calcularPromedio(numeros))  # Salida: 3.0


# Ejemplo de uso
N = len(numeros)
print("N ",N)
nivel_confianza = 0.95
desvio_estandar = calcular_desvio_estandar(numeros)
intervalo = calcular_intervalo_confianza_varianza(20, nivel_confianza, 210)
print("Intervalo de confianza para la varianza:", intervalo)