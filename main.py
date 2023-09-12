import tkinter as tk
from tkinter import *
import random
import pyperclip

# Create the main Tkinter window
root = tk.Tk()
root.title('Password Generator')
root.geometry('720x500')
root.config(bg='#252525')

root.minsize(720,500)
root.maxsize(820,600)



# Define the characters that can be used to generate the password
chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
         'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
         '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
         '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '|', ':', ';', ',', '.', '<', '>', '/', '?']

# Variable to hold the generated password
password_var = StringVar()

# Function to generate a random password
def generate():
    # Shuffle the characters to get a random order
    random.shuffle(chars)
    # Get the chosen length of the password from the slider
    length = int(length_slider.get())
    # Take a sample of the shuffled characters based on the chosen length
    generated_password = ''.join(random.sample(chars, length))
    # Set the generated password in the password_var variable
    password_var.set(generated_password)

# Function to copy the generated password to the clipboard
def copy_to_clipboard():
    result_text = password_var.get()
    pyperclip.copy(result_text)

# Create and configure the GUI elements
title = Label(root, text='Password Generator', font='Verdana 25 bold', bg='#252525', fg='white')
title.pack(pady=20)

length_label = Label(root, text='Choose Length:', font='Verdana 14', bg='#252525', fg='white')
length_label.pack()

length_slider = Scale(root, from_=8, to=50, orient=HORIZONTAL, length=200, bg='#252525', fg='white', highlightbackground='#252525', sliderlength=20)
length_slider.pack()

gen_button = Button(root, text='Generate', font='Verdana 14', command=generate, bg='#a834eb', fg='white', activebackground='#8828bf', activeforeground='white')
gen_button.pack(pady=10)

copy_button = Button(root, text='Copy', font='Verdana 14', command=copy_to_clipboard, bg='#1c62c9', fg='white', activebackground='#0056b3', activeforeground='white')
copy_button.pack(pady=10)

result = Label(root, textvariable=password_var, font='Verdana 16', bg='#252525', fg='white')
result.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
