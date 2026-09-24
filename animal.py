class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def emitir_som(self):
        return (f"O {self.nome} está emitindo um som genérico.")

class cachorro(Animal):
    def emitir_som(self):
        print(f"O {self.nome} latiu!")
class gato(Animal):
    def emitir_som(self):
        return (f"O {self.nome} miou!")

cachorrinho = cachorro("Rex", 3)
gatinho = gato("Mia", 2)

cachorrinho.emitir_som()
gatinho.emitir_som()




