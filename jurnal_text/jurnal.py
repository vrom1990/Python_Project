g = open('list1.txt','a')
ss = 0
while ss != "конец":
    ss = input("действие ")
    if ss == "новый":
        f = input("Фамиия ")
        d = input("Имя ")
        q = input("Оценка ")
        rr = f + " " + d  + " " + q
        print(rr)
        g.write(rr + "\n")
    if ss == "стереть":
        g.close()
        g = open('list1.txt','w')
        g.close()
        g = open('list1.txt','a')
g.close()
