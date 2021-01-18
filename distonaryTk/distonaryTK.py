from tkinter import *
lool = open('dist.txt', 'r')
d = []
tr = 0
def lolol(event):
    tr = 1
    nam.pack()
    snam.pack()
    ag.pack()
#def eeee(event):
    
root = Tk()
root.title("Distonary on tkinder")
root.geometry('300x300+200+100')
root["bg"] = "brown4"
for stroke in lool:
    templist = stroke.split()
    d.append({"name" : templist[0],"surname" : templist[1], "age" : templist[2]})
but = Button(root,text="New",font="2")
but.place(x=0-9999, y=0)
but2 = Button(root,text="show all",font="2")
but.place(x=0, y=100)
but3 = Button(root,text="show",font="2")
but4 = Button(root,text="save",font="2")
nam = Entry(root,width=20)
snam = Entry(root,width=20)
ag = Entry(root,width=20)
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
but.pack()
but2.pack()
but3.pack()
but4.pack()
root.mainloop()
