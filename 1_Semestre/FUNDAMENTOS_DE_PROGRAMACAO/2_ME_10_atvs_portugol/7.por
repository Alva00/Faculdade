programa {
  funcao inicio() {
    real dinheiro_usuario, cambio_dolar_real    
    escreva("Insira o valor desejado em reais. \nR$ ")
    leia(dinheiro_usuario)
    escreva("Insira a taxa de c�mbio do d�lar para real (ex.: 0.18).\n")
    leia(cambio_dolar_real)

    escreva("R$ ", dinheiro_usuario, " em d�lar: ", dinheiro_usuario*cambio_dolar_real, ".\n")
  }
}