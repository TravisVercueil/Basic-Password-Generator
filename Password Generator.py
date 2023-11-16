#Imports we use
import secrets
import string
from tkinter import *
import pyperclip

#Initialize our Window
root = Tk()
root.geometry("350x350")

#Title of Window
root.title("Random Password Generator")

#Defining our Alphabet
alphabet = string.ascii_letters + string.digits + string.punctuation
output_pass = StringVar()
special_chars = string.punctuation
digits = string.digits

#Random password function with restrictions
def PassGen():
#Generate our password that meets our restrictions
    while True:
        password = ''
        for i in range(pass_length.get()):
            password += ''.join(secrets.choice(alphabet))

        if (any(char in special_chars for char in password) and
            sum(char in digits for char in password) >= 3 and 
            any(char.isupper() for char in password) and 
            any(char.islower() for char in password)):
             break
    output_pass.set(password)

#Copy to Clipboard Function
def copyPass():
    pyperclip.copy(output_pass.get())

#Password heading
pass_heading = Label(root, text = 'Password Length', font = 'arial 14 bold').pack(pady=15)
#Password Length Spinbox
pass_length = IntVar()
length = Spinbox(root, from_ = 12, to_ = 32 , textvariable = pass_length, width = 24, font = 'arial 16').pack()
#Password Generator Button
Button(root, text = "Generate Password", command = PassGen, font= "arial 12 bold", bg='white', fg='Black', activebackground="teal", padx=5, pady=5 ).pack(pady=20)
#Generated Password Length
pass_label = Label(root, text='Randomly Generated Password', font='arial 14 bold').pack(pady="30 10")
Entry(root, textvariable= output_pass, width=24,font='arial 16').pack()
#Password Copy to Clipboard Button
Button(root, text='Copy to Clipboard', command = copyPass, font='Arial 16 bold', bg='white', fg='Black', activebackground="teal", padx=5,pady=5).pack(pady=20)
#Packing the code for Tkinter
root.mainloop()