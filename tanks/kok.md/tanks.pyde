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
def setup():
    size(850,700)
    background(34, 139, 34)
def draw():
    global x1, y1, ul, ul2, x2, y2
    background(34, 139, 34)
    push()
    translate(x1,y1)
    tank(750,650)
    pop()
    push()
    translate(x2,y2)
    tank2(60,60)
    pop()
    if keyPressed:
        if keyCode == UP:
            x1 = x1 + cos(radians(ul))
            y1 = y1 + sin(radians(ul))
        if keyCode == DOWN:
            x1 = x1 - cos(radians(ul))
            y1 = y1 - sin(radians(ul))
        if keyCode == RIGHT:
            ul = ul + 1
        if keyCode == LEFT:
            ul = ul - 1
            
        if key == 'w':
            x2 = x2 + cos(radians(ul2))
            y2 = y2 + sin(radians(ul2))
        if key == 's':
            x2 = x2 - cos(radians(ul2))
            y2 = y2 - sin(radians(ul2))
        if key == 'd':
            ul2 = ul2 + 1
        if key == 'a':
            ul2 = ul2 - 1
def tank(x, y):
    rectMode(CENTER)
    fill(0,65,0)
    noStroke()
    translate(x, y)
    rotate(radians(ul))
    rect(0,0, 80, 35)
    fill(46,70,70)
    rect(0,-18, 80, 10)
    rect(0,18, 80, 10)
    fill(0, 85, 0)
    rect(10,0,35,25)
    fill(0,60,0)
    rect(48,0,42,8)
    fill(0,50,01)
    rect(-25,-6,15,6)
    rect(-25,6,15,6)
    ellipseMode(CENTER)
    ellipse(0,-4,11,11)

def tank2(xr, yr):
    rectMode(CENTER)
    fill(65)
    noStroke()
    translate(xr, yr)
    rotate(radians(ul2))
    fill(65)
    rect(0,0, 80, 35)
    fill(46,70,70)
    rect(0,-18, 80, 10)
    rect(0,18, 80, 10)
    fill(85)
    rect(10,0,35,25)
    fill(60)
    rect(48,0,42,8)
    fill(50)
    rect(-25,-6,15,6)
    rect(-25,6,15,6)
    ellipseMode(CENTER)
    ellipse(0,-4,11,11)
