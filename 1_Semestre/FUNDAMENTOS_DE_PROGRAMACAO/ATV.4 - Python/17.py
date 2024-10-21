list_current_athletes_informations = []
attempts_per_athlete = 5

i = 0

while True:
    current_athlete = input("Insira o nome do atleta. Caso esteja em branco, o programa será finalizado.\n").strip()
    if current_athlete == "":
        break
    
    list_current_athletes_informations.append([current_athlete])
    for j in range(attempts_per_athlete):
        list_current_athletes_informations[i].append(float(input(f'Insira a pontuação {j+1}.\n')))
    
    i += 1
    
for informations_athlete in list_current_athletes_informations:
    print(f"Atleta: {informations_athlete[0]}")
    print("Saltos: ", end="")
    for j in range(1, attempts_per_athlete + 1):
        print(f'{informations_athlete[j]}', end=" | ")
    print()
    print(f'Média dos saltos: {sum(informations_athlete[1:])/attempts_per_athlete}')