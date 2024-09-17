programa {
  funcao inicio() {
    real valor_inicial, taxa_juros, tempo_operacao, valor_final_investimento
    escreva("Insira o valor inicial.\n R$ ")
    leia(valor_inicial)
    escreva("Insira a taxa de juros (ex.: 0.1 para 10%).\n")
    leia(taxa_juros)
    escreva("Insira o tempo da operação, em meses.\n")
    leia(tempo_operacao)

    valor_final_investimento = valor_inicial + (valor_inicial*taxa_juros*tempo_operacao)

    escreva("Valor final do investimento: R$ ", valor_final_investimento, ".")
  }
}
