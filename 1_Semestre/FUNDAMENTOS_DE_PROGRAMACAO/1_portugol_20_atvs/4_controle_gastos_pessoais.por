programa {
  funcao inicio() {
    inteiro contagem, dia_de_menor_gasto
    real gasto_do_dia, total_gasto = 0, media_diaria, menor_gasto_do_dia = 1000000000

    para (contagem = 1; contagem < 8; contagem++) {
      escreva("Insira o gasto do dia ", contagem, ".\n")
      leia(gasto_do_dia)
      total_gasto += gasto_do_dia
      se (gasto_do_dia < menor_gasto_do_dia) {
        dia_de_menor_gasto = contagem
        menor_gasto_do_dia = gasto_do_dia
      }
    }
    
    media_diaria = total_gasto/7
    
    escreva("Dia de menor gasto: ", dia_de_menor_gasto, ", com valor de: R$ ", menor_gasto_do_dia, ".\n")
    escreva("Média diária de gastos: R$", media_diaria, ".\n")
    escreva("Total gasto: R$ ", total_gasto, ".\n")
    
  }
}