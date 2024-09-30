class Persona:
    def __init__(self, nombre, edad, altura, sexo):
        self.__nombre = nombre
        self.__edad = edad
        self.__altura = altura
        self.__sexo = sexo

    def getNombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def getEdad(self):
        return self.__edad

    def set_edad(self, edad):
        self.__edad = edad

    def getAltura(self):
        return self.__altura

    def set_altura(self, altura):
        self.__altura = altura

    def getSexo(self):
        return self.__sexo

    def set_sexo(self, sexo):
        self.__sexo = sexo
