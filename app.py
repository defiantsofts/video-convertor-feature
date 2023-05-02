import tkinter as tk
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename()
    print("Selected file:", file_path)
    file_label.config(text="Selected file: " + file_path)

root = tk.Tk()
root.title("Video File Selector")

button = tk.Button(root, text="Select Video File", command=open_file)
button.pack(pady=20)

file_label = tk.Label(root, text="")
file_label.pack()

root.mainloop()