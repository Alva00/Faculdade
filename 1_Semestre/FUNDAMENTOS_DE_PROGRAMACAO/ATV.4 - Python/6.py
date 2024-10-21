num_students = 2
num_notes_each_student = 4
list_all_average_notes = []
num_approved_students = 0

for i in range(num_students):
    list_all_average_notes.append(0)
    for j in range(num_notes_each_student):
        list_all_average_notes[i] += float(input(f"Insira a nota {j+1}.\n"))
    list_all_average_notes[i] /= 4
    if list_all_average_notes[i] >= 7.0:
        num_approved_students += 1

print(f'Quantidade de estudantes com média superior a 7: {num_approved_students}')