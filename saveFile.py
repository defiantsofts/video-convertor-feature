import tkinter as tk
from tkinter import filedialog
import os
from moviepy.editor import VideoFileClip

def open_file():
    file_path = filedialog.askopenfilename()
    print("Selected file:", file_path)
    #file_label.config(text="Selected file: " + file_path)
    convert_to_mp3(file_path)

def convert_to_mp3(file_path):
    if file_path:
        video = VideoFileClip(file_path)
        mp3_file_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 Files", "*.mp3")])
        if mp3_file_path:
            video.audio.write_audiofile(mp3_file_path)
            print("File converted to MP3:", mp3_file_path)
            status_label.config(text="File is Converted")

root = tk.Tk()
root.title("Video File Selector")

button = tk.Button(root, text="Select Video File", command=open_file)
button.pack(pady=20)

file_label = tk.Label(root, text="")
file_label.pack()

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
