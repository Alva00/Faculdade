programa {
  funcao inicio() {
    real celsius, fahrenheit
    escreva("Insira uma temperatura em celsius.\n")
    leia(celsius)
    
    fahrenheit = celsius*1.8+32
    
    escreva("Temperatura em Fahrenheit: ", fahrenheit, "°F.")
  }
}