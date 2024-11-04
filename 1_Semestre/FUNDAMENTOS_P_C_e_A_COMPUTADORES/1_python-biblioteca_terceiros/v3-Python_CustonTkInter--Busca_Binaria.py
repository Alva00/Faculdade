import customtkinter

prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
user_attempts = 0
current_height_text = 15
left_margin_text = 25
current_number_user = [0]

def main():
    #Aqui, há itens (i)mutáveis da biblioteca do CustomTkInter.
    global main_window, current_height_text
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")
    
    main_window = customtkinter.CTk()
    main_window.title("Busca Binária")
    main_window.geometry("400x400")
    main_window.resizable(False, False)

    main_title_label = customtkinter.CTkLabel(main_window, text="Números primos", font=("Arial", 20))
    main_title_label.place(x=left_margin_text, y=current_height_text)

    current_height_text += 40
    placeholder_label = customtkinter.CTkLabel(main_window, text="Insira um número natural <= 100")
    placeholder_label.place(x=left_margin_text, y=current_height_text)
    
    current_height_text += 40
    user_num_input_box = customtkinter.CTkEntry(main_window, width=100)
    user_num_input_box.place(x=left_margin_text, y=current_height_text)
    current_number_user[0] = user_num_input_box

    current_height_text += 40
    confirm_button = customtkinter.CTkButton(main_window, text="Enviar")
    confirm_button.configure(command=validate_num_user)
    confirm_button.place(x=left_margin_text, y=current_height_text)
    
    current_height_text += 40
    current_status_to_user_num_label("Aguardando a ação do usuário.")
    
    main_window.mainloop()

def current_status_to_user_num_label(text_to_user):
    global current_height_text, user_attempts, current_status_label, current_text_label

    if user_attempts == 0:
        current_status_label = customtkinter.CTkLabel(main_window, text=text_to_user)
        current_status_label.place(x=left_margin_text, y=current_height_text)
    else:
        current_status_label.configure(text=text_to_user)
    user_attempts += 1
    
    current_text_label = text_to_user
     
def validate_num_user():
    num_user = current_number_user[0].get()
    try:
        num_user = int(num_user)
        if (0 <= num_user <= 100):
            num_primo(num_user)
        else:
            current_status_to_user_num_label("Insira um número entre 0 e 100.")
    except ValueError:
        current_status_to_user_num_label("Insira um número válido (entre 0 e 100).") 

def num_primo(num_user):
    for i, num in enumerate(prime_numbers):
        if num_user == num:
            current_status_to_user_num_label(f'O número inserido ({num_user}) é um número primo.\nEle se encontra na posição {i} da lista.\n*Listas começam com índice 0.')
            break
    if num_user != num:
        current_status_to_user_num_label(f'O número inserido ({num_user}) não é um número primo.')
    
    busca_binaria(num_user)
    
def busca_binaria(num_user):
    start_position = 0
    end_position = 100
    binary_search_list = list(range(end_position + 1))
    
    bool_element_found = False
    attempts = 0
    
    while start_position <= end_position:
        attempts += 1 
        middle_position = round((start_position + end_position) / 2)
        
        if binary_search_list[middle_position] < num_user:
            start_position = middle_position + 1
        elif binary_search_list[middle_position] > num_user:
            end_position = middle_position - 1
        else:
            current_status_to_user_num_label(current_text_label + f"\nBusca binária: Elemento encontrado em {attempts} tentativa(s).")
            bool_element_found = True
            break
    if not bool_element_found:
        current_status_to_user_num_label(current_text_label + f"\nBusca binária: Elemento não encontrado após {attempts} tentativa(s).")

if __name__ == "__main__":
    main()