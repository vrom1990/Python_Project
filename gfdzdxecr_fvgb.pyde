krrjekuio = []
lol = 0
hg = 1
colors = [color(255, 0, 0),color(255,150,0),color(0, 255, 0),color(0,0,255),color(255,255,0),color(50,50,50),color(111, 60, 5),color(250, 3, 197),color(250, 250, 250),color(154, 3, 250),color(0, 100, 0),color(0, 255, 255)]
class Ciorcle():
    def __init__(self, x, y, sizee,ccolor):
        self.x = x
        self.y = y
        self.sizee = sizee
        self.ccolor = ccolor
    def draw(self):
        push()
        fill(self.ccolor)
        ellipse(self.x, self.y,self.sizee,self.sizee)
        pop()
def setup():
    size(700,500)
    background(255)
def draw():
    global lol,hg
    background(lol)
    if lol < 255:
        hg = 1
    if hg < 0:
        hg = 0
    if hg == 1:
        lol = lol + 1
    if hg == 0:
        lol = lol - 1
    background(255)
    for lox in range(len(krrjekuio)):
        krrjekuio[lox].draw()
def mousePressed():
    krrjekuio.append(Ciorcle(mouseX,mouseY,random(5,40),colors[floor(random(0,12))]))
    
