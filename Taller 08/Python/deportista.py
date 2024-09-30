from persona import Persona

class Deportista(Persona):
    def __init__(self, nombre, edad, altura, sexo, deporte, años_practicando):
        super().__init__(nombre, edad, altura, sexo)
        self.__deporte = deporte
        self.__años_practicando = años_practicando

    def getDeporte(self):
        return self.__deporte

    def set_deporte(self, deporte):
        self.__deporte = deporte

    def getAñosPracticando(self):
        return self.__años_practicando

    def set_años_practicando(self, años_practicando):
        self.__años_practicando = años_practicando

