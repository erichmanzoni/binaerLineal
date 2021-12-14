# Buchstabe 'u' (für Unicode) vor sämtlichen Textausgaben eingefügt, damit Problem mit Umlautdarstellung nicht auftritt (unabhängig ob Umlaut im Text oder nicht)

# wiederkehrende Variablen
# displayhoehe = initial festgelegter Wert für die Anzeigehöhe des Programms
# displaybreite = initial festgelegter Wert für die Anzeigebreite des Programms
# displayzaehler = Multiplikator für die angezeigten Skalawerte (Startwert = 0)
# x_lineal_links = x-Koordinaten-Startwert des Lineals (bei 10 % der Displaybreite) 
# x_lineal_rechts = x-Koordinaten-Endwert des Lineals (bei 90 % der Displaybreite)
# delta = Pixelabstand zwischen zwei Werten auf dem Lineal, abhängig von den beiden x-Werten (Start- und Endwert) des Lineals und der gewünschten Unterteilung
# y_lineal_oben = y-Koordinaten-Startwert des Lineals (bei 70 % der Displayhöhe)
# y_lineal_unten = x-Koordinaten-Endwert des Lineals (bei 85 % der Displayhöhe)
# x_marker_a = x-Koordinaten-Wert der Markierung, wenn die Taste 'A' gedrückt wird (Startwert = 0)
# x_marker_s = x-Koordinaten-Wert der Markierung, wenn die Taste 'S' gedrückt wird (Startwert = 0)
# x_marker_d = x-Koordinaten-Wert der Markierung, wenn die Taste 'D' gedrückt wird (Startwert = 0)
# run = Variable für die Aktivierung des Hauptprogramms (Startwert = 0; sobald Wert bei 1 wird Hauptprogramm gestartet)
# Font = Definition der Schriftart

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

# Festlegung der grundlegenden Einstellungen
def setup ():
    
    # displayhoehe = initial festgelegter Wert für die Anzeigehöhe des Programms
    # displaybreite = initial festgelegter Wert für die Anzeigebreite des Programms
    # Font = Definition der Schriftart
    global displayhoehe, displaybreite, Font
    
    size (displaybreite, displayhoehe)
    fullScreen ()
    background (0, 0, 0)
    Font = createFont ("Arial Bold", 18)
    
# Zeichnerische Darstellung des gesamten Programms    
def draw ():
    
    # displayhoehe = initial festgelegter Wert für die Anzeigehöhe des Programms
    # displaybreite = initial festgelegter Wert für die Anzeigebreite des Programms
    # run = Variable für die Aktivierung des Hauptprogramms (Startwert = 0; sobald Wert bei 1 wird Hauptprogramm gestartet)
    # Font = Definition der Schriftart
    global displayhoehe, displaybreite, run, Font
    
    textFont (Font)
    
    # Darstellung der Introseite
    intro ()
    
    # Darstellung des Hauptprogramms (Ansicht der Infoseite und des Binärlineals)
    if run == 1:
        
        # Anzeige der Informationsseite, wenn der Mauszeiger im Bereich des Infos-Button
        if mouseX in range (displaybreite / 100 * 85, displaybreite / 100 * 95) and mouseY in range (displayhoehe / 100 * 6, displayhoehe / 100 * 16):
            info_fenster ()
            info_button ()
            titel ()
            alle_infos ()
        
        # Anzeige des Binärlineals, wenn der Mauszeiger nicht im Bereich des Infos-Button
        elif mouseX not in range (displaybreite / 100 * 85, displaybreite / 100 * 95) or mouseY not in range (displayhoehe / 100 * 6, displayhoehe / 100 * 16):
            smartphone_ansicht ()
            titel ()
            info_button ()
            home_button ()
            lineal_buttons ()
            lineal ()
            marker ()
            beschriftung ()
            displayzaehler_reset ()
            markierungen_reset ()
            infotext_marker ()
            infotext_lineal ()
            fenster_schliessen ()
        
