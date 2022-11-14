"""
Universidad del Valle de Guatemala
Teoría de La computación
Corto 3
Jorge Caballeros
Alejandra Guzmán 
Pablo Escobar
"""
import time


# Ejercicio 5
# Eliminar los elementos de una lista y agregarlos a otra mediante funciones lambda

# Mismas listas para cada una de las funciones
list1 = ["rojo", "verde", "azul", "amarillo", "gris", "blanco", "negro"]
delList = ["amarillo", "cafe", "blanco"]

print("\n\nLista Original:                ", list1)
print("Lista de elementos a eliminar: ", delList, "\n\n")

# Programa SIN funciones lambda


def nonLambdaFunc(originalList: list, delList: list):
    for i in originalList:
        if (i in delList):
            originalList.remove(i)

    return originalList


# No usando lambda
noLambda_time = time.time()
print("-> Resultado de la función NO LAMBDA:\n"
      + "---------------------------------------------\n" +
      str(nonLambdaFunc(list1, delList))
      + "\n---------------------------------------------\n" +
      "-> Tiempo de ejecución sin utilizar lambda:"
      )
print(str(time.time()-noLambda_time), "\n\n\n")


lambda_time = time.time()
listDeleter = list(filter(lambda item: item not in delList, list1))
print("-> Resultado con LAMBDA:\n"
      + "---------------------------------------------\n" +
      str(listDeleter)
      + "\n---------------------------------------------\n" +
      "-> Tiempo de ejecución sin utilizar lambda:")
print("Tiempo de ejecución utilizando funciones lambda , \n" +
      str(time.time()-lambda_time), "\n\n\n")
