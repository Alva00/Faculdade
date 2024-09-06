programa {
  funcao inicio() {
    real distancia_percorrida, consumo_veiculo, preco_combustivel, custo_total
    escreva("Insira a distância percorrida (km).\n")
    leia(distancia_percorrida)
    escreva("Insira o consumo médio do veículo (km/l).\n")
    leia(consumo_veiculo)
    escreva("Insira o preço do combustível.\n")
    leia(preco_combustivel)

    custo_total = (preco_combustivel*distancia_percorrida)/consumo_veiculo

    escreva("O custo total foi de R$ ", custo_total, ".")
  }
}
