import tkinter as tk
from tkinter import filedialog
import os
from moviepy.editor import VideoFileClip

def open_file():
    file_path = filedialog.askopenfilename()
    print("Selected file:", file_path)
    file_label.config(text="Selected file: " + file_path)
    convert_to_mp3(file_path)

def convert_to_mp3(file_path):
    if file_path:
        video = VideoFileClip(file_path)
        mp3_file_path = os.path.splitext(file_path)[0] + ".mp3"
        video.audio.write_audiofile(mp3_file_path)
        print("File converted to MP3:", mp3_file_path)

root = tk.Tk()
root.title("Video File Selector")

button = tk.Button(root, text="Select Video File", command=open_file)
button.pack(pady=20)

file_label = tk.Label(root, text="")
file_label.pack()

root.mainloop()
