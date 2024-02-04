# Выполните следующие задания:
# Задание №1
# а) Загрузите одиночный json – объект с сайта jsonplaceholder, используя библиотеку requests.
# б) Сохраните его в файл.
# а) Загрузите одиночный json – объект с сайта jsonplaceholder, используя библиотеку aiohttp.
# б) Сохраните его в файл.

import requests 
import aiohttp
import asyncio
url="https://jsonplaceholder.typicode.com/posts/1"
response=requests.get(url)
response.raise_for_status()
with open("1.txt","a") as file:
    file.write(response.text)
    file.close()

async def get_page(session,url):
    async with session.get(url) as r: 
        return await r.text()

async def main():
    async with aiohttp.ClientSession() as s:
        text=await get_page(s,"https://jsonplaceholder.typicode.com/posts/1")
        with open("2.txt","a") as file:
            file.write(text)
            file.close()


if __name__=="__main__":
    asyncio.run(main()) 




