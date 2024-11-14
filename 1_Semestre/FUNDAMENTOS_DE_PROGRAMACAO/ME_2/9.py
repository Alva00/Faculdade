def cadastro_pesos():
    all_weights = []
    while True:
        current_weight = (input("Insira o valor da massa levantada pelo competidor, em kg. Insira -1 para encerrar.\n")).replace(",", ".")
        if current_weight == "-1":
            if len(all_weights) == 0:
                print("Insira pelo menos 1 elemento.")
                continue
            else:
                maior_numero(all_weights)
                break
        try:
            current_weight = float(current_weight)
            all_weights.append(round(current_weight, 2))
        except ValueError:
            print("Insira um valor válido.")
            
def maior_numero(all_weights):
    print(f"Maior peso levantado: {max(all_weights):.2f} kg.")
    print(f"Lista completa: {all_weights}")
    
def main():
    cadastro_pesos()

if __name__ == "__main__":
    main()
