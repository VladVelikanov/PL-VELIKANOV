import json
import requests
from tkinter import *
from tkinter import ttk


window = Tk()
window.geometry('480x480')
variant = Entry(window, width=15)
variant.grid(column=0, row=0)
info = Text(window, width=50, height=25, wrap=WORD)
info.grid(column=3, row=1)

def check():
    url_address = "https://api.github.com/users/"+variant.get()
    req = requests.get(url_address)
    user_json = req.json()
    ans = {
        'company': user_json['company'],
        'created_at': user_json['created_at'],
        'email': user_json['email'],
        'id': user_json['id'],
        'name': user_json['name'],
        'url': user_json['url']}
    json_ans = json.dumps(ans, indent=2)
    info.insert('1.0', json_ans)
button = Button(window, text="Клик", command=check)
button.grid(column=1, row=0)


window.mainloop()