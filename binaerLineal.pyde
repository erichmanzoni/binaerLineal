# wiederkehrende Variablen
displayhoehe = displayHeight
displaybreite = displayWidth
x_lineal_links = displaybreite - (displaybreite / 100 * 95)
x_lineal_rechts = displaybreite - (displaybreite / 100 * 5)
delta = (x_lineal_rechts - x_lineal_links) / 256
y_lineal_oben = displayhoehe / 100 * 70
y_lineal_unten = displayhoehe / 100 * 85

def setup ():
    global displayhoehe, displaybreite 
    size (displaybreite, displayhoehe)
    fullScreen ()
    background (0, 0, 0)
    # Übermalt Zahl wieder mit weiss
    frameRate (100)
    
def draw ():
    smartphone_ansicht()
    titel()
    home_button()
    beschriftung()
    overlay()
    lineal()
    fenster_schliessen()

def titel():
    global displayhoehe, displaybreite
    textSize (displayhoehe / 100 * 12)
    fill (0, 0, 0)
    textAlign (CENTER)
    text ("Binaerlineal: 0 bis 255", displaybreite / 2, displayhoehe / 100 * 20)

# Ausgabe der Binärzahl
def beschriftung():
    global displayhoehe, displaybreite, x_lineal_links, x_lineal_rechts, delta, y_lineal_oben, y_lineal_unten                   

    textSize (displayhoehe / 100 * 7)
    textAlign (LEFT)
    fill (200, 55, 55)
    text ("Binaerzahl", displaybreite / 100 * 35, displayhoehe / 100 * 40)
    
    # Binärzahlberechnung
    binary = bin((mouseX - x_lineal_links) / delta)
    fill (0, 0, 0)
    textSize (displayhoehe / 100 * 7)
    text (mouseX, displaybreite / 2, displayhoehe / 2)
    if mouseX in range (x_lineal_links, x_lineal_rechts + 2) and mouseY in range (y_lineal_oben, y_lineal_unten):
        text (binary, displaybreite / 100 * 60, displayhoehe / 100 * 40)

# Smartphone-Design
def smartphone_ansicht(): 
    global displayhoehe, displaybreite   
    noStroke()
    fill (255, 255, 255)
    rect (displayhoehe / 100 * 2, displaybreite / 100, displaybreite - (displaybreite / 100 * 2), displayhoehe - (displayhoehe / 100 * 4), 70)

# Homebutton (für Schliessen des Fensters --> da Fullscreen-Ansicht)    
def home_button():
    global displayhoehe, displaybreite
    strokeWeight (displayhoehe / 100 * 4)
    stroke(0, 0, 0)
    fill (200, 55, 55)
    rect (displaybreite / 100 * 4, displayhoehe / 2, displayhoehe / 100 * 2, displayhoehe / 100 * 2, 3)
    strokeWeight (1)
    textSize (displayhoehe / 100 * 2)
    textAlign (LEFT)
    text ("Fenster schliessen", displaybreite / 100 * 4, displayhoehe / 2 - displayhoehe / 100 * 6)
    text ("=> Klick auf roten Homebutton", displaybreite / 100 * 4, displayhoehe / 2 - displayhoehe / 100 * 3) 
       
# Overlay überdeckt das "0b" bei Binärzahl
def overlay():
    noFill ()
    strokeWeight (displayhoehe / 100 * 4)
    stroke (255, 255, 255)
    rect (displaybreite / 100 * 60, displayhoehe / 100 * 35, displaybreite / 100 * 4, displayhoehe / 100 * 4, 3)
    
# Lineal-Design  
def lineal():
    global displayhoehe, displaybreite, x_lineal_links, x_lineal_rechts, delta, y_lineal_oben, y_lineal_unten
    x_wert = 0
    
    # Linealkontur
    noFill()
    strokeWeight (2)
    stroke (0, 0, 0)
    rect (x_lineal_links, y_lineal_oben, x_lineal_rechts - x_lineal_links + delta, y_lineal_unten - y_lineal_oben, 5)        
    
    # 1er-Striche auf dem Lineal
    for einer in range (1, 256):
        x_wert = x_lineal_links + (1 * einer * delta)
        strokeWeight (1)
        line (x_wert, y_lineal_oben, x_wert, y_lineal_oben + (y_lineal_oben / 100 * 3))
    
    # 5er-Striche auf dem Lineal
    for fuenfer in range (1, 52):
        x_wert = x_lineal_links + ( 5 * fuenfer * delta)
        strokeWeight (3)
        line (x_wert, y_lineal_oben + 1, x_wert, y_lineal_oben + (y_lineal_oben / 100 * 6))    
    
    # 10er-Striche auf dem Lineal
    for zehner in range (1, 26):
        x_wert = x_lineal_links + (10 * zehner * delta)
        strokeWeight (5)
        line (x_wert, y_lineal_oben + 2, x_wert, y_lineal_oben + (y_lineal_oben / 100 * 12))
        textSize (displayhoehe / 100 * 2)
        textAlign (CENTER)
        fill (200, 55, 55)
        text (zehner * 10, x_wert, y_lineal_oben + (y_lineal_oben / 100 * 20))

    # Anzeige grüner Balken
    noStroke ()
    if mouseX in range (x_lineal_links, x_lineal_rechts + delta) and mouseY in range (y_lineal_oben, y_lineal_unten):
        fill (0, 255 - (mouseX / 10), 0)
        rect (x_lineal_links, y_lineal_oben, mouseX - x_lineal_links, displayhoehe / 100 * 3, 10)
        textSize (displayhoehe / 100 * 6)
        text ((mouseX - x_lineal_links) / delta, mouseX, y_lineal_oben - y_lineal_oben / 100 * 2)
        stroke (255, 0, 0)
        strokeWeight (5)
        line (mouseX, y_lineal_oben + 2, mouseX, y_lineal_oben + y_lineal_oben / 100 * 12)
        
    # Info-Text unter Lineal
    textAlign (CENTER)
    textSize (displayhoehe / 100 * 3)
    fill (0, 150, 0)
    text ("Anzeigen der Binaerzahl => mit dem Mauszeiger im Linealbereich herumbewegen.", displaybreite / 2, displayhoehe - displayhoehe / 100 * 10)

# Funktion für das Schliessen des Fensters (da Fullscreen-Ansicht)
def fenster_schliessen():
    global displayhoehe, displaybreite
    if mouseX in range (displaybreite * 4 / 100, displaybreite * 4 / 100 + displayhoehe / 100 * 2) and mouseY in range (displayhoehe / 2, displayhoehe / 2 + displayhoehe / 100 * 2) and mousePressed == True:
        exit ()    
