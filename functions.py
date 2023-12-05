
import random
import pickle
import os

import pandas as pd

def choose_random_value(mi_lista):

    if not mi_lista:
        return None
    else:
        return random.choice(mi_lista)

def obtener_archivos_dbf(path,extension):

    todos_los_archivos = os.listdir(path)
    archivos_dbf = [archivo for archivo in todos_los_archivos if archivo.lower().endswith(extension)]


    return archivos_dbf

def writing_file(cantidad_registros, nombre_archivo,lista_nombres,lista_codigos,lista_pesos,lista_proveedores,objeto):
    indexlist=[]
    with open(nombre_archivo,"wb") as F:
        for i in range(0, cantidad_registros):
            nombre = choose_random_value(lista_nombres)
            codigo_producto = choose_random_value(lista_codigos)
            pesos_unitarios = choose_random_value(lista_pesos)
            proveedores = choose_random_value(lista_proveedores)
            producto=objeto(nombre, codigo_producto, pesos_unitarios, proveedores)
            pickle.dump(producto, F)
            indexlist.append(F.tell())
    with open(f"{nombre_archivo[:len(nombre_archivo)-4]}.idx","wb") as index_file:
        pickle.dump(indexlist,index_file)


    print(f"Se han escrito {cantidad_registros} de registros en el archivo: {nombre_archivo}")







def leer_archivo(path_archivo,registro_buscado):

    with open(path_archivo, "rb") as archivo:
        count=0

        while count <= registro_buscado:
            try:
                objeto = pickle.load(archivo)
                print(objeto)
                count += 1
            except EOFError:
                break  # Reached the end of the file






def count_records(file_path):
    try:
        with open(file_path, "rb") as file:
            count = 0
            while True:
                # Attempt to load an object from the file
                try:
                    pickle.load(file)
                    count += 1
                except EOFError:
                    break  # Reached the end of the file
    except FileNotFoundError:
        count = 0  # File doesn't exist

    return count


def search_by_index(idx_file, nombre_archivo, index):
    with open(idx_file, "rb") as index_file:
        indices = pickle.load(index_file)

    with open(nombre_archivo, "rb") as data_file:
        data_file.seek(indices[index])
        producto = pickle.load(data_file)
        print(producto)

    return producto