from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

FONT = ("Arial", 24, "bold")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_numbers + password_symbols + password_letters

    random.shuffle(password_list)

    password = "".join(password_list)
    input_pass.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = input_web.get()
    email = input_mail.get()
    password = input_pass.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                # reading the old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # updating old data with new data
            data.update(new_data)
            with open("data.json", 'w') as data_file:
                # saving the updated data
                json.dump(data, data_file, indent=4)

        finally:
            input_web.delete(0, END)
            input_pass.delete(0, END)
#-------------------FIND PASSWORD---------------------------3
def search_web():
    website = input_web.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="ERROR!!", message="No data file found")

    else:
        if website in data:
            email = data[website]['email']
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\n Password: {password}")
        else:
            messagebox.showinfo(title='ERROR', message=f"No details of {website} exists")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)
label_web = Label(text="Website:", font=FONT)
label_web.grid(column=0, row=1)
label_email = Label(text="Email/Username:", font=FONT)
label_email.grid(column=0, row=2)
label_pass = Label(text="Password:", font=FONT)
label_pass.grid(column=0, row=3)
button_generate = Button(text="Generate Password", command=generate_pass)
button_generate.grid(column=2, row=3)
button_search = Button(text="            Search         ", command=search_web)
button_search.grid(column=2, row=1)
button_add = Button(text="Add", command=save, width=36)
button_add.grid(column=1, row=4, columnspan=2)
input_web = Entry(width=21)
input_web.grid(column=1, row=1)
input_mail = Entry(width=39)
input_mail.grid(column=1, row=2, columnspan=2)
input_mail.insert(0, "pawanvirat32@gmail.com")
input_pass = Entry(width=21)
input_pass.grid(column=1, row=3)

window.mainloop()
