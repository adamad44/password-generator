# Import all modules


try:
    from tkinter import *
    import tkinter as tk
    from tkinter import filedialog
    from tkinter import messagebox
    import os
    import threading
    import json
    import subprocess
    import sys
    from win32api import GetSystemMetrics
    from tkinter import ttk
    import platform
except ImportError:
    # If any modules fail to import, display an error message and quit the program
    print('There has been an error with importing modules. Please ensure that you have pip installed requirements.txt')
    quit()

# Function to check if the operating system is Windows
def is_windows():
    return 'windows' in platform.system().strip().lower()

# Main function to set up the text editor
def main():
    # Create the main window for the text editor
    root = tk.Tk()
    root.title("Text Editor")
    root.config(bg='#181915')

    # If the OS is not Windows, show a warning message to the user
    if not is_windows():
        ask_windows = messagebox.askyesno('WARNING', 'This text editor is designed to run on Windows 10 and newer only. Do you acknowledge that there may be errors if run otherwise?')
        if not ask_windows:
            # If the user clicks 'No' in the warning, quit the program
            quit()

    # Function to save the content of the text box to the selected file
    def save_file():
        try:
            global file
            file = open(str(selected_file), 'r+')
            file.truncate(0)
            file.write(str(text_box.get("1.0","end")))
            file.close()
            messagebox.showinfo("Success", "File saved successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save file:\n{str(e)}")

    # Function to run the selected Python file in a separate thread
    def main_run():
        python = f'python "{selected_file}"'
        os.system(python)

    # Function to start running the Python file in a new thread
    def run():
        x = threading.Thread(target=main_run)
        x.start()
saf
    # Function to choose a file and open it in the text box
    def choose_file_and_open():
        try:
            ask_open = filedialog.askopenfile(initialdir=os.getcwd())
            global selected_file
            selected_file = (ask_open.name)
            global file
            file = open(str(selected_file), 'r+')

            text_box.delete(1.0, END)
            text_box.insert(1.0, file.read())

            # Update the visibility of the "Run Python" button based on the selected file's extension
            update_run_button_visibility()

            # Hide the "Choose File" button and show other buttons after opening a file
            choose_file.pack_forget()
            save_button.pack(side=LEFT, padx=8, pady=12)
            choose_file.pack(side=LEFT, padx=8, pady=12)
            clear_button.pack(side=RIGHT, padx=8, pady=12)
            delete_file_button.pack(side=RIGHT, padx=8, pady=12)
        except Exception as e:
            pass

    # Function to clear the content of the text box
    def clear():
        text_box.delete(1.0, END)

    # Function to delete the selected file
    def delete():
        ask = messagebox.askyesno('WARNING', f'Would you like to delete this file:\n {selected_file}')
        if ask:
            file.close()
            os.remove(selected_file)
            clear()

    # Function to update the visibility of the "Run Python" button based on the selected file's extension
    def update_run_button_visibility():
        if '.py' in str(selected_file):
            run_py_button.pack_forget()
            run_py_button.pack(side=LEFT, padx=8, pady=12)
        else:
            run_py_button.pack_forget()

    # Function to open the settings window
    def open_settings():
        # Create a new top-level window for settings
        global master
        master = Toplevel(root)
        master.config(bg='#181915')
        master.geometry(f'{int(GetSystemMetrics(0)/1.9)}x{int(GetSystemMetrics(1)/1.9)}')
        
        # Label and entry to adjust text size
        textsize_label = Label(master, text='Text Size:', bg='#181915', fg='#F8F8F2', font='verdana 17')
        textsize_label.pack(side=TOP)
        global textsize_entry
        textsize_entry = Entry(master, font='verdana 14', bg='grey')
        textsize_entry.pack(side=TOP)
        
        # Submit button to apply the selected text size
        submit_textsize = Button(master, text='Submit', bg='#181915', fg='#F8F8F2', font='verdana 14', command=font_submit)
        submit_textsize.pack(side=TOP)

    # Function to submit the selected font size for the text box
    def font_submit():
        try:
            text_size = int(textsize_entry.get())
            if text_size > 0:
                text_box.config(font=f'verdana {text_size}')
                master.destroy()
            else:
                # Show an error message if an invalid font size is entered
                error_textsize.config(text="Invalid font size.")
                error_textsize.pack()
        except ValueError:
            # Show an error message if an invalid font size is entered
            error_textsize.config(text="Invalid font size.")
            error_textsize.pack()

    # Create the "Choose File" button
    choose_file = Button(root, text='Choose File', command=choose_file_and_open, bg='#20211C', font='verdana 13', padx=10, pady=10, fg='#c9c9c5')
    choose_file.pack(side=BOTTOM, padx=8, pady=12)

    # Create other buttons
    clear_button = Button(root, text='Clear', command=clear, bg='#20211C', font='verdana 13', padx=10, pady=10, fg='#c9c9c5')
    delete_file_button = Button(root, text='Delete File', command=delete, bg='#20211C', font='verdana 13', padx=10, pady=10, fg='#c9c9c5')
    save_button = Button(root, text='Save', command=save_file, bg='#20211C', font='verdana 13', padx=10, pady=10, fg='#c9c9c5')
    run_py_button = Button(root, text='▶', command=run, font='verdana 13', padx=10, pady=10, bg='#20211C', fg='#F8F8F2')

    # Create the text box
    text_box = Text(root, bg='#282923', fg='#F8F8F2', font='verdana 13', highlightthickness=0, padx=6, pady=6, height=30, width=140, wrap='none')
    text_box.pack(padx=8, pady=12)

    # Start the main event loop
    root.mainloop()

# Run the main function to start the text editor
if __name__ == "__main__":
    main()