programa {
  funcao inicio() {
    real distancia_percorrida, consumo_medio_veiculo, combustivel_necessario
    escreva("Insira a distância percorrida (km).\n")
    leia(distancia_percorrida)
    escreva("Insira o consumo médio do veículo (km/l).\n")
    leia(consumo_medio_veiculo)

    combustivel_necessario = distancia_percorrida/consumo_medio_veiculo

    escreva("Quantidade de combustível necessária: ", combustivel_necessario, " litros.")
  }
}