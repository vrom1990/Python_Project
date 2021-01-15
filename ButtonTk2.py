from tkinter import *
global e
e = 'white'
def str_to_sort_list(event):
    s = ent.get()
    s = s.split()
    s.sort()
    lab['text'] = ' '.join(s)
def ratatata(event):
    global e
    e = sus.get()
    lab.configure(foreground=e)
 
 
root = Tk()
root.geometry('200x200+200+100')
root["bg"] = "red4"
 
ent = Entry(width=20)
but = Button(text="Преобразовать")
lab = Label(width=20, bg='black', foreground=str(e))
sus = Entry(width=20 )
kon = Button(text="Поставить цвет")
 
but.bind('<Button-1>', str_to_sort_list)
kon.bind('<Button-2>', ratatata)
 
ent.pack()
but.pack()
sus.pack()
kon.pack()
lab.pack()
root.mainloop()
