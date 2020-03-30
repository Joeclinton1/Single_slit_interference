import math

out_cnt = 500 # number of output points to be calculated
src_cnt = 100 # number of secondary sources within the slit
w=0.05 # wavelength 
b=0.05 # slit diameter 
D=0.1 #distance from slit to wall 

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
    intensity_plt = calculate_intensity_plt()
    #draw the intensity plot
    for o in range(-out_cnt/2, out_cnt/2, 1):
        x_o = (float(o)/out_cnt+0.5)*float(width)
        stroke(intensity_plt[o]**2/src_cnt/2)
        line(x_o,height/4,x_o,height/5);
        
def calculate_intensity_plt():
    intensity_plt = {}
    
    for o in range(-out_cnt/2, out_cnt/2): #Loop through wall output points
        x_o = float(o)/out_cnt #x position on wall
        for s in range(-src_cnt/2,src_cnt/2,1): # Loop through secondary sources
            x_s= s*b/src_cnt #x position on source
            path_dist = math.sqrt((x_o-x_s)**2 + D**2) #Calculate path distance from secondary source to point on wall
            intensity= math.cos(path_dist/w*TWO_PI) #Find phase of wavelength with path distance and map from -1 to 1
            #sum intensity to the intensity plot
            if s == -src_cnt/2:
                intensity_plt[o] = intensity
            else:
                intensity_plt[o] += intensity
    return intensity_plt
                
#change wavelength with up or down arrows
def keyPressed():
    global w
    if(keyCode == UP):
        w+=0.01
    elif(keyCode == DOWN):
        w-=0.01
    print(w)
