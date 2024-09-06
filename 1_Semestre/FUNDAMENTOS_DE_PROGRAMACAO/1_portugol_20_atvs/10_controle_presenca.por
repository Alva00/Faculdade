programa {
  funcao inicio() {
    inteiro quantidade_alunos = 10
    inteiro contador, dias_uteis, faltas_aluno[quantidade_alunos]
    cadeia nome_aluno[quantidade_alunos]

    escreva("Insira a quantidade de dias úteis do mês.\n")
    leia(dias_uteis)

    para(contador = 0; contador < quantidade_alunos; contador++){
      escreva("Insira o nome do(a) aluno(a).\n")
      leia(nome_aluno[contador])
      escreva("Insira a quantidade de dias que o aluno faltou (de ", dias_uteis, ").\n")
      leia(faltas_aluno[contador])
    }

    para(contador = 0; contador < quantidade_alunos; contador++){
      escreva("Aluno(a): ", nome_aluno[contador], " | ")
      real presenca_aluno = ((dias_uteis - faltas_aluno[contador])/dias_uteis)*100
      escreva("Presença: ", presenca_aluno, "%.\n" )
    }
  }
}