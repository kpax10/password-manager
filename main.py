from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    password_entry.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for char in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for symbol in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for num in range(random.randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters
    random.shuffle(password_list)

    password = ''.join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if website == '' or username == '' or password == '':
        messagebox.showwarning('Warning', "Please don't leave any fields empty!")
        return

    response = messagebox.askokcancel(title=website, message="Save site details?")

    if response:
        with open('data.txt', 'a') as file:
            file.write(f"{website} | {username} | {password}\n")

        website_entry.delete(0, END)
        password_entry.delete(0, END)
        website_entry.focus_set()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=40, pady=40, bg='white')

canvas = Canvas(width=200, height=200, bg='white', highlightthickness=0)
img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

website_label = Label(text='Website:', bg='white')
website_label.grid(column=0, row=1)
website_entry = Entry()
website_entry.focus_set()
website_entry.grid(column=1, columnspan=2, row=1, sticky=EW)

username_label = Label(text='Email/Username:', bg='white')
username_label.grid(column=0, row=2)
username_entry = Entry()
username_entry.insert(0, "notxap55@yahoo.com")
username_entry.grid(column=1, columnspan=2, row=2, sticky=EW)

password_label = Label(text='Password:', bg='white')
password_label.grid(column=0, row=3)
password_entry = Entry()
password_entry.grid(column=1, row=3, sticky=EW)
password_button = Button(text='Generate Password', pady=0, bg='white', highlightthickness=0, command=generate_password)
password_button.grid(column=2, row=3, sticky=EW)

add_button = Button(text='Add', bg='white', highlightthickness=0, pady=0, command=save)
add_button.grid(column=1, columnspan=2, row=4, sticky=EW)






window.mainloop()