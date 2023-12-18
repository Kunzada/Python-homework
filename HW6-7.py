import math
import random
import time
# # Задание №1.
# # Напишите программу для создания списка, длина которого равна N.
# # После создания списка нужно подсчитать нечетные и четные числа.
# # Если нечетных чисел больше, чем четных, вывод должен быть «Нет», в остальных ключах «Да». 
numbers=[]
size=int(input("Введите размер списка:"))
for i in range(size):
    numbers.append(random.randint(1,30))
print(numbers)
even=list()
odd=list()
for i in numbers:
    if(i%2==0):
        even.append(i)
    else :
        odd.append(i)

if(len(odd)>len(even)):
    print(f"Четные:{even}")
    print(f"Нечетные:{odd}")
    print("Нет")
else:
    print(f"Четные:{even}")
    print(f"Нечетные:{odd}")
    print("Да")
time.sleep(1.5)
# # Создайте вложенный список размером 3*3 через функцию. И посчитайте сумму элементов главной диагонали. 
# import random;

print("Task 2")
time.sleep(1)
def Print(list1):
    for i in range(3):
        for j in range(3):
            print(list1[i][j],end=' ')
        print()
def Initialization(list1):
    for i in range(3):
        row=[]
        for j in range(3):
            row.append(random.randint(0,9))
        list1.append(row)

def CalculateMainDiagonal(list1):
    cnt=[]
    for i in range(3):
        for j in range(3):
            if(i==j):
                cnt.append(list1[i][j])
    return cnt
A=[]
Initialization(A)
Print(A)
diagonals=CalculateMainDiagonal(A)
print(f"Diagonals: {diagonals[0]} + {diagonals[1]} + {diagonals[2]} = {diagonals[0]+diagonals[1]+diagonals[2]}")

time.sleep(1.5)
# Задание №3.
# Написать рекурсивную функцию, которая по заданному целому числу возвращает
# n-e число Фибоначчи. Ряд Фибоначчи 0, 1, 1, 2, 3, 5, 8, 13,…… 
# fibonacci number 1 = 1 
# fibonacci number 2 = 1 
# fibonacci number 3 = 2 
# fibonacci number 4 = 3 
# fibonacci number 5 = 5 
# fibonacci number 6 = 8 
# fibonacci number 7 = 13 
print("Task 3")
time.sleep(1)
def Fibonacci(num):
    if num <=1:
        return num
    return Fibonacci(num-1)+Fibonacci(num-2)

print(Fibonacci(7))
time.sleep(1.5)
# Напишите функцию, которая проверяет является ли число степенью двойки. Если истинно выведите True, иначе False.
print("Task 4")
time.sleep(1)
def checkTwo(number):
    while number %2==0:
        number=number/2
    if(number==1):
        print("True")
    else :
        print("False")
checkTwo(6)
checkTwo(12)
checkTwo(64)
time.sleep(1.5)

# Реализовать инженерный калькулятор, для всех арифметических действий, включая нахождение факториала, Фибоначчи, и всех тригонометрических функций, также возведения числа в степени. 
# В ходе решения, допустимо использования модуля math, функции определяемой пользователем, рекурсивной функции и лямбда-функции. 
# Реализуйте диалог с пользователем.

print("Task 5") 
time.sleep(1)
Arithmetic='''
Введите выбор:
1.+     3./
2.-     4.* 
  5.Выход
'''
while True:
    choose=int(
        input('''
Введите выбор:
1.Найти факториал
2.Найти Фибоначчи
3.Арифмическое действие
4.Тригонометрические функций
5.Выход
    '''))
    match choose:
        case 1:
            number=int(input("Введите число:"))
            print(f"Факториал {number}:{math.factorial(number)}")
        case 2:
            number=int(input("Введите число:"))
            print(Fibonacci(number))
        case 3:
            while True:
                first=int(input("Введите первое число:"))
                second=int(input("Введите второе число:"))
                choose2=int(input(Arithmetic))  

                result=0
                if choose2==1 :
                    result=first+second
                    print(f"{first}+{second}={result}")
                elif choose2==2:
                    result=first-second
                    print(f"{first}-{second}={result}")
                elif choose2==3:
                    result=first*second
                    print(f"{first}*{second}={result}")
                elif choose2==4:
                    result=first/second
                    print(f"{first}/{second}={result}")
                elif choose2==5:
                    break
                else:
                    print("Вы ввели неверное пункт меню")

        case 4:
            while True:
                number=int(input("Введите число:"))
                choose2=int(input("Введите выбор:\n"+
                      "1.sin(x)\n"+
                      "2.cos(x)\n"+
                      "3.tg(x)\n"+
                      "4.asin(x)\n"+
                      "5.acos(x)\n"+
                      "6.atg(x)\n"+
                      "7.Выход\n"
                      ))
                match choose2:
                    case 1:
                        print(math.sin(math.radians(number)))
                    case 2:
                        print(math.cos(math.radians(number)))
                    case 3:
                        print(math.tan(math.radians(number)))
                    case 4:
                        print(math.asin(math.radians(number)))
                    case 5:
                        print(math.acos(math.radians(number)))
                    case 6:
                        print(math.atan(math.radians(number)))
                    case 7:
                        break
        case 5:
            break
        case _:    
            print("Вы ввели неверное пункт меню")
time.sleep(1.5)
# Пользователю предоставляется список кандидатов, каждый из голосующих делает свой выбор. 
# Выбранный кандидат добавляется в список. 
# В итоге имеется неизменяемый список кандидатов.
# Определить победителя, в зависимости от количества встречаемости в списке кандидата. 
# Определить количество голосов победителя.
# В случае, если будет двое победителей, сделать сортировку по длине слова между ними и выбрать победителя
#  с минимальным количеством букв в имени. 
print("Task 2.1")
time.sleep(1)
candidates=["Аскаров","Бекмуханов","Ернур","Пешая","Карим","Шаримазданов"]
new_candidates=()
for i in range(3):
    print(f"Голосующий {i+1}" )
    print(f"Кандидаты в выборы: {candidates}")
    new_Value=input(f"Вы отдаете голос за:\n")
    if (new_Value in candidates):
        candidates.append(new_Value)
    else:
        print("Такого кандидата нет в списке. Попробуйте еще раз.")
vote_cnt={candidate:candidates.count(candidate) for candidate in set(candidates)}
max_vote=max(vote_cnt.values())
winners=[]
for candidate,votes in vote_cnt.items():
    if votes==max_vote:
        winners.append(candidate)
if len(winners)>1:
    winners.sort(key=lambda x:len(x))
print(f"Победитель выборов:{winners[0]}")
# Кандидаты в выборы: Аскаров, Бекмуханов, Ернур, Пешая, Карим, Шаримазданов и т.д.
# Вы отдаете голос за: 
# Победитель выборов: Ернур.
