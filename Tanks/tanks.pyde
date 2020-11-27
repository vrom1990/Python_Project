x1 = 0
y1 = 0
ul = 180
x2 = 0
y2 = 0
ul2 = 0
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
xBullet = 0
yBullet = 0
ule = 0
ula = 0
def setup():
    size(600,550)
    background(34, 139, 34)
def draw():
    global x1, y1, ul, ul2, x2, y2, tanka, tanke,T1UP,T1DOWN,T1LEFT,T1RIGHT,T2UP,T2DOWN,T2LEFT,T2RIGHT,T1SHOOT,T2SHOOT,boom,ldf,xBullet,yBullet,ule
    background(34, 139, 34)
    text(boom,100,100)
    push()
    translate(x1,y1)
    tank(500,500)
    if ldf == 1:
        bullet1()    
    pop()
    push()
    translate(x2,y2)
    tank2(60,60)
    pop()
    if T1UP:
        x1 = x1 + cos(radians(ul))
        y1 = y1 + sin(radians(ul))
    if T1DOWN:
        x1 = x1 - cos(radians(ul))
        y1 = y1 - sin(radians(ul))
    if T1RIGHT:
        ul = ul + 0.8
    if T1LEFT:
        ul = ul - 0.8
        
    if T2UP:
        x2 = x2 + cos(radians(ul2))
        y2 = y2 + sin(radians(ul2))
    if T2DOWN:
        x2 = x2 - cos(radians(ul2))
        y2 = y2 - sin(radians(ul2))
    if T2RIGHT:
        ul2 = ul2 + 0.8
    if T2LEFT:
        ul2 = ul2 - 0.8
    if T1SHOOT:
        ldf = 1
        boom = 1
    if ldf == 1:
        xBullet = xBullet - cos(radians(ule))
        ybullet = yBullet - sin(radians(ule))
        ule = ule - 500
def keyPressed():
    global x1, y1, ul, ul2, x2, y2, tanka, tanke,T1UP,T1DOWN,T1LEFT,T1RIGHT,T2UP,T2DOWN,T2LEFT,T2RIGHT,T1SHOOT,T2SHOOT,boom,ldf
    
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
    global tanka, ul
    tanka = loadImage("1.png")
    translate(x, y)
    rotate(radians(ul))
    imageMode(CENTER)
    image(tanka,0,0)

def tank2(xr, yr):
    global tanke
    tanke = loadImage("2.png")
    imageMode(CENTER)
    translate(xr, yr)
    rotate(radians(ul2))
    image(tanke,0,0)
def keyReleased():
    global T1UP,T1DOWN,T1LEFT,T1RIGHT,T2UP,T2DOWN,T2LEFT,T2RIGHT,T1SHOOT,T2SHOOT,boom,xBullet,yBulllet
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
        T2SHOOT = True
def bullet1():
    fill(255,230,0)
    noStroke()
    rect(20+xBullet,yBullet,60,2)
