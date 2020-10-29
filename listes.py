d = [4,7,1,9,4,2,7,3]
f = input("действие ")
while f != "exit":
    if f == "+":
        k = int(input("на сколько? "))
        for step in range(0,8):
            d[step] = d[step] + k
    if f == "-":
        k = int(input("на сколько? "))
        for step in range(0,8):
            d[step] = d[step] - k
    if f == "input":
        for stepp in range(0,8):
            print(d[stepp])
    f = input("действие ")
