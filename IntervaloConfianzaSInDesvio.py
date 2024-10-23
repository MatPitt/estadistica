import scipy.stats as stats
import math


def calcular_punto_critico(confianza, grados_libertad):
    """
    Calcula el punto crítico t de la distribución t de Student.
    
    :param confianza: Nivel de confianza (por ejemplo, 0.95 para un intervalo de confianza del 95%)
    :param grados_libertad: Grados de libertad (n - 1, donde n es el tamaño de la muestra)
    :return: Valor crítico t
    """
    alfa = 1 - confianza
    t = stats.t.ppf(alfa, df=grados_libertad)
    return t

# T se Student

def calcular_intervalo_confianza(n, media_muestral, desvio_muestral, confianza):
    # Calcular el valor crítico t
    alfa = 1 - confianza
    t = stats.t.ppf(1 - alfa/2, df=n-1)
    
    # Calcular el margen de error
    margen_error = t * (desvio_muestral / math.sqrt(n))
    
    # Calcular el intervalo de confianza
    limite_inferior = media_muestral - margen_error
    limite_superior = media_muestral + margen_error
    
    return limite_inferior, limite_superior

def calcular_t_puntual(n, media, media_muestral, desvio_muestral):
    """
    Calcula el valor de t puntual.
    
    :param n: Tamaño de la muestra
    :param media: Media poblacional
    :param media_muestral: Media muestral
    :param desvio_muestral: Desvío muestral
    :return: Valor de t puntual
    """
    t_puntual = (media_muestral - media) / (desvio_muestral / math.sqrt(n))
    return t_puntual

def calcularError( confianza , desvio_muestral, n):
    alfa = 1 - (confianza/2)
    tete = stats.t.ppf(alfa, df=n-1)
    segundo_termino = desvio_muestral / math.sqrt(n)
    error= tete*segundo_termino
    return error

# Ejemplo de uso
n = 20  # Tamaño de la muestra
mu0 = 250
media_muestral = 280
desvio_muestral = 15
confianza = 0.99  # Intervalo de confianza del %

limite_inferior, limite_superior = calcular_intervalo_confianza(n, media_muestral, desvio_muestral, confianza)

print(f"El intervalo de confianza para la media poblacional es: ({limite_inferior}, {limite_superior})")

puntoCritico=calcular_punto_critico(confianza, n-1)

print(f"El punto crítico t es: {puntoCritico}")

t_puntual = calcular_t_puntual(n, mu0, media_muestral, desvio_muestral)
print(f"El valor de t puntual es: {t_puntual}")

print(f"El error es: {calcularError(confianza, desvio_muestral, n)}")