# Intro-Seite mit Infos und Möglichkeit über ESC-Taste das Programm gleich wieder zu beenden oder über Taste 'R' (-> Rückgabe von run mit Wert 1, wenn die Taste 'R' gedrückt wird) zu starten
def intro ():
    
    # displayhoehe = initial festgelegter Wert für die Anzeigehöhe des Programms
    # displaybreite = initial festgelegter Wert für die Anzeigebreite des Programms
    # run = Variable für die Aktivierung des Hauptprogramms (Startwert = 0; sobald Wert bei 1 wird Hauptprogramm gestartet)
    global displayhoehe, displaybreite, run
    
    if run == 0:
        fill (100, 100, 100)
        textAlign (CENTER)
        textSize (displayhoehe / 100 * 20)
        text (u"Live-Binärlineal", displaybreite / 2, displayhoehe / 4)
        textSize (displayhoehe / 100 * 4)
        fill (255, 255, 255)
        text (u"=> Mauszeiger auf Lineal nach links oder rechts bewegen.", displaybreite / 2, displayhoehe / 3)
        text (u"=> Für weitere Informationen die Maus auf den Infos-Button", displaybreite / 2, displayhoehe / 3 + displayhoehe / 100 * 10)
        text (u"oder einzelne Fensterelemente bewegen.", displaybreite / 2, displayhoehe / 3 + displayhoehe / 100 * 15)
        textSize (displayhoehe / 100 * 6)
        fill (0, 255 , 100)
        text (u"Taste 'R' => Live-Binärlineal wird gestartet", displaybreite / 2, displayhoehe / 3 * 2)
        fill (255, 0 , 0)
        text (u"Taste 'Esc' => Programm wird beendet", displaybreite / 2, displayhoehe / 4 * 3)
        if keyPressed == True:
            delay (1)
            if key == "r":
                run = 1
    return run

# Visualisierung des grossen Infofensters
def info_fenster ():
    
    # displayhoehe = initial festgelegter Wert für die Anzeigehöhe des Programms
    # displaybreite = initial festgelegter Wert für die Anzeigebreite des Programms
    global displayhoehe, displaybreite
    
    # gleicher Code wie beim Smartphone-Design, lediglich anderer Farbwert bei der Füllung des Rechtecks
    noStroke ()
    fill (200, 200, 200)
    rect (displayhoehe / 100 * 2, displaybreite / 100, displaybreite - (displaybreite / 100 * 2), displayhoehe - (displayhoehe / 100 * 4), 70)

# Visualisierung des Smartphone-Designs
def smartphone_ansicht (): 
    
    # displayhoehe = initial festgelegter Wert für die Anzeigehöhe des Programms
    # displaybreite = initial festgelegter Wert für die Anzeigebreite des Programms
    global displayhoehe, displaybreite   
    
    # gleicher Code wie beim Info-Fenster, lediglich anderer Farbwert bei der Füllung des Rechtecks
    noStroke ()
    fill (255, 255, 255)
    rect (displayhoehe / 100 * 2, displaybreite / 100, displaybreite - (displaybreite / 100 * 2), displayhoehe - (displayhoehe / 100 * 4), 70)

# Visualisierung von Programmtitel und Trennlinie
def titel ():

    # displayhoehe = initial festgelegter Wert für die Anzeigehöhe des Programms
    # displaybreite = initial festgelegter Wert für die Anzeigebreite des Programms    
    global displayhoehe, displaybreite
    
    textSize (displayhoehe / 100 * 12)
    fill (0, 0, 0)
    textAlign (CENTER)
    text (u"Binärlineal", displaybreite / 2, displayhoehe / 100 * 15)
    strokeWeight (displayhoehe / 100 * 3)
    stroke (0, 0, 0)
    line (0, displayhoehe / 100 * 20, displaybreite, displayhoehe / 100 * 20)

# Visualisierung aller Text-Infos im Info-Fenster
def alle_infos ():
    
    # displayhoehe = initial festgelegter Wert für die Anzeigehöhe des Programms
    # displaybreite = initial festgelegter Wert für die Anzeigebreite des Programms
    global displayhoehe, displaybreite
    
    fill (0, 0, 0)
    textAlign (LEFT)
    textSize (displayhoehe / 100 * 4)
    text (u"Programm schliessen:", displaybreite / 100 * 5, displayhoehe / 100 * 40)
    text (u"=> auf roten Homebutton klicken", displaybreite / 3, displayhoehe / 100 * 40)
    text (u"Anzeige Live-Binärzahl:", displaybreite / 100 * 5, displayhoehe / 100 * 50)
    text (u"=> Mauszeiger auf Lineal nach links oder rechts bewegen", displaybreite / 3, displayhoehe / 100 * 50)
    text (u"Markierungen setzen:", displaybreite / 100 * 5, displayhoehe / 100 * 60)
    text (u"=> Tasten 'A', 'S' & 'D', wenn Maus im Linealbereich", displaybreite / 3, displayhoehe / 100 * 60)
    text (u"Lineal-Skala anpassen:", displaybreite / 100 * 5, displayhoehe / 100 * 70)
    text (u"=> mit Maustasten:   links = - 250 ;   rechts = + 250", displaybreite / 3, displayhoehe / 100 * 70)
    text (u"Auto-Skala-Scrolling:", displaybreite / 100 * 5, displayhoehe / 100 * 80)
    text (u"=> Klick auf blauen / grünen Button und Maus nicht bewegen", displaybreite / 3, displayhoehe / 100 * 80)
    text (u"Reset-Funktionen:", displaybreite / 100 * 5, displayhoehe / 100 * 90)
    text (u"=> Skala: Taste 'Q' ;   Markierungen: Taste 'F'", displaybreite / 3, displayhoehe / 100 * 90)

