def store_hour_handling():
    while True:
        error_flag = False
        
        start_time = input("Insira o horário de abertura do estabelecimento (ex.: 0h, 10h ou 10:00).\n")
        end_time = input("Insira o horário de encerramento do estabelecimento (ex.: 0h, 10h ou 10:00).\n")
        current_time = input("Insira o horário atual (ex.: 0h, 10h ou 10:00).\n")
        
        important_hours_string = [start_time, end_time, current_time]
        important_hours_formatted = [""] * len(important_hours_string)
        
        for i, hour in enumerate(important_hours_string): #Hora bruta (ex.: 20)
            for caracter in hour:
                if caracter.isnumeric():
                    important_hours_formatted[i] += caracter
                
        for i, hour in enumerate(important_hours_formatted): #Hora com 4 caracteres (ex.: 2000)
            if len(hour) == 1:
                important_hours_formatted[i] = "0" + hour + "00"
            elif len(hour) in [2, 4]:
                while len(important_hours_formatted[i]) != 4:
                    important_hours_formatted[i] += "0"
            else:
                break
        
        if len(hour) not in [1, 2, 4]:
            error_flag = True
            print("O horário foi inserido incorretamente.")
        else:
            for hour in important_hours_formatted:
                if int(hour[:2]) >= 24 or int(hour[2:]) >= 60:
                    error_flag = True
                    print("Horas e minutos não podem ser iguais ou superiores a, respectivamente, 24 e 60.")
        if error_flag:
            continue
        
        for i, hour in enumerate(important_hours_formatted): #Hora formatada (ex.: 20:00)
            important_hours_formatted[i] = hour[:2] + ":" + hour[2:]
        
        print(f'Abertura: {important_hours_formatted[0]}. Encerramento: {important_hours_formatted[1]}. Hora atual: {important_hours_formatted[2]}.')
        while True:
            option_user = input("Os dados estão corretos? \nInsira '1' caso estejam.\nInsira '0' caso não estejam.\n")
            if option_user == "0":
                print("Lembre-se de corrigir os dados mediante a formatação correta.")
                break
            elif option_user == "1":
                break
            print("Opção inválida.")
        
        if option_user == "0":
            continue
        break
        
    current_status_store(important_hours_formatted)

def current_status_store(important_hours_formatted):
    hours_minutes = []
    for complete_hour in important_hours_formatted:
        hours_minutes.append([int(complete_hour[:2]), int(complete_hour[3:])])
    
    open_hour, open_minutes = hours_minutes[0]
    close_hour, close_minutes = hours_minutes[1]
    current_hour, current_minutes = hours_minutes[2]
    
    open_time_in_minutes = open_hour*60 + open_minutes
    close_time_in_minutes = close_hour*60 + close_minutes + (60*24 if open_hour > close_hour else 0)
    current_time_in_minutes = current_hour*60 + current_minutes + (60*24 if (open_hour > close_hour) and (current_hour < open_hour) else 0)
    
    print(f'Abertura: {important_hours_formatted[0]}. Encerramento: {important_hours_formatted[1]}. Hora atual: {important_hours_formatted[2]}.')
    if open_time_in_minutes <= current_time_in_minutes < close_time_in_minutes:    
        print("O estabelecimento está aberto!")
    else:
        print("O estabelecimento está fechado.")

def main():
    store_hour_handling()
    
if __name__ == "__main__":
    main()