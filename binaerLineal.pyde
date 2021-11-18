# wiederkehrende Variablen
displayhoehe = 1080
displaybreite = 1920
displayzaehler = 0
x_lineal_links = displaybreite / 100 * 10
x_lineal_rechts = displaybreite - x_lineal_links
delta = (x_lineal_rechts - x_lineal_links) / 256
y_lineal_oben = displayhoehe / 100 * 70
y_lineal_unten = displayhoehe / 100 * 85
x_marker_a = 0
x_marker_s = 0
x_marker_d = 0
run = 0

def setup ():
    global displayhoehe, displaybreite
    size (displaybreite, displayhoehe)
    fullScreen ()
    background (0, 0, 0)
    # Übermalt Zahl wieder mit weiss
    frameRate (100)
    
def draw ():
    global run
    intro()
    if run == 1:
        smartphone_ansicht()
        titel()
        info_button()
        home_button()
        lineal_buttons()
        displayzaehler_reset()
        markierungen_reset()
        beschriftung()
        infotext_marker()
        infotext_lineal()
        lineal()
        marker()
        fenster_schliessen()

def intro():
    global run, displayhoehe, displaybreite
    fill (100, 100, 100)
    textAlign (CENTER)
    textSize (displayhoehe / 100 * 20)
    text ("Live-Binaerlineal", displaybreite / 2, displayhoehe / 4)
    textSize (displayhoehe / 100 * 4)
    fill (255, 255, 255)
    text ("=> Mauszeiger auf Lineal nach links oder rechts bewegen.", displaybreite / 2, displayhoehe / 3)
    textSize (displayhoehe / 100 * 6)
    fill (0, 255 , 100)
    text ("Taste 'R' => Live-Binaerlineal wird gestartet", displaybreite / 2, displayhoehe / 3 * 2)
    fill (255, 0 , 0)
    text ("Taste 'Esc' => Programm wird beendet", displaybreite / 2, displayhoehe / 4 * 3)
    if keyPressed == True:
        delay (1)
        if key == "r":
            run = 1
    return run

def info_button():
    global displayhoehe, displaybreite
    strokeWeight (5)
    stroke (140, 140, 140)
    fill (140, 140, 140)
    rect (displaybreite / 100 * 85, displayhoehe / 100 * 6, displaybreite / 100 * 10 , displayhoehe / 100 * 10, 10)
    textAlign (CENTER)
    fill (0, 0, 0)
    textSize (displayhoehe / 100 * 6)
    text ("Infos", displaybreite / 100 * 90, displayhoehe / 100 * 13)

def titel():
    global displayhoehe, displaybreite
    textSize (displayhoehe / 100 * 12)
    fill (0, 0, 0)
    textAlign (CENTER)
    text ("Binaerlineal", displaybreite / 2, displayhoehe / 100 * 15)
    strokeWeight (displayhoehe / 100 * 3)
    stroke (0, 0, 0)
    line (0, displayhoehe / 100 * 20, displaybreite, displayhoehe / 100 * 20)

# Ausgabe der Binärzahl
def beschriftung():
    global x_marker_a, x_marker_s, x_marker_d, displayzaehler, displayhoehe, displaybreite, x_lineal_links, x_lineal_rechts, delta, y_lineal_oben, y_lineal_unten                   
    # Beschriftungen
    textAlign (LEFT)
    textSize (displayhoehe / 100 * 7)
    fill (200, 55, 55)
    text ("Live-Binaerzahl", displaybreite / 100 * 15, displayhoehe / 100 * 35)
    textSize (displayhoehe / 100 * 4)
    fill (20, 120, 120)  
    text ("Markierung 'A':", displaybreite / 100 * 22, displayhoehe / 100 * 45)
    fill (220, 100, 10)
    text ("Markierung 'S':", displaybreite / 100 * 22, displayhoehe / 100 * 50)
    fill (200, 50, 200)
    text ("Markierung 'D':", displaybreite / 100 * 22, displayhoehe / 100 * 55)
    
    # Binärzahlberechnung und Ausgabe (.replace entfernt das "0b" bei der Binärzahl)
    binary = bin(((mouseX - x_lineal_links) / delta) + displayzaehler * 250).replace("0b", "")
    fill (0, 0, 0)
    textSize (displayhoehe / 100 * 7)
    if mouseX in range (x_lineal_links, x_lineal_rechts) and mouseY in range (y_lineal_oben, y_lineal_unten):
        text (binary, displaybreite / 100 * 50, displayhoehe / 100 * 35)

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
    if mouseX in range (displaybreite * 4 / 100, displaybreite * 4 / 100 + displayhoehe / 100 * 2) and mouseY in range (displayhoehe / 2, displayhoehe / 2 + displayhoehe / 100 * 2):
        strokeWeight (1)
        textSize (displayhoehe / 100 * 2)
        textAlign (LEFT)
        text ("Fenster schliessen:", displaybreite / 100 * 4, displayhoehe / 2 - displayhoehe / 100 * 6)
        text ("=> Klick auf roten Button", displaybreite / 100 * 4, displayhoehe / 2 - displayhoehe / 100 * 3)

# Veränderung von Displayzähler und somit der Linealskala
def mouseClicked():
    global displayzaehler
    if mouseButton == LEFT:
        displayzaehler = displayzaehler - 1
    if mouseButton == RIGHT:
        displayzaehler = displayzaehler + 1
    return displayzaehler

# Displayzähler zurücksetzen auf 0
def displayzaehler_reset():
    global displayzaehler
    if keyPressed == True:
        if key == "q":
            displayzaehler = 0
    return displayzaehler

# bestehende Markierungen löschen
def markierungen_reset():
    global x_marker_a, x_marker_s, x_marker_d
    if keyPressed == True:
        if key == "f":
            x_marker_a = 0
            x_marker_s = 0
            x_marker_d = 0
    return x_marker_a, x_marker_s, x_marker_d

# Info-Text neben "Markierungsanzeige"
def infotext_marker():
    if mouseX in range (displaybreite / 100 * 85, displaybreite / 100 * 95) and mouseY in range (displayhoehe / 100 * 6, displayhoehe / 100 * 16):
        textAlign (LEFT)
        fill (0, 150, 0)
        textSize (displayhoehe / 100 * 4)
        text ("Markierungen setzen", displaybreite / 100 * 75, displayhoehe / 100 * 35)
        text ("Markierungen loeschen", displaybreite / 100 * 75, displayhoehe / 100 * 55)
        textSize (displayhoehe / 100 * 3)
        text ("=> Tasten 'A', 'S' und 'D'", displaybreite / 100 * 75, displayhoehe / 100 * 43)
        text ("=> Taste 'F'", displaybreite / 100 * 75, displayhoehe / 100 * 60)
        textSize (displayhoehe / 100 * 2)
        text ("(wenn Maus im Linealbereich)", displaybreite / 100 * 75, displayhoehe / 100 * 38)

# Info-Text unter Lineal
def infotext_lineal():
    textAlign (CENTER)
    textSize (displayhoehe / 100 * 3)
    fill (0, 150, 0)
    if mouseX in range (displaybreite / 100 * 85, displaybreite / 100 * 95) and mouseY in range (displayhoehe / 100 * 6, displayhoehe / 100 * 16):
        text ("Skala anpassen: Maustaste links => - 250 ; Maustaste rechts => + 250", displaybreite / 2, displayhoehe - displayhoehe / 100 * 15)
        text ("Reset der Skala mit der Taste 'Q' !!", displaybreite / 2, displayhoehe - displayhoehe / 100 * 10)
    if mouseX in range (x_lineal_links - 10, x_lineal_links + displayhoehe / 100 * 10 + 10) and mouseY in range (y_lineal_unten + displayhoehe / 100 * 5 - 10, y_lineal_unten + displayhoehe / 100 * 5 + displayhoehe / 100 * 10 + 10):
        text ("Automatisches Skala-Scrolling: Klick und Maus nicht bewegen!!", displaybreite / 2, displayhoehe - displayhoehe / 100 * 15)
        text ("=>  -/+ 250 pro Sekunde", displaybreite / 2, displayhoehe - displayhoehe / 100 * 10)
    if mouseX in range (x_lineal_rechts - displayhoehe / 100 * 10 - 10, x_lineal_rechts + 10) and mouseY in range (y_lineal_unten + displayhoehe / 100 * 5 - 10, y_lineal_unten + displayhoehe / 100 * 5 + displayhoehe / 100 * 10 + 10):
        text ("Automatisches Skala-Scrolling: Klick und Maus nicht bewegen!!", displaybreite / 2, displayhoehe - displayhoehe / 100 * 15)
        text ("=>  -/+ 2500 pro Sekunde", displaybreite / 2, displayhoehe - displayhoehe / 100 * 10)
    

