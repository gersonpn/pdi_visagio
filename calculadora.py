class Calculadora:
  
  def __init__(self):
    self.resultado = 0

    def adicao(self,valor):
      self.resultado += valor

    def subtracao(self,valor):
      self.resultado -= valor

    def mult(self,valor):
      self.resultado *= valor

    def divisao(self,valor):
      self.resultado /= valor

    def resultado(self):
      return self.resultado
