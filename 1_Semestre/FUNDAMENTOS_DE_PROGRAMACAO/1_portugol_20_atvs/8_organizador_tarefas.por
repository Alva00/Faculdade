programa {
  funcao inicio() {
    inteiro contagem
    cadeia nome_tarefa[10], prioridade_tarefa[10]

    para (contagem = 0; contagem < 10; contagem++) {
      escreva("Insira o nome da tarefa.\n")
      leia(nome_tarefa[contagem])
      escreva("Insira a prioridade da tarefa.\n")
      escreva("1 = alta, 2 = media, 3 = baixa\n")
      leia(prioridade_tarefa[contagem])
    }
    
    escreva("Prioridade Alta:\n")
    para (contagem = 0; contagem < 10; contagem++) {
      se (prioridade_tarefa[contagem] == "1"){
        escreva("Tarefa: ", nome_tarefa[contagem], ".\n")
      } 
    }
    escreva("Prioridade Média:\n")
    para (contagem = 0; contagem < 10; contagem++) {
      se (prioridade_tarefa[contagem] == "2"){
        escreva("Tarefa: ", nome_tarefa[contagem], ".\n")
      } 
    }
    escreva("Prioridade Baixa:\n")
    para (contagem = 0; contagem < 10; contagem++) {
      se (prioridade_tarefa[contagem] == "3"){
        escreva("Tarefa: ", nome_tarefa[contagem], ".\n")
      } 
    }

  }
}
