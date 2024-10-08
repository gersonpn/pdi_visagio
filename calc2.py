import tkinter as tk

interface = tk.Tk()
interface.title("Calculadora")

display = tk.Entry(interface, width=20, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
display.grid(row=0, column=0, columnspan=4)

class Calculadora:
    def __init__(self):
        self.n1 = 0
        self.n2 = 0
        self.operador = None

    def limpar(self):
        display.delete(0, tk.END)
        return

    def digitar(self, valor):
        display.insert(tk.END, valor)
        return

    def capturar_primeiro_numero(self, operador):
        self.n1 = float(display.get())
        self.operador = operador
        self.limpar()
        return self.n1, self.operador

    def capturar_segundo_numero(self):
        self.n2 = float(display.get())
        self.limpar()
        return self.n2

    def adicionar(self):
        resultado = self.n1 + self.n2
        display.insert(tk.END, str(resultado))
        return resultado

    def subtrair(self):
        resultado = self.n1 - self.n2
        display.insert(tk.END, str(resultado))
        return resultado

    def multiplicar(self):
        resultado = self.n1 * self.n2
        display.insert(tk.END, str(resultado))
        return resultado

    def dividir(self):
        if self.n2 != 0:
            resultado = self.n1 / self.n2
        else:
            resultado = "Erro"
        display.insert(tk.END, str(resultado))
        return resultado


    def elevar(self):
        resultado = self.n1 ** self.n2
        self.limpar()
        display.insert(tk.END, str(resultado))
        return resultado

calc = Calculadora()


buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
    ('0', 4, 0),
    ('C', 4, 1), ('=', 4, 2),
    ('+', 1, 3), ('-', 2, 3),
    ('*', 3, 3), ('/', 4, 3)
]

for (text, row, col) in buttons:
    if text == '=':
        tk.Button(interface, text=text, command=lambda: (calc.adicionar() if calc.operador == '+' else calc.subtrair() if calc.operador == '-' else calc.multiplicar() if calc.operador == '*' else calc.dividir() if calc.operador == '/' else None)).grid(row=row, column=col)
    elif text == 'C':
        tk.Button(interface, text=text, command=calc.limpar).grid(row=row, column=col)
    elif text in ['+', '-', '*', '/', '&']:
        tk.Button(interface, text=text, command=lambda op=text: calc.capturar_primeiro_numero(op)).grid(row=row, column=col)
    else:
        tk.Button(interface, text=text, command=lambda val=text: calc.digitar(val)).grid(row=row, column=col)

for i in range(4):
    interface.grid_columnconfigure(i, weight=1)

interface.mainloop()
