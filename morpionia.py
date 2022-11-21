from random import randint
caseJouable = True
joueur = input("Quel est votre pseudo ?: \n")
coupJoueur = "X"
coupMilieuJoueur = False
coupMilieuIA = False
tableJeu = [["-","-","-"],["-","-","-"],["-","-","-"]]
gameRound = 0 


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
def isPlayerWin(board, player):
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

def isBoardFilled(board):
    for row in board:
        for item in row:
            if item == '-':
                return False
    return True
#######################

def coupIA(tableau, x, y):
    tableau[x][y] = 'O'



def ia(tableau):
    global gameRound, coupMilieuIA, coupMilieuJoueur
    if tableau[1][1] == '-' : 
        coupMilieuIA = True
        tableau[1][1] = 'O'
    elif tableau[1][1] != '-' and tableau[1][1] == coupJoueur :
        coupMilieuJoueur = True
        tableau[0][0] = 'O'
    elif tableau[2][2] == 'X' :
        tableau[1][0] = coupIA(tableau, 1,0)
    elif bonCourage(tableJeu, 'O') == False:
        if bonCourage(tableJeu, 'X') == False:
            if tableau[1][0] == '-' :
                coupIA(tableau, 1, 0)
            else :
                coupIA(tableau,1,2)
            
   
    print(bonCourage(tableJeu, 'O'))
    print(bonCourage(tableJeu, 'X'))


def isIaWin(case1, case2, case3, coupDuJoueur) :
    if case1 == case2 == coupDuJoueur and case3 == '-' :
        return True, 2
    elif case1 == case3 == coupDuJoueur and case2 == '-' :
        return True, 1
    elif case2 == case3 == coupDuJoueur and case1 == '-' :
        return True, 0
    return False

def bonCourage(tableau, coupDuJoueur):
    for i in range(3) :
        ligne = isIaWin(tableau[i][0], tableau[i][1], tableau[i][2], coupDuJoueur)
        colonne = isIaWin(tableau[0][i], tableau[1][i], tableau[2][i], coupDuJoueur)
        if ligne != False :
            tableau[i][ligne[1]] = 'O'
            #print(ligne)
            return True
        if colonne!= False :
            tableau[colonne[1]][i] = 'O'
            #print(colonne)
            return True 
    diagonale1 = isIaWin(tableau[0][0], tableau[1][1], tableau[2][2], coupDuJoueur)
    diagonale2 = isIaWin(tableau[0][2], tableau[1][1], tableau[2][0], coupDuJoueur)
    #print(diagonale1)
    #print(diagonale2)
    if diagonale1!= False :
        tableau[diagonale1[1]][diagonale1[1]] = 'O'
        return tableau
    if diagonale2!= False :
        tableau[diagonale2[1]][2 - diagonale2[1]] = 'O'
        return tableau
    
    return False

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
        ia(tableJeu)
        showTable(tableJeu)
        
        if isPlayerWin(tableJeu, 'O'):
            print("L'IA à gagné + ratio")
            joueurGagnant = True
            break
        elif isPlayerWin(tableJeu, coupJoueur):
            print("Le joueur " + joueur + " a gagné ! :)")
            joueurGagnant = True
            break

        if isBoardFilled(tableJeu):
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