programa {
  funcao inicio() {
    inteiro contagem
    cadeia nome_aluno[5]
    real media_aluno[5]
    real nota_aluno

    para (contagem = 0; contagem < 5; contagem++) {
      real soma_notas = 0
      escreva("Insira o nome do aluno.\n")
      leia(nome_aluno[contagem])
      escreva("Insira a primeira nota.\n")
      leia(nota_aluno)
      soma_notas += nota_aluno
      escreva("Insira a segunda nota.\n")
      leia(nota_aluno)
      soma_notas += nota_aluno
      escreva("Insira a terceira nota.\n")
      leia(nota_aluno)
      soma_notas += nota_aluno

      media_aluno[contagem] = soma_notas / 3
    }
    
    para (contagem = 0; contagem < 5; contagem++) {
      escreva("Aluno(a): ", nome_aluno[contagem], ". Média: ", media_aluno[contagem], "\n")
      se (media_aluno[contagem] < 6){
        escreva("Situação: reprovado\n")
      }
      senao {
        escreva("Situação: aprovado\n")
      }
      }
    }
  }
}
