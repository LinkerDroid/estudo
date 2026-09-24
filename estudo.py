lista = ["1 - Soma", "2 - Subtração", "3 - Multiplicação", "4 - Divisão"]

while True:
     print("\n--- MENU PRINCIPAL ---")

     
     print("\n".join([f"{item.upper()}" for item in lista]))
     try:
        escolha = int(input("\nEscolha uma opção: "))
        if escolha == 1: 
          numero1 = int(input("Digite um número: "))
          numero2 = int(input("Digite outro número: "))
          resultado = lambda x, y: x + y
          print(resultado(numero1, numero2))

        elif escolha == 2:
               numero1 = int(input("Digite um número: "))
               numero2 = int(input("Digite outro número: "))
               resultado = lambda x, y: x - y
               print(resultado(numero1, numero2))

        elif escolha == 3:
               numero1 = int(input("Digite um número: "))
               numero2 = int(input("Digite outro número: "))
               resultado = lambda x, y: x * y
               print(resultado(numero1, numero2)) 

        elif escolha == 4:
               numero1 = int(input("Digite um número: "))
               numero2 = int(input("Digite outro número: "))
               resultado = lambda x, y: x / y
               print(resultado(numero1, numero2))
            
     except ValueError:
        print("Ops! Você precisa digitar um número inteiro válido.")
     except ZeroDivisionError:
        print("Ops! Não é possível dividir um número por zero.")


    
     



    




 
