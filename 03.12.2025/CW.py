# Є список чисел. Створи новий список, де будуть тільки числа, більші за 10.
# Вхід: [3, 14, 1, 25, 9, 100]
# Вихід: [14, 25, 100]

# Завдання 2: Підрахунок
# Порахуй, скільки разів елемент зустрічається у списку.
# Вхід:
# ['apple', 'banana', 'apple', 'orange', 'apple']
# слово: 'apple'
# Вихід:3

# Завдання 3: Унікальні елементи з двох set
# Отримай унікальні елементи з двох set.
# Вхід:[1, 2, 3], [3, 4, 5]
# Вихід:{1, 2, 4, 5}

input_list = [3, 14, 1, 25, 9, 100]
output = [i for i in input_list if i > 10]
print(output)


input_list2 = ['apple', 'banana', 'apple', 'orange', 'apple']
count = 0
for i in input_list2:
    if i == 'apple':
        count += 1
print(count)


set1 = {1, 2, 3}
set2 = {3, 4, 5}
unique= set1.difference(set2).union(set2.difference(set1))
print(unique)