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
    global board

def spielbrett_verdeckt():
    '''
    Schiff auf verdecktem Spielbrett einzeichnen
    '''
    zeile_verdeckt = random.randint(0, 9)
    spalte_verdeckt = random.randint(0, 14)
    board_verdeckt = copy.deepcopy(board)
    board_verdeckt[spalte_verdeckt][zeile_verdeckt] = " S"
    global board_verdeckt
    
def spielbrett_ausgabe(spielbrett):
    '''
    Print Funktion für das Spielbrett
    '''
    for ab in range(0, 15):
        print(''.join(spielbrett[ab]))
    
def spielbrett_prüfen(column, row):
    '''
    Überprüft Spielbrett und fügt Zeichen auf Spielbrett
    '''
    if " S" == board_verdeckt[column-1][row-1]:
        board[column-1][row-1] = " S"
        global board
        return True
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
    print("Sie haben noch" 10-a "Versuche übrig.")
    b = input(int("Zeile eingeben: ")) - 1
    c = input(int("Spalte eingeben: ")) - 1
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
                z = input("Drücken Sie Enter zum Fortfahren des Spiels.")    
                     
                      
                
            
    