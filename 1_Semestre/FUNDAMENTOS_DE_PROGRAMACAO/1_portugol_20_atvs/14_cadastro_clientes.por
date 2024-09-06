programa {
  funcao inicio() {
    inteiro contagem, contagem_mais_um, qtnd_clientes = 5
    cadeia nome_cliente[qtnd_clientes], telefone_cliente[qtnd_clientes], email_cliente[qtnd_clientes]
    cadeia temp_nome, temp_telefone, temp_email

    para (contagem = 0; contagem < qtnd_clientes; contagem++) {
      escreva("Insira o nome do cliente.\n")
      leia(nome_cliente[contagem])
      escreva("Insira o telefone do cliente.\n")
      leia(telefone_cliente[contagem])
      escreva("Insira o e-mail do cliente.\n")
      leia(email_cliente[contagem])
    }

    para (contagem = 0; contagem < qtnd_clientes - 1; contagem++) {
      para (contagem_mais_um = contagem + 1; contagem_mais_um < qtnd_clientes; contagem_mais_um++) {
        se (nome_cliente[contagem] > nome_cliente[contagem_mais_um]) {
          temp_nome = nome_cliente[contagem]
          nome_cliente[contagem] = nome_cliente[contagem_mais_um]
          nome_cliente[contagem_mais_um] = temp_nome

          temp_telefone = telefone_cliente[contagem]
          telefone_cliente[contagem] = telefone_cliente[contagem_mais_um]
          telefone_cliente[contagem_mais_um] = temp_telefone

          temp_email = email_cliente[contagem]
          email_cliente[contagem] = email_cliente[contagem_mais_um]
          email_cliente[contagem_mais_um] = temp_email
        }
      }
    }

    para (contagem = 0; contagem < qtnd_clientes; contagem++) {
      escreva("Nome: ", nome_cliente[contagem], ";\n")
      escreva("Telefone: ", telefone_cliente[contagem], ";\n")
      escreva("E-mail: ", email_cliente[contagem], ".\n")
      escreva("-\n")
    }
  }
}
