from textwrap import indent
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
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
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if website == '' or email == '' or password == '':
        messagebox.showwarning('Warning', "Please don't leave any fields empty!")
        return


    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file) #Reading old data
            data.update(new_data) #Update old data w/ new data
        with open('data.json', 'w') as data_file:
            json.dump(data, data_file, indent=4) #Save updated data

    except FileNotFoundError:
        with open('data.json', 'w') as data_file:
            json.dump(new_data, data_file, indent=4) #Write new file and save data


    website_entry.delete(0, END)
    password_entry.delete(0, END)
    website_entry.focus_set()
# ----------------------------- SEARCH -------------------------------- #
def find_password():
    user_search_text = website_entry.get()
    with open('data.json', 'r') as data_file:
        data = json.load(data_file)
        if user_search_text.lower() in data:
            matching_data = data[user_search_text]
            print(matching_data)
    #check if the user's text entry matches an item in the data.json
        #if yes, show a messagebox with the website's name and password
    #catch an exception trying to access the data.json showing a messagebox, 'No data file found'
    #if the website does not exist in the data.json, show a messagebox that reads "No details for the website exist
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
website_entry.grid(column=1, row=1, sticky=EW)

search_button = Button(text='Search', padx=0, pady=0, highlightthickness=0, bg='white', command=find_password)
search_button.grid(column=2, row=1, sticky=EW)

email_label = Label(text='Email/Username:', bg='white')
email_label.grid(column=0, row=2)
email_entry = Entry()
email_entry.insert(0, "notxap55@yahoo.com")
email_entry.grid(column=1, columnspan=2, row=2, sticky=EW)

password_label = Label(text='Password:', bg='white')
password_label.grid(column=0, row=3)
password_entry = Entry()
password_entry.grid(column=1, row=3, sticky=EW)
password_button = Button(text='Generate Password', pady=0, bg='white', highlightthickness=0, command=generate_password)
password_button.grid(column=2, row=3, sticky=EW)

add_button = Button(text='Add', bg='white', highlightthickness=0, pady=0, command=save)
add_button.grid(column=1, columnspan=2, row=4, sticky=EW)






window.mainloop()