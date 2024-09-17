programa {
  inclua biblioteca Matematica --> mat
  funcao inicio() {
    real divida_usuario, valor_da_conta, gorjeta = 1.1
    escreva("Insira o valor do pagamento.\n")
    leia(divida_usuario)

    divida_usuario *= gorjeta
    divida_usuario = mat.arredondar(divida_usuario, 2)
    gorjeta = mat.arredondar(gorjeta-1.0, 2)*100
    
    escreva("Gorjeta: ", gorjeta ,"%.\n")
    escreva("Valor do pagamento: ", divida_usuario, ".")
  }
}
