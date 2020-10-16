f = open('datad.txt','r')
kek = f.read(10)
kek = int(kek) + 1
outt = open('datad2.txt','w')
outt.write(str(kek))
print(kek)
f.close()
outt.close()
