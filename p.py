import tkinter as tk

def show_input():
    user_text = entry.get()  # получаем текст из Entry
    label.config(text=f"Вы ввели: {user_text}")

root = tk.Tk()
root.title("Пример Input")
root.geometry("300x150")

entry = tk.Entry(root)  # поле ввода
entry.pack(pady=10)

button = tk.Button(root, text="Показать", command=show_input)  # кнопка
button.pack(pady=5)

label = tk.Label(root, text="")  # метка для вывода
label.pack(pady=10)

root.mainloop()
