from tkinter import*
import random
import smtplib
from email.message import EmailMessage


b_latter = "ABCDEFGHIJKLMNOPQRSTUVWYZ"
s_latter = "abcdefghijklmnopqrstuvwxyz"
char = "!@#$%^&*()"
numbers = "1234567890"
email_id = "Your Email"
email_pass = "Password for the Given email"
root = Tk()
root.geometry("1080x1080")
root.title("PASSWORD GENERATOR")
Label(root, text="ENTER YOUR NAME SIR").grid(row=0, column=0)
Label(root, text="ENTER THE LENGTH OF THE PASSWORD ").grid(row=2, column=0)
Label(root, text="NAME OF THE APP FOR WHICH THE PASSWORD IS GANRETED").grid(
    row=4, column=0)
Label(root, text="ENTER YOUR EMAIL_ID").grid(row=6, column=0)
Label(root, text="SET THE DIFFICULTY OF YOUR PASSWORD").grid(row=8, column=0)

user_name = StringVar()
user_entry1 = Entry(root, textvariable=user_name)
user_entry1.grid(row=1, column=0)
password_length = IntVar()
user_entry3 = Entry(root, textvariable=password_length)
user_entry3.grid(row=3, column=0)
app_name = StringVar()
user_entry4 = Entry(root, textvariable=app_name)
user_entry4.grid(row=5, column=0)
email = StringVar()
user_entry5 = Entry(root, textvariable=email)
user_entry5.grid(row=7, column=0)
var = IntVar()
radio_low = Radiobutton(root, text="Low", variable=var, value=1)
radio_low.grid(row=11, column=0, sticky='W')
radio_middle = Radiobutton(root, text="Medium", variable=var, value=2)
radio_middle.grid(row=12, column=0, sticky='W')
radio_strong = Radiobutton(root, text="Strong", variable=var, value=3)
radio_strong.grid(row=13, column=0, sticky='W')
def g():
    a = str(user_entry1.get())
    d = str(user_entry4.get())
    e = str(user_entry5.get())
    c = int(user_entry3.get())
    f = var.get()
    value = ""
    if f == 1:
        value = ("".join(random.choices(s_latter+b_latter, k=c)))
    elif f == 2:
        value = ("".join(random.choices(s_latter+b_latter+numbers, k=c)))
    elif f == 3:
        value = ("".join(random.choices(s_latter+b_latter+numbers+char, k=c)))
        msg = EmailMessage()
        msg["subject"] = "The Password"
        msg["From"] = "textsender123456@gmail.com"
        msg["To"] = e
        msg.set_content("File Added")

    with open("Password_file.txt","w") as file:
        file.write("//n"+"Hi"+a+"Your"+d+"Password is"+value)


    files=["Password_file.txt"]
    for file in files:
        with open(file,"rb") as f:
            file_data=f.read()
            file_name=f.name


        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            msg = EmailMessage()
            msg["subject"] = "The Password"
            msg["From"] = "textsender123456@gmail.com"
            msg["To"] = e
            msg.set_content("File Added")
            smtp.login(email_id,email_pass)
            msg.add_attachment(file_data, maintype='application',subtype='txt', filename=file_name)
            smtp.send_message(msg)

b1 = Button(root, text="GENRET", command=g)
b1.grid()
root.mainloop()
