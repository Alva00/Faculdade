num_notes = 4
list_notes = []
for i in range(num_notes):
    current_note = float(input(f'Insira a nota {i+1}.\n'))
    list_notes.append(current_note)
print(f'Média final: {sum(list_notes)/num_notes}')