# а) Напишите функцию, которая будет создавать файл, с задержкой 1 секунду.
# б) Запустите циклом 100 таких функций, а также замерьте время.
# в) Добавьте функционал многопоточного запуска, с замером времени.
import asyncio
import time
import threading 
import os
def create_file(file_name):
    asyncio.sleep(1)
    open(file_name,"w") 
if __name__=="__main__":
    for i in range(1,101):
        try:
            os.remove(f"{i}.txt")
        except:
            print("The file has already been deleted")
    s_time=time.perf_counter()
    for i in range(1,101):
        create_file(f"{i}.txt")
    e_time=time.perf_counter()
    print("Without thread:",e_time-s_time)
    thread_list=[]
    for i in range(1,101):
        start_time=time.perf_counter()
        thread=threading.Thread(target=create_file,args=(f"{i}.txt",))
        thread_list.append(thread)
        thread.start()
    for i in thread_list:
        thread.join()

    end_time=time.perf_counter()
    print("With thread:",end_time-start_time)