# Visualisierung des Infos-Button (einzublende Text-Infos unter "def alle_infos" zu finden)
def info_button ():
    
    # displayhoehe = initial festgelegter Wert für die Anzeigehöhe des Programms
    # displaybreite = initial festgelegter Wert für die Anzeigebreite des Programms
    global displayhoehe, displaybreite
    
    strokeWeight (5)
    stroke (0, 0, 0)
    fill (200, 200, 200)
    rect (displaybreite / 100 * 85, displayhoehe / 100 * 6, displaybreite / 100 * 10 , displayhoehe / 100 * 10, 10)
    textAlign (CENTER)
    fill (0, 0, 0)
    textSize (displayhoehe / 100 * 6)
    text (u"Infos", displaybreite / 100 * 90, displayhoehe / 100 * 13)

# Visualisierung des Homebuttons (für Schliessen des Fensters --> da Fullscreen-Ansicht; inkl. Info-Text, wenn Maus auf rotem Homebutton)     
def home_button ():
    
    # displayhoehe = initial festgelegter Wert für die Anzeigehöhe des Programms
    # displaybreite = initial festgelegter Wert für die Anzeigebreite des Programms
    global displayhoehe, displaybreite
    
    strokeWeight (displayhoehe / 100 * 4)
    stroke (0, 0, 0)
    fill (200, 55, 55)
    rect (displaybreite / 100 * 4, displayhoehe / 2, displayhoehe / 100 * 2, displayhoehe / 100 * 2, 3)
    
    # Info-Text erscheint nur, wenn Maus im Bereich des Homebuttons
    if mouseX in range (displaybreite * 4 / 100, displaybreite * 4 / 100 + displayhoehe / 100 * 2) and mouseY in range (displayhoehe / 2, displayhoehe / 2 + displayhoehe / 100 * 2):
        strokeWeight (1)
        textSize (displayhoehe / 100 * 2)
        textAlign (LEFT)
        text (u"Programm schliessen:", displaybreite / 100 * 4, displayhoehe / 2 - displayhoehe / 100 * 6)
        text (u"=> Klick auf roten Button", displaybreite / 100 * 4, displayhoehe / 2 - displayhoehe / 100 * 3)

# Visualiserung der beiden Buttons links und rechts des Lineals (inkl. Darstellung der Zeichen für schnelles / langsames "Spulen") sowie Initialisierung der Linealskalaverändernung, wenn Maus auf einem der beiden Buttons und es zu einem Mausklick kommt 
def lineal_buttons ():
    
    # displayhoehe = initial festgelegter Wert für die Anzeigehöhe des Programms
    # x_lineal_links = x-Koordinaten-Startwert des Lineals (bei 10 % der Displaybreite) 
    # x_lineal_rechts = x-Koordinaten-Endwert des Lineals (bei 90 % der Displaybreite)
    # y_lineal_unten = x-Koordinaten-Endwert des Lineals (bei 85 % der Displayhöhe)
    global displayhoehe, x_lineal_links, x_lineal_rechts, y_lineal_unten
    
    strokeWeight (displayhoehe / 100)
    # Design des linken Lineal-Buttons
    stroke (0, 50, 200)
    fill (0, 50, 200)
    rect (x_lineal_links, y_lineal_unten + displayhoehe / 100 * 3, displayhoehe / 100 * 8, displayhoehe / 100 * 8, 50)
    
    # Design des rechten Lineal-Buttons
    stroke (0, 155, 55)
    fill (0, 155, 55)
    rect (x_lineal_rechts - displayhoehe / 100 * 8, y_lineal_unten + displayhoehe / 100 * 3, displayhoehe / 100 * 8, displayhoehe / 100 * 8, 50)
    
    # Design des Zeichens für langsames "Spulen" auf dem linken Lineal-Button und für schnelles "Spulen" auf dem rechten Lineal-Button 
    fill (255, 255, 255)
    textSize (displayhoehe / 100 * 3)
    textAlign (CENTER)
    
    # Zeichen links (langsames "Spulen")
    text (u"<", x_lineal_links + displayhoehe / 100 * 4, y_lineal_unten + displayhoehe / 100 * 7)
    text (u">", x_lineal_links + displayhoehe / 100 * 4, y_lineal_unten + displayhoehe / 100 * 9)
    
    # Zeichen rechts (schnelles "Spulen")
    text (u"<<<<", x_lineal_rechts - displayhoehe / 100 * 4, y_lineal_unten + displayhoehe / 100 * 7)
    text (u">>>>", x_lineal_rechts - displayhoehe / 100 * 4, y_lineal_unten + displayhoehe / 100 * 9)
            
    # schnelles / langsames Verändern "Spulen" der Linealskala, wenn der Mauszeiger im Bereich des jeweiligen Buttons links oder rechts (inkl. Cursorveränderung) und wenn es gleichzeitig zu einem Mausklick (egal ob linke oder rechte Maustaste) kommt
    noStroke ()
    # langsames "Spulen" beim linken Lineal-Button (aufgrund des Delaywertes von 1000 -> entspricht 1 Änderung pro Sekunde)
    if mouseX in range (x_lineal_links, x_lineal_links + displayhoehe / 100 * 8) and mouseY in range (y_lineal_unten + displayhoehe / 100 * 3, y_lineal_unten + displayhoehe / 100 * 3 + displayhoehe / 100 * 8):
        cursor (HAND)
        delay (1000)
        mouseClicked ()
        
    # schnelles "Spulen" beim rechten Lineal-Button (aufgrund des Delaywertes von 100 -> entspricht 1 Änderung pro 1/10 Sekunde)
    if mouseX in range (x_lineal_rechts - displayhoehe / 100 * 8, x_lineal_rechts) and mouseY in range (y_lineal_unten + displayhoehe / 100 * 3, y_lineal_unten + displayhoehe / 100 * 3 + displayhoehe / 100 * 8):
        cursor (HAND)
        delay (100)
        mouseClicked ()

# Veränderung des Displayzählers aufgrund des Drückens der linken oder rechten Maustaste und somit Anpassung der Linealskala
def mouseClicked ():
    
    # displayzaehler = Multiplikator für die angezeigten Skalawerte (Startwert = 0)
    global displayzaehler
    
    if mouseButton == LEFT:
        displayzaehler = displayzaehler - 1
    if mouseButton == RIGHT:
        displayzaehler = displayzaehler + 1
    return displayzaehler

# Visualisierung des Lineal-Designs und Setzen der Marker beim Lineal, wenn gedrückte Taste losgelassen wird
def lineal ():
    
    # displayhoehe = initial festgelegter Wert für die Anzeigehöhe des Programms
    # displayzaehler = Multiplikator für die angezeigten Skalawerte (Startwert = 0)
    # x_lineal_links = x-Koordinaten-Startwert des Lineals (bei 10 % der Displaybreite) 
    # x_lineal_rechts = x-Koordinaten-Endwert des Lineals (bei 90 % der Displaybreite)
    # delta = Pixelabstand zwischen zwei Werten auf dem Lineal, abhängig von den beiden x-Werten (Start- und Endwert) des Lineals und der gewünschten Unterteilung
    # y_lineal_oben = y-Koordinaten-Startwert des Lineals (bei 70 % der Displayhöhe)
    # y_lineal_unten = x-Koordinaten-Endwert des Lineals (bei 85 % der Displayhöhe)
    global displayhoehe, displayzaehler, x_lineal_links, x_lineal_rechts, delta, y_lineal_oben, y_lineal_unten
    
    frameRate (100)
    # x_wert = lokale Variable, welche unabhänig der restlichen Variablen innerhalb von "def lineal ():" stets mit dem Wert 0 starten muss (wird nur für das Zeichnen der Lineal-Striche benötigt) 
    x_wert = 0
    
    # Visualisierung der Linealkontur
    noFill ()
    strokeWeight (2)
    stroke (0, 0, 0)
    rect (x_lineal_links, y_lineal_oben, x_lineal_rechts - x_lineal_links, y_lineal_unten - y_lineal_oben, 5)        
    
    # Visualisierung der 1er-Striche auf dem Lineal (einer = Zählervariable für diese Schleife)
    for einer in range (1, 257):
        x_wert = x_lineal_links + (1 * einer * delta)
        strokeWeight (1)
        line (x_wert, y_lineal_oben, x_wert, y_lineal_oben + (y_lineal_oben / 100 * 6))
    
    # Visualisierung der 5er-Striche auf dem Lineal (fuenfer = Zählervariable für diese Schleife)
    for fuenfer in range (1, 52):
        x_wert = x_lineal_links + ( 5 * fuenfer * delta)
        strokeWeight (3)
        line (x_wert, y_lineal_oben + 1, x_wert, y_lineal_oben + (y_lineal_oben / 100 * 10))    
    
    # Visualisierung der 10er-Striche auf dem Lineal (zehner = Zählervariable für diese Schleife) sowie 10er-Beschriftung im Lineal drin
    for zehner in range (1, 26):
        x_wert = x_lineal_links + (10 * zehner * delta)
        strokeWeight (5)
        line (x_wert, y_lineal_oben + 2, x_wert, y_lineal_oben + (y_lineal_oben / 100 * 14))
        textSize (displayhoehe / 100 * 1.5)
        textAlign (CENTER)
        fill (200, 55, 55)
        text (zehner * 10 + displayzaehler * 250, x_wert, y_lineal_oben + (y_lineal_oben / 100 * 20))

    # Visualisierung des grünen (Grünton abhängig von X-Wert der Maus) Live-Balkens innerhalb des Lineals, nur dann wenn Mauszeiger im Bereich des Lineals
    noStroke ()
    if mouseX in range (x_lineal_links, x_lineal_rechts) and mouseY in range (y_lineal_oben, y_lineal_unten):
        fill (0, 255 - (mouseX / 10), 0)
        rect (x_lineal_links, y_lineal_oben, mouseX - x_lineal_links, y_lineal_oben / 100 * 4, 10)
        textSize (displayhoehe / 100 * 6)
        text (((mouseX - x_lineal_links) / delta) + displayzaehler * 250, mouseX, y_lineal_oben - y_lineal_oben / 100 )
        stroke (255, 0, 0)
        strokeWeight (5)
        line (mouseX, y_lineal_oben + 2, mouseX, y_lineal_oben + y_lineal_oben / 100 * 14)

    # Marker zeichnen und beschriften, wenn die entsprechende Taste losgelassen wird
    keyReleased ()    

# Visualisierung der Tasten-Marker inkl. Beschriftung, wenn Taste 'A', 'S' oder 'D' losgelassen wird sowie Berechnung und Notation der Binärzahl
def keyReleased ():
    
    # displayhoehe = initial festgelegter Wert für die Anzeigehöhe des Programms
    # displaybreite = initial festgelegter Wert für die Anzeigebreite des Programms
    # displayzaehler = Multiplikator für die angezeigten Skalawerte (Startwert = 0)
    # x_lineal_links = x-Koordinaten-Startwert des Lineals (bei 10 % der Displaybreite) 
    # delta = Pixelabstand zwischen zwei Werten auf dem Lineal, abhängig von den beiden x-Werten (Start- und Endwert) des Lineals und der gewünschten Unterteilung
    # y_lineal_oben = y-Koordinaten-Startwert des Lineals (bei 70 % der Displayhöhe)
    # x_marker_a = x-Koordinaten-Wert der Markierung, wenn die Taste 'A' gedrückt wird (Startwert = 0)
    # x_marker_s = x-Koordinaten-Wert der Markierung, wenn die Taste 'S' gedrückt wird (Startwert = 0)
    # x_marker_d = x-Koordinaten-Wert der Markierung, wenn die Taste 'D' gedrückt wird (Startwert = 0)
    # Werte für x_marker_a, x_marker_s & x_marker_d sind standardmässig auf 0 gesetzt und darum werden diese vor dem Drücker der jeweiligen Tasten noch nicht angezeigt
    global displayhoehe, displaybreite, displayzaehler, x_lineal_links, delta, y_lineal_oben, x_marker_a, x_marker_s, x_marker_d
    
    textAlign (LEFT)
    strokeWeight (5)
    textSize (displayhoehe / 100 * 4)
        
    # Visualisierung des Markers der Taste 'A' -> aktueller Wert für x_marker_a kommt von "def marker ():" und Ausgabe der Dezimalzahl beim Marker und der entsprechenden Binärzahl beim dazugehörigen Textblock (Markierung 'A':)
    if x_marker_a > 0: 
        stroke (20, 120, 120)
        fill (20, 120, 120)
        line (x_marker_a, y_lineal_oben, x_marker_a, y_lineal_oben - displayhoehe / 100 * 10)
        triangle (x_marker_a, y_lineal_oben - displayhoehe / 100 * 10, x_marker_a, y_lineal_oben - displayhoehe / 100 * 6, x_marker_a + displaybreite / 100 * 2, y_lineal_oben - displayhoehe / 100 * 8)
        
        # Binärzahlberechnung und Ausgabe der beiden Zahlen (.replace entfernt das "0b" bei der Binärzahl)
        binary = bin(((x_marker_a - x_lineal_links) / delta) + displayzaehler * 250).replace("0b", "")
        text (binary, displaybreite / 100 * 40, displayhoehe / 100 * 45)
        text (((x_marker_a - x_lineal_links) / delta) + displayzaehler * 250, x_marker_a + displaybreite / 100 * 3, y_lineal_oben - displayhoehe / 100 * 7)
    
    # Visualisierung des Markers der Taste 'S' -> aktueller Wert für x_marker_s kommt von "def marker ():" und Ausgabe der Dezimalzahl beim Marker und der entsprechenden Binärzahl beim dazugehörigen Textblock (Markierung 'S':)
    if x_marker_s > 0:
        stroke (220, 100, 0)
        fill (220, 100, 0)
        line (x_marker_s, y_lineal_oben, x_marker_s, y_lineal_oben - displayhoehe / 100 * 10)
        triangle (x_marker_s, y_lineal_oben - displayhoehe / 100 * 10, x_marker_s, y_lineal_oben - displayhoehe / 100 * 6, x_marker_s + displaybreite / 100 * 2, y_lineal_oben - displayhoehe / 100 * 8)
        
        # Binärzahlberechnung und Ausgabe der beiden Zahlen (.replace entfernt das "0b" bei der Binärzahl)
        binary = bin(((x_marker_s - x_lineal_links) / delta) + displayzaehler * 250).replace("0b", "")
        text (binary, displaybreite / 100 * 40, displayhoehe / 100 * 50)
        text (((x_marker_s - x_lineal_links) / delta) + displayzaehler * 250, x_marker_s + displaybreite / 100 * 3, y_lineal_oben - displayhoehe / 100 * 7)
    
    # Visualisierung des Markers der Taste 'D' -> aktueller Wert für x_marker_d kommt von "def marker ():" und Ausgabe der Dezimalzahl beim Marker und der entsprechenden Binärzahl beim dazugehörigen Textblock (Markierung 'D':)
    if x_marker_d > 0:
        stroke (200, 50, 200)
        fill (200, 50, 200)
        line (x_marker_d, y_lineal_oben, x_marker_d, y_lineal_oben - displayhoehe / 100 * 10)
        triangle (x_marker_d, y_lineal_oben - displayhoehe / 100 * 10, x_marker_d, y_lineal_oben - displayhoehe / 100 * 6, x_marker_d + displaybreite / 100 * 2, y_lineal_oben - displayhoehe / 100 * 8)
        
        # Binärzahlberechnung und Ausgabe der beiden Zahlen (.replace entfernt das "0b" bei der Binärzahl)
        binary = bin(((x_marker_d - x_lineal_links) / delta) + displayzaehler * 250).replace("0b", "")
        text (binary, displaybreite / 100 * 40, displayhoehe / 100 * 55)
        text (((x_marker_d - x_lineal_links) / delta) + displayzaehler * 250, x_marker_d + displaybreite / 100 * 3, y_lineal_oben - displayhoehe / 100 * 7)

# Definierung des x-Wertes vom jeweiligen Marker (aktueller x-Wert des Mauszeigers), wenn Taste 'A', 'S' oder 'D' gedrückt wird
def marker ():
    
    # x_lineal_links = x-Koordinaten-Startwert des Lineals (bei 10 % der Displaybreite) 
    # x_lineal_rechts = x-Koordinaten-Endwert des Lineals (bei 90 % der Displaybreite)
    # y_lineal_oben = y-Koordinaten-Startwert des Lineals (bei 70 % der Displayhöhe)
    # y_lineal_unten = x-Koordinaten-Endwert des Lineals (bei 85 % der Displayhöhe)
    # x_marker_a = x-Koordinaten-Wert der Markierung, wenn die Taste 'A' gedrückt wird (Startwert = 0)
    # x_marker_s = x-Koordinaten-Wert der Markierung, wenn die Taste 'S' gedrückt wird (Startwert = 0)
    # x_marker_d = x-Koordinaten-Wert der Markierung, wenn die Taste 'D' gedrückt wird (Startwert = 0)
    global x_lineal_links, x_lineal_rechts, y_lineal_oben, y_lineal_unten, x_marker_a, x_marker_s, x_marker_d
    
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

# Visualisierung diverser Beschriftungen und Ausgabe der Live-Binärzahl, wenn Maus im Bereich des Lineals bewegt wird
def beschriftung ():
    
    # displayhoehe = initial festgelegter Wert für die Anzeigehöhe des Programms
    # displaybreite = initial festgelegter Wert für die Anzeigebreite des Programms
    # displayzaehler = Multiplikator für die angezeigten Skalawerte (Startwert = 0)
    # x_lineal_links = x-Koordinaten-Startwert des Lineals (bei 10 % der Displaybreite) 
    # x_lineal_rechts = x-Koordinaten-Endwert des Lineals (bei 90 % der Displaybreite)
    # delta = Pixelabstand zwischen zwei Werten auf dem Lineal, abhängig von den beiden x-Werten (Start- und Endwert) des Lineals und der gewünschten Unterteilung
    # y_lineal_oben = y-Koordinaten-Startwert des Lineals (bei 70 % der Displayhöhe)
    # y_lineal_unten = x-Koordinaten-Endwert des Lineals (bei 85 % der Displayhöhe)
    global displayhoehe, displaybreite, displayzaehler, x_lineal_links, x_lineal_rechts, delta, y_lineal_oben, y_lineal_unten                   
    
    # Visualisierung der Beschriftungen
    textAlign (LEFT)
    textSize (displayhoehe / 100 * 7)
    fill (200, 55, 55)
    text (u"Live-Binärzahl", x_lineal_links, displayhoehe / 100 * 35)
    textSize (displayhoehe / 100 * 4)
    fill (20, 120, 120)  
    text (u"Markierung 'A':", displaybreite / 100 * 22, displayhoehe / 100 * 45)
    fill (220, 100, 10)
    text (u"Markierung 'S':", displaybreite / 100 * 22, displayhoehe / 100 * 50)
    fill (200, 50, 200)
    text (u"Markierung 'D':", displaybreite / 100 * 22, displayhoehe / 100 * 55)
    
    # Binärzahlberechnung und Ausgabe der Live-Binärzahl (.replace entfernt das "0b" bei der Binärzahl), wenn der Mauszeiger im Bereich des Lineals
    binary = bin(((mouseX - x_lineal_links) / delta) + displayzaehler * 250).replace("0b", "")
    fill (0, 0, 0)
    textSize (displayhoehe / 100 * 7)
    if mouseX in range (x_lineal_links, x_lineal_rechts) and mouseY in range (y_lineal_oben, y_lineal_unten):
        text (binary, displaybreite / 100 * 40, displayhoehe / 100 * 35)

