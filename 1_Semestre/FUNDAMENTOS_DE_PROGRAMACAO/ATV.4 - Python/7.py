num_quantify_user_selected = 5
list_all_user_numbers = []
num_product_all_user_numbers = 1

for i in range(num_quantify_user_selected):
    list_all_user_numbers.append(int(input(f"Insira o {i+1}° número inteiro.\n")))

print("Números inseridos: ", end="")    
for num in list_all_user_numbers:
    num_product_all_user_numbers *= num
    print(num, end=" | ")
print()

print(f'Produto de todos os termos: {num_product_all_user_numbers}')
print(f'Soma de todos os termos: {sum(list_all_user_numbers)}')