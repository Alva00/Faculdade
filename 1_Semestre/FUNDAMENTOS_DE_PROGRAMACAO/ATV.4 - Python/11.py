random_list = [num for num in range(0, 50, 5)]
another_random_list = [num for num in range(-50, -100, -5)]
more_one_random_list = [num for num in range(200, 220, 2)]

completed_list = []

for i in range(len(random_list)):
    completed_list.append(random_list[i])
    completed_list.append(another_random_list[i])
    completed_list.append(more_one_random_list[i])
    
print(completed_list)