NAME = input("Введите свое имя ")
print(NAME)

AGE = int(input("Введите свой возраст "))
print("Меня зовут %s, мне %s лет" % (NAME, AGE))

print(NAME*5)

NAME = input("Введите свое имя ")
AGE = int(input("Введите свой возраст "))
if AGE>18:
    print("Привет %s, ты старше меня" % NAME)
elif AGE==18:
    print("Привет %s, ты мой ровесник" % NAME)
else:
    print("Привет %s, ты младше меня" % NAME)

print(NAME[1:-1])
print(NAME[::-1])
print(NAME[:5])

AGE1 = input("Введите ваш возраст ")
print(len(NAME))
one = int(AGE1[0])
two = int(AGE1[1])
print(one+two)
print(one*two)

print(NAME.lower())
print(NAME.upper())

for i in NAME:
    if i == " ":
        print("В имени есть пробелы")
    elif AGE > 150:
        print("Старше 150")
    elif AGE < 0:
        print("Младше 0")
    else:
        print("Введенные данные верны")


TASK = int(input("2+2*2="))
if TASK == 6:
    print("Вверно")
else:
    print("Неверно")