x1 = 500
y1 = 500 
angleTank1 = 180
x2 = 30
y2 = 30
angleTank2 = 0
T1UP = False
T1DOWN = False
T1LEFT = False
T1RIGHT = False
T2UP = False
T2DOWN = False
T2LEFT = False
T2RIGHT = False
T1SHOOT = False
T2SHOOT = False
boom = 0
ldf = 0
ldf2 = 0
xBullet = 0
yBullet = 0
ule = 0 
ula = 0
xBullet2 = 0
yBullet2 = 0
def setup():
    size(600,550)
    background(34, 139, 34)
def draw():
    global x1, y1, angleTank1, angleTank2, x2, y2, tanka, tanke,T1UP,T1DOWN,T1LEFT,T1RIGHT,T2UP,T2DOWN,T2LEFT,T2RIGHT,T1SHOOT,T2SHOOT,boom,ldf,xBullet,yBullet,ule
    background(34, 139, 34)
    text(str(xBullet) + " " + str(yBullet),30,30)
    tank(x1,y1)
    bullet1()    
    push()
    tank2()
    bullet2() 
    pop()
    if T1UP:
        x1 = x1 + cos(radians(angleTank1))
        y1 = y1 + sin(radians(angleTank1))
    if T1DOWN:
        x1 = x1 - cos(radians(angleTank1))
        y1 = y1 - sin(radians(angleTank1))
    if T1RIGHT:
        angleTank1 = angleTank1 + 0.8
    if T1LEFT:
        angleTank1 = angleTank1 - 0.8
        
    if T2UP:
        x2 = x2 + cos(radians(angleTank2))
        y2 = y2 + sin(radians(angleTank2))
    if T2DOWN:
        x2 = x2 - cos(radians(angleTank2))
        y2 = y2 - sin(radians(angleTank2))
    if T2RIGHT:
        angleTank2 = angleTank2 + 0.8
    if T2LEFT:
        angleTank2 = angleTank2 - 0.8
    if T1SHOOT:
        ldf = 1
        boom = 1
        xBullet = x1
        yBullet = y1
        ule = angleTank1
        T1SHOOT = False
    if T2SHOOT:
        ldf = 1
        xBullet2 = x2
        yBullet2 = y2
        ula = angleTank2
        T2SHOOT = False
    if ldf == 1:
        xBullet = xBullet + cos(radians(ule)) * 33
        yBullet = yBullet + sin(radians(ule)) * 33
    if ldf2 == 1:
        xBullet2 = xBullet2 + cos(radians(ula)) * 33
        yBullet2 = yBullet2 + sin(radians(ula)) * 33
def keyPressed():
    global x1, y1, angleTank1, angleTank1, x2, y2, tanka, tanke,T1UP,T1DOWN,T1LEFT,T1RIGHT,T2UP,T2DOWN,T2LEFT,T2RIGHT,T1SHOOT,T2SHOOT,boom,ldf,ldf2,xBullet2,yBullet2
    
    if keyCode == 38:
        T1UP = True
    if keyCode == 40:
        T1DOWN = True
    if keyCode == 39:
        T1RIGHT = True
    if keyCode == 37:
        T1LEFT = True
    if key == "w":
        T2UP = True
    if key == "s":
        T2DOWN = True
    if key == "a":
        T2LEFT = True
    if key == "d":
        T2RIGHT = True
        
    if key == " ":
        T1SHOOT = True
    if key == "e":
        T2SHOOT = True
def tank(x, y):
    #ul = ul + 0.1
    push()
    global tanka,angleTank1 
    tanka = loadImage("1.png")
    translate(x, y)
    rotate(radians(angleTank1))
    imageMode(CENTER)
    image(tanka,0,0)
    pop() 
def tank2():
    global tanke
    tanke = loadImage("2.png")
    imageMode(CENTER)
    translate(x2, y2)
    rotate(radians(angleTank2))
    image(tanke,0,0)
    
def keyReleased():
    global T1UP,T1DOWN,T1LEFT,T1RIGHT,T2UP,T2DOWN,T2LEFT,T2RIGHT,T1SHOOT,T2SHOOT,boom,xBullet,yBulllet,ldf2,xBullet2,yBullet2
    if keyCode == UP:
        T1UP = False
    if keyCode == DOWN:
        T1DOWN = False
    if keyCode == RIGHT:
        T1RIGHT = False
    if keyCode == LEFT:
        T1LEFT = False
        
    if key == "w":
        T2UP = False
    if key == "s":
        T2DOWN = False
    if key == "a":
        T2LEFT = False
    if key == "d":
        T2RIGHT = False
    
    if key == " ":
        T1SHOOT = False
        boom = 0  
    if key == "e":
        T2SHOOT = False
        ldf2 = 0
def bullet1():
    if ldf == 1:
        fill(255,230,0)
        push()
        translate(xBullet,yBullet)
        rotate(radians(ule))
        noStroke()
        rectMode(CENTER)
        #rect(0,0,60,2)
        rect(60,1,65,2)
        pop()
def bullet2():
    if ldf2 == 1:
        fill(255,230,0)
        push()
        translate(xBullet2,yBullet2)
        rotate(radians(ula))
        noStroke()
        rectMode(CENTER)
        #rect(0,0,60,2)
        rect(60,1,65,2)
        pop()
