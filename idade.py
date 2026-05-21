def idade(x):
    return 2026-x
if __name__ == '__main__':
    nascimento=int(input("Informe o ano de nascimento    : "))
    y=idade(nascimento)
    print("A idade é igual a ",y)