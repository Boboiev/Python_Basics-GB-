number = int(input("Введите число:"))
x = number
last = x % 10
while x:
    cur = x % 10
    if cur > last:
        last = cur
        if last == 9:
            break

    x = x // 10
print(f"В числе {number} самой большой цифрой является цифра {last}")
