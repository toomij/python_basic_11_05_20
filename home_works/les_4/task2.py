"""2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и генератор."""
import random

# var_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

var_list = [random.randint(0, 10) for _ in range(12)]


def next_bigger(array):
    s = []
    n = len(array)
    for i in range(n - 1):
        if i < n - 1:
            if var_list[i + 1] > var_list[i]:
                s.append(var_list[i + 1])
        else:
            break

    return s


print(next_bigger(var_list))
