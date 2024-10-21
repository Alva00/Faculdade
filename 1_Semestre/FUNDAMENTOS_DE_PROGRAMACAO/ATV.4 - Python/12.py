num_students = 30
list_age_heights = []
average_height = 0
quantify_students_approved_conditions = 0

for i in range(num_students):
    current_age = int(input(f"Insira a idade da {i+1}ª pessoa.\n"))
    current_height = float(input(f"Insira a altura da {i+1}ª pessoa.\n"))
    average_height += current_height
    list_placeholder = [current_age, current_height]
    list_age_heights.append(list_placeholder)
    
average_height /= num_students

for current_list in list_age_heights:
    if (current_list[0] > 13) and (current_list[1] < average_height):
        quantify_students_approved_conditions += 1
        
print("Quantidade de alunos com idade superior a 13 anos e menores que a média:")
print(quantify_students_approved_conditions)