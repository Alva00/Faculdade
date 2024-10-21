list_word = ["akepqoflsw", ""]
for letter in list_word[0]:
    if letter not in "aeiou":
        if letter not in list_word[1]:
            list_word[1] += letter
print(f'A palavra {list_word[0]} contém {len(list_word[1])} consoantes, sendo elas: {list_word[1]}.')
