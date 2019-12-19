"""
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""
#
# a = "1234"
# print(a)
# print(type(a))
#
# a = int(a)
# print(a)
# print(type(a))

a = input()
b = a
c = a + a
d = a + a + a
result = int(b) + int(c) + int(d)
print(result)