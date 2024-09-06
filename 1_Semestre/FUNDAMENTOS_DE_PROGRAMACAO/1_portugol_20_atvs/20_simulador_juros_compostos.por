programa {
  inclua biblioteca Matematica --> mat
  funcao inicio() {
    inteiro parcelas, contagem
    real valor_investimento, taxa_de_juros_compostos, valor_total = 0

    escreva("Insira o valor do investimento.\n")
    leia(valor_investimento)
    escreva("Insira o número de meses para pagamento.\n")
    leia(parcelas)
    escreva("Insira a taxa de juros compostos mensais (ex.: 0.02 para 2%).\n")
    leia(taxa_de_juros_compostos)
    
    valor_total = valor_investimento*(mat.potencia(1+taxa_de_juros_compostos, parcelas))
    escreva("Valor total a ser pago: R$ ", valor_total, ".\n")
  }
}

