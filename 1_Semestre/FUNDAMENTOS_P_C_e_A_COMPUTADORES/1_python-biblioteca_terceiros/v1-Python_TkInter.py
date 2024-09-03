from tkinter import *

prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
user_attempts = 0
current_height_text = 15
left_margin_text = 25
current_number_user = [0]

def main():
    #Aqui, há itens (i)mutáveis da biblioteca do Tkinter.
    global main_window, current_height_text
    main_window = Tk()
    main_window.title("Números primos - M.E. Opcional")
    main_window.geometry("320x400")
    main_window.resizable(False, False)

    main_title_label = Label(main_window, text="Números primos", font=("Arial", 20))
    main_title_label.place(x=left_margin_text, y=current_height_text)

    current_height_text += 40
    placeholder_label = Label(main_window, text="Insira um número natural <= 100")
    placeholder_label.place(x=left_margin_text, y=current_height_text)
    
    current_height_text += 40
    user_num_input_box = Entry(main_window, bd=3, width=20)
    user_num_input_box.place(x=left_margin_text, y=current_height_text)
    current_number_user[0] = user_num_input_box

    current_height_text += 40
    confirm_button = Button(main_window, text="Enviar")
    confirm_button.config(command=validate_num_user)
    confirm_button.place(x=left_margin_text, y=current_height_text)
    
    current_height_text += 40
    current_status_to_user_num_label("Aguardando a ação do usuário.")
    
    main_window.mainloop()

def current_status_to_user_num_label(text_to_user):
    global current_height_text, user_attempts, current_status_label

    if user_attempts == 0:
        current_status_label = Label(main_window, text=text_to_user)
        current_status_label.place(x=left_margin_text, y=current_height_text)
    else:
        current_status_label.config(text=text_to_user)
    user_attempts += 1
     
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
         
if __name__ == "__main__":
    main()