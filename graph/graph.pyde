y = [0]
gi = 0
def setup():
    size(500,300)
    background(140,10,10)
    frameRate(1)
def draw():
    global gi
    y.append(floor(random(10,290)))
    noStroke()
    gi = gi + 1
    for i in range(gi):
        ellipse(gi*20,y[i],5,5)
