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
    global board
    row = [" O"] * 10
    for a in range(15):
        board.append(row[:])


def spielbrett_verdeckt():
    '''
    Schiff auf verdecktem Spielbrett einzeichnen
    '''
    global board_verdeckt
    zeile_verdeckt = random.randint(0, 9)
    spalte_verdeckt = random.randint(0, 14)
    print(zeile_verdeckt)
    print(spalte_verdeckt)
    print(board_verdeckt)
    board_verdeckt[spalte_verdeckt][zeile_verdeckt] = " S"


def spielbrett_ausgabe(spielbrett):
    '''
    Print Funktion für das Spielbrett
    '''
    for ab in range(0, 15):
        print(''.join(spielbrett[ab]))


def spielbrett_pruefen(column, row):
    '''
    Überprüft Spielbrett und fügt Zeichen auf Spielbrett
    '''
    global board_verdeckt
    global board

    if " S" == board_verdeckt[column - 1][row - 1]:
        board[column - 1][row - 1] = " S"
        return True
    else:
        board[column - 1][row - 1] = " X"
        return False

    ##############################


# Spiel

board = list()
spielbrett_neu()
board_verdeckt = copy.deepcopy(board)
spielbrett_verdeckt()
spielbrett_ausgabe(board)
for a in range(0, 11):
    print("Sie haben noch " + str(10 - a) + " Versuche übrig.")
    b = int(input("Zeile eingeben: ")) - 1
    c = int(input("Spalte eingeben: ")) - 1

    if 0 <= b <= 14 and 0 <= c <= 9:
        d = spielbrett_pruefen(b, c)
        if d:
            print('''Herzlichen Glückwunsch,
                  Sie haben das Schiff versenkt.

                  ''')
            spielbrett_ausgabe(board)
            z = input("Drücken Sie Enter um das Spiel zu beenden.")
            sys.exit()
        if not (d):
            print('''Sie haben das Schiff nicht getroffen.
                  Probieren Sie es noch einmal.''')
            spielbrett_ausgabe(board)
            z = input("Drücken Sie Enter zum Fortfahren des Spiels.")
    else:
        print('''Bitte geben Sie einen Punkt innerhalb des Speilfelds an.

                  ''')
        spielbrett_ausgabe(board)
        z = input("Drücken Sie Enter zum Fortfahren des Spiels.")
