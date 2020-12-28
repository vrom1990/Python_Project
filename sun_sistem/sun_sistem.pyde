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
        translate(self.position,0)
        rotate(radians(-self.speedChange))
        textAlign(CENTER,CENTER)
        fill(0)
        textSize(12)
        text(self.name,0,0)
        fill(255)
        textSize(14)
        text(self.name,0,0)
        pop()
merkuri = Planet(u"Меркурий",2,2,10-2,135,191,168,125)
venera = Planet(u"Венерна",1,3,18-2,169,191,140,44)
earth = Planet(u"Земля",1.4,2.4,20-2,226,53,74,250)
mars = Planet(u"Марс",1.3,4,17-2,268,232,134,101)
upiter = Planet(u"Юпритер",0.6,0.4,47,374,245,184,143)
saturn = Planet(u"Сатурн",0.4,0.4,39,437,244,247,197)
uran = Planet(u"Уран",0.3,0.4,31,478+15,143,214,212)
neptune = Planet(u"Нептун",0.4,0.3,32,534+25,103,147,216)
def setup():
    size(1040,1040)
    frameRate(60)
def draw():
    global merkuri
    background(20,0,40)
    push()
    fill(255,200,0)
    noStroke()
    translate(width/2,height/2)
    ellipseMode(CENTER)
    ellipse(0,0,200,200)
    pop()
    merkuri.draw()
    venera.draw()
    earth.draw()
    mars.draw()
    upiter.draw()
    saturn.draw()
    uran.draw()
    neptune.draw()
