import math

steps = 500
steps_2 = 50
w=0.02
b=0.01
y=0
def setup():
    global y
    size(500,500)
    stroke(0)
    strokeWeight(2)
    background(255)
    line(0,3*height/4,width*(1-b)/2,3*height/4);
    line(width*(1+b)/2,3*height/4,width,3*height/4);
    line(0,height/4,width,height/4);
    strokeWeight(1)
    stroke(200)
    line(width*(1-b)/2,3*height/4,width*(1+b)/2,3*height/4);
    y=height*4
    
def draw():
    intensity_plot = {}
    for i in range(steps):
        x1 = i*width/steps
        for u in range(steps_2):
            x2 = width*(1-b)/2 + u*b*width/steps_2 
            path_dist = math.sqrt((x1-x2)**2+y**2)
            intensity= (math.cos(path_dist/(w*width)*(TWO_PI)))
            if u == 0:
                intensity_plot[i] = intensity
            else:
                intensity_plot[i] += intensity
    for i in range(steps):
        x1 = i*width/steps
        stroke((intensity_plot[i]**2)/10)
        line(x1,height/4,x1,height/5);
def keyPressed():
    global w
    if(keyCode == UP):
        w+=0.01
    elif(keyCode == DOWN):
        w-=0.01
    print(w)
