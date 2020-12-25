class Planet():
    def __init__(self, name, speed, speedChange, sizer, position, color1, color2, color3):
        self.name = name
        self.speed = speed
        self.speedChange = speedChange
        self.sizer = sizer
        self.position = position
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        
    def draw(self):
        push()
        noStroke()
        self.speedChange = self.speedChange + self.speed
        fill(self.color1,self.color2,self.color3)
        translate(width/2,height/2)
        rotate(radians(self.speedChange))
        ellipse(self.position,0,self.sizer,self.sizer)
        pop()
merkuri = Planet("Merkuri",2,2,10,115,191,168,125)
venera = Planet("Venera",4,3,18,127,191,140,44)
def setup():
    size(600,600)
def draw():
    global merkuri
    background(0,0,50)
    push()
    fill(255,200,0)
    noStroke()
    translate(width/2,height/2)
    ellipseMode(CENTER)
    ellipse(0,0,200,200)
    pop()
    merkuri.draw()
    venera.draw()
    
