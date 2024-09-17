programa {
  inclua biblioteca Texto --> tx
  funcao inicio() {
    inteiro i, true_false = 1
    cadeia cpf_usuario
    caracter digito
    escreva("Insira a estrutura de um CPF:\n")
    leia(cpf_usuario)

    para(i = 1; i != tx.numero_caracteres(cpf_usuario); i++) {
      digito = tx.obter_caracter(cpf_usuario, i-1)
      se (tx.numero_caracteres(cpf_usuario) != tx.numero_caracteres("000.000.000-00")) {
        true_false = 0
      } senao se (i == 12) {
        se(digito != "-") {
          true_false = 0
        }
      } senao se (i == 4 ou i == 8) {
        se (digito != ".") {
          true_false = 0
        }
      }
    }

    se (true_false == 0) {
      escreva("ESTRUTURA DE CPF INVÁLIDA.")
    } senao {
      escreva("ESTRUTURA DE CPF VÁLIDA")
    }
  }
}
