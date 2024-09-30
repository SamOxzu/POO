class TV:
    num_tv = 0

    def __init__(self, marca, estado):
        TV.num_tv += 1
        self.marca = marca
        self.estado = estado
        self.canal = 1
        self.precio = 500
        self.volumen = 1
        self.control = None

    def volumen_up(self):
        if self.estado and self.volumen < 7:
            self.volumen += 1

    def canal_up(self):
        if self.estado and self.canal < 120:
            self.canal += 1

    def volumen_down(self):
        if self.estado and self.volumen > 0:
            self.volumen -= 1

    def canal_down(self):
        if self.estado and self.canal > 1:
            self.canal -= 1

    def turn_on(self):
        self.estado = True

    def turn_off(self):
        self.estado = False

    @staticmethod
    def get_num_tv():
        return TV.num_tv

    @staticmethod
    def set_num_tv(num_tv):
        TV.num_tv = num_tv

    def get_marca(self):
        return self.marca

    def set_marca(self, marca):
        self.marca = marca

    def get_canal(self):
        return self.canal

    def set_canal(self, canal):
        if 1 <= canal <= 120:
            self.canal = canal

    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio

    def get_volumen(self):
        return self.volumen

    def set_volumen(self, volumen):
        if 0 <= volumen <= 7:
            self.volumen = volumen

    def get_control(self):
        return self.control

    def set_control(self, control):
        self.control = control
