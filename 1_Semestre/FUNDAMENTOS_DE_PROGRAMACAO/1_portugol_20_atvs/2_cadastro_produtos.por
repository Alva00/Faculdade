programa {
  funcao inicio() {
    inteiro contagem, quantidade_item
    real preco_item, preco_total_estoque = 0
    cadeia nome_item
        
    para (contagem = 0; contagem < 5; contagem++) {
        escreva("Insira o nome do produto: \n")
        leia(nome_item)
        escreva("Insira a quantidade do produto ", nome_item, ": \n")
        leia(quantidade_item)
        escreva("Insira o preço do produto ", nome_item, ": \n")
        leia(preco_item)
        preco_total_estoque += preco_item * quantidade_item
    }
    
    escreva("O valor total do estoque é: R$ ", preco_total_estoque, ".")
    }
}
