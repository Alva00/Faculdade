def shopping_cart_user(shopping_cart):
    num_final_items = total_items_shopping_cart()
        
    while len(shopping_cart) < num_final_items:
        current_item_name, is_name_correct = get_item_name(shopping_cart)
        if not is_name_correct:
            continue
        
        is_repeated_item, is_user_choice_switch_item = validate_repeated_item(shopping_cart, current_item_name)
        if is_user_choice_switch_item:
            continue            
        
        current_item_quantity = get_item_quantity(current_item_name)

        if is_repeated_item:
            add_repeated_item_quantity(shopping_cart, current_item_name, current_item_quantity)             
        else:
            current_item_price = get_item_price(current_item_name)
            shopping_cart.append([current_item_name, current_item_price, current_item_quantity])
    
    return shopping_cart

def total_items_shopping_cart():
    while True:
        try:
            num_final_items = int(input("Insira o número de produtos a serem cadastrados.\n"))
            if num_final_items <= 0:
                print("Insira um número positivo não nulo.\n")
                continue
            return num_final_items
        except ValueError:
            print("Insira um número válido (ex.: 5 | 20).")

def get_item_name(shopping_cart):
    current_item_name = input(f"Insira o nome do {len(shopping_cart)+1}° item.\n").capitalize()
    user_choice = input(f"O nome do item inserido foi: {current_item_name}\nO nome está correto? \nDigite '1' para Sim. Outro para Não.\n").strip()
    if user_choice == "1":
        return current_item_name, True
    else:
        return current_item_name, False

def validate_repeated_item(shopping_cart, current_item_name):
    is_repeated_item = False
    if len(shopping_cart) != 0:
        for item in shopping_cart:
            if item[0] == current_item_name:
                is_repeated_item = True
    
    if is_repeated_item:
        while True:
            user_choice_repeated_item = input(f"O produto {current_item_name} foi inserido anteriormente. \nDigite '1' para escolher outro produto. \nDigite '0' para adicionar mais unidades do mesmo item.\n")
            if (user_choice_repeated_item == "0"):
                return is_repeated_item, False 
            elif (user_choice_repeated_item == "1"):
                return is_repeated_item, True
            print("Opção inválida.")
    
    return is_repeated_item, False

def get_item_price(current_item_name):
    while True:
        current_item_price = input(f"Insira o valor do item ({current_item_name}).\nR$ ").replace(",", ".")
        try:
            current_item_price = round(float(current_item_price), 2)
            return current_item_price
        except ValueError:
            print("Insira um valor válido (ex.: 10 | 10,50).")

def get_item_quantity(current_item_name):
    while True:
        current_item_quantity = input(f"Insira a quantidade do item ({current_item_name}).\n")
        try:
            current_item_quantity = int(current_item_quantity)
            if current_item_quantity <= 0:
                print("Insira um valor natural não nulo.")
                continue
            return current_item_quantity
        except ValueError:
            print("Insira um valor válido (natural).")

def add_repeated_item_quantity(shopping_cart, current_item_name, current_item_quantity):
    for i, item in enumerate(shopping_cart):
        if item[0] == current_item_name:
            shopping_cart[i][2] += current_item_quantity
                    
def display_shopping_cart_user(shopping_cart):
    final_price_shopping_cart = 0
    quantity_products = 0
    col_width = 30 
    
    print(f"{'Produto:':<{col_width}} | {'Valor (em R$)':<{col_width}} | {'Quantidade':<{col_width}} |")
    
    for item in shopping_cart:
        print(f"{'- ' + item[0]:<{col_width}} | {item[1]:<{col_width}} | {item[2]:<{col_width}} |")
        final_price_shopping_cart += item[1]*item[2]
        quantity_products += item[2]
    print(f"Valor total = R$ {round(final_price_shopping_cart, 2)}.")
    
    while True:
        user_choice = input("Deseja visualizar o preço médio por item?\nDigite '1' para Sim\nDigite '0' para Não.\n")
        if user_choice == "1":
            print(f"Preço médio por item: R$ {(final_price_shopping_cart/quantity_products):.2f}.")
        elif user_choice == "0":
            print("Fim do Programa.")
        else:
            print("Opção inválida.")
            continue
        break
    
def main():
    shopping_cart = []
    shopping_cart = shopping_cart_user(shopping_cart)
    display_shopping_cart_user(shopping_cart)

if __name__ == "__main__":
    main()