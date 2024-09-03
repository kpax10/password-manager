from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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
website_entry.grid(column=1, columnspan=2, row=1, sticky=EW)

username_label = Label(text='Email/Username:', bg='white')
username_label.grid(column=0, row=2)
username_entry = Entry()
username_entry.grid(column=1, columnspan=2, row=2, sticky=EW)

password_label = Label(text='Password:', bg='white')
password_label.grid(column=0, row=3)
password_entry = Entry()
password_entry.grid(column=1, row=3, sticky=EW)
password_button = Button(text='Generate Password', pady=0, bg='white', highlightthickness=0)
password_button.grid(column=2, row=3, sticky=EW)

add_button = Button(text='Add', bg='white', highlightthickness=0, pady=0)
add_button.grid(column=1, columnspan=2, row=4, sticky=EW)






window.mainloop()