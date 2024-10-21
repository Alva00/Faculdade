num_quantify_numbers = 10
list_all_numbers = [num for num in range(num_quantify_numbers)]

print(f"Quadrado dos {num_quantify_numbers} primeiros números inteiros não negativos:")
for num in list_all_numbers:
    print(num**2, end=" | ")