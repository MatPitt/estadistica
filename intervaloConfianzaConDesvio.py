import scipy.stats as stats
import math

# Z - Moelo Normal

def calcular_z_critico(confianza):
    """
    Calcula el valor crítico Z de la distribución normal estándar.
    
    :param confianza: Nivel de confianza (por ejemplo, 0.95 para un intervalo de confianza del 95%)
    :return: Valor crítico Z
    """
    alfa = 1 - confianza
    z = stats.norm.ppf(alfa)
    return z

def calcular_z_puntual(media_muestral, mu_observado, desvio_poblacional, n):
    numerador = (media_muestral - mu_observado)
    denominador = desvio_poblacional / math.sqrt(n)
    resultado = numerador / denominador
    return resultado


def calcular_x_estrella(mu_0, desvio_poblacional, n, confianza):
    alfa = 1 - confianza
    z = stats.norm.ppf(confianza)
    x_estrella = mu_0 +( z * (desvio_poblacional / math.sqrt(n)))
    return x_estrella

def calcular_intervalo_confianza(media_muestral, desvio_poblacional, n, confianza):
    # Calcular el valor crítico Z
    z = stats.norm.ppf(confianza)
    
    # Calcular el margen de error
    margen_error = z * (desvio_poblacional / math.sqrt(n))
    
    # Calcular el intervalo de confianza
    limite_inferior = media_muestral - margen_error
    limite_superior = media_muestral + margen_error
    
    return limite_inferior, limite_superior

def calcularBetaIzquierda(confianza, mu_0, mu_1, desvio_poblacional, n):
    x_estrella = calcular_x_estrella(mu_0, desvio_poblacional, n, confianza)
    valorParaZ = (x_estrella - mu_1) / (desvio_poblacional / math.sqrt(n))
    beta = 1 - stats.norm.cdf(valorParaZ)
    return beta

def calcularBetaDerecha(confianza, mu_0, mu_1, desvio_poblacional, n):
    x_estrella = calcular_x_estrella(mu_0, desvio_poblacional, n, confianza)
    valorParaZ = (x_estrella - mu_1) / (desvio_poblacional / math.sqrt(n))
    beta = stats.norm.cdf(valorParaZ)
    return beta

# Ejemplo de uso
media_muestral = 246
desvio_poblacional = 15
n = 25  # Tamaño de la muestra
confianza = 0.90  # Intervalo de confianza del %


mu_0 = 1 #Valor de Mu Observado
mu_1 = 1.05 #Valor de Mu Observado

limite_inferior, limite_superior = calcular_intervalo_confianza(media_muestral, desvio_poblacional, n, confianza)

print(f"El intervalo de confianza para la media poblacional es: ({limite_inferior}, {limite_superior})")

print(f"El punto crítico Z es: {calcular_z_critico(confianza)}")

print(f"El Z puntual es: {calcular_z_puntual(media_muestral, mu_0, desvio_poblacional, n)}")

print(f"El x estrella es: {calcular_x_estrella(mu_0, desvio_poblacional, n, confianza)}")

print(f"El Beta izquierda es: {calcularBetaIzquierda(confianza, mu_0, mu_1, desvio_poblacional, n)}")

print(f"El Beta derecha es: {calcularBetaDerecha(confianza, mu_0, mu_1, desvio_poblacional, n)}")

