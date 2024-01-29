# # Задание №1
# # Напишите программу, которая использует многопроцессорность для сортировки большого списка чисел. 
# # a)	Создайте большой список, который содержит 100000 случайных чисел
# # b)	Создайте одну копию с помощью list.copy()
# # c)	Отсоритруйте копию с помощью метода sort. Засеките, сколько времени это заняло
# # d)	Разедилите оригинальный список на 10000 кусочков. 
# # e)	Отсоритуйте каждый кусочек в отдельном процессе. 
# # f)	Соедените отсрортированные кусочки методом heapq.merge(*sorted_chunks), где sorted_chunks – список отсорированных списков.
# # g)	Засекити, сколько времени это заняло.

import random 
import asyncio
from multiprocessing import Pool
import time 
import heapq
big_list=[]

for i in range(1,100_000):
    big_list.append(random.randint(1,100))

copy_big_list=big_list.copy()
s_time=time.perf_counter()
copy_big_list.sort()
e_time=time.perf_counter()

size_chunk=len(big_list)//10_000
chunk=[big_list[i:i+size_chunk] for i in range(0,len(big_list),size_chunk)]


def sort_chunk(chunk):
    return sorted(chunk)


if __name__=="__main__":
    with Pool() as p:
        sorted_chunks=p.map(sort_chunk,chunk)

    start_time=time.time()
    result=list(heapq.merge(*sorted_chunks))
    end_time=time.time()
    print("Сортировка :",e_time-s_time) #0.008579799992730841
    print("соединение кусочков",end_time-start_time) #0.41901063919067383

