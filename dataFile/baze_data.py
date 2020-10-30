dataFile = open("list2.txt", "r")
dataList = []
for stroke in dataFile:
    dataList.append(int(stroke.rstrip('\n')))
#for elem in dataList:
#    print(elem)
dataFile.close()
o = input("action ")
while o != "exit":

    #показывает список
    if o == "show":
        t = len(dataList)
        if t != 0:
            for elem in dataList:
                print(elem)
        else:
            print("list is empty")
    
    if o == "+ up":
        j = input("number ")
        dataList.insert(0,j)
        
    if o == "+ down":
        j = input("number ")
        dataList.append(j)
        
    if o == "- down":
        t = len(dataList)
        if t != 0:
            dataList.pop()
        else:
            print("list is empty")
        
    if o == "- up":
        t = len(dataList)
        if t != 0:
            dataList.pop(0)
        else:
            print("list is empty")

    if o == "deleteAll":
        dataList.clear()

    if o == "save":
        dataFile = open("list2.txt", "w")
        dataFile.write(str(dataList))
        dataFile.close()
    o = input("action ")
