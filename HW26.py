from tkinter import *
import tkinter as tk
import requests
import json 

class Application(tk.Tk):
    def __init__(self):
        super().__init__() 
        self.geometry("500x500") 
        self.create_elem()

    def create_elem(self):
        self.label = tk.Label(self,text="Enter id:")
        self.label.pack(anchor=NW, padx=6, pady=6)  
        self.entry = tk.Entry()
        self.entry.pack(anchor=NW, padx=6, pady=6)
        self.btn = tk.Button(text="Click", command=self.get_info)
        self.btn.pack(anchor=NW, padx=6, pady=6)
        self.label1 = tk.Label(anchor=NW)
        self.label1.pack()

    def get_info(self):
        url=f"https://jsonplaceholder.typicode.com/posts/{self.entry.get()}"
        response=requests.get(url)
        parsed_body=json.loads(response.text)
        self.label1["text"]=f"Post Id {parsed_body["id"]} \n"\
        f"User id:  {parsed_body["userId"]} \n"\
        f"title:  {parsed_body["title"]} \n"\
        f"body:  {parsed_body["body"]} "

app=Application()
app.mainloop()