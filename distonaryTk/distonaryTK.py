from tkinter import *
d = []
lool = open('dist.txt', 'r')
for stroke in lool:
    templist = stroke.split()
    d.append({"name" : templist[0],"surname" : templist[1], "age" : templist[2]})
tr = 0
def lolol(event):
    tr = 1
    ag.delete(0,END)
    nam.delete(0,END)
    snam.delete(0,END)
    killer.place_forget()
    l1.place(x=141, y=127)
    nam.place(x=105, y=151)
    l2.place(x=135, y=170)
    snam.place(x=105, y=195)
    l3.place(x=150, y=215)
    ag.place(x=105, y=239)
    bommb.place(x=142, y=275)

    l4.place_forget()
    kek.place_forget()
    l5.place_forget()
    keka.place_forget()
    tanki.place_forget()
def biiolog(event):
    #exit()
    killer.place_forget()
    l1.place_forget()
    l2.place_forget()
    l3.place_forget()
    nam.place_forget()
    snam.place_forget()
    ag.place_forget()
    bommb.place_forget()
    m = nam.get()
    q = snam.get()
    a = ag.get()
    d.append({"name" : m,"surname" : q, "age" : a})
def eeee(event):
    killer.place_forget()
    tr = 2
    kek.delete(0,END)
    keka.delete(0,END)
    l4.place(x=141, y=127)
    kek.place(x=105, y=151)
    l5.place(x=80, y=170)
    keka.place(x=105, y=195)
    tanki.place(x=135, y=225)

    l1.place_forget()
    l2.place_forget()
    l3.place_forget()
    nam.place_forget()
    snam.place_forget()
    ag.place_forget()
    bommb.place_forget()
def nain(event):
    l4.place_forget()
    kek.place_forget()
    l5.place_forget()
    keka.place_forget()
    tanki.place_forget()
    j = int(kek.get())
    j = j - 1
    k = keka.get()
    killer["text"] = (d[j][k])
    killer.place(relx=0.5, y=142, anchor=CENTER)
def bolit(event):
    global lool
    lool.close()
    lool = open('dist.txt', 'w')
    for dict in d:
        lool.write(dict["name"] + " " + dict["surname"]  + " " + dict["age"] + "\n")
        #print(dict["name"], dict["surname"], dict["age"])
    lool.close()
    exit()
root = Tk()
root.title("Distonary on tkinder")
root.geometry('330x330+200+100')
root["bg"] = "#708090"
for stroke in lool:
    templist = stroke.split()
    d.append({"name" : templist[0],"surname" : templist[1], "age" : templist[2]})
but = Button(root,text="New",font="2",padx = "20.4")
but.place(x=127, y=95)
but2 = Button(root,text="Show all",font="2",padx = "7")
but2.place(x=127, y=33)
but3 = Button(root,text="Show",font="2",padx = "16.5")
but3.place(x=127, y=0)
but4 = Button(root,text="Save And Exit",font="2",padx = "18")
but4.place(x=95, y=67)
bommb = Button(root,text="Add",font="2",padx = "7")
tanki = Button(root,text="Show",font="2",padx = "7")
nam = Entry(root,width=20)
kek = Entry(root,width=20)
keka = Entry(root,width=20)
snam = Entry(root,width=20)
ag = Entry(root,width=20)
l1 = Label(text="Name",font="Verdana",pady = "1")
l1.config(bg='#708090', fg='#FFFFFF')
l2 = Label(text="Surame",font="Verdana",pady = "1")
l2.config(bg='#708090', fg='#FFFFFF')
l3 = Label(text="Age",font="Verdana",pady = "1")
l3.config(bg='#708090', fg='#FFFFFF')
l4 = Label(text="Place",font="Verdana",pady = "1")
l4.config(bg='#708090', fg='#FFFFFF')
l5 = Label(text="Name/Surname/Age",font="Verdana",pady = "1")
l5.config(bg='#708090', fg='#FFFFFF')
killer = Label(pady = "1", bg='black', fg='white',font="Verdana")

but.bind('<Button-1>', lolol)
but4.bind('<Button-1>', bolit)
bommb.bind('<Button-1>', biiolog)
but3.bind('<Button-1>', eeee)
tanki.bind('<Button-1>',nain)
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
#but.pack()
#but2.pack()
#but3.pack()
#but4.pack()
root.mainloop()
