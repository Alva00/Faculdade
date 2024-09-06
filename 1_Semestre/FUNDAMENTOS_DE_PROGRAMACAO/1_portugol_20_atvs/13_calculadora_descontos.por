programa {
  funcao inicio() {
    real valor_produto
    real desconto_maximo = 0.15, desconto_progressivo = 0.03
    inteiro quantidade_produtos, desconto_por_qtnd_produtos = 50, acumulo_descontos
    
    escreva("Insira o valor do produto.\n")
    leia(valor_produto)
    escreva("Insira a quantidade de produtos.\n")
    leia(quantidade_produtos)

    real maxima_razao_descontos = desconto_maximo/desconto_progressivo

    para(acumulo_descontos = 0; acumulo_descontos < maxima_razao_descontos; acumulo_descontos++) {
      se ((quantidade_produtos/desconto_por_qtnd_produtos) < acumulo_descontos+1){
        pare
      }
    }
    
    real valor_sem_desconto = quantidade_produtos*valor_produto
    escreva("Valor sem desconto: R$", valor_sem_desconto , ".\n")
    escreva("Desconto de: ", acumulo_descontos*desconto_progressivo*100, "%.\n")
    escreva("Valor com desconto (", acumulo_descontos, " acúmulos): R$ ", valor_sem_desconto*(1-(desconto_progressivo*acumulo_descontos)))
  }
}
