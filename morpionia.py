from random import randint
caseJouable = True
joueur = input("Quel est votre pseudo ?: \n")
coupJoueur = "X"
tableJeu = [["-","-","-"],["-","-","-"],["-","-","-"]]

def showTable(tableJeu):
    for row in tableJeu :
        for item in row :
            print(item, end=" ")
        print()

showTable(tableJeu)

def caseRemplie(tableJeu, posx, posy):
    if tableJeu[posx][posy] == "-" :
        return False
    else:
        return True

#######################
def is_player_win(board, player):
    win = None

    n = len(board)

    # checking rows
    for i in range(n):
        win = True
        for j in range(n):
            if board[i][j] != player:
                win = False
                break
        if win:
            return win

    # checking columns
    for i in range(n):
        win = True
        for j in range(n):
            if board[j][i] != player:
                win = False
                break
        if win:
            return win

    # checking diagonals
    win = True
    for i in range(n):
        if board[i][i] != player:
            win = False
            break
    if win:
        return win

    win = True
    for i in range(n):
        if board[i][n - 1 - i] != player:
            win = False
            break
    if win:
        return win
    return False

def is_board_filled(board):
    for row in board:
        for item in row:
            if item == '-':
                return False
    return True
#######################






def ia(tableau):
    if tableau[1][1] == '-' : 
        tableau[1][1] = 'O'
    elif tableau[1][1] != '-' :
        tableau[0][0] = 'O'



def isIaWin(case1, case2, case3) :
    if case1 == case2 == 'O' and case3 == '-' :
        return True, 2
    elif case1 == case3 == 'O' and case2 == '-' :
        return True, 1
    elif case2 == case3 == 'O' and case1 == '-' :
        return True, 0

    if case1 == case2 == coupJoueur and case3 == '-' :
        return 2
    elif case1 == case3 == coupJoueur and case2 == '-' :
        return 1
    elif case2 == case3 == coupJoueur and case1 == '-' :
        return 0

def bonCourage(tableau):
    for i in range(3) :
        ligne = isIaWin(tableau[i][0], tableau[i][1], tableau[i][2])
        colonne = isIaWin(tableau[i][0], tableau[i][1], tableau[i][2])
        if ligne == True :
            tableau[i][ligne] = 'O'
            return tableau
        if isIaWin(tableau[0][i], tableau[1][i], tableau[2][i]) == True :
            tableau[colonne][i] = 'O'
            return tableau 
    diagonale1 = isIaWin(tableau[0][0], tableau[1][1], tableau[2][2])
    diagonale2 = isIaWin(tableau[0][2], tableau[1][1], tableau[2][0])
    if diagonale1 == True :
        tableau[diagonale1][diagonale1] = 'O'
        return tableau
    if diagonale2 == True :
        tableau[diagonale2][2 - diagonale2] = 'O'
        return tableau
    
def game():
    global joueur, coupJoueur, tableJeu
    coupCorrect = False
    joueurGagnant = False
    while joueurGagnant == False :
        while coupCorrect == False :
            choiceX = int(input("Quel ligne voulez-vous modifier (0-2) ?: \n"))
            choiceY = int(input("Quel colonne voulez-vous modifier (0-2) ?: \n"))
            if caseRemplie(tableJeu, choiceX, choiceY) != True :
                tableJeu[choiceX][choiceY] = coupJoueur
                coupCorrect = True
            bonCourage(tableJeu)
            ia(tableJeu)
        showTable(tableJeu)
        
        if is_player_win(tableJeu, coupJoueur):
            print("Le joueur " + joueur + " a gagné ! :)")
            joueurGagnant = True
            break

        if is_board_filled(tableJeu):
            print("Egalité !")
            break

        coupCorrect = False
    while joueurGagnant :
        replay = input("Voulez-vous rejouer ?: ")
        if replay == "Oui" or replay == "oui" :
            tableJeu = [['-','-','-'],['-','-','-'],['-','-','-']]
            showTable(tableJeu)
            game()
        elif replay == "Non" or replay == "non" :
            print("D'accord à la prochaine !")
            break
        else :
            print("Veuillez saisir Oui si vous voulez rejouer et Non si vous souhaitez quitter le jeu")
            continue

game()