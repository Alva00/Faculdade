def inverter_string(mensagem):
    return mensagem[::-1]  # Inverte a string

def main():
    message = input("Insira a mensagem que deseja decifrar:\n")
    reversed_message = inverter_string(message)
    print(f"Mensagem decifrada: {reversed_message}")

if __name__ == "__main__":
    main()