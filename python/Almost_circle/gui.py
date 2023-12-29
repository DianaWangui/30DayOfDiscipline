import os 
import tkinter
from tkinter import *


root = Tk()
root.title("To Do List")
root.geometry('400x650+400+100')
root.resizable(False, False)

task_list = []

# Image_icon = PhotoImage(file="C:\\Users\\GAMER\\Desktop\\Image\\delete.png")
# root.iconphoto(False, Image_icon)

# TopImage=PhotoImage(file="C:\\Users\\GAMER\\Desktop\\Image\\delete.png")
# Label(root, image=TopImage).pack()

heading=Label(root, text="ALL TASK", font="arial 20 bold", fg="white", bg="#32405b")
heading.place(x=130, y=20)


#Main
frame=Frame(root, width=400,height=50, bg="white")
frame.place(x=0, y=180)

task=StringVar()
task_entry=Entry(frame, width=18, font="arial 20", bd=0)
task_entry.place(x=10, y=7)
task_entry.focus()

button=Button(frame, text="ADD", font="arial 20 bold", width=6, bg="#5a95ff", fg="#fff", bd=0)
button.place(x=300, y=0)

#listbox
frame1=Frame(root, bd=3, width=700, height=280, bg="#32405b")
frame1.pack(pady=(160,0))


root.mainloop()