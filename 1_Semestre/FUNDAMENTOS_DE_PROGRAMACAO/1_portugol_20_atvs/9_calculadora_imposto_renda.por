programa {
  funcao inicio() {
    real salario, aliquota, parcela_a_deduzir, imposto

    escreva("Insira o seu salário bruto.\n")
    leia(salario)
    
    se(salario <= 2259.20){
      escreva("Alíquota nula.\n")
      aliquota = 0
      parcela_a_deduzir = 0
    }
    senao se(salario <= 2828.65){
      escreva("Alíquota de 7,5%.\n")
      aliquota = 0.075
      parcela_a_deduzir = 169.44
    }
    senao se(salario <= 3751.05){
      escreva("Alíquota de 15%.\n")
      aliquota = 0.15
      parcela_a_deduzir = 381.44
    }
    senao se(salario < 4664.68){
      escreva("Alíquota de 22,5%.\n")
      aliquota = 0.225
      parcela_a_deduzir = 662.77
    }
    senao{
      escreva("Alíquota de 27,5%.\n")
      aliquota = 0.275
      parcela_a_deduzir = 896.00
    }
    imposto = salario*aliquota - parcela_a_deduzir
    escreva("Imposto de renda a ser pago: R$ ", imposto, ".\n")
  }
}