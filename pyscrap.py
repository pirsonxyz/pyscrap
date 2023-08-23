import requests
from bs4 import BeautifulSoup

print(f"Creado por Pirson\n")

inicio = int(input("1 para analizar, ctrl + c para salir:"))

def scrap():
    url = input("introduce el url que quieres analizar: ")

    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")
    print(doc.prettify())

    opcion = int(input("Deseas guardar el archivo? 1/0: \n"))

    if opcion == 1:
        nombre = input("Introduce el nombre que deseas ponerle\n")
        with open(nombre, "w") as file:
            file.write(str(doc.prettify()))
        print(f"el archivo se ha guardado correctamente!")
    else:
        print("Adios!")

while inicio == 1:
    scrap()
