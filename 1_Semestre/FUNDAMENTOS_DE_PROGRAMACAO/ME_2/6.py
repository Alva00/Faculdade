def soma():
    while True:
        first_price = input("Insira o valor da dívida da 1ª pessoa, em reais.\nR$ ").replace(",", ".")
        second_price = input("Insira o valor da dívida da 2ª pessoa, em reais.\nR$ ").replace(",", ".")
        try:
            first_price = float(first_price)
            second_price = float(second_price)
            total_price = first_price + second_price 
            
            print(f"Valor da dívida: R$ {total_price:.2f}.")
            print(f"Valor da dívida por pessoa: R$ {(total_price/2):.2f}.")
            break
        
        except ValueError:
            print("Insira um valor válido.")
                        
def main():
    soma()

if __name__ == "__main__":
    main()