programa {
  funcao inicio() {
    real qtnd_litros_abastecido, quilometragem_rodada
    escreva("Insira a quantidade de litros abastecida.\n")
    leia(qtnd_litros_abastecido)
    escreva("Insira a quilometragem rodada.\n")
    leia(quilometragem_rodada)
    
    real media_consumo = quilometragem_rodada/qtnd_litros_abastecido
    escreva("A média de consumo é de ", media_consumo, " km/l.\n")

    se (media_consumo >= 11) {
        escreva("Consumo bom.\n")
    } senao se (media_consumo >= 8) {
        escreva("Consumo esperado.\n")
    } senao {
        escreva("Consumo abaixo do esperado.\n")
   }
 }
}