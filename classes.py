#classe pai (superclasse)
class Nova_classe:
    def __init__(self, nome,):
       self.nome = nome

    def mostrar_nome(self):
        print(f"Nome: {self.nome}")

#classe filha (subclasse)
class pessoa(Nova_classe):
    def comer(self):
        print(f"{self.nome} está comendo.")

humano = pessoa ("João")

humano.mostrar_nome()
humano.comer()



