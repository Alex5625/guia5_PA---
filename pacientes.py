class Pacientes():

    def __init__(self):
        self.__nombre = ""
        self.__edad = ""
        self.__genero = ""
        self.__antecedentes_medicos = []
        self.__historial_atencion = {
            "Fecha":"", 
            "Motivo_atencion":[],  
            "Diagnostico" : "",
            "Recomendacion": ""
        }


# ---------------------set-------------------------

    def set_nombre(self,nombre):
        self.__nombre = nombre

    def set_edad(self,edad):
        if isinstance(edad,str):
            self.__edad = edad


    def set_genero(self,genero):
        
        if isinstance(genero,str):

            self.__genero = genero


    def set_antecedentes(self,lista):
        if isinstance(lista,list):
            self.__antecedentes_medicos = lista

    
    def set_historial(self,fecha, motivoAtencion, diagnostico, recomendacion):

# sigue el siguiente modelo

        if isinstance(fecha,str):

            self.__historial_atencion.update({"Fecha":fecha})

        if isinstance(motivoAtencion,list):
            
            self.__historial_atencion.update({"Motivo_atencion":motivoAtencion})

        if isinstance(diagnostico,str):

            self.__historial_atencion.update({"Diagnostico":diagnostico})

        if isinstance(recomendacion,str):

            self.__historial_atencion.update({"Recomendacion": recomendacion})

        pass
        


# ---------------------set-------------------------




# ---------------------get-------------------------
    def get_nombre(self):
        return self.__nombre
    

    def get_edad(self):
        return self.__edad
    

    def get_genero(self):
        return self.__genero
    

    def get_antecedentes_medicos(self):
        return self.__antecedentes_medicos

    
    def get_historial(self):
        return self.__historial_atencion
# ---------------------get-------------------------
