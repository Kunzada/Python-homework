# 1. Задание 1 (cycle): Напишите функцию cycle_string, которая принимает строку и целое
# число n в качестве входных данных и возвращает строку, являющуюся результатом
# повторения входной строки n раз. Например, cycle_string("abc", 3) должна
# вернуть "abcabcabc".
from itertools import repeat,count,starmap,accumulate,dropwhile
def cycle_string(string,num):
    data =[f"{i}" for i in repeat(string,num)]
    return ''.join(data)
print(cycle_string("abc",3))
# 2. Задание 2 (count): Напишите функцию count_from, которая принимает целое
# число start и целое число n в качестве входных данных и возвращает список из n целых
# чисел, начиная от start. Например, count_from(5, 3) должна вернуть [5, 6, 7].
def count_from(start ,n):
    cnt=0
    rtnElem=[]
    for i in count(start,1):
        if(cnt>=n):
            break
        
        rtnElem.append(i)
        cnt+=1
    return rtnElem
print(count_from(5,3))
# 3. Задание 3 (starmap): Напишите функцию multiply_elements, которая принимает
# список кортежей, где каждый кортеж содержит два целых числа, и возвращает список
# произведений чисел в каждом кортеже. Например, multiply_elements([(1, 2), (3, 4), (5,
# 6)]) должна вернуть [2, 12, 30].
def multiply_elements(elem):
    data=list(starmap(lambda x,y:x*y ,elem))
    return data
elements=[(1,2),(3,4),(5,6)]
print(multiply_elements(elements))
# 4. Задание 4 (accumulate): Напишите функцию accumulate_sums, которая принимает
# список целых чисел и возвращает список накопленных сумм.
# Например, accumulate_sums([1, 2, 3, 4, 5]) должна вернуть [1, 3, 6, 10, 15].
def accumulate_sums(elem):
    data=list(accumulate(elem))
    return data
elements1=accumulate_sums([1, 2, 3, 4, 5])
print(elements1) 
# 5. Задание 5 (dropwhile): Напишите функцию drop_less_than, которая принимает список
# целых чисел и целое число n в качестве входных данных и возвращает список целых
# чисел из входного списка, начиная с первого числа, которое не меньше n.
# Например, drop_less_than([1, 2, 3, 4, 5], 3) должна вернуть [3, 4, 5].
def drop_less_than(elem,n):
    data=list(dropwhile(lambda i:i!=n,elem))
    return data
elements3=drop_less_than([1, 2, 3, 4, 5], 3)
print(elements3)