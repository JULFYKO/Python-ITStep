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

# *Завдання 4: Сортування списку кортежів
# Відсортуйте список кортежів по другому елементу.
# Вхід: [(1, 5), (2, 1), (3, 4)]
# Вихід: [(2, 1), (3, 4), (1, 5)]
 
# *Завдання 5: Плоский список
# Зроби з вкладеного списку звичайний.
# Вхід:[[1, 2], [3, 4, 5], [6]]
# Вихід:[1, 2, 3, 4, 5, 6]
 
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


input_list3 = [(1, 5), (2, 1), (3, 4)]
sorted_list = sorted(input_list3, key=lambda x: x[1])
print(sorted_list)


input_list4 = [[1, 2], [3, 4, 5], [6]]
flat_list = [j for i in input_list4 for j in i]
print(flat_list)