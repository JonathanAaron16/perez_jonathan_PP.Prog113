

def obtener_path_actual(nombre_archivo: str) -> str:
    """
    Obtiene la ruta del directorio actual.

    Parámetros:
    nombre_archivo (str): El nombre del archivo.

    Retorna:
    str: La ruta completa del archivo.
    """
    import os

    path = os.path.dirname(__file__)
    return os.path.join(path, nombre_archivo)


import random

 
def leer_archivo_csv(nombre_archivo) :
    """
    Lee un archivo CSV y devuelve una lista de diccionarios representando los datos.

    Parámetros:
    nombre_archivo (str): El nombre del archivo CSV.

    Retorna:
    list: Una lista de diccionarios representando los datos del archivo CSV.
    """
   
    with open(obtener_path_actual(nombre_archivo),"r", encoding="utf-8") as archivo:
        lista = []
        encabezado = archivo.readline().split(",")
        print(encabezado)
        # encabezado = encabezado.split(",")
        # print(encabezado)
        lineas = archivo.readlines()
        modificar_archivos(lineas, lista)
    return lista

def modificar_archivos(lineas: list, listas: list) -> None:    
    """
    Modifica las líneas del archivo y las convierte en diccionarios.

    Parámetros:
    lineas (list): Las líneas del archivo CSV.
    listas (list): La lista para almacenar los diccionarios.

    """

    for linea in lineas:
        datos_bike = {}
        linea = linea.strip("\n").split(",")

        id_bike, nombre, tipo, tiempo = linea

        datos_bike["id_bike"] = int(id_bike)
        datos_bike["nombre"] = nombre
        datos_bike["tipo"] = tipo
        datos_bike["tiempo"] = int(tiempo)

        
        datos_bike["tiempo"] = random.randint(50, 120)
        listas.append(datos_bike)




def tiempo_aleatorio(lista):
    """
    Asigna tiempos aleatorios entre 50 y 120 a cada elemento de la lista.

    Parámetros:
    lista (list): Una lista de diccionarios representando datos.

    """
    for campo in lista:
        campo["tiempo"] = random.randint(50, 120)
        print(campo)


def mostrar_datos(lista):
    """
    Muestra los datos de cada elemento en la lista.

    Parámetros:
    lista (list): Una lista de diccionarios representando datos.

    """
    for datos in lista:
        print(datos)


def mapear_campo(lista: list, campo: str):
    """
    Mapea un campo específico de cada elemento en la lista y devuelve una lista con los valores del campo.

    Parámetros:
    lista (list): Una lista de diccionarios representando datos.
    campo (str): El nombre del campo que se desea mapear.

    Retorna:
    list: Una lista con los valores del campo especificado.
    """
    lista_retorno = []
    for el in lista:
        lista_retorno.append(el[campo])
    return lista_retorno


def calcular_menor(lista: list):
    """
    Calcula el valor mínimo en una lista de números.

    Parámetros:
    lista (list): Una lista de números.

    Retorna:
    float or int: El valor mínimo en la lista.
    """
    menor = lista[0]
    for i in range(1, len(lista)):
        if lista[i] < menor:
            menor = lista[i]
    return menor


def mapear_tiempo(lista, campo):
    """
    Mapea el campo de tiempo de cada elemento en la lista y encuentra el que tiene el menor tiempo.

    Parámetros:
    lista (list): Una lista de diccionarios representando datos.
    campo (str): El nombre del campo que se desea mapear y encontrar el menor valor.

    """
    tiempo = mapear_campo(lista, campo)
    menortiempo = calcular_menor(tiempo)

    for empleado in lista:
        if empleado[campo] == menortiempo:
            print(f"El empleado que llegó en menor tiempo es: {empleado['nombre']}, con: {empleado[campo]}, ")

def filtrar_lista(funcion, lista):
    lista_retorno= []
    for el in lista:
        if funcion(el):
            lista_retorno.append(el)
    return lista_retorno

def pedir_bici(lista,campo):
    aux = input("ingrese un tipo de bicicleta (bmx, playera, mtb, paseo) ").strip().lower()
    
    filtrar = [datos for datos in lista if datos[campo].strip().lower() == aux]
    
    if filtrar == "":
        print(f"No se encontraron bicicletas del tipo '{aux}'.")

    for datos in filtrar:
        print(datos)

    return filtrar



def pasar_achivo_csv(nombre_archivo: str, lista: list) -> None:
    """
    Escribe una lista de diccionarios en un archivo CSV.

    Parámetros:
    nombre_archivo (str): El nombre del archivo CSV.
    lista (list): La lista de diccionarios a escribir en el archivo.

    Retorna:
    None
    """
    with open(obtener_path_actual(nombre_archivo), "w", encoding="utf-8") as archivo:
        encabezado = ",".join(list(lista[0].keys())) + "\n"
        archivo.write(encabezado)

        for persona in lista:
            l = []
            values = list(persona.values())
            for value in values:
                if isinstance(value, int):
                    l.append(str(value))
                elif isinstance(value, float):
                    l.append(str(value))
                else:
                    l.append(value)

            linea = ",".join(l) + "\n"
            archivo.write(linea)

     

def totalizarLista(lista:list):
    total = 0
    for valor in lista:
        total += valor

    return  total
     
def calcular_promedio(lista: list):
    """
    Calcula el promedio de los elementos en la lista.

    Parámetros:
    lista (list): La lista cuyos elementos se promediarán.

    Retorna:
    float: El promedio de los elementos en la lista.
    """
def CalcularPromedio(lista:list):
    if isinstance(lista, list):
        cant = len(lista)
        if cant == 0:
            raise ValueError ("no esta definido el priomedio en una lista vacia")
        
        return totalizarLista(lista) / cant  
    raise ValueError ("no es una lista")

def promediar_tiempo(lista: list, campo_uno, campo_dos):
    """
    Calcula el promedio de la altura de los héroes de un género específico.

    Parámetros:
    lista (list): La lista de datos que contiene los héroes.
    campo_uno (str): El campo específico que se utilizará para determinar la altura.
    campo_dos (str): El campo específico que se utilizará para filtrar los héroes.
    genero: El género de los héroes para el cual se calculará el promedio de la altura.

    """
    if not isinstance(lista, list):
        raise TypeError("El argumento 'lista' debe ser una lista.")
    prom_lista = []
    for dato in lista:
        if dato[campo_dos] :        
            altura = float(dato[campo_uno])
            prom_lista.append(altura)
    
    print(f"El promedio es: {CalcularPromedio(prom_lista):00.4}")

def swap_lista(lista:list, i, j):
    aux = lista[i]
    lista[i] = lista[j]
    lista[j] = aux

    
def ordenar_doble_criterio(lista:list,campo_uno,campo_dos):
    tam = len(lista)
    for i in range (tam - 1):
        for j in range (i + 1, tam):
            if lista[i][campo_uno] == lista[j][campo_uno]:
               if lista[i][campo_dos] > lista[j][campo_dos]:
                    swap_lista(lista,i,j)

            elif lista[i][campo_uno] > lista[j][campo_uno]:
                    swap_lista(lista,i,j)

    