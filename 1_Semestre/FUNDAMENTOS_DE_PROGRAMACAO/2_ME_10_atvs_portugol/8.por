programa {
  funcao inicio() {
    real peso_da_pessoa, altura_da_pessoa, imc_da_pessoa
        
    escreva("Insira sua altura.\n")
    leia(altura_da_pessoa)
    escreva("Insira seu peso.\n")
    leia(peso_da_pessoa)
    imc_da_pessoa = peso_da_pessoa/(altura_da_pessoa*altura_da_pessoa)
    
    se (imc_da_pessoa < 18.5){
      escreva("Categoria: Magreza.\n")
    } senao se (imc_da_pessoa < 25.0){
      escreva("Categoria: Normal.\n")
    } senao se (imc_da_pessoa < 30){
      escreva("Categoria: Sobrepeso.\n")
    } senao se (imc_da_pessoa < 40){
      escreva("Categoria: Obesidade.\n")
    } senao {
      escreva("Categoria: Obesidade grave.\n")
    }    
    
    escreva("Seu IMC: ", imc_da_pessoa, ".")
    }
}