programa {
  inclua biblioteca Matematica --> mat
  funcao inicio() {
    real n1, n2, n3, media_notas
    escreva("Insira a nota 1.\n")
    leia(n1)
    escreva("Insira a nota 2.\n")
    leia(n2)
    escreva("Insira a nota 3.\n")
    leia(n3)

    media_notas = (n1+n2+n3)/3
    media_notas = mat.arredondar(media_notas, 2)

    escreva("Média das notas: ", media_notas)
  }
}
