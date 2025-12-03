# Завдання 1: Написати ф-ю filter яка фільтрує елементи масива по певній умові. Ф-я приймає масив в параметри та функцію яка містить логіку фільтрації (func(x) -> bool). Викликати дану ф-ю декілька разів передавши логіку фільтрації як лямбда.
# Завдання 2: Створіть функцію, яка повертає всі значення зі списку, що не перебувають у діапазоні, зазначеному користувачем. Функція приймає список, початок і кінець діапазону як параметри. Використовуйте механізм генераторів усередині функції.

def filter(arr, func):
        result = []
        for x in arr:
            if func(x):
                result.append(x)
        return result
    
    
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filter(array, lambda x: x % 2 == 0))
print(filter(array, lambda x: x > 5))


def filterInRange(arr, start, end):
    for i in arr:
        if i < start or i > end:
            yield i
            
for i in filterInRange(array, 3, 7):
    print(i)