"""Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали n журавликов.

Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

Выведите кортеж из количества журавликов, сделанных Петей, Катей и Сережей.

Пример:


n = 6 -> (1, 4, 1)
n = 24 -> (4, 16, 4)
n = 60 -> (10, 40, 10)
"""
n = 6

b = (n//3)*2
a = b//4
c = b//4

print(f"{a}, {b}, {c}")

"""Бумажные журавлики

n1 = n // 6
n2 = n // 6
n3 = (n // 6) * 4
print(n1, n3, n2) """