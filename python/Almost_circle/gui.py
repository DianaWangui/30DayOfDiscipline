import os 
import tkinter
from tkinter import *


root = Tk()
root.title("To Do List") # title of my project displayed at the top of the gui window
root.geometry('400x650+400+100') # creating a size that your window should open to
root.resizable(False, False)

#empty list
task_list = []

#add task
def addTask():
  task = task_entry.get()
  task_entry.delete(0, END)

  if task:
    with open("tasklist.txt", "a", encoding="utf-8") as taskfile:
      taskfile.write(f"\n{task}")
      task_list.append(task)
      listbox.insert(END, task)

#delete task
def deleteTask():
  global task_list
  task = str(listbox.get(ANCHOR))
  if task in task_list:
    task_list.remove(task)
    with open("tasklist.txt", "w", encoding="utf-8") as taskfile:
      for task in task_list:
        taskfile.write(task + '\n')
    listbox.delete(ANCHOR)


#open file
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

heading=Label(root, text="MY TO DO LIST", font="arial 20 bold", width=30, fg="white", bg="#32405b")
heading.pack()


#Main
frame=Frame(root, width=400,height=50, bg="grey")
frame.place(x=0, y=180)

task=StringVar()
task_entry=Entry(frame, width=18, font="arial 20", bg="grey", bd=0)
task_entry.place(x=10, y=7)
task_entry.focus()

button=Button(frame, text="ADD", font="arial 20 bold", width=6, bg="#5a95ff", fg="#fff", bd=0, command=addTask)
button.place(x=300, y=0)


#listbox
frame1= Frame(root, bd=3,width=700,height=200,bg="#32405b")
frame1.pack(pady=(200, 0))

listbox = Listbox(frame1,font=('arial',12),width=40,height=16,bg="#32405b", fg="white", cursor="hand2", selectbackground="#5a95ff")
listbox.pack(side=LEFT , fill=BOTH, padx=2)
scrollbar= Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)


listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

openTaskFile()

#delete
Delete_icon= Button(root, text="Remove Task", font="arial 13 bold", bg="#5a95ff", fg="#fff", bd=0, command=deleteTask)
Delete_icon.pack(pady=10)

root.mainloop()