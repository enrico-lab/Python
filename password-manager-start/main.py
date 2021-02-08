from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    capitals = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    password_letters = [choice(letters) for _ in range(randint(4, 6))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_capitals = [choice(capitals) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers + password_capitals

    shuffle(password_list)

    password = "".join(password_list)
    e_password.insert(0, password)
    pyperclip.copy(password)




# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = e_website.get()
    email = e_email.get()
    password = e_password.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Opss", message="Please make sure you haven't left any field empty.")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details you entered: \nEmail: {email}"
                                                   f"\nPassword: {password}\n Is it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                e_website.delete(0, END)
                e_password.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas =  Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
l_website = Label(text="Website")
l_website.grid(row=1, column=0)
l_email = Label(text="Email/Username")
l_email.grid(row=2, column=0)
l_password = Label(text="Password")
l_password.grid(row=3, column=0)

e_website = Entry(width=35)
e_website.grid(row=1, column=1, columnspan=2)
e_website.focus()
e_email = Entry(width=35)
e_email.grid(row=2, column=1, columnspan=2)
e_email.insert(0, "enricofavaro@yahoo.it")
e_password = Entry(width=21)
e_password.grid(row=3, column=1)

b_password = Button(text="Generate Password", width=10, command=generate_password)
b_password.grid(row=3, column=2)
add_button = Button(text="ADD", width=33, command=save)
add_button.grid(row=4, column=1, columnspan=2)







window.mainloop()
