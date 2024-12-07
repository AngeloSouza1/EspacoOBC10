# modulo_fuga.py

def calcular_velocidade_necessaria(distancia_km):
    """
    Calcula a velocidade média necessária (em km/h) para percorrer a distância fornecida em 30 minutos.

    Parâmetros:
    - distancia_km (float): A distância até o ponto de segurança em quilômetros.

    Retorna:
    - float: A velocidade média necessária em km/h com duas casas decimais.
    """
    tempo_horas = 30 / 60  # 30 minutos convertidos para horas
    velocidade_media = distancia_km / tempo_horas
    return round(velocidade_media, 2)
