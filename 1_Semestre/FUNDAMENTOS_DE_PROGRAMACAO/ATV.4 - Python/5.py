num_quantify_numbers = 20
list_numbers = [num for num in range(num_quantify_numbers)]
odd_numbers = []
even_numbers = []
for num in list_numbers:
    if (num % 2 == 0):
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

print(f'Números ímpares: {odd_numbers}')
print(f'Números pares: {even_numbers}')
print(f'Todos os números: {list_numbers}')