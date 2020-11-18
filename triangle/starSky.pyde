distX = []
distY = []
bebra = 0
job = 0
x1 = 0
x2 = 0
x3 = 0
y1 = 0
y2 = 0
y3 = 0
p = 0
kadilacX = 0
kadilacY = 0
def setup():
    frameRate(1)
    size(550,500)
    background(5,0,30)
def draw():
    global bebra, job, x1, x2, x3, y1, y2, y3, p, kadilacX, kadilacY
    x1 = 0
    x2 = 0
    x3 = 0
    y1 = 0
    y2 = 0
    y3 = 0
    kadilacX = floor(random(0,500))
    kadilacY = floor(random(0,450))
    bebra = floor(random(1,2))
    job = floor(random(1,2))
    if bebra == 1:
        x1 = x1 + floor(random(50,100))
        x1 = x1 + kadilacX
    if bebra == 2:
        x1 = x1 - floor(random(50,100))
        x1 = x1 + kadilacX
    if job == 1:
        y1 = y1 + floor(random(50,200))
        y1 = y1 + kadilacY
    if job == 2:
        y1 = y1 - floor(random(50,200))
        y1 = y1 + kadilacY
        
    bebra = floor(random(1,2))
    job = floor(random(1,2))
    if bebra == 1:
        x2 = kadilacX
        x2 = x2 + floor(random(150,280))
    if bebra == 2:
        x2 = kadilacX
        x2 = x2 - floor(random(-150,-280))
    if job == 1:
        y2 = y2 + floor(random(50,200))
        y2 = y2 + kadilacY
    if job == 2:
        y2 = y2 - floor(random(50,200))
        y2 = y2 + kadilacY
        
    bebra = floor(random(1,2))
    job = floor(random(1,2))
    if bebra == 1:
        x3 = x3 + floor(random(10,30))
        x3 = x3 + kadilacX
    if bebra == 2:
        x3 = x3 - floor(random(10,30))
        x3 = x3 + kadilacX
    if job == 1:
        y3 = y3 + floor(random(10,30))
        y3 = y3 + kadilacY
    if job == 2:
        y3 = y3 - floor(random(10,30))
        y3 = y3 + kadilacY
    distX.append({"w1" : x1,"w2" : x2,"w3" : x3})
    distY.append({"q1" : y1,"q2" : y2,"q3" : y3})
    #print(distX[p]["w1"], distX[p]["w2"], distX[p]["w3"])
    #print(distY[p]["q1"], distY[p]["q2"], distY[p]["q3"])
    stroke(255)
    strokeWeight(5)
    noFill()
    #scale(1,-1)
    triangle(distX[p]["w1"],distY[p]["q1"],distX[p]["w2"],distY[p]["q2"],distX[p]["w3"],distY[p]["q3"])
    p = p + 1
