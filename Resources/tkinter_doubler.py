from Tkinter import *

root = Tk()
root.title("Doubler")
#root.configure(bg="#FFFF00")

entrybox = Entry(root, width=50)
entrybox.grid(row=0,column=0, padx=20, pady=20)

def doubleMe():
    number = float(entrybox.get())
    newNumber = number * 2
    answer.set(newNumber)

button1 = Button(text="Double", command=doubleMe, fg="#FFFFFF", bg="#0000FF")
button1.grid(row=1,column=0, padx=20, pady=20)

answer = StringVar()

text = Label(root, text='', textvariable=answer)
text.grid(row=2, column=0, padx=20, pady=20)

root.mainloop()