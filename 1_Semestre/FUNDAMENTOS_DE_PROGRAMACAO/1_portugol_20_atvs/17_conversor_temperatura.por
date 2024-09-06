programa {
  funcao inicio() {
    real celsius, fahrenheit, kelvin
    escreva("Insira uma temperatura em celsius.\n")
    leia(celsius)
    fahrenheit = celsius*1.8+32
    kelvin = celsius+273.15
    escreva("Temperaturas: ", celsius, "°C, ", fahrenheit, "°F e ", kelvin, " K.")
  }
}
