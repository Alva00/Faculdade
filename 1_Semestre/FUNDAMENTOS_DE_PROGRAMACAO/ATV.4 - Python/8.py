num_quantify_people = 5
list_age_heights = []

for i in range(num_quantify_people):
    current_age = int(input(f"Insira a idade da {i+1}ª pessoa.\n"))
    current_height = float(input(f"Insira a altura da {i+1}ª pessoa.\n"))
    list_placeholder = [current_age, current_height]
    list_age_heights.append(list_placeholder)

for i in list_age_heights:
    print(f"Altura: {i[1]}. Peso: {i[0]}")
