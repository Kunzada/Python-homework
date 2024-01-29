from tkinter import *
import tkinter as tk
import requests
import json 
def get_info():
    url=f"https://jsonplaceholder.typicode.com/posts/{entry.get()}"
    response=requests.get(url)
    parsed_body=json.loads(response.text)
    label1["text"]=f"Post Id {parsed_body["id"]} \n"\
    f"User id:  {parsed_body["userId"]} \n"\
    f"title:  {parsed_body["title"]} \n"\
    f"body:  {parsed_body["body"]} "
    
root = Tk()
root.geometry("500x500") 
 
label = tk.Label(root,text="Enter id:")
label.pack(anchor=NW, padx=6, pady=6)  
entry = tk.Entry()
entry.pack(anchor=NW, padx=6, pady=6)
 
btn = tk.Button(text="Click", command=get_info)
 
btn.pack(anchor=NW, padx=6, pady=6)
label1 = tk.Label(anchor=NW)
label1.pack()
  
root.mainloop()