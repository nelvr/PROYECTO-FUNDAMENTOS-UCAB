import re

# Función para leer un archivo y devolver una lista de líneas
def leer_archivo(archivo):
    with open(archivo, 'r', encoding='utf-8') as archivo:
        return [linea.strip() for linea in archivo.readlines()]

# Función para calcular el puntaje de seguridad de una contraseña
def calcular_puntaje_seguridad(contrasena):
    puntaje = 0
    longitud = len(contrasena)
    
    # Sumar puntos por longitud
    puntaje += longitud
    
    # Sumar puntos por tipos de caracteres
    if re.search(r'[a-z]', contrasena):
        puntaje += 1  # letras minúsculas
    if re.search(r'[A-Z]', contrasena):
        puntaje += 1  # letras mayúsculas
    if re.search(r'[0-9]', contrasena):
        puntaje += 1  # números
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', contrasena):
        puntaje += 3  # símbolos
        puntaje += 2 * (len(re.findall(r'[!@#$%^&*(),.?":{}|<>]', contrasena)) - 1)  # símbolos adicionales

    # Restar puntos por patrones obvios
    patrones_obvios = leer_archivo('../patrones_obvios.txt')
    for patron in patrones_obvios:
        if patron.lower() in contrasena.lower():
            puntaje -= 5

    return puntaje
