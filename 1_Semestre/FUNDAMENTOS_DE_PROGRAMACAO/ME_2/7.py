import time

def contagem_regressiva(seconds):
    while seconds >= 0:
        print(f"Resta(m) {seconds} segundos!")
        time.sleep(1)  # Pausa de 1 segundo
        seconds -= 1
    print("Lançamento!")

def main():
    try:
        segundos = int(input("Insira o número de segundos para o lançamento:\n"))
        contagem_regressiva(segundos)
    except ValueError:
        print("Insira um número inteiro válido.")

if __name__ == "__main__":
    main()
