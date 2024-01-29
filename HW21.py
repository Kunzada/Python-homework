# Задание №1
# а) Напишите функцию, которая будет загружать информацию сразу с 100 ссылок.
# б) Запустите эту функцию, а также замерьте время.
# в) Добавьте функционал асинхронного запуска, с замером времени. Обязательно посмотрите нагрузку на ЦП в этот момент
#  (через диспетчер задач).

import asyncio 
import time
import requests
import aiohttp 
async def download_info_session(session,url):
    async with session.get(url) as res:
         json_body=await res.text()
         return json_body

async def main():
    async with aiohttp.ClientSession() as session:
        links=['https://jsonplaceholder.typicode.com/todos/1']*100
        results=[]
        for i in links:
            result=download_info_session(session,i)
            results.append(result)
        await asyncio.gather(*results)

async def Download_info(url):
        results=[]
        response=requests.get(url)
        if response.status_code==200:
            results=response.text
        else:
            print("error")
        return results

if __name__=="__main__":
     links=['https://jsonplaceholder.typicode.com/todos/1']*100
     start=time.perf_counter()
     for i in links:
        Download_info(i)
     end=time.perf_counter()
     print("Without async/await: ",end-start)
     start=time.perf_counter()
     asyncio.run(main())
     end=time.perf_counter()
     print("With async/await:",end-start)
    



# if __name__=="__main__":
#     links=['https://jsonplaceholder.typicode.com/todos/1']*100
#     start=time.perf_counter()
#     for i in links:
#         Download_info(i)
#     end=time.perf_counter()
#     print(end-start)
