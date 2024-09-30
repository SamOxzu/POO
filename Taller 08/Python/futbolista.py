from deportista import Deportista

class Futbolista(Deportista):
    def __init__(self, nombre, edad, altura, sexo, años_practicando, goles_marcados, tarjetas_rojas, pierna_habil):
        super().__init__(nombre, edad, altura, sexo, "Futbol", años_practicando)
        self.__goles_marcados = goles_marcados
        self.__tarjetas_rojas = tarjetas_rojas
        self.__pierna_habil = pierna_habil
    
    def getGolesMarcados(self):
        return self.__goles_marcados

    def set_goles_marcados(self, goles_marcados):
        self.__goles_marcados = goles_marcados

    def getTarjetasRojas(self):
        return self.__tarjetas_rojas

    def set_tarjetas_rojas(self, tarjetas_rojas):
        self.__tarjetas_rojas = tarjetas_rojas

    def getPiernaHabil(self):
        return self.__pierna_habil

    def set_pierna_habil(self, pierna_habil):
        self.__pierna_habil = pierna_habil

    def __str__(self) -> str:
        #"Mi nombre es Juan Pablo soy profesional en el deporte Futbol Tengo 30 años de edad y llevo 12 años en el deporte"
        return f"Mi nombre es {self.getNombre()} soy profesional en el deporte Futbol Tengo {self.getEdad()} años de edad y llevo {self.getAñosPracticando()} años en el deporte"
