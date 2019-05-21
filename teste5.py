def main():
    minutos=int(input("Quantos minutos voce utilizou este mes:"))
    if minutos < 200:
        preco = 0.20
    else:
        if minutos < 400:
            preco = 0.18
        else:
            preco = 0.15
    print("Voce vai pagar este mes: R$%6.2f" %(minutos * preco))
main()
