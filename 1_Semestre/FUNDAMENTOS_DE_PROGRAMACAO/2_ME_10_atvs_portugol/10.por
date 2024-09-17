programa {
  inclua biblioteca Matematica --> mat
  funcao inicio() {
    real valor_base_multa = 100, intervalo_quilometragem_para_multa = 10, valor_multa_intervalo = 10
    real velocidade_usuario, limite_velocidade
    real quantidade_de_acrescimos_multa, condicional

    escreva("Insira a velocidade da pessoa.\n")
      leia(velocidade_usuario)
      escreva("Insira o limite de velocidade.\n")
      leia(limite_velocidade)

    se (velocidade_usuario < limite_velocidade) {
      escreva("Não há multa.")
    } senao {
      condicional = (velocidade_usuario - limite_velocidade)/intervalo_quilometragem_para_multa

      para(quantidade_de_acrescimos_multa = 0; condicional > quantidade_de_acrescimos_multa; quantidade_de_acrescimos_multa++) {
      }
      
      escreva("Valor da multa: R$ ", valor_base_multa + quantidade_de_acrescimos_multa*valor_multa_intervalo)
    }
    
  }
}
