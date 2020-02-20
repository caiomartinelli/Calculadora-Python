#TEXT INPUTS

#selecionar a operação

def calculadora():

    operacao = int(input("Selecione a operação: soma=1, subtracao=2, Multiplicacao=3, Divisao=4 "))

    primeiro = int(input("primeiro numero: "))

    segundo = int(input("segundo numero: "))


    if operacao == 1:
        primeiro + segundo
        print(primeiro + segundo)
    elif operacao ==2:
        primeiro - segundo
        print(primeiro - segundo)
    elif operacao ==3:
        primeiro * segundo
        print(primeiro * segundo)
    elif operacao ==4:
        primeiro / segundo
        print(primeiro / segundo)
    
calculadora()

    