import json
import random
from pacientes import Pacientes

FILENAME_SINTOMAS = "./archivos/virus_sintomas.json"
FILENAME_ENFERMEDADES = "./archivos/virus_estacionales.txt"



def open_file_json(filename):
    """ Procesa un archivo de texto json y
    retorna un diccionario"""
    with open(filename) as texto:
        new_dict = json.load(texto)
    return new_dict


def crea_lista_sintomas():
    datos = open_file_json(FILENAME_SINTOMAS)
    # print(datos)
    datos = datos.get("virus_sintomas")
    lista_sintomas = []


    for item in datos:
        # print(item.get("sintomas"))
        for sintoma in item.get("sintomas"):

            #PARA CREAR LA LISTA DE SINTOMAS NO REPETIDA
            if not lista_sintomas:
                lista_sintomas.append(sintoma)
            else:
                if sintoma not in lista_sintomas:
                    lista_sintomas.append(sintoma)
        pass
    # print(lista_sintomas)
    return lista_sintomas




def asoocia_sintomas_pacientes(sintomas=None):

    sintomas_asociados = []

    sintomas_agregados = set()  # Conjunto para almacenar los síntomas agregados a este paciente
    for i in range(0, random.randint(3, 7)):
        temp = sintomas[random.randint(0, len(sintomas) - 1)]

        while temp in sintomas_agregados:  # Verificar si el síntoma ya ha sido agregado
            temp = sintomas[random.randint(0, len(sintomas) - 1)]

        sintomas_asociados.append(temp)
        sintomas_agregados.add(temp)  # Agregar el síntoma al conjunto

    # print(f"{sintomas_asociados}")
    return sintomas_asociados


if __name__ == "__main__":


    alexis = Pacientes()
    lista_sintomas = crea_lista_sintomas()

    #leo diccionario e ingreso a una variable con una lista, los sintomas que se agregaran al nuevo diccionario
    sintomas_paciente = asoocia_sintomas_pacientes(sintomas = lista_sintomas)

    # print(alexis.get_historial())
    alexis.set_nombre("Alexis Hernandez")
    alexis.set_edad(str(random.randint(20,54)))
    alexis.set_genero("Hombre")
    alexis.set_antecedentes(["---------"])
    alexis.set_historial("15-04-2024",sintomas_paciente,"dolor de estomago","sana sana colita de rana, si no sana hoy sanara mañana")



    print(alexis.get_nombre())
    print(alexis.get_edad())
    print(alexis.get_genero()) 
    print(f"Sus antecedentes son: {alexis.get_antecedentes_medicos()}")
    print(alexis.get_historial())

    pass



