from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list=password_letters+password_symbols+password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    pass_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def savepassword():
    new_data={web_entry.get():{"email":email_entry.get(),"password":pass_entry.get()}}
    if len(web_entry.get())==0 and len(pass_entry.get())==0:
        messagebox.showerror(title="ERROR", message="Website and Password fields should not be empty!")
    elif len(web_entry.get())==0:
        messagebox.showerror(title="ERROR",message="Website field should not be empty!")
    elif len(pass_entry.get())==0:
        messagebox.showerror(title="ERROR", message="Password field should not be empty!")
    else:
        ok=messagebox.askokcancel(title=f"{web_entry}",message=f"you entered the details for {web_entry.get()}\n username: {email_entry.get()}\n "
                                                            f"password:{pass_entry.get()}\nDo you want to save?")
        if ok==True:
            try:
                with open("file.json","r") as file:
                    data = json.load(file)
            #file.write(f"{web_entry.get()} | {email_entry.get()} | {pass_entry.get()}\n")
            except FileNotFoundError:
                with open("file.json","w") as file:
                    json.dump(new_data,file,indent=4)
            else:
                data.update(new_data)
                with open("file.json","w") as file:
                    json.dump(new_data, file,indent=4)
            finally:
                web_entry.delete(0,END)
                pass_entry.delete(0,END)

def find_password():
    website=web_entry.get()
    try:
        with open("file.json") as file:
            data=json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="error",message="File not found")
    else:
        if website in data:
            email=data[website]["email"]
            password=data[website]["password"]
            messagebox.showinfo(title=website,message=f"email:{email}\npassword:{password}")
        else:
            messagebox.showerror(title="error",message=f"No details for {website} at the moment!!")



    # ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("PASSWORD MANAGER")
#window.minsize(width=700,height=500)
window.config(padx=50,pady=50)
canvas=Canvas(width=200,height=200)
image=PhotoImage(file="logo.png")
lock_image=canvas.create_image(100,100,image=image)
canvas.grid(row=0,column=1)

website_label=Label(text="Website:")
website_label.grid(row=1,column=0)

web_entry=Entry(width=21)
web_entry.grid(column=1,row=1)
web_entry.focus()

Email_label=Label(text="Email/Username: ")
Email_label.grid(row=2,column=0)

email_entry=Entry(width=39)
email_entry.grid(column=1,row=2,columnspan=2)
email_entry.insert(0,"udayreddys2607@gmail.com")


pass_label=Label(text="Password: ")
pass_label.grid(row=3,column=0)

pass_entry=Entry(width=21)
pass_entry.grid(column=1,row=3)


generate_button=Button(text="Generate Password",command=gen_pass)
generate_button.grid(row=3,column=2,)

search_button=Button(text="Search",width=13,command=find_password)
search_button.grid(row=1,column=2)

add_button=Button(text="Add",width=34,command=savepassword)
add_button.grid(row=4,column=1,columnspan=2)

window.mainloop()