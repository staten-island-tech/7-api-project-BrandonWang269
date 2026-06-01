import requests
import tkinter as tk
window = tk.Tk()
window.title("Disney Character Search")
window.geometry ("500x400")
def search():
    name = entry.get().lower()
    link = "https://api.disneyapi.dev/character"
    response = requests.get(link)
    data = response.json()
    found = False   
    for disney in data["data"]:
        if disney["name"].lower() == name:
            result.config(text=f"Name: {disney['name']}\nFilms: {', '.join(disney['films'])}")
            found = True
            break
        if not found:
            result.config(text="Character not found.")
titel_label = tk.Label(window, text="Search Disney Character")
titel_label.pack(pady=20)
entry = tk.Entry(window, width=30)
entry.pack(pady=10)
search_button = tk.Button(window, text="Search", command=search)
search_button.pack(pady=10)
result = tk.Label(window, text="", wraplength=450)
result.pack(pady=20)
window.mainloop()