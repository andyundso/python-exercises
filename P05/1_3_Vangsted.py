##############################
# P05 - 1.3 Battleship
##############################

# Import
import random
import copy
import sys

##############################

# Definitionen

def spielbrett_neu():
    '''
    Neues Spielbrett erzeugen
    '''
    row = [" O"] * 10
    board = list()
    for a in range(15):
        board.append(row[:])

    # Das "global" Stichwort in Python funktioniert wie folgt:
    # Grundsätzlich können Funktionen die Variablen im globalen Namespace lesen, aber nicht schreiben
    # Damit man auf die globale Variable schreiben kann, braucht es das "global"-Keyword
    # Im Fall, wenn das global-Keyword fehlt, (z.B hier bei der Variable "board"), dann wird einfach eine lokale Variable
    # namens "board" erstellt und diese beschrieben, anstatt die globale Variable.
    # Guter Artikel als Referenz: https://www.datacamp.com/community/tutorials/scope-of-variables-python

    # Um dies nun zu fixen, kannst du die nachfolgende Zeile mit "global board" vor die Zeile mit "row = [" O"] * 10" verschieben
    # Die Anweisung "board = list()" kannst du dann vor dem Funktionsaufruf um Zeile XX einfügen, damit die board Variable
    # global bereits initialisiert ist, damit das global-Keyword korrekt greift.
    global board

def spielbrett_verdeckt():
    '''
    Schiff auf verdecktem Spielbrett einzeichnen
    '''
    zeile_verdeckt = random.randint(0, 9)
    spalte_verdeckt = random.randint(0, 14)
    board_verdeckt = copy.deepcopy(board)
    board_verdeckt[spalte_verdeckt][zeile_verdeckt] = " S"
    # Hier nochmals dasselbe wie bereits eine Funktion weiter oben:
    # Die nachfolgende Zeile mit "global board_verdeckt" kannst du vor "zeile_verdeckt = random.randint(0, 9)" einfügen.
    # damit deine Funktion auf die globale Variable "board_verdeckt" zugreifen kann.
    # Die Zeile "board_verdeckt = copy.deepcopy(board)" musst du nach Funktionsaufruf auf "spielbrett_neu()" einfügen (Zeile XXX)
    # damit die Variable global initialisiert ist, bevor diese Funktion aufgerufen wird.
    global board_verdeckt
    
def spielbrett_ausgabe(spielbrett):
    '''
    Print Funktion für das Spielbrett
    '''
    for ab in range(0, 15):
        print(''.join(spielbrett[ab]))

# Generell Funktionsnamen immer ohne Sonderzeichen definieren, ggf. können diese zu Fehlfunktionen innerhalb des
# Codes führen. spielbrett_prüfen daher zu spielbrett_pruefen umbennen.
def spielbrett_prüfen(column, row):
    '''
    Überprüft Spielbrett und fügt Zeichen auf Spielbrett
    '''
    if " S" == board_verdeckt[column-1][row-1]:
        board[column-1][row-1] = " S"
        global board
        return True
    # Hier braucht es ein "else" anstatt eine "elif". "Elif" erwartet wie das "If" eine Anweisung, welche True or False
    # ergeben können. "Else" hingegen wird immer ausgeführt, wenn eine vorhergehende "If"-Anweisung nicht True ergeben hat.
    elif:
        board[column-1][row-1] = " X"
        global board
        return False
        
##############################        
        
# Spiel

spielbrett_neu()
spielbrett_verdeckt()
spielbrett_ausgabe(board)
for a in range(0,11):
    # Wenn du Anweisungen innerhalb eines prints verwenden willst, sind folgende zwei Sachen zu beachten:
    # 1. Du musst die Teile der Nachricht im Print zusammenfügen (z.B. print("Dies ist " + "eine Fügung")
    # 2. Müssen alle Teile der Nachricht ein String sein. Da 10 - a einen Integer ergeben, musst du dies noch zu einem
    # String konvertieren: str(10 - a)
    print("Sie haben noch" 10-a "Versuche übrig.")

    # Hier sind noch die input und int-Anweisungen vertauscht. Du fragst ja zuerst nach einem Input, daher muss dieser
    # zuerst ausgeführt werden, bevor die Konvertiertung zu Int stattfindet. Beispiel: int(input("Hello"))
    # Zu merken: Die Ausführung der Klammern erfolgt immer von innen nach aussen (wie auch in der Mathe).
    b = input(int("Zeile eingeben: ")) - 1
    c = input(int("Spalte eingeben: ")) - 1

    # Die untenstehenden Anweisungen musst du noch eine Zeile zurückrücken, damit dies ausgeführt werden kann.
    # Die Operatoren kannst du zusätzlich zusammennehmen.
    # D.h. folgende Codezeilen: 0 =< q and 12 => q kann auch so vereinfach: 0 =< q <= 12
        if 0 =< b and 0 =< c and 14 => b and 9 => c:
            d = spielbrett_prüfen(b, c)
            if True == d:
                print('''Herzlichen Glückwunsch,
                      Sie haben das Schiff versenkt.
                      
                      ''')
                spielbrett_ausgabe(board)
                z = input("Drücken Sie Enter um das Spiel zu beenden.")
                sys.exit()
            if False == d:
                print('''Sie haben das Schiff nicht getroffen.
                      Probieren Sie es noch einmal.''')
                spielbrett_ausgabe(board)
                z = input("Drücken Sie Enter zum Fortfahren des Spiels.")
        else:
            print('''Bitte geben Sie einen Punkt innerhalb des Speilfelds an.
                      
                      ''')
            spielbrett_ausgabe(board)
            # Nachfolgende Zeile noch eins zurückrücken.
                z = input("Drücken Sie Enter zum Fortfahren des Spiels.")    
                     
                      
                
            
    