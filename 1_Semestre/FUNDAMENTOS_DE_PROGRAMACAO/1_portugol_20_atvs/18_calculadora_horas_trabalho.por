programa {
  funcao inicio() {
    inteiro total_num_horas_trabalhadas = 0, num_horas_trabalhadas_dia, num_dias_trabalhados, contagem
    escreva("Insira a quantidade de dias trabalhados.\n")
    leia(num_dias_trabalhados)
    para (contagem = 1; contagem < num_dias_trabalhados+1; contagem++) {
      escreva("Insira a quantidade de horas trabalhadas no dia ", contagem, ".\n")
      leia(num_horas_trabalhadas_dia)
      total_num_horas_trabalhadas += num_horas_trabalhadas_dia
      }
    escreva("Quantidade de horas trabalhadas para ", num_dias_trabalhados, " dias: ")
    escreva(total_num_horas_trabalhadas, " horas.")
    }
}