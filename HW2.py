# Пользователь вводит строку, состоящую только из двух слов, разделенных пробелом.
# Переставьте эти слова местами. Результат запишите в строку и выведите получившуюся
# строку. 

userStr1=input("Введите строку из двух слов: ")
string=userStr1.split(" ")
print(string[1]+" "+string[0])

# 2 Пользователь вводит строку, состоящую из слов, разделенных пробелами. Определите,
# сколько в ней слов. Используйте для решения задачи метод count(). Например, 

userStr2=input("Введите строку: ")
print("Количество слов: "+userStr2.count(" ")+1)

# 3 Наступил Новый год, а Вася все еще ставит в документе прошедший, 2020, год.
# Помогите автоматизировать процесс замены номера старого года на новый. Используйте для
# решения метод replace(). Например, 

txt="В 2020 году я буду все делать"
print(txt.replace("2020","2024"))

# Петя решил подвести итоги четверти и посчитать, сколько он получил пятерок,
# четверок, троек и двоек. Пользователь вводит список цифр через пробел. В первой строке вам
# необходимо вывести количество пятерок, четверок, троек и двоек через пробел. Во второй –
# средний балл Васи. 
    
userMark=input('Введите свои оценки через пробел:')
marks=userMark.split(" ")
five=0
four=0
three=0
two=0
sum=0
for i in range(len(marks)):
    marks[i]=int(marks[i])
for i in marks:
    if i==5:
        five+=1
    elif i==4:
        four+=1
    elif i==3:
        three+=1
    elif i==2:
        two+=1
    sum+=i
avarage=sum/len(marks)
print(f"5:{five} 4:{four} 3:{three} 2:{two}")
print(f"{avarage}")

# 2 Петя очень умный школьник, и поэтому уверен, что оценки в жизни не главное! И,
# чтобы доказать это всем, он придумал план: заменить свои плохие оценки на хорошие. А
# чтобы было не очень заметно, Петя решил заменить двойки на трояки. Да вот одна проблема:
# оценок много, а времени мало. Помогите мальчику автоматизировать процесс.
# Обратите внимание, числа вводятся и выводятся в строку, при этом между элементами
# стоит пробел. 

marksUser2=input("Введи свои оценки:")
marks2=marksUser2.split(" ")
for i in range(len(marks2)):
    marks2[i]=int(marks2[i])
for i in range(len(marks2)):
    if marks2[i]==2:
        marks2[i]=3
print(marks2)

# 1. Напишите программу которая будет шифровать текст шифром Цезаря.
# В шифре Цезаря используется прописные буквы латинского алфавита и пробел
# ' abcdefghijklmnopqrstuvwxyz'
# Схема работы: Шифр Цезаря заключается в замене каждого символа входной строки на
# символ, находящийся на несколько позиций левее или правее его в алфавите.
# Для всех символов сдвиг один и тот же. Сдвиг циклический, если к последнему символу
# алфавита применить единичный сдвиг, то он заменится на первый символ, и наоборот.
# Пользователь вводит число – сдвиг шифрования. Если число положительное сдвиг
# вправо, отрицательное влево. На второй строке вводится текст.
# Используйте функцию chr(),ord()
caesar=' abcdefghijklmnopqrstuvwxyz'
cntShift=int(input("Введите количество сдвигов:"))
strToShift=input("Введите слово для сдвига на латинице:").lower()
result=''
for i in strToShift:
    old_place=caesar.find(i)
    new_place=old_place+cntShift
    if i in caesar:
        result+=caesar[new_place]
    else:
        result+=i
print(result)

# 2. Пользователь вводит с клавиатуры название фрукта. Необходимо вывести на экран
# количество раз, сколько фрукт встречается в кортеже в качестве элемента.
fruitUser=input("Введите навание фрукта: ")
fruit=('ананас','банан','мандарин','банан','банан')
cnt=0
for i in fruit:
    if i==fruitUser:
        cnt+=1

if(cnt==0):
    print("Этот фрукт не встречается в кортеже")
else:
    print(cnt)
# 3. Добавьте к заданию 1 подсчет количества раз, когда название фрукта является частью
# элемента. Например, banana, apple, bananamango, mango, strawberry-banana. В примере выше
# banana встречается три раза.

# 4. Есть кортеж с названиями производителей автомобилей (название производителя
# может встречаться от 0 до N раз). Пользователь вводит с клавиатуры название производителя
# и слово для замены. Необходимо заменить в кортеже все элементы с этим названием на слово
# для замены. Совпадение по названию должно быть полным.
cars=('BMW','Honda','Volkswagen','BMW','Ford','Hyundai','BMW','Audi')
brand1=input("Введите название производителя: ")
brand2=input("Введите слово для замены: ")
carsList=list(cars)
for i in range(len(carsList)):
    if carsList[i]==brand1:
        carsList[i]=brand2

multi=tuple(carsList)
print(multi)

# Напишите программу, которая считывает с консоли числа (по одному в строке) до тех
# пор, пока сумма введённых чисел не будет равна 0 и сразу после этого выводит сумму
# квадратов всех считанных чисел.
# Гарантируется, что в какой-то момент сумма введённых чисел окажется равной 0, после
# этого считывание продолжать не нужно.
# В примере мы считываем числа 1, -3, 5, -6, -10, 13; в этот момент замечаем, что сумма
# этих чисел равна нулю и выводим сумму их квадратов, не обращая внимания на то, что
# остались ещё не прочитанные значения.
print("Введите цифры:")
num=int(input())
s=num
powSum=num**2
while s!=0:
    num=int(input())
    s=s+num
    powSum+=num**2

print(powSum)