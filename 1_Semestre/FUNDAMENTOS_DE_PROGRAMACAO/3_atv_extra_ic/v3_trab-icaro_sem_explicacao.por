programa {
  inclua biblioteca Texto --> tx
  funcao inicio() {
    inteiro i, j
    
    cadeia cpf_usuario
    caracter digito

    inteiro num_user_caracteres_cpf, num_caracteres_cpf 
    inteiro bool_estrutura_cpf = 1

    escreva("Insira um CPF formatado:\n")
    leia(cpf_usuario)
    
    num_user_caracteres_cpf = tx.numero_caracteres(cpf_usuario)
    num_caracteres_cpf = tx.numero_caracteres("000.000.000-00")

    se (num_user_caracteres_cpf != num_caracteres_cpf) {
      bool_estrutura_cpf = 0
    } senao {
    para(i = 0; i != num_caracteres_cpf; i++) {
      digito = tx.obter_caracter(cpf_usuario, i) 
       
       se (i == 11) {
        se(digito != "-") {
          bool_estrutura_cpf = 0
        } 
      
      } senao se (i == 3 ou i == 7) {
        se (digito != ".") {
          bool_estrutura_cpf = 0
        }
      
      } senao {
        para(j = 0; j < 10; j++) {
          cadeia caractere_pos_j = "" + j
          se (caractere_pos_j == digito) {
            pare
          } senao se (j == 9) {
            bool_estrutura_cpf = 0
          }
        }
      }
      se (bool_estrutura_cpf == 0) {
        pare
      }
    }
  }
    
    se (bool_estrutura_cpf == 0) {
      escreva("\nCPF INVÁLIDO (referente à estrutura).\n")
    } senao {
      escreva("\nCPF VÁLIDO (referente à estrutura).\n")
    }
  }
}