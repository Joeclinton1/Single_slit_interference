import math

steps = 500 # number of output points to be calculated
steps_2 = 50 # number of secondary sources within the slit
w=0.02 # wavelength
b=0.01 # slit diameter
D=0 #distance from slit to wall

def setup():
    #draw the background lines
    global D
    size(500,500) #for those 
    stroke(0)
    strokeWeight(2)
    background(255)
    line(0,3*height/4,width*(1-b)/2,3*height/4);
    line(width*(1+b)/2,3*height/4,width,3*height/4);
    line(0,height/4,width,height/4);
    strokeWeight(1)
    stroke(200)
    line(width*(1-b)/2,3*height/4,width*(1+b)/2,3*height/4);
    D=height*4 # sets distance to some arbitarily large value. 
    
def draw():
    intensity_plot = {}
    for i in range(steps): #Loop through wall output points
        x1 = i*width/steps
        for u in range(steps_2): # Loop through secondary sources
            x2 = width*(1-b)/2 + u*b*width/steps_2 
            path_dist = math.sqrt((x1-x2)**2+D**2) #Calculate path distance from secondary source to point on wall
            intensity= (math.cos(path_dist/(w*width)*(TWO_PI))) #Find phase of wavelength with path distance and map from -1 to 1
            #sum intensity to the intensity plot
            if u == 0:
                intensity_plot[i] = intensity
            else:
                intensity_plot[i] += intensity
    #draw the intensity plot
    for i in range(steps):
        x1 = i*width/steps
        stroke((intensity_plot[i]**2)/10)
        line(x1,height/4,x1,height/5);
        
#change wavelength with up or down arrows
def keyPressed():
    global w
    if(keyCode == UP):
        w+=0.01
    elif(keyCode == DOWN):
        w-=0.01
    print(w)
