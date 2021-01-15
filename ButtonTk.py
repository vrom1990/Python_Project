from tkinter import *
#def str_to_sort_list(event):
    #s = ent.get()
    #s = s.split()
    #s.sort()
    #lab['text'] = len(ent)
def hahahaha(event):
    s = ent.get()
    lab['text'] = len(s)



 
 
root = Tk()
root.geometry('200x100+200+100')
root["bg"] = "red4"

ent = Entry(width=20)
but = Button(text="Писать число символов")
lab = Label(width=20, bg='black', fg='white')
 
but.bind('<Button-1>', hahahaha)
 
ent.pack()
but.pack()
lab.pack()
root.mainloop()
