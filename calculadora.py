import tkinter as tk

janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("600x200+40+40") # Tamanho da janela

lblMsg = tk.Label(janela, text="Teste")
lblMsg.pack()

janela.mainloop # Exibição

def menu():
    print("\nEscolha uma operação:")
    print("1. Adicionar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Sair")

class Calculadora:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def adicao(self):
        return self.a + self.b

    def subt(self):
        return self.a - self.b

    def mult(self):
        return self.a * self.b

    def div(self):
        if self.b == 0:
            return "Erro: divisão por zero"
        return self.a / self.b


def calculo():

  a = float(input("Digite o primeiro número: "))
  b = float(input("Digite o segundo número: "))
  calc = Calculadora(a,b)

  while True:
    menu()
    opcao = input ("Digite o número da operação desejada: ")

    if opcao == '5':
      print("Você saiu.")
      break
    if opcao == '1':
        print(f"Resultado da Adição: {calc.adicao()}")
    elif opcao == '2':
        print(f"Resultado da Subtração: {calc.subt()}")
    elif opcao == '3':
        print(f"Resultado da Multiplicação: {calc.mult()}")
    elif opcao == '4':
        print(f"Resultado da Divisão: {calc.div()}")
    else:
        print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    calculo()