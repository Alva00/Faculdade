def e_par(ticket):
    if ticket % 2 == 0:
        print("Válido.")
    else:
        print("Inválido.")

def main():
    while True:
        try:
            ticket = int(input("Insira o número do ticket:\n"))
            e_par(ticket)
            break
        except ValueError:
            print("Insira um número inteiro válido.")

if __name__ == "__main__":
    main()
