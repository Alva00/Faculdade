programa {
  funcao inicio() {
    real distancia_percorrida, consumo_medio_veiculo, combustivel_necessario
    escreva("Insira a dist�ncia percorrida (km).\n")
    leia(distancia_percorrida)
    escreva("Insira o consumo m�dio do ve�culo (km/l).\n")
    leia(consumo_medio_veiculo)

    combustivel_necessario = distancia_percorrida/consumo_medio_veiculo

    escreva("Quantidade de combust�vel necess�ria: ", combustivel_necessario, " litros.")
  }
}