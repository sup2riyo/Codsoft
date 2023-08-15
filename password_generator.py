import tkinter as tk
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_password_button_clicked():
    try:
        password_length = int(length_entry.get())
        if password_length <= 0:
            password_display.config(text="Password length should be a positive integer.")
            return

        password = generate_password(password_length)
        password_display.config(text="Generated Password: " + password)
    except ValueError:
        password_display.config(text="Please enter a valid integer for password length.")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create GUI elements
name_label = tk.Label(root, text="Enter your name:")
name_label.pack()

name_entry = tk.Entry(root)
name_entry.pack()

length_label = tk.Label(root, text="Enter password length:")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password_button_clicked)
generate_button.pack()

password_display = tk.Label(root, text="")
password_display.pack()

# Start the GUI event loop
root.mainloop()