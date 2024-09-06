programa {
  funcao inicio() {
    real peso_pessoa, altura_pessoa, imc_pessoa
        
    escreva("Insira sua altura.\n")
    leia(altura_pessoa)
    escreva("Insira o seu peso.\n")
    leia(peso_pessoa)
    imc_pessoa = peso_pessoa/(altura_pessoa*altura_pessoa)
    
    se (imc_pessoa < 18.5){
      escreva("Categoria: magreza\n")
    }
    senao se (imc_pessoa < 25.0){
      escreva("Categoria: normal\n")
    }    
    senao se (imc_pessoa < 30){
      escreva("Categoria: sobrepeso\n")
    }    
    senao se (imc_pessoa < 40){
      escreva("Categoria: obesidade\n")
    }    
    senao {
      escreva("Categoria: obesidade grave\n")
    }    
    
    escreva("IMC: ", imc_pessoa, ".")
    }
}

