import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    selected_task = task_list.curselection()
    if selected_task:
        task_list.delete(selected_task)
    else:
        messagebox.showwarning("Warning", "Please select a task to remove.")

root = tk.Tk()
root.title("To-Do List")

task_entry = tk.Entry(root, font=("Arial", 14))
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task, font=("Arial", 12))
add_button.pack()

remove_button = tk.Button(root, text="Remove Task", command=remove_task, font=("Arial", 12))
remove_button.pack()

task_list = tk.Listbox(root, font=("Arial", 12), selectmode=tk.SINGLE)
task_list.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

root.mainloop()
