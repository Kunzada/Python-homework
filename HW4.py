# Напишите программу, где я ввожу логин и пароль. И если данные были введены верно, 
# то мы выводим Authentication completed, иначе Invalid login or password. Правильность логина не зависит от 
# (Логин должен быть user, пароль - qwerty) 

# Input 
# ilyas 
# qwerty 
# Output 
# Invalid Login or Password 
login ="user"
password="qwerty"
userLogin=input("Введите логин:")
userPassword=input("Введите пароль:")
if login==userLogin and password==userPassword:
    print("Authentication completed")
else:
    print("Invalid login or password")
# Напишите программу обмена валют, где я ввожу сумму в тенге и выбираю на какую валюту хочу перевести. 
# (Курс USD – 420, EUR – 510, RUB - 5.8).

currencyTg=int(input("Введите сумму в тенге:"))
while True:
    choose=int(input('''Choose currency: 
           [1]	USD
           [2]	EUR 
           [3]	RUB
           [4]	Exit\n'''))
    result=0
    match choose:
        case 1:
            result= currencyTg/ 420
            print(result)
        case 2:
            result=currencyTg/510
            print(result)
        case 3:
            result=currencyTg/5.8
            print(result)
        case 4:
            break
        case _:
            print("Вы ввели неверный символ!")


# Вася получил первую зарплату и захотел это отпраздновать: провести вечер за любимым сериалом и пиццей.
# Хватит ли Васе денег, если подписка на онлайн кинотеатр стоит s рублей, пицца – p рублей, а всего он заработал m рублей? 
# На вход подается стоимость подписки на онлайн-кинотеатр (s), стоимость пиццы (p) и зарплата Пети (m), а выводится «Да»,
# если он сможет позволить себе покупку, а иначе – «Нет». Например:    
s=int(input("Введите стоимость подписки на онлайн-кинотеатр: "))
p=int(input("Введите стоимость пиццы: "))
m=int(input("Введите свою зарплату: "))
summa=s+p
if(summa<=m):
    print("Да")
else:
    print("Нет")


# Паша очень любит кататься на общественном транспорте, а получая билет, сразу проверяет, счастливый ли ему попался. 
# Билет считается счастливым, если сумма первых трех цифр совпадает с суммой последних трех цифр номера билета.
# Однако Паша очень плохо считает в уме, поэтому попросил вас написать программу, которая проверит равенство сумм и выведет "Счастливый", если суммы совпадают, и "Обычный", если суммы различны.
# На вход программе подаётся строка из шести цифр.
# Выводить нужно только слово "Счастливый" или "Обычный", с большой буквы.
numberUser=input("Введите цифру из 6-ти цифр: ")
cnt=0
firstThree=0
lastThree=0
for i in range(len(numberUser)):
    if i<=2:
        firstThree+=int(numberUser[i])
    else:
        lastThree+=int(numberUser[i])

if(firstThree==lastThree):
    print("Счастливый")
else:
    print("Обычный")

#2.1    
# По данному натуральном n вычислите сумму 1!+2!+3!+...+n!. 
# В решении этой задачи можно использовать только один цикл.
# Пользоваться математической библиотекой math в этой задаче запрещено.
# # i=3
# # while i !=1:
# #     sum*=i
# #     i-=1
userNum=int(input("Введите число: "))
i=1
sum=1
result=0
while i<=userNum:
    sum*=i
    result+=sum
    i+=1

print(result)

#2.2
# По данному натуральному n ≤ 9 выведите лесенку из n ступенек, i-я ступенька состоит из чисел от 1 до i без пробелов.
n=int(input("Введите число:"))
num=''
if(n<=9):
    i=1
    while i <= n:
        num+=f"{i}"
        print(num)
        i+=1
else:
    print("Число должно находится диапозоне до 9")


#2.3    
# Для настольной игры используются карточки с номерами от 1 до N. Одна карточка потерялась. 
# Найдите ее, зная номера оставшихся карточек.
# Дано число N, далее N − 1 номер оставшихся карточек (различные числа от 1 до N). 
# Программа должна вывести номер потерянной карточки.
size=int(input("Введите размер колоды: "))
numbers=list()
i=1
print("Введите цифры:")
while i<=size-1:
    numbers.append(int(input()))
    i+=1
i=1
while i<=size:
    if i in numbers:
        i+=1
    else:
        print(i)
        break
print(f"В колоде нету цифры {i}")


#2.4
import math
# По данному целому числу N распечатайте все квадраты натуральных чисел, не превосходящие N, в порядке возрастания.
digit=int(input("Введите число: "))
ndigit=''
i=1
while i <=digit:
    if(i%math.sqrt(i)==0):
        ndigit+=f'{i} '
    i+=1
print(ndigit)