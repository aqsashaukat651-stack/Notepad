import tkinter as tk
from tkinter import filedialog, messagebox 

 # Create main window code
window = tk.Tk ()
window.title ("My Text Editor")
window.geometry ("400x300")

# create text area 

text = tk.Text(
    window,
    wrap= tk.WORD,
    font= ("celabri body", 14)
)

text.pack (expand=True, fill=tk.BOTH)

# functin 1 : To create a new file 

def new_file():
    text.delete(1.0 ,tk.END)

# function 2 : T open a new file
def open_file():
    file_path= filedialog.askopenfilename(

    defaultextension= ".txt",
    filetypes= [("Text files ", "*.txt")]
     )

    if file_path:
        #open selected file
        with open(file_path , "r") as file:
            text.delete(1.0 , tk.END)
            text.insert(tk.END , file.read())

def save_file():
    file_path= filedialog.asksaveasfilename(
        defaultextension= ".txt",
        filetypes= [("Text files ", "*.txt")]
    )
    if file_path:
        with open(file_path , "w") as file:
            file.write(text.get(1.0 , tk.END))

    messagebox.showinfo ("Info", "File Save Successfully")

# Create Menu Bar 
menu= tk.Menu(window)
window.config(menu=menu)
file_menu= tk.Menu(menu)

# New, Open File, Save , Exit 

# add filemenu to menu bar 
menu.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)

file_menu.add_command(label="Exit", command=window.quit)



# start and keep the window open
window.mainloop()
