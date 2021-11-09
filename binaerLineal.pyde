def setup ():
    size (1480, 820)
    background (0, 0, 0)
    x_start = 100
    x_end = 1380
    y_start = 600
    y_end = 700
    #Übermalt Zahl wieder mit weiss
    frameRate (10)
    
def draw ():
    smartphone_ansicht()
    titel()
    beschriftung()
    overlay()
    lineal()
    fenster_schliessen()

def titel():
    textSize (100)
    fill(0, 0, 0)
    textAlign(LEFT)
    text ("Binaerlineal: 0 bis 255", 200, 150)

def beschriftung():
    global x_start
    global x_end
    global y_start
    global y_end
    x_start = 100
    x_end = 1380
    y_start = 600
    y_end = 700
                
    #Beschriftung
    textSize (50)
    textAlign(LEFT)
    fill (200, 55, 55)
    text ("Dezimalzahl", 400, 300)
    text ("Binaerzahl", 400, 500)
    
    #Binärzahl
    binary = bin((mouseX-100)/((x_end-x_start)/256))
    fill (0, 0, 0)
    textSize (50)
    if mouseX > x_start and mouseX < x_end and mouseY > y_start and mouseY < y_end:
        text ((mouseX-100)/5, 815, 300)
        text (binary, 750, 500)

def smartphone_ansicht():    
    #Smartphone
    strokeWeight (30)
    stroke(0, 0, 0)
    fill(255, 255, 255)
    rect (15, 15, 1450, 790, 70)
    strokeWeight(40)
    fill (200, 55, 55)
    rect (80, 400, 20, 20, 3)
    
def overlay():
    #übermalt das 0b bei Binärzahl
    noFill ()
    strokeWeight (50)
    stroke (255, 255, 255)
    rect (740, 450, 50, 50, 3)
    
def lineal():
    global x_start
    global x_end
    x_start = 100
    x_end = 1380
    y_start = 600
    y_end = 700
    x_wert = 0
    
    strokeWeight(1)
    stroke (0, 0, 0)
    rect (x_start, y_start, x_end-x_start, y_end-y_start, 5)        
    for einer in range (1, 256):
        x_wert = x_start + einer * (x_end-x_start)/256
        line(x_wert, 600, x_wert, 620)
    for fuenfer in range (1, 52):
        x_wert = x_start + 5 * fuenfer * (x_end-x_start)/256
        strokeWeight(3)
        line(x_wert, 601, x_wert, 630)    
    for zehner in range (1, 26):
        x_wert = x_start + 10 * zehner * (x_end-x_start)/256
        strokeWeight(5)
        line(x_wert, 602, x_wert, 650)
        textSize(15)
        textAlign(CENTER)
        fill (200, 55, 55)
        text (zehner*10, x_wert, 680)

def fenster_schliessen():
    if mouseX > 80 and mouseX < 120 and mouseY > 400 and mouseY < 440 and mousePressed == True:
        exit()    
    
    
