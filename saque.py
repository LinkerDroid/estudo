class ContaBancaria:

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def Sacar(self, valor):

        self.saldo -= valor    

    def exibir_saldo(self):
        print(f"Saldo atual de {self.titular}: R${self.saldo:.2f}")

class ContaPoupanca(ContaBancaria):
    def __init__(self, titular, saldo, taxa_juros):
        super().__init__(titular, saldo)
        self.taxa_juros = taxa_juros

    def Sacar(self, valor):
        super().Sacar(valor)
        self.saldo -= 2

    def render_juros(self):
      juros = self.saldo * self.taxa_juros
      self.saldo += juros
      print(f"Juros de R${juros:.2f} aplicados. Novo saldo: R${self.saldo:.2f}") 

