import scipy.stats as stats
import math

def calcular_z_critico(confianza):
    """
    Calcula el valor crítico Z de la distribución normal estándar.
    
    :param confianza: Nivel de confianza (por ejemplo, 0.95 para un intervalo de confianza del 95%)
    :return: Valor crítico Z
    """
    alfa = 1 - confianza
    z = stats.norm.ppf(1 - alfa/2)
    return z

def intervalo_confianza_bernoulli(confianza, probabilidad_muestral, n):
    """
    Calcula el intervalo de confianza para un proceso de Bernoulli.
    
    :param confianza: Nivel de confianza (por ejemplo, 0.95 para un intervalo de confianza del 95%)
    :param probabilidad_muestral: Proporción muestral (por ejemplo, 0.5)
    :param n: Número de experimentos
    :return: Intervalo de confianza (limite_inferior, limite_superior)
    """
    z = calcular_z_critico(confianza)
    margen_error = z * math.sqrt((probabilidad_muestral * (1 - probabilidad_muestral)) / n)
    
    limite_inferior = probabilidad_muestral - margen_error
    limite_superior = probabilidad_muestral + margen_error
    
    return limite_inferior, limite_superior

def calcular_tamano_muestra(confianza, probabilidad_muestral, margen_error):
    """
    Calcula la cantidad de experimentos necesarios para un proceso de Bernoulli.
    
    :param alfa: Nivel de error esperado (por ejemplo, 0.05 para un nivel de confianza del 95%)
    :param probabilidad_muestral: Proporción muestral (por ejemplo, 0.5)
    :param margen_error: Margen de error (por ejemplo, 0.05)
    :return: Tamaño de la muestra (n)
    """
    z = calcular_z_critico(confianza)
    print(z)
    n = (z**2 * probabilidad_muestral * (1 - probabilidad_muestral)) / (margen_error**2)
    return math.ceil(n)  # Redondear hacia arriba para asegurar que el tamaño de la muestra sea suficiente

# Ejemplo de uso
confianza = 0.90  # Intervalo de confianza del 90%
probabilidad_muestral = 0.25  # Proporción muestral
n = 600  # Número de experimentos

limite_inferior, limite_superior = intervalo_confianza_bernoulli(confianza, probabilidad_muestral, n)
print(f"El intervalo de confianza para la proporción poblacional es: ({limite_inferior:.4f}, {limite_superior:.4f})")

# Calcular tamaño de muestra necesario
  # Nivel de error esperado (5%)
margen_error = 0.01  # Margen de error (5%)

tamano_muestra = calcular_tamano_muestra(confianza, probabilidad_muestral, margen_error)
print(f"La cantidad de experimentos necesarios es: {tamano_muestra}")



