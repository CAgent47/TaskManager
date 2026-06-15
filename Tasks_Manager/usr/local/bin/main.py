import datetime
import tkinter
from tkinter import messagebox
import os

def Show_info():
    data_show = tkinter.Text(master, width=45, height=15)
    data_show.grid(row=4, column=1)
    with open("Tsk.txt", "r") as data_db:
        content = data_db.read()

    data_show.insert("1.0", content)
    data_show.config(state="disabled")


def delete_file():
    if os.path.exists("Tsk.txt"):
        result = messagebox.askyesno("Warning", "Delete task information?")
        if result:
            with open("Tsk.txt", "w", encoding="utf-8") as f:
                pass
            messagebox.showinfo("Notification", "Deleted File Information")
        else:
            messagebox.showinfo("Success", "OK")
    else:
        with open("Tsk.txt", "w", encoding="utf-8") as create:
            pass
    Show_info()

def showTasks():
    if e1.get() == '':
        messagebox.showerror("Validation", "Enter your task")
    else:
        with open("Tsk.txt", "a") as db:
            db.write(f"Task: {e1.get()} \n Date: {datetime.datetime.now()} \n=========================================\n")
        e1.delete(0, tk.END)
        Show_info()


with open("Tsk.txt", "a", encoding="utf-8") as create:
    pass

master = tkinter.Tk()
title = master.title("Task_Manager")
master.minsize(400, 400)
master.maxsize(500, 500)
tkinter.Label(master, text="Task: ").grid(row=1)

Show_info()

e1 = tk.Entry(master)
e1.grid(row=1, column=1)
button = tk.Button(master, text="Save_Task", command=showTasks)
button.grid(row=2, column=1)

button2 = tk.Button(master, text="Delete Tasks information", command=delete_file).grid(row=3, column=1)

master.mainloop()
