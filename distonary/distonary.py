lool = open('dist.txt', 'r')
d = []
for stroke in lool:
    templist = stroke.split()
    d.append({"name" : templist[0],"surname" : templist[1], "age" : templist[2]})
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
lool.close()
