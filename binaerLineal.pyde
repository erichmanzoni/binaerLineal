def setup ():
    size (800, 800)
    
def draw ():
    #Übermalt Zahl wieder mit weiss
    frameRate (3)
    background (255, 255, 255)
    
    #Beschriftung
    textSize (50)
    text ("Dezimalzahl", 200, 400)
    textSize (50)
    text ("Binaerzahl", 200, 500)
    
    #Binärzahl
    binary = bin(mouseX/10)
    fill (0, 0, 0)
    textSize (50)
    text (mouseX/10, 400, 400)
    text (binary, 400, 500)
    
    #Smartphone
    strokeWeight (20)
    text ("Binaerlineal", 250, 100)
    noFill ()
    rect (100, 250, 600, 400, 70)
    fill (200, 55, 55)
    rect (95, 450, 10, 10, 3)
    
    
    
    
