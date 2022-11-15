from random import randint

tableJeu = [['-','-','-'],['-','-','-'],['-','-','-']]

def showTable(tableJeu):
    for row in tableJeu :
        for item in row:
            print(item, end="  ")
        print()

def caseRemplie(board, posx, posy):
    if board[posx][posy] == '-':
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


def jeu():
    joueur1 = input("Joueur 1, choisissez votre pseudo : ")
    joueur2 = input("Joueur 2, choisissez votre pseudo : ")
    coupJoueur1 = "X"
    coupJoueur2 = "O"
    startingPlayer = randint(1,2)
    if startingPlayer == 1 :
        print(joueur1 + " commence à jouer")
        joueurTour = joueur1
        coupJoueur = coupJoueur1
    else : 
        print(joueur2 + " commence à jouer")
        joueurTour = joueur2
        coupJoueur = coupJoueur2
    coupCorrect = False
    winJ = False 
    showTable(tableJeu)
    while winJ == False:
        while coupCorrect == False :
            print("Tour de " + joueurTour)
            choiceX = int(input("Choisissez la ligne à modifier: "))
            choiceY = int(input("Choisissez la colonne à modifier: "))
            if caseRemplie(tableJeu, choiceX, choiceY) != True:
                tableJeu[choiceX][choiceY] = coupJoueur
                coupCorrect = True 
        showTable(tableJeu)

        if is_player_win(tableJeu, coupJoueur):
            print("Le joueur " + joueurTour +  " a gagné ! :)")
            break
        
        if is_board_filled(tableJeu):
            print("Egalité !")
            break

        if coupJoueur == coupJoueur1:
            coupJoueur = coupJoueur2
            joueurTour = joueur2
        else : 
            coupJoueur = coupJoueur1
            joueurTour = joueur1

        coupCorrect = False
    replay = input("Rejouer? : ")
    if replay == "Oui" :
        jeu()

jeu()