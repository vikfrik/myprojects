p = int(input('Введи основание системы '))
np = float(input('Введи число '))
k = int(1)
n10 = int(0)
while not np == 0:
    n10 = n10 + (np % 10) * k
    k = k*p
    np = np // 10
print(f"Число в десятичной системе счисления равно = {n10}")
