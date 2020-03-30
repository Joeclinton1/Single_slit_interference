import math

out_pt_count = 500 # number of output points to be calculated
sec_source_count = 50 # number of secondary sources within the slit
w=0.02 # wavelength/width
b=0.01 # slit diameter/width
D=500 #distance from slit to wall

def setup():
    #draw the background lines
    size(500,500) #width = 500, height = 500
    stroke(0)
    strokeWeight(2)
    background(255)
    line(0,3*height/4,width*(1-b)/2,3*height/4);
    line(width*(1+b)/2,3*height/4,width,3*height/4);
    line(0,height/4,width,height/4);
    strokeWeight(1)
    stroke(200)
    line(width*(1-b)/2,3*height/4,width*(1+b)/2,3*height/4);
    
def draw():
    intensity_plot = {}
    for i in range(out_pt_count): #Loop through wall output points
        x1 = i*width/out_pt_count
        for u in range(sec_source_count): # Loop through secondary sources
            x2 = width*(1-b)/2 + u*b*width/sec_source_count
            path_dist = math.sqrt((x1-x2)**2+D**2) #Calculate path distance from secondary source to point on wall
            intensity= (math.cos(path_dist/(w*width)*(TWO_PI))) #Find phase of wavelength with path distance and map from -1 to 1
            #sum intensity to the intensity plot
            if u == 0:
                intensity_plot[i] = intensity
            else:
                intensity_plot[i] += intensity
    #draw the intensity plot
    for i in range(out_pt_count):
        x1 = i*width/out_pt_count
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
