g = open('list1.txt','w')
ss = 0
while ss != "конец":
    ss = input("действие ")
    if ss == "новый":
        f = input("Фамиия ")
        d = input("Имя ")
        q = input("Оценка ")
        rr = f + " " + d  + " " + q
        print(rr)
        rr.write('list1.txt')
