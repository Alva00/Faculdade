num_elementos = 10
lista_c_elementos = [num for num in range(1, (num_elementos + 1))]
lista_c_elementos_invertida = [lista_c_elementos[num] for num in range((num_elementos - 1), -1, -1)]
print(lista_c_elementos_invertida)