# X-Wert von Marker (letzter Wert) festlegen, wenn Taste "a", "s" oder "d" gedrückt wird, Zurücksetzen der Marker bei Taste "f"
def marker():
    global x_marker_a, x_marker_s, x_marker_d, displayhoehe, displaybreite
    if mouseX in range (x_lineal_links, x_lineal_rechts) and mouseY in range (y_lineal_oben, y_lineal_unten):
        if keyPressed == True:
            if key == "a":
                x_marker_a = mouseX
        if keyPressed == True:
            if key == "s":
                x_marker_s = mouseX
        if keyPressed == True:
            if key == "d":
                x_marker_d = mouseX
    return x_marker_a, x_marker_s, x_marker_d

# Marker zeichnen und beschriften, wenn Taste "a", "s" oder "d" losgelassen wird + Binärzahl berechnen und notieren
def keyReleased():
    global x_marker_a, x_marker_s, x_marker_d, y_lineal_oben, displaybreite, delta, x_lineal_links, displayzaehler
    textAlign (LEFT)
    strokeWeight (5)
    textSize (displayhoehe / 100 * 4)
    if x_marker_a > 0: 
        stroke (20, 120, 120)
        fill (20, 120, 120)
        line (x_marker_a, y_lineal_oben, x_marker_a, y_lineal_oben - displayhoehe / 100 * 10)
        triangle (x_marker_a, y_lineal_oben - displayhoehe / 100 * 10, x_marker_a, y_lineal_oben - displayhoehe / 100 * 6, x_marker_a + displaybreite / 100 * 2, y_lineal_oben - displayhoehe / 100 * 8)
        binary = bin(((x_marker_a - x_lineal_links) / delta) + displayzaehler * 250).replace("0b", "")
        text (binary, displaybreite / 100 * 40, displayhoehe / 100 * 45)
        text (((x_marker_a - x_lineal_links) / delta) + displayzaehler * 250, x_marker_a + displaybreite / 100 * 3, y_lineal_oben - displayhoehe / 100 * 7)
    if x_marker_s > 0:
        stroke (220, 100, 0)
        fill (220, 100, 0)
        line (x_marker_s, y_lineal_oben, x_marker_s, y_lineal_oben - displayhoehe / 100 * 10)
        triangle (x_marker_s, y_lineal_oben - displayhoehe / 100 * 10, x_marker_s, y_lineal_oben - displayhoehe / 100 * 6, x_marker_s + displaybreite / 100 * 2, y_lineal_oben - displayhoehe / 100 * 8)
        binary = bin(((x_marker_s - x_lineal_links) / delta) + displayzaehler * 250).replace("0b", "")
        text (binary, displaybreite / 100 * 40, displayhoehe / 100 * 50)
        text (((x_marker_s - x_lineal_links) / delta) + displayzaehler * 250, x_marker_s + displaybreite / 100 * 3, y_lineal_oben - displayhoehe / 100 * 7)
    if x_marker_d > 0:
        stroke (200, 50, 200)
        fill (200, 50, 200)
        line (x_marker_d, y_lineal_oben, x_marker_d, y_lineal_oben - displayhoehe / 100 * 10)
        triangle (x_marker_d, y_lineal_oben - displayhoehe / 100 * 10, x_marker_d, y_lineal_oben - displayhoehe / 100 * 6, x_marker_d + displaybreite / 100 * 2, y_lineal_oben - displayhoehe / 100 * 8)
        binary = bin(((x_marker_d - x_lineal_links) / delta) + displayzaehler * 250).replace("0b", "")
        text (binary, displaybreite / 100 * 40, displayhoehe / 100 * 55)
        text (((x_marker_d - x_lineal_links) / delta) + displayzaehler * 250, x_marker_d + displaybreite / 100 * 3, y_lineal_oben - displayhoehe / 100 * 7)

