from funciones import *


lista_bike = leer_archivo_csv("bicicletas.csv")

while True:
    respuesta = int(input("1.Cargar archivo .CSV\n2.mprimir listar\n3.Asignar tiempos\n4.nformar ganador\n5.Filtrar por tipo y subir a un csv\n6.\n7.ordenar por tipo y por asc\n8.Guardar posiciones\n9.salir elija una opcion:"))
    
    match respuesta:
        case 1:
            lista_bike = leer_archivo_csv("bicicletas.csv")
            print("---------------------------------------------")
        case 2:
            mostrar_datos(lista_bike)
           
            print("---------------------------------------------")
        case 3:
            tiempo_aleatorio(lista_bike)
            
            print("---------------------------------------------")
        case 4:
            mapear_tiempo(lista_bike,"tiempo")

            print("---------------------------------------------")
        case 5:
            aux = pedir_bici(lista_bike,"tipo")
            pasar_achivo_csv("bici_selecionado.csv",aux)
            print("---------------------------------------------")
        case 6:
            promediar_tiempo(lista_bike,"tiempo","tipo")
            print("---------------------------------------------")
        case 7:
            ordenar_doble_criterio(lista_bike,"tipo","tiempo")
            mostrar_datos(lista_bike)

            print("---------------------------------------------")
        case 8:
            pasar_achivo_csv("bicis_ordenados.csv",ordenar_doble_criterio(lista_bike,"tipo","tiempo"))

            print("---------------------------------------------")
        case 9:
            break
