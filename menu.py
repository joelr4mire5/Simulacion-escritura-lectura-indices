
import random
import functions
from Producto import Producto
import os
from datetime import datetime
import pandas as pd


start_time = []
end_time = []

def menu():
    print("Seleccione una opcion del siguiente menu")
    print("Seleccione 1 para Generar un archivo")
    print("Seleccione 2 para buscar un registro")
    print("Presione cualquier otra tecla para salir")

    opcion= input("Seleccione una opción del ménu anterior: ")

    if opcion=="1":
        nombrearchivo= input("Como desea llamar al archivo: ")
        path = os.getcwd()+"/"+nombrearchivo + ".dbf"
        print("¿Cuantos registros desea guardar?")
        print("1. 10000 registros")
        print("2. 15000 registros")
        print("3. 25000 registros")
        print("4. 50000 registros")
        print("presione cualquier otra tecla para volver al menu principal")
        print("***********************************************************")

        opcionregistros= input("seleccione una opción del ménu anterior: ")

        # Product Names
        nombres_productos = ["Widget A", "Gadget B", "Thingamajig C", "Doodad X", "Whatchamacallit Y", "Contraption Z"]

        # Product Codes
        codigos_productos = ["P001", "P002", "P003", "P004", "P005", "P006"]

        # Unitary Weights (in kg)
        pesos_unitarios = [random.uniform(0.1, 5.0) for _ in range(6)]

        # Providers
        proveedores = ["Supplier1", "Vendor2", "Manufacturer3", "Distributor4", "Importer5", "Wholesaler6"]



        if opcionregistros=="1":
            functions.writing_file(10000,path,nombres_productos,codigos_productos,pesos_unitarios,proveedores,Producto)
            print("Regresando al menu principal")
            menu()

        elif opcionregistros=="2":
            functions.writing_file(15000,path,nombres_productos,codigos_productos,pesos_unitarios,proveedores,Producto)
            print("Regresando al menu principal")
            menu()
        elif opcionregistros=="3":
            functions.writing_file(25000,path,nombres_productos,codigos_productos,pesos_unitarios,proveedores,Producto)
            print("Regresando al menu principal")
            menu()
        elif opcionregistros=="4":
            functions.writing_file(50000,path,nombres_productos,codigos_productos,pesos_unitarios,proveedores,Producto)
            print("Regresando al menu principal")
            menu()
        else:
            print("Regresando al menu principal")
            menu()

    elif opcion=="2":
        lista_archivos=functions.obtener_archivos_dbf(os.getcwd(),".dbf")
        lista_archivos_indice=functions.obtener_archivos_dbf(os.getcwd(),".idx")

        if len(lista_archivos)==0:
            print("No hay archivos .dbf, volviendo al menu principal")
            menu()
        elif len(lista_archivos)!=0:
            print("Seleccione un archivo para buscar un registro")
            number = 0
            for i in lista_archivos:

                print(str(number) + ": " + i)
                number+=1
            archivo_seleccionado= int(input("Porfavor seleccione el archivo que desea abrir para buscar un registro con un numero de la lista anterior: "))

            if archivo_seleccionado>=len(lista_archivos):
                print("Por favor intente una opcion valida")
                print("Volviendo al ménu principal")
                menu()
            elif archivo_seleccionado>=0 and archivo_seleccionado <=len(lista_archivos):
                path_archivo_seleccionado=lista_archivos[archivo_seleccionado]
                registro_seleccionado=int(input("Porfavor seleccione el registro que desea buscar: "))
                if registro_seleccionado>functions.count_records(path_archivo_seleccionado):
                    print(f"El archivo seleccionado solo posee {functions.count_records(path_archivo_seleccionado)} registros por lo tanto el numero seleccionado está fuera del rango")
                    print("Volviendo al menu principal")
                    menu()
                elif registro_seleccionado>=0 and registro_seleccionado <= functions.count_records(path_archivo_seleccionado):
                    path_archivo_seleccionado_indice=path_archivo_seleccionado[:-4]+".idx"
                    print(path_archivo_seleccionado_indice)


                    start_time.append(datetime.utcnow())


                    functions.search_by_index(path_archivo_seleccionado_indice,path_archivo_seleccionado,registro_seleccionado)

                    end_time.append(datetime.utcnow())

                    print(f"La busqueda del registro número {registro_seleccionado} ha terminado")
                    menu()
            else:
                print("Opción invalida... volviendo al menu principal")
                menu()



    else:

        df = pd.DataFrame({'start_time': start_time, 'end_time': end_time})
        df['Duration'] = df['end_time'] - df['start_time']
        df.to_csv("time_data/time.csv")
        print("saliendo del programa........")


















menu()