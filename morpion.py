from random import randint
caseJouable = True
joueur1 = input("Joueur 1 quel est votre pseudo ?: ")
joueur2 = input("Joueur 2 quel est votre pseudo ?: ")
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

def game():
    global joueur1, joueur2, tableJeu
    coupJoueur1 = "X"
    coupJoueur2 = "O"
    premierJoueur = randint(1,2)
    if premierJoueur == 1 :
        print(joueur1 + " vous commencez à jouer avec les X")
        joueurTour = joueur1
        coupJoueur = coupJoueur1
    else :
        print(joueur2 + " vous commencez à jouer avec les O")
        joueurTour = joueur2
        coupJoueur = coupJoueur2
    coupCorrect = False
    joueurGagnant = False
    while joueurGagnant == False :
        while coupCorrect == False :
            print("Tour de " + joueurTour)
            choiceX = int(input("Quel ligne voulez-vous modifier (0-2) ?: "))
            choiceY = int(input("Quel colonne voulez-vous modifier (0-2) ?: "))
            if caseRemplie(tableJeu, choiceX, choiceY) != True :
                tableJeu[choiceX][choiceY] = coupJoueur
                coupCorrect = True
        showTable(tableJeu)

        if is_player_win(tableJeu, coupJoueur):
            print("Le joueur " + joueurTour + " a gagné ! :)")
            break

        if is_board_filled(tableJeu):
            print("Egalité !")
            break

        if coupJoueur == coupJoueur1 :
            coupJoueur = coupJoueur2
            joueurTour = joueur2
        else :
            coupJoueur = coupJoueur1
            joueurTour = joueur1

        coupCorrect = False
    replay = input("Voulez-vous rejouer ?: ")
    if replay == "Oui" or "oui" :
        tableJeu = [['-','-','-'],['-','-','-'],['-','-','-']]
        showTable(tableJeu)
        game()
    else :
        print("Veuillez saisir Oui si vous voulez rejouer et Non si vous souhaitez quitter le jeu")
        replay = input("Voulez-vous rejouer ?: ")

game()