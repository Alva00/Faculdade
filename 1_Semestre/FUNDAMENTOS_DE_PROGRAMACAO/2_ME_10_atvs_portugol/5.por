programa {
  funcao inicio() {
    inteiro quantidade_itens, i
    real preco_item, preco_final = 0

    escreva("Insira a quantidade de itens.\n")
    leia(quantidade_itens)

    para(i = 0; i != quantidade_itens; i++) {
      escreva("Insira o valor do item ", i+1, ".\n")
      leia(preco_item)
      preco_final += preco_item
    }
    escreva("Valor do estoque: R$ ", preco_final, ".")
  }
}
