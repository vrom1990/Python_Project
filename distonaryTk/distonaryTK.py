from tkinter import *
lool = open('dist.txt', 'r')
d = []
tr = 0
def lolol(event):
    tr = 1
    l1.place(x=141, y=127)
    nam.place(x=105, y=151)
    l2.place(x=141, y=147)
    #nam.place(x=105, y=161)
    #snam.place(x=105, y=146)
    #ag.place(x=105, y=166)
    bommb.place(x=142, y=180)
#def eeee(event):
    
root = Tk()
root.title("Distonary on tkinder")
root.geometry('330x300+200+100')
root["bg"] = "#2F4F4F"
for stroke in lool:
    templist = stroke.split()
    d.append({"name" : templist[0],"surname" : templist[1], "age" : templist[2]})
but = Button(root,text="New",font="2",padx = "20.4")
but.place(x=127, y=95)
but2 = Button(root,text="Show all",font="2",padx = "7")
but2.place(x=127, y=33)
but3 = Button(root,text="Show",font="2",padx = "16.5")
but3.place(x=127, y=0)
but4 = Button(root,text="Save",font="2",padx = "18")
but4.place(x=127, y=65)
bommb = Button(root,text="Add",font="2",padx = "7")
nam = Entry(root,width=20)
#nam.place(x=90, y=126)
snam = Entry(root,width=20)
ag = Entry(root,width=20)
l1 = Label(text="Name",font="Verdana",pady = "1")
l1.config(bg='#2F4F4F', fg='#FFFFFF')
l2 = Label(text="Surame",font="Verdana",pady = "1")
l2.config(bg='#2F4F4F', fg='#FFFFFF')
but.bind('<Button-1>', lolol)
#but2.bind('<Button-2>', rere)
#but3.bind('<Button-3>', eeee)
'''
e = input("action ")
while e != "exit":
    if e == "new":
        w = input("name ")
        q = input("surname ")
        a = input("age ")
        d.append({"name" : w,"surname" : q, "age" : a})
    if e == "showAll":
        for dict in d:
            print(dict["name"], dict["surname"], dict["age"])
    if e == "show":
        j = int(input("plase "))
        k = input("what ")
        print(d[j][k])
    if e == "save":
        lool.close()
        lool = open('dist.txt', 'w')
        for dict in d:
            #print(dict["name"], dict["surname"], dict["age"])
            lool.write(dict["name"] + " " + dict["surname"]  + " " + dict["age"] + "\n")
            
    e = input("action ")
'''
lool.close()
#but.pack()
#but2.pack()
#but3.pack()
#but4.pack()
root.mainloop()
