programa {
  funcao inicio() {
    inteiro quantidade_cadastro = 3
    inteiro contagem = 0, quantidade_itens_estoque = 0
    cadeia nome_item[quantidade_cadastro]
    real quantidade_item[quantidade_cadastro], valor_item[quantidade_cadastro], valor_estoque = 0

    para (contagem = 0; contagem < quantidade_cadastro; contagem++) {
      escreva("Insira o nome do item.\n")
      leia(nome_item[contagem])
      escreva("Insira a quantidade do item.\n")
      leia(quantidade_item[contagem])
      escreva("Insira o valor do item (unidade).\n")
      leia(valor_item[contagem])

      valor_estoque += valor_item[contagem]*quantidade_item[contagem]
      quantidade_itens_estoque += quantidade_item[contagem]
    }

    escreva("Valor total do estoque: R$ ", valor_estoque, ".\n")
    escreva("Quantidade de itens do estoque: ", quantidade_itens_estoque, ".\n")
  }
}
