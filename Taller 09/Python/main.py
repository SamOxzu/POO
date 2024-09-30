from tkinter import Tk, Button, Entry

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.pantalla = Entry(root, width=21, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"))
        self.pantalla.grid(row=0, column=0, columnspan=4, padx=1, pady=1)
        self.operador = ""
        self.temp_num = ""
        self.resultado = ""
        self.nueva_operacion = True

    def click(self, valor):
        if self.nueva_operacion:
            self.temp_num = str(valor)
            self.nueva_operacion = False
        else:
            self.temp_num += str(valor)
        self.pantalla.delete(0, "end")
        self.pantalla.insert(0, self.temp_num)

    def igual(self):
        if self.operador == "+":
            self.resultado = float(self.resultado) + float(self.temp_num)
        elif self.operador == "-":
            self.resultado = float(self.resultado) - float(self.temp_num)
        elif self.operador == "*":
            self.resultado = float(self.resultado) * float(self.temp_num)
        elif self.operador == "/":
            self.resultado = float(self.resultado) / float(self.temp_num)

        self.pantalla.delete(0, "end")
        self.pantalla.insert(0, self.resultado)
        self.operador = ""
        self.temp_num = str(self.resultado)
        self.nueva_operacion = True

    def operacion(self, operador):
        if self.operador != "":
            self.igual()
        self.operador = operador
        self.resultado = self.temp_num
        self.temp_num = ""
        self.nueva_operacion = False

root = Tk()
root.title("Calculadora POO")
root.resizable(0,0)
root.geometry("")

calc = Calculadora(root)

# Configuración botones
Button(root, text="1", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: calc.click(1)).grid(row=1, column=0, padx=1, pady=1)
Button(root, text="2", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: calc.click(2)).grid(row=1, column=1, padx=1, pady=1)
Button(root, text="3", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: calc.click(3)).grid(row=1, column=2, padx=1, pady=1)
Button(root, text="4", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: calc.click(4)).grid(row=2, column=0, padx=1, pady=1)
Button(root, text="5", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: calc.click(5)).grid(row=2, column=1, padx=1, pady=1)
Button(root, text="6", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: calc.click(6)).grid(row=2, column=2, padx=1, pady=1)
Button(root, text="7", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: calc.click(7)).grid(row=3, column=0, padx=1, pady=1)
Button(root, text="8", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: calc.click(8)).grid(row=3, column=1, padx=1, pady=1)
Button(root, text="9", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: calc.click(9)).grid(row=3, column=2, padx=1, pady=1)
Button(root, text="=", width=20, height=3, bg="red", fg="white", borderwidth=0, cursor=" hand2", command=lambda: calc.igual()).grid(row=4, column=0, columnspan=2, padx=1, pady=0)
Button(root, text=".", width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0, command=lambda: calc.click(".")).grid(row=4, column=2, padx=1, pady=1)
Button(root, text="+", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=lambda: calc.operacion("+")).grid(row=1, column=3, padx=1, pady=1)
Button(root, text="-", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=lambda: calc.operacion("-")).grid(row=2, column=3, padx=1, pady=1)
Button(root, text="*",  width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=lambda: calc.operacion("*")).grid(row=3, column=3, padx=1, pady=1)
Button(root, text="/", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=lambda: calc.operacion("/")).grid(row=4, column=3, padx=1, pady=1)

root.mainloop()
