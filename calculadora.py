import tkinter as tk
from tkinter import messagebox

interface = tk.Tk()  # Criação da janela principal
interface.title("Calculadora")

display = tk.Entry(interface, width=20, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")  # Exibição dos números, utilizando o método Entry
display.grid(row=0, column=0, columnspan=4)

numeros = [('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
           ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
           ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
           ('0', 4, 1)]  # Lista com números

numeros_digitados = []  # Lista para armazenar os números digitados

# Função para inserir números
def inserir_numero(numero):
    valor_atual = display.get()  # Pega o valor atual no display
    display.delete(0, tk.END)  # Limpa o display
    display.insert(tk.END, valor_atual + str(numero))  # Adiciona o número clicado
    numeros_digitados.append(str(numero))  # Armazena o número digitado

# Botões numéricos
for (text, row, col) in numeros:  # Percorre os números da lista
    tk.Button(interface, text=text, width=5, height=2, font=("Arial", 18), command=lambda t=text: inserir_numero(t)).grid(row=row, column=col)

# Funções para operações básicas
def limpar():
    display.delete(0, tk.END)

def adicionar():
    global operador, valor_armazenado
    valor_armazenado = float(display.get())
    operador = "adicao"
    limpar()

def subtrair():
    global operador, valor_armazenado
    valor_armazenado = float(display.get())
    operador = "subtracao"
    limpar()

def multiplicar():
    global operador, valor_armazenado
    valor_armazenado = float(display.get())
    operador = "multiplicacao"
    limpar()

def dividir():
    global operador, valor_armazenado
    valor_armazenado = float(display.get())
    operador = "divisao"
    limpar()

# Botões de operações
tk.Button(interface, text='+', width=5, height=2, font=("Arial", 18), command=adicionar).grid(row=1, column=3)
tk.Button(interface, text='-', width=5, height=2, font=("Arial", 18), command=subtrair).grid(row=2, column=3)
tk.Button(interface, text='*', width=5, height=2, font=("Arial", 18), command=multiplicar).grid(row=3, column=3)
tk.Button(interface, text='/', width=5, height=2, font=("Arial", 18), command=dividir).grid(row=4, column=3)

# Função para calcular o resultado
def calcular():
    global operador, valor_armazenado
    segundo_valor = float(display.get())  # Pega o segundo número

    if operador == "adicao":
        resultado = valor_armazenado + segundo_valor
    elif operador == "subtracao":
        resultado = valor_armazenado - segundo_valor
    elif operador == "multiplicacao":
        resultado = valor_armazenado * segundo_valor
    elif operador == "divisao":
        if segundo_valor != 0:
            resultado = valor_armazenado / segundo_valor
        else:
            messagebox.showerror("Erro", "Divisão por zero!")
            return
    limpar()  # Limpa o display
    display.insert(tk.END, str(resultado))  # Mostra o resultado no display

# Botão de igual
tk.Button(interface, text='=', width=5, height=2, font=("Arial", 18), command=calcular).grid(row=4, column=2)


# Iniciar a interface
interface.mainloop()
