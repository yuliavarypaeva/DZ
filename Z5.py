# Найдите сумму цифр трехзначного числа n.

# Результат сохраните в перменную res.

# Пример:


# n = 123 -> res = 6 (1 + 2 + 3)

# n = 100 -> res = 1 (1 + 0 + 0)

n = 123
res = 0
a = n // 100
b = n // 10 % 10
c = n % 10
res = a + b + c
print(res)

'''Сумма цифр трехзначного числа

n1 = n // 100 # Нахождение первой цифры числа
n2 = (n % 100) // 10 # Нахождение второй цифры числа
n3 = n % 10 # Нахождение третьей цифры числа
res = n1 + n2 + n3 '''