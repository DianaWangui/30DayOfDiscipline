import os 
import tkinter
from tkinter import *


root = Tk()
root.title("To Do List")
root.geometry('400x650+400+100')
root.resizable(False, False)

task_list = []

def addTask():
  task = task_entry.get()
  task_entry.delete(0, END)

  if task:
    with open("tasklist.txt", "a", encoding="utf-8") as taskfile:
      taskfile.writ(f"\n{task}")
      task_list.append(task)
      listbox.insert(END, task)


def openTaskFile():
  try:
    global task_list
    with open("tasklist.txt", "r", encoding="utf-8") as taskfile:
      tasks = taskfile.readlines()

    for task in tasks:
      if task != '\n':
        task_list.append(task)
        listbox.insert(END, task)
  except:
    file = open("tasklist.txt", "w", encoding="utf-8")
    file.close()

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

button=Button(frame, text="ADD", font="arial 20 bold", width=6, bg="#5a95ff", fg="#fff", bd=0, command=)
button.place(x=300, y=0)


#listbox
frame1= Frame(root, bd=3,width=700,height=200,bg="#32405b")
frame1.pack(pady=(231, 0))

listbox = Listbox(frame1,font=('arial',12),width=40,height=16,bg="#32405b", fg="white", cursor="hand2", selectbackground="#5a95ff")
listbox.pack(side=LEFT , fill=BOTH, padx=2)
scrollbar= Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)


listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

openTaskFile()
#delete
Delete_icon= Button(root, text="Remove Task", font="arial 13 bold", bg="#5a95ff", fg="#fff", bd=0)
Delete_icon.pack(pady=10)









root.mainloop()