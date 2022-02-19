income = int(input("Введите значение выручки:"))
cost = int(input("Введите значение издержек:"))
value = income / cost
if value > 1:
    profitability = ((income - cost) / income) * 100
    print("Поздравляю, Вы в плюсе! Рентабельность:", profitability, "%")
    empl = int(input("Ввведите количество сотрудников:"))
    emplprofit = ((income - cost) / empl)
    print("Прибыль фирмы в расчёте на одного сотрудника составляет:", emplprofit)
elif value == 1:
    print("Работая в ноль, денег много не заработаешь :-(")
else:
    print("Что-то пошло не так и с этим нужно разобраться, - работаете в минус.")
