all_user_numbers = []

while True:
    current_number = float(input("Insira um número inteiro ou decimal. Para cancelar, insira '-1'.\n"))
    if current_number == -1:
        break
    
    all_user_numbers.append(current_number)

print(f"Quantidade de valores inseridos: {len(all_user_numbers)}")

print("Lista dos números inseridos:")
for num in all_user_numbers:
    print(num, end= " | ")
print()

print("Lista decrescente dos números inseridos:")
for i in range(len(all_user_numbers) - 1, -1, -1):
    print(all_user_numbers[i])

print(f'Soma dos valores inseridos: {sum(all_user_numbers)}')

average_numbers = sum(all_user_numbers)/len(all_user_numbers)
print(f'Média dos valores inseridos: {average_numbers}')

i = 0
j = 0
for num in all_user_numbers:
    if num > average_numbers:
        i += 1
    if num < 7:
        j += 1
print(f"Quantidade de valores acima da média: {i}.")
print(f'Quantida de valores abaixo de 7: {j}')

print("Fim do Programa.")
