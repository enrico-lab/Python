from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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

b_password = Button(text="Generate Paasword", width=10)
b_password.grid(row=3, column=2)
add_button = Button(text="ADD", width=33)
add_button.grid(row=4, column=1, columnspan=2)







window.mainloop()
