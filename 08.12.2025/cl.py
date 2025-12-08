# Створіть функцію, що повертає список з усіма парними числами, від 0 до 100000.
# Використовуючи механізм декораторів, порахуйте скільки секунд знадобилося для 
# обчислення всіх чисел. Відобразіть на екран кількість секунд і всі парні числа від 0 до 100 000.
import time

def Timer(func):
    def out(*args):
        start=time.time()
        res=func(*args)
        end=time.time()
        elapsed_time = end - start
        print(elapsed_time, "seconds")
        return res
    return out

@Timer
def even_numbers():
    even_nums = [i for i in range(100001) if i % 2 == 0]
    print(even_nums)
    return even_nums

even_numbers()