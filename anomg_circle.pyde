d = [floor(random(1,9)),floor(random(1,9)),floor(random(1,9)),floor(random(1,9)),floor(random(1,9)),floor(random(1,9)),floor(random(1,9)),floor(random(1,9)),floor(random(1,9)),floor(random(1,9)),floor(random(1,9)),floor(random(1,9)),floor(random(1,9))]
l = 0
p = 0
def setup():
    size(510,372)
def draw():
    background(255)
    global d,l,p
    for c in range(12):
        if c == 0:
            fill(255,0,0)
        if c == 1:
            fill(255,150,0)
        if c == 2:
            fill(0, 255, 0)
        if c == 3:
            fill(0,0,255)
        if c == 4:
            fill(255,255,0)
        if c == 5:
            fill(50,50,50)
        if c == 6:
            fill(111,60,5)
        if c == 7:
            fill(250,3,197)
        if c == 8:
            fill(250,250,250)
        if c == 9:
            fill(154, 3, 250)
        if c == 10:
            fill(0, 100, 0)
        if c == 11:
            fill(0, 255, 255)
        for s in range(d[c]):
            l = l + 1
            ellipse(l*30-15,c*31+15,30,30)
        l = 0
def keyPressed():
    global p
    if keyCode == UP:
        p = p + 1
        for step in range(12):
            d[step] = d[step] + 1
    if keyCode == DOWN:
        p = p - 1
        for step in range(12):
            d[step] = d[step] - 1
