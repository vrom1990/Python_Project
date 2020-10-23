e = 0
w = 0
q = 0
def setup():
    size(500,500)
    background(255)
    frameRate(12)
   
def draw():
    global e
    global w,q 
    e = random(50,500)
    e = floor(e)
    background(random(0,50),random(0,50),random(0,50))
    for ster in range(25):
        w = floor(random(-300,700))
        strokeWeight(random(3,8))
        stroke(random(0,255),random(0,255),random(0,255),120)
        line(w-185,0,w+185,500)
    for stey in range(25):
        e = floor(random(-300,700))
        strokeWeight(random(3,8))
        stroke(random(0,255),random(0,255),random(0,255),120)
        line(e+185,0,e-185,500)
    noStroke()
    for step in range(200):
        fill(random(0,255),random(0,255),random(0,255))
        push()
        translate(random(0,500),random(0,500))
        rotate(radians(random(0,360)))
        square(0,0,random(5,15))
        pop()
        fill(random(0,255),random(0,255),random(0,255))
        circle(random(0,500),random(0,500),random(5,15))