# Displayzähler zurücksetzen auf 0, wenn die Taste 'Q' gedrückt wird (durch das auf den Startwert 0 Zurücksetzen des Displyzählers)
def displayzaehler_reset ():
    
    # displayzaehler = Multiplikator für die angezeigten Skalawerte (Startwert = 0)
    global displayzaehler
    
    if keyPressed == True:
        if key == "q":
            displayzaehler = 0
    return displayzaehler

# bestehende Markierungen löschen, wenn die Taste 'F' gedrückt wird (durch das auf den Startwert 0 Zurücksetzen der Variablen x_marker_a, x_marker_s und x_marker_d)
def markierungen_reset ():
    
    # x_marker_a = x-Koordinaten-Wert der Markierung, wenn die Taste 'A' gedrückt wird (Startwert = 0)
    # x_marker_s = x-Koordinaten-Wert der Markierung, wenn die Taste 'S' gedrückt wird (Startwert = 0)
    # x_marker_d = x-Koordinaten-Wert der Markierung, wenn die Taste 'D' gedrückt wird (Startwert = 0)
    global x_marker_a, x_marker_s, x_marker_d
    
    if keyPressed == True:
        if key == "f":
            x_marker_a = 0
            x_marker_s = 0
            x_marker_d = 0
    return x_marker_a, x_marker_s, x_marker_d

