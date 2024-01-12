from datetime import datetime, timedelta
import os
# Задание №1.

# Реализуйте программу, чтобы найти дату первого понедельника данной недели. 
# Date: 2015, 50
# Output: пн 14 декабря 00:00:00 2015

def first_monday(year,week):
    firstday=datetime(year,1,1)
    day_of_first_monday=(7-firstday.weekday())%7
    return firstday+timedelta(days=day_of_first_monday+(week-1)*7)
firstMonday=first_monday(2015,50)

print(firstMonday.strftime("%a %d %B %H:%M:%S %Y"))
# Задание №2
# Реализуйте программу, для преобразования двух разностей дат в дни, часы, минуты и секунды
first_date=datetime(2019, 12, 29)
second_date=datetime.now()
result=second_date-first_date
# print(result, type(result))
print("days:",result.days,"hour:",result.seconds//3600,"minute:",(result.seconds//60)%60,"second:",result.seconds%60)
# print(result.strftime("%a %d %B %H:%M:%S %Y"))
# Задание №3
# Дан текстовый файл. Необходимо создать новый файл убрав из него все неприемлемые слова. Список неприемлемых слов находится в другом файле.
with open("File1.txt","r") as ftext,open("ListOfWords.txt",'r') as fword,open("newFile.txt","w") as fresult:
    words=[word.strip() for word in fword.readlines()]
    data=ftext.readlines()
    for lines in data:
        cleanLine=' '.join(word for word in lines.split() if word.lower() not in words)
        fresult.write(cleanLine+ "\n")
 
# Задание №4
# Пользователь с клавиатуры вводит названия файлов, до тех пор, пока он не введет слово quit. 
# После завершения ввода программа должна объединить содержимое всех перечисленных пользователем файлов в один.
filenames=set()
while True:
    file=input("Enter file name:")
    if file=="quit":
        break
    filenames.add(file)
filedescription=list()
for name in filenames:
    try:
        with open(name,"r") as file, open("allFiles.txt","a")as fw:
            filedescription=file.readlines()
            filedescription.append("\n")
            fw.writelines(filedescription)
    except IOError:
        print(f"{name}","файл не существует")

# Задание №5
# В текущей папке лежат две другие папки: video и sub. Создайте новую папку watch_me и переложите туда содержимое указанных папок (сами папки класть не надо).

if not os.path.isdir("watch_me"):
     os.mkdir("watch_me")
sub= os.listdir(".\sub")
video=os.listdir(".\\video")
print(sub)
print(video)
for i in sub:
     os.replace(f".\sub\{i}",f"watch_me/{i}")
for i in video:
     os.replace(f".\\video\{i}",f"watch_me/{i}")

# Задание №6
# В текущей папке лежат файлы типа Nina_Stoletova.jpg, Misha_Perelman.jpg и т.п. Переименуйте их переставив имя и фамилию местами.
string="Nina_Stoletova".split("_")
string2="Misha_Perelman".split("_")
os.replace("Nina_Stoletova.jpg",f"./{string[1]}_{string[0]}.jpg")
os.replace("Misha_Perelman.jpg",f"./{string2[1]}_{string2[0]}.jpg")
