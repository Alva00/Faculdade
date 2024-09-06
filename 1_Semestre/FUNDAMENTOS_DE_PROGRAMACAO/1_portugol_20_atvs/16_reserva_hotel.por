programa {
  funcao inicio() {
    inteiro contagem, qtnd_clientes = 3
    cadeia nome_cliente[qtnd_clientes] 
    inteiro data_entrada[qtnd_clientes], data_saida[qtnd_clientes]
    
    para (contagem = 0; contagem < qtnd_clientes; contagem++) {
      escreva("Insira o nome do cliente.\n")
      leia(nome_cliente[contagem])
      escreva("Insira a data de entrada do cliente.\n")
      leia(data_entrada[contagem])
      escreva("Insira a data de saída do cliente.\n")
      leia(data_saida[contagem])
    }

    para (contagem = 0; contagem < qtnd_clientes; contagem++) {
      escreva("Cliente: ", nome_cliente[contagem], " | Qtnd de dias reservados: ")
      se (data_entrada[contagem] < data_saida[contagem]){
        escreva(data_saida[contagem] - data_entrada[contagem], ".\n")
      } senao {
        escreva(30 - (data_entrada[contagem] - data_saida[contagem]), ".\n")
      }
    }
  }
}