# Visualisierung des entsprechenden Info-Textes unter dem Lineal, wenn der Mauszeiger im Bereich des Lineals (Skala anpassen + Skala-Reset) oder auf einem der beiden Lineal-Buttons (automatisches Skala-Scrolling)
def infotext_lineal ():
    
    # displayhoehe = initial festgelegter Wert für die Anzeigehöhe des Programms
    # displaybreite = initial festgelegter Wert für die Anzeigebreite des Programms
    # x_lineal_links = x-Koordinaten-Startwert des Lineals (bei 10 % der Displaybreite) 
    # x_lineal_rechts = x-Koordinaten-Endwert des Lineals (bei 90 % der Displaybreite)
    # y_lineal_oben = y-Koordinaten-Startwert des Lineals (bei 70 % der Displayhöhe)
    # y_lineal_unten = x-Koordinaten-Endwert des Lineals (bei 85 % der Displayhöhe)
    global displayhoehe, displaybreite, x_lineal_links, x_lineal_recht, y_lineal_oben, y_lineal_unten
    
    textAlign (CENTER)
    textSize (displayhoehe / 100 * 3)
    if mouseX in range (x_lineal_links, x_lineal_rechts) and mouseY in range (y_lineal_oben, y_lineal_unten):
        fill (140, 140, 140)
        text (u"Skala anpassen mit Maustasten:  links => - 250 ; rechts => + 250", displaybreite / 2, y_lineal_unten + displayhoehe / 100 * 6)
        text (u"Reset der Skala mit der Taste 'Q' !!", displaybreite / 2, y_lineal_unten + displayhoehe / 100 * 10)
    if mouseX in range (x_lineal_links - 10, x_lineal_links + displayhoehe / 100 * 10 + 10) and mouseY in range (y_lineal_unten + displayhoehe / 100 * 5 - 10, y_lineal_unten + displayhoehe / 100 * 5 + displayhoehe / 100 * 10 + 10):
        fill (0, 50, 200)
        text (u"Automatisches Skala-Scrolling: Klick und Maus nicht bewegen!!", displaybreite / 2, y_lineal_unten + displayhoehe / 100 * 6)
        text (u"=>  -/+ 250 pro Sekunde", displaybreite / 2, y_lineal_unten + displayhoehe / 100 * 10)
    if mouseX in range (x_lineal_rechts - displayhoehe / 100 * 10 - 10, x_lineal_rechts + 10) and mouseY in range (y_lineal_unten + displayhoehe / 100 * 5 - 10, y_lineal_unten + displayhoehe / 100 * 5 + displayhoehe / 100 * 10 + 10):
        fill (0, 150, 0)
        text (u"Automatisches Skala-Scrolling: Klick und Maus nicht bewegen!!", displaybreite / 2, y_lineal_unten + displayhoehe / 100 * 6)
        text (u"=>  -/+ 2500 pro Sekunde", displaybreite / 2, y_lineal_unten + displayhoehe / 100 * 10)

# Visualisierung des Info-Text neben der "Markierungsanzeige", wenn der Mauszeiger im Bereich des Lineals (Markierung setzen & löschen)
def infotext_marker ():
    
    # displayhoehe = initial festgelegter Wert für die Anzeigehöhe des Programms
    # displaybreite = initial festgelegter Wert für die Anzeigebreite des Programms
    # x_lineal_links = x-Koordinaten-Startwert des Lineals (bei 10 % der Displaybreite) 
    # x_lineal_rechts = x-Koordinaten-Endwert des Lineals (bei 90 % der Displaybreite)
    # y_lineal_oben = y-Koordinaten-Startwert des Lineals (bei 70 % der Displayhöhe)
    # y_lineal_unten = x-Koordinaten-Endwert des Lineals (bei 85 % der Displayhöhe)
    global displayhoehe, displaybreite, x_lineal_links, x_lineal_recht, y_lineal_oben, y_lineal_unten 
    
    if mouseX in range (x_lineal_links, x_lineal_rechts) and mouseY in range (y_lineal_oben, y_lineal_unten):
        textAlign (LEFT)
        fill (140, 140, 140)
        textSize (displayhoehe / 100 * 3)
        text (u"Markierungen setzen", displaybreite / 100 * 75, displayhoehe / 100 * 30)
        text (u"Markierungen löschen", displaybreite / 100 * 75, displayhoehe / 100 * 50)
        text (u"=> Tasten 'A', 'S' und 'D'", displaybreite / 100 * 75, displayhoehe / 100 * 38)
        text (u"=> Taste 'F'", displaybreite / 100 * 75, displayhoehe / 100 * 55)
        textSize (displayhoehe / 100 * 2)
        text (u"(wenn Maus im Linealbereich)", displaybreite / 100 * 75, displayhoehe / 100 * 33)

# Funktion für das Schliessen des Fensters (da Fullscreen-Ansicht), wenn der Mauszeiger im Bereich des roten Homebuttons und gleichzeitig eine Maustaste gedrückt wird (inkl. Cursorveränderungen)
def fenster_schliessen ():
    
    # displayhoehe = initial festgelegter Wert für die Anzeigehöhe des Programms
    # displaybreite = initial festgelegter Wert für die Anzeigebreite des Programms
    global displayhoehe, displaybreite
    
    if mouseX in range (displaybreite * 4 / 100, displaybreite * 4 / 100 + displayhoehe / 100 * 2) and mouseY in range (displayhoehe / 2, displayhoehe / 2 + displayhoehe / 100 * 2):
        cursor (HAND)
        if mousePressed == True:
            cursor (WAIT)
            delay (1000)
            exit ()
    if mouseX not in range (displaybreite * 4 / 100, displaybreite * 4 / 100 + displayhoehe / 100 * 2) or mouseY not in range (displayhoehe / 2, displayhoehe / 2 + displayhoehe / 100 * 2):
        cursor (ARROW)
