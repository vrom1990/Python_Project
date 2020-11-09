y = [0]
x = []
milpops = [0]
gi = 0
lom = 0
def setup():
    size(500,300)
    background(140,10,10)
    frameRate(5)
def draw():
    push()
    global gi, lom
    background(140,10,10)
    translate(0,height)
    scale(1,-1)
    y.append(floor(random(10,300)))
    #text(y[gi],100,100)
    noStroke()
    if gi < 20:
        gi = gi + 1
        
    else:
        del y[0]
    if gi > 1:
        for i in range(gi-1):
        #ellipse(i*25,y[i],5,5)
        
            strokeWeight(5)
            stroke(255)
            line(i* 25, y[i],(i + 1) * 25, y[i + 1])
    lom = lom + 1
    pop()
    textSize(35)
    fill(0)
    text("number:" + str(lom),10,296)
    text("graph:" + str(y[gi]),320,296)
