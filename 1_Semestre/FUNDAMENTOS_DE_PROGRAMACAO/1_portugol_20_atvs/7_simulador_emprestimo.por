programa {
  funcao inicio() {
    inteiro parcelas, contagem
    real valor_emprestimo, taxa_de_juros, valor_total = 0

    escreva("Insira o valor do empréstimo.\n")
    leia(valor_emprestimo)
    escreva("Insira o número de meses para pagamento.\n")
    leia(parcelas)
    escreva("Insira a taxa de juros mensal (ex.: 0.1 para 10%).\n")
    leia(taxa_de_juros)
    
    para(contagem = 0; contagem < parcelas; contagem++){
      valor_total += (valor_emprestimo/parcelas) + (valor_emprestimo/parcelas)*taxa_de_juros*contagem
    }
    escreva("Valor total a ser pago: R$ ", valor_total, ".\n")
    escreva("Valor da parcela mensal: R$ ", valor_total/parcelas, ".\n")
  }
}

