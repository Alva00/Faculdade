programa {
  funcao inicio() {
    inteiro escolha_usuario
    real saldo_usuario = 0, operacoes_usuario
    
    enquanto(escolha_usuario != 0){
      escreva("Escolha:\n'1' para depósito;\n'2' para saque;\n'3' para consultar saldo;\n'0' para sair do programa.\n")
      leia(escolha_usuario)
      se (escolha_usuario == "1"){
        escreva("Insira o valor do depósito.\n")
        leia(operacoes_usuario)
        saldo_usuario += operacoes_usuario
        escreva("O depósito foi realizado.\n")
      }
      senao se (escolha_usuario == "2"){
        escreva("Insira o valor do saque.\n")
        leia(operacoes_usuario)
        se (saldo_usuario < operacoes_usuario){
          escreva("Saldo insuficiente.\n")
        }
        senao{
          saldo_usuario -= operacoes_usuario
          escreva("O saque foi realizado.\n")
        }
      }
      senao se (escolha_usuario == "3") {
        escreva("Saldo = R$ ", saldo_usuario, ".\n")
      }
      senao se (escolha_usuario == "0") {
        escreva("Fim do Programa.\n")
      }
    }
  }
}
