from importlib.resources import path
import tkinter as tk
from docx2pdf import convert
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfile
from tkinter.messagebox import showinfo
from pathlib import Path

win = tk.Tk()
win.title("CONVERT WORD TO PDF")

def open_file():
    file = askopenfile(filetypes=[('word file', ('*.docx', '*.doc', '*.odt'))])
    file_path = file.name
    file_name = Path(f'{file_path}').stem
    print(f'THe file {file_name} has been successfully saved')
    convert(file.name, r'C:\D DISK\convertedDocs' + f'\{file_name}' + '.pdf')
    showinfo('File converted!')

label = tk.Label(win, text="Choose file")
label.grid(row=0, column=0, padx=5, pady=5)
btn = ttk.Button(win, text="Select", width=50, command=open_file)
btn.grid(row=0, column=1, padx=5, pady=5)

win.mainloop()