# 1. Напишите функцию superset(), которая принимает 2 множества. Результат работы функции: вывод в консоль одного из сообщений в зависимости от ситуации:
# 1 - «Супермножество не обнаружено»
# 2 – «Объект {X} является чистым супермножеством» 
# 3 – «Множества равны»
def superset(set1,set2):
    if set1<set2:
        print(f"Объект {set2} является чистым супермножеством")
    elif set1>set2:
        print(f"Объект {set1} является чистым супермножеством")
    elif set1==set2:
        print("Множества равны")
    else:
        print("Супермножество не обнаружено")

set1={9,3,4,1}
set2={7, 10 }
set3={4}
superset(set1,set2)
superset(set1,set3)



# 2. Создайте программу «Англо-французский словарь». 
# Нужно хранить слово на английском языке и его перевод на французский. 
# Требуется реализовать возможность добавления, удаления, поиска, замены данных. 
# Используйте словарь для хранения информации.

print("________________________________________________________________________")
print("|Note:После вызова каждого пункта лучше вызвать 5 чтобы видеть результат|")
print("|_______________________________________________________________________|")
dictionary={
    "car":"voiture",
    "woman":"femme",
    "table":"tableau"}

while True:
   
    choice=int(input("\nВведите выбор\n"+
          "1.Добавления\n"+
          "2.Удаления\n"+
          "3.Поиск\n"+
          "4.Замены данных\n"
          "5.Просмотр словаря\n"+
          "6.Выйти\n"))

    match(choice):
        case 1:
            eng=input("Введите слово на английском: ")
            fr=input("Введите слово на французком: ")
            dictionary.update({f"{eng}" : f"{fr}"})
      
        case 2:
            eng=input("Введите слово на английскои для удаления:")
            if eng in dictionary:
                del dictionary[eng]
                print(f"Слово {eng} успешно удален из словаря")
            else: 
                print("Слово не найден")
        case 3:
            eng=input("Введите слово на английскои для поиска:")
            word=dictionary.get(eng,"Слово не найдено")
            print(word)
        case 4:
            choice =int(input("Введите выбор\n"+
                          "1.Изменить английское слово\n"+
                          "2.Изменить французкое слово\n"))
            match(choice):
                case 1:
                    eng=input("Введите слово на английскои для поиска:")
                    fr=input("Введите слово на французкое для замены:")
                    dictionary[eng]=fr
                case 2:
                    fr=input("Введите слово на французкое для поиска:")
                    eng=input("Введите слово на английскои для замены:")
                    # keys=[key for key in dictionary if dictionary[key]==fr ]
                    # print(keys)4
                    for key in dictionary:
                        if dictionary[key]==fr:
                            dictionary[key]=eng
                            break
        case 5:
            print(dictionary)
        case 6:
            print("Goodbye!")
            break

# 3. Предоставлен список натуральных чисел. Требуется сформировать из них множество. 
# Если какое-либо число повторяется, то преобразовать его в строку по образцу: 
# например, если число 4 повторяется 3 раза, то в множестве будет следующая запись:
# само число 4, строка «44» (второе повторение, т.е. число дублируется в строке),
# строка «444» (третье повторение, т.е. строка множится на 3).
# Реализуйте вывод множества через функцию set_gen().
numbers = [1, 2, 2, 4, 5]
def set_gen(numbers):
    index=0
    while index<len(numbers):
        cnt=numbers.count(numbers[index])
        if cnt>1:
            numbers[index]=str(numbers[index])*cnt
        index+=1
    return set(numbers)
print(numbers)
print(set_gen(numbers))
# 1. Иван решил создать самый большой словарь в мире. Для этого он придумал функцию biggest_dict(**kwargs),
# которая принимает неограниченное количество параметров «ключ: значение» и обновляет созданный им словарь my_dict,
# состоящий всего из одного элемента «first_one» со значением «we can do it». Воссоздайте эту функцию.
# Output:
# {'first_one': 'we can do it', 'k1': 22, 'k2': 31, 'k3': 11, 'k4': 91, 'name': 'Елена', 'age': 31, 'weight': 61, 'eyes_color': 'grey'}
my_dict={}
def biggest_dict(**kwargs):
    my_dict.update(**kwargs)
biggest_dict(first_one='we can do it',k1=22,k2=31)
print(my_dict)

#2 Создайте словарь с количеством элементов не менее 5-ти.
# Поменяйте местами первый и последний элемент объекта. Удалите второй элемент.
# Добавьте в конец ключ «new_key» со значением «new_value». Выведите на печать итоговый словарь.
# Важно, чтобы словарь остался тем же (имел тот же адрес в памяти).

dictionary2={
    1:"Car",
    2:"Table",
    3:"Map",
    4:"Pencil",
    5:"Pen"
}
lenght=len(dictionary2)
# print(dictionary2[lenght])
# меняем местами первый и послений элемент
temp=dictionary2[1]
dictionary2[1]=dictionary2[lenght]
dictionary2[lenght]=temp
#удаляем 2 элемент
del dictionary2[2]
# Добавляем в конец ключ «new_key» со значением «new_value»
dictionary2['new_key']='new_value'
print(dictionary2)