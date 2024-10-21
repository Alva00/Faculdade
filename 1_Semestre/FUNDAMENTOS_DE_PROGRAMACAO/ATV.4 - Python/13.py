list_months_temperature = [
["Janeiro"],
["Fevereiro"],
["Março"],
["Abril"],
["Maio"],
["Junho"],
["Julho"],
["Agosto"],
["Setembro"],
["Outubro"],
["Novembro"],
["Dezembro"]
]

average_year_temperature = 0

for current_list in list_months_temperature:
    current_list.append(float(input(f"Insira a temperatura média de {current_list[0]}.\n")))
    average_year_temperature += current_list[1]
average_year_temperature /= len(list_months_temperature)

print(f"Meses acima da temperatura média ({average_year_temperature}) °C:")
for current_list in list_months_temperature:
    if current_list[1] > average_year_temperature:
        print(f'{current_list[0]}: {current_list[1]} °C.')