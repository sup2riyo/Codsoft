import tkinter as tk
def button_click(event):
    current_text = result_label["text"]
    button_text = event.widget["text"]
    
    if button_text == "=":
        try:
            result = eval(current_text)
            result_label["text"] = str(result)
        except Exception as e:
            result_label["text"] = "Error"
    elif button_text == "C":
        result_label["text"] = ""
    else:
        result_label["text"] = current_text + button_text

root = tk.Tk()
root.title("Calculator")

result_label = tk.Label(root, text="", font=("Arial", 24))
result_label.grid(row=0, column=0, columnspan=4)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0)
]

for button_text, row, col in buttons:
    button = tk.Button(root, text=button_text, font=("Arial", 18))
    button.grid(row=row, column=col, padx=5, pady=5)
    button.bind("<Button-1>", button_click)

root.mainloop()
