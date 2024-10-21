list_all_questions = ["Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou com a vítima?"]
list_answer_questions = []
quantify_true_user_answers = 0

print("Responda as perguntas com 'S' (Sim) ou 'N'(Não).")
for question in list_all_questions:
    answer = input(f'{question}\n').lower()
    if "s" in answer:
        quantify_true_user_answers += 1

if quantify_true_user_answers == 5:
    print("Assassino")
elif quantify_true_user_answers >= 3:
    print("Cúmplice")
elif quantify_true_user_answers == 2:
    print("Suspeita")
else:
    print("Inocente")