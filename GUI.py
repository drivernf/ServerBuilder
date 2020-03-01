import tkinter as tk
from tkinter import filedialog, Text
import os.path
from os.path import basename
import ServerBuilder

root = tk.Tk()
root.resizable(False, False)
root.title("Server Builder")
pathToZipTK = tk.StringVar()

def guiSetup(pathToZip):
    # Styling
    bgColor = '#343434'
    labelFont = ("Helvetica", 16)

    # Canvas
    canvas = tk.Canvas(root, height=700, width=700, bg=bgColor).pack()

    # Frame
    frame = tk.Frame(root, bg=bgColor)
    frame.place(relx=.5, rely=.5, anchor="center")

    # Change Folder Label
    changeFolderLabel = tk.Label(frame, textvariable=pathToZipTK, fg="white", bg=bgColor, font=labelFont).pack()
    pathToZipTK.set('Local Folder: {}'.format(pathToZip))

    # Change Folder Button
    changeFolder = tk.Button(frame, text="Change Folder", padx=10, pady=5, fg="black", bg="white",
        command=ServerBuilder.changeFolder).pack(pady = (5,300))

    e1 = tk.Entry(frame).pack()

    # Zip & Transfer Button
    zipIt = tk.Button(frame, text="Zip & Transfer", padx=10, pady=5, fg="black", bg="white",
        command=ServerBuilder.zipFolder).pack()

    root.mainloop()