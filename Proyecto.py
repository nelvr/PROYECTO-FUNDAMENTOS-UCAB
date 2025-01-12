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
    patrones_obvios = leer_archivo('patrones obvios.txt')
    for patron in patrones_obvios:
        if patron.lower() in contrasena.lower():
            puntaje -= 5

    return puntaje

# Función para clasificar la contraseña según su puntaje
def clasificar_contrasena(puntaje):
    if puntaje <= 15:
        return "Débil"
    elif 15 < puntaje <= 35:
        return "Moderada"
    elif 35 < puntaje <= 50:
        return "Buena"
    elif 50 < puntaje <= 100:
        return "Excelente"
    else:
        return "Impenetrable"

# Función para ordenar contraseñas por puntaje de seguridad
def ordenar_contrasenas(contrasenas):
    n = len(contrasenas)
    for i in range(n):
        for j in range(0, n-i-1):
            if contrasenas[j][2] > contrasenas[j-1][2]:
                contrasenas[j], contrasenas[j-1] = contrasenas[j-1], contrasenas[j]
    return contrasenas

# Función principal
def main():
    contrasenas = leer_archivo('claves proyecto.txt')
    resultados = []

    for contrasena in contrasenas:
        puntaje = calcular_puntaje_seguridad(contrasena)
        categoria = clasificar_contrasena(puntaje)
        resultados.append((contrasena, categoria, puntaje))

    # Ordenar resultados
    resultados_ordenados = ordenar_contrasenas(resultados)

    # Exportar resultados a un archivo
    with open('resultados_contrasenas.txt', 'w', encoding='utf-8') as archivo_salida:
        for contrasena, categoria, puntaje in resultados_ordenados:
            archivo_salida.write(f"{contrasena} | {categoria} | {puntaje}\n")

if __name__ == "__main__":
    main()