# Buttons (+ und - für schnelles / langsames Verändern der Skala)
def lineal_buttons():
    global displayzaehler, displayhoehe, displaybreite, x_lineal_links, x_lineal_rechts, delta, y_lineal_oben, y_lineal_unten
    strokeWeight (10)
    stroke (0, 50, 200)
    fill (0, 50, 200)
    rect (x_lineal_links, y_lineal_unten + displayhoehe / 100 * 5, displayhoehe / 100 * 10, displayhoehe / 100 * 10, 50)
    stroke (255, 255, 255)
    line (x_lineal_links + displayhoehe / 100 * 2, y_lineal_unten + displayhoehe / 100 * 10, x_lineal_links + displayhoehe / 100 * 8, y_lineal_unten + displayhoehe / 100 * 10)
    stroke (0, 155, 55)
    fill (0, 155, 55)
    rect (x_lineal_rechts - displayhoehe / 100 * 10, y_lineal_unten + displayhoehe / 100 * 5, displayhoehe / 100 * 10, displayhoehe / 100 * 10, 50)
    stroke (255, 255, 255)
    line (x_lineal_rechts - displayhoehe / 100 * 8, y_lineal_unten + displayhoehe / 100 * 10, x_lineal_rechts - displayhoehe / 100 * 2, y_lineal_unten + displayhoehe / 100 * 10)
    line (x_lineal_rechts - displayhoehe / 100 * 5, y_lineal_unten + displayhoehe / 100 * 7, x_lineal_rechts - displayhoehe / 100 * 5, y_lineal_unten + displayhoehe / 100 * 13)
    noStroke ()
    if mouseX in range (x_lineal_links, x_lineal_links + displayhoehe / 100 * 10) and mouseY in range (y_lineal_unten + displayhoehe / 100 * 5, y_lineal_unten + displayhoehe / 100 * 5 + displayhoehe / 100 * 10):
        cursor (HAND)
        delay (1000)
        mouseClicked()
    if mouseX in range (x_lineal_rechts - displayhoehe / 100 * 10, x_lineal_rechts) and mouseY in range (y_lineal_unten + displayhoehe / 100 * 5, y_lineal_unten + displayhoehe / 100 * 5 + displayhoehe / 100 * 10):
        cursor (HAND)
        delay (100)
        mouseClicked()
    
# Lineal-Design und Marker zeichnen bei Lineal 
def lineal():
    global displayzaehler, displayhoehe, displaybreite, x_lineal_links, x_lineal_rechts, delta, y_lineal_oben, y_lineal_unten
    frameRate (100)
    x_wert = 0
    
    # Linealkontur
    noFill()
    strokeWeight (2)
    stroke (0, 0, 0)
    rect (x_lineal_links, y_lineal_oben, x_lineal_rechts - x_lineal_links, y_lineal_unten - y_lineal_oben, 5)        
    
    # 1er-Striche auf dem Lineal
    for einer in range (1, 257):
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
        textSize (displayhoehe / 100 * 1.5)
        textAlign (CENTER)
        fill (200, 55, 55)
        text (zehner * 10 + displayzaehler * 250, x_wert, y_lineal_oben + (y_lineal_oben / 100 * 20))

    # Anzeige grüner Balken
    noStroke ()
    if mouseX in range (x_lineal_links, x_lineal_rechts) and mouseY in range (y_lineal_oben, y_lineal_unten):
        fill (0, 255 - (mouseX / 10), 0)
        rect (x_lineal_links, y_lineal_oben, mouseX - x_lineal_links, displayhoehe / 100 * 3, 10)
        textSize (displayhoehe / 100 * 6)
        text (((mouseX - x_lineal_links) / delta) + displayzaehler * 250, mouseX, y_lineal_oben - y_lineal_oben / 100 )
        stroke (255, 0, 0)
        strokeWeight (5)
        line (mouseX, y_lineal_oben + 2, mouseX, y_lineal_oben + y_lineal_oben / 100 * 12)

    # Marker zeichnen und beschriften
    keyReleased()

# Funktion für das Schliessen des Fensters (da Fullscreen-Ansicht)
def fenster_schliessen():
    global displayhoehe, displaybreite
    if mouseX in range (displaybreite * 4 / 100, displaybreite * 4 / 100 + displayhoehe / 100 * 2) and mouseY in range (displayhoehe / 2, displayhoehe / 2 + displayhoehe / 100 * 2):
        cursor (HAND)
        if mousePressed == True:
            cursor (WAIT)
            delay(1000)
            exit ()
    if mouseX not in range (displaybreite * 4 / 100, displaybreite * 4 / 100 + displayhoehe / 100 * 2) or mouseY not in range (displayhoehe / 2, displayhoehe / 2 + displayhoehe / 100 * 2):
        cursor (ARROW)
