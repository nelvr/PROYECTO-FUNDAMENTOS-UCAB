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
    patrones_obvios = leer_archivo("patrones obvios.txt")
    for patron in patrones_obvios:
        if patron.lower() in contrasena.lower():
            puntaje -= 5

    return puntaje
# Función para procesar las contraseñas y devolverlas ordenadas por puntaje de seguridad
def procesar_contrasenas():
    # Leer las contraseñas del archivo
    claves = leer_archivo("claves proyecto.txt")
    
    # Calcular el puntaje de seguridad para cada contraseña
    contrasenas_con_puntaje = [(clave, calcular_puntaje_seguridad(clave)) for clave in claves]
    
    # Ordenar las contraseñas por puntaje de seguridad usando bubble sort
    n = len(contrasenas_con_puntaje)
    for i in range(n):
        for j in range(0, n-i-1):
            if contrasenas_con_puntaje[j][1] < contrasenas_con_puntaje[j+1][1]:
                contrasenas_con_puntaje[j], contrasenas_con_puntaje[j+1] = contrasenas_con_puntaje[j+1], contrasenas_con_puntaje[j]
    
    return contrasenas_con_puntaje
# Función principal para ejecutar el procesamiento de contraseñas
def main():
    contrasenas_procesadas = procesar_contrasenas()
    for contrasena, puntaje in contrasenas_procesadas:
        print(f"Contraseña: {contrasena}, Puntaje: {puntaje}")

# Llamar a la función principal
if __name__ == "__main__":
    main()