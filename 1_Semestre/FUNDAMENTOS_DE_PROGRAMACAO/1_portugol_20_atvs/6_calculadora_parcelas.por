programa {
  funcao inicio() {
    inteiro parcelas, contagem
    real valor_da_compra, taxa_de_juros

    escreva("Insira o valor total da compra.\n")
    leia(valor_da_compra)
    escreva("Insira a quantidade de parcelas.\n")
    leia(parcelas)
    escreva("Insira a taxa de juros (ex.: 0.1 para 10%).\n")
    leia(taxa_de_juros)
    
    para(contagem = 0; contagem < parcelas; contagem++){
      real valor_parcela = (valor_da_compra/parcelas) + (valor_da_compra/parcelas)*taxa_de_juros*contagem
      escreva("Parcela ", contagem + 1, ": R$", valor_parcela, ".\n")
    }
  }
}

