def saudacao():
    while True:
        current_name = input("Insira o nome do participante. Para encerrar, digite '-1'.\n").capitalize()
        if current_name == "-1":
            print("Programa encerrado.")
            break
        elif current_name.strip() == "":
            print("Insira um nome válido.")
        else:
            print(f"Olá, {current_name}! Bem-vindo.")
    
def main():
    saudacao()

if __name__ == "__main__":
    main()