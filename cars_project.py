print("Это калькулятор для примерного подсчета времении на накопление определенной суммы.")

p = float(input("Введите сумму которую хотите накопить:"))
x = float(input("Введиите сколько денег вы готовы откладывать каждый месяц:"))

if p > 0 and x > 0:
    print("Столько лет придется копить:", ((p / x) / 12 ))
    print("Столько месяцов придется копить:", (p / x) / 12 * 360 / 30 )
    print("Столько дней придется копить:", (p / x) / 12 * 360 )

else:
    print("Вы что-то напуталии: ОШИБКА")





