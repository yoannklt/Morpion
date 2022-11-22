#DEBUT

#Importer depuis random la fonction randint
#Associer la valeur True à la variable caseJouable
#Associer le renvoi de la fonction input("Quel est votre pseudo ?:" en sautant une ligne) à la variable joueur
#Associer la valeur X à la variable coupJoueur
#Associer la valeur O à la variable coupOrdi
#Associer la valeur False à la variable coupMilieuJoueur
#Associer la valeur False à la variable coupMilieuIA
#Créer un tableau tableJeu avec trois listes ["-","-","-"]
#Associer la valeur 0 à la variable gameRound

#Définir la variable showTable avec pour argument tableJeu
    #Pour chaque ligne dans tableJeu
        #Pour chaque objet dans ligne
            #Afficher item avec un espace à la fin
        #Afficher

#Exécuter la fonction showTable avec pour argument tableJeu

#Définir la fonction caseRemplie avec pour arguments tableJeu, posx et posy
    #Si les index posx et posy de tableJeu valent "-"
        #Alors renvoyer False
    #Sinon
        #Renvoyer True

#Définir la fonction isPlayerWin avec pour arguments board et player
    #Associer la valeur None à la variable win
    #Associer la longueur de board à la variable n
    #Pour i allant de 0 à n
        #Associer la valeur True à la variable win
        #Pour j allant de 0 à n
            #Si les index i et j de board sont différents de player
                #Alors associer la valeur False à la variable win
                #Sortir de la boucle
        #Si win
            #Alors renvoyer win

    #Pour i allant de 0 à n
        #Associer la valeur True à la variable win
        #Pour j allant de 0 à n
            #Si les index j et i de board sont différents de player
                #Alors associer la valeur False à la variable win
                #Sortir de la boucle
        #Si win
            #Alors renvoyer win

    #Associer la valeur True à la variable win
    #Pour i allant de 0 à n
        #Pour j allant de 0 à n
            #Si les index i et i de board sont différents de player
                #Alors associer la valeur False à la variable win
                #Sortir de la boucle
        #Si win
            #Alors renvoyer win

    #Associer la valeur True à la variable win
    #Pour i allant de 0 à n
        #Pour j allant de 0 à n
            #Si les index i et n - 1 - i de board sont différents de player
                #Alors associer la valeur False à la variable win
                #Sortir de la boucle
        #Si win
            #Alors renvoyer win
        #Renvoyer False

#Définir la fonction coupIA avec pour arguments tableau, x et y
    #Associer la valeur O aux index x et y de tableau

#Définir la fonction isIaWin avec pour arguments case1, case2, case3 et coupDuJoueur
    #Si case1 vaut case2 et coupDuJoueur ET case3 vaut -
        #Alors renvoyer True et 2
    #Sinon si case1 vaut case3 et coupDuJoueur ET case2 vaut -
        #Alors renvoyer True et 1
    #Sinon si case2 vaut case3 et coupDuJoueur ET case1 vaut -
        #Alors renvoyer True et 0
    #Renvoyer False

#Définir la fonction bonCourage avec pour arguments tableau et coupDuJoueur
    #Pour i allant de 0 à 3
        #Associer le renvoi de la fonction isIaWin avec pour arguments les index i et 0 de tableau, les index i et 1 de tableau, les index i et 2 de tableau et coupDuJoueur à la variable ligne
        #Associer le renvoi de la fonction isIaWin avec pour arguments les index 0 et i de tableau, les index 1 et i de tableau, les index 2 et i de tableau et coupDuJoueur à la variable colonne
        #Si la variable ligne est différente de False
            #Alors associer le string O aux index i et 1 de ligne de tableau
            #Renvoyer True
        #Si la variable colonne est différente de False
            #Alors associer le string O aux index 1 de colonne et i de tableau
            #Renvoyer True
    #Associer le renvoi de la fonction isIaWin avec pour arguments les index 0 et 0 de tableau, les index 1 et 1 de tableau, les index 2 et 2 de tableau et coupDuJoueur à la variable diagonale1
    #Associer le renvoi de la fonction isIaWin avec pour arguments les index 0 et 2 de tableau, les index 1 et 1 de tableau, les index 2 et 0 de tableau et coupDuJoueur à la variable diagonale2
    #Si la variable diagonale1 est différente de False
        #Alors associer le string O aux index 1 de diagonale1 et 1 de diagonale1 de tableau
        #Renvoyer True
    #Si la variable diagonale2 est différente de False
        #Alors associer le string O aux index 1 de diagonale2 et 2 - 1 de diagonale2 de tableau
        #Renvoyer True

    #Renvoyer False

#Définir la fonction ia avec pour argument tableau
    #Appeller les variables gameRound, coupMilieuIA et coupMilieuJoueur déclarées en dehors de la fonction
    #Si les index 1 et 1 de tableau valent -
        #Alors associer la valeur True à la variable coupMilieuIA
        #Associer le string O aux index 1 et 1 de tableau
    #Sinon si les index 1 et 1 de tableau valent - ET les index 0 et 0 de tableau valent -
        #Alors associer la valeur True à la variable coupMilieuJoueur
        #Associer le string O aux index 0 et 0 de tableau
    #Sinon si le renvoi de la fonction bonCourage avec pour arguments tableJeu et O vaut False
        #Si le renvoi de la fonction bonCourage avec pour arguments tableJeu et X vaut False
            #Si les index 2 et 2 de tableau valent coupJoueur ET les index 0 et 0 de tableau valent coupJoueur ET le renvoi de la fonction caseRemplie avec pour arguments tableau, 1 et 0 vaut False
                #Alors exécuter la fonction coupIA avec pour arguments tableau, 1 et 0
            #Sinon si les index 0 et 2 de tableau valent coupJoueur ET les index 2 et 0 de tableau valent coupJoueur ET le renvoi de la fonction caseRemplie avec pour arguments tableau, 1 et 2 vaut False
                #Alors exécuter la fonction coupIA avec pour arguments tableau, 1 et 2
            #Sinon si les index 1 et 0 de tableau sont différents de coupJoueur ET les index 1 et 2 de tableau sont différents de - ET les index 0 et 1 de tableau sont différents de coupJoueur ET les index 0 et 1 de tableau sont différents de -
                #Alors exécuter la fonction coupIA avec pour arguments tableau, 0 et 1
            #Sinon si les index 0 et 1 de tableau valent coupJoueur ET les index 1 et 0 de tableau valent coupJoueur ET le renvoi de la fonction caseRemplie avec pour arguments tableau, 1 et 2 vaut False
                #Alors exécuter la fonction coupIA avec pour arguments tableau, 2 et 0
            #Sinon si les index 0 et 1 de tableau valent coupJoueur ET les index 1 et 2 de tableau valent coupJoueur ET le renvoi de la fonction caseRemplie avec pour arguments tableau, 2 et 2 vaut False
                #Alors exécuter la fonction coupIA avec pour arguments tableau, 2 et 2
            #Sinon si les index 1 et 0 de tableau valent coupJoueur ET les index 2 et 1 de tableau valent coupJoueur ET le renvoi de la fonction caseRemplie avec pour arguments tableau, 2 et 0 vaut False
                #Alors exécuter la fonction coupIA avec pour arguments tableau, 2 et 0
            #Sinon si les index 0 et 1 de tableau valent les index 1 et 0 de tableau et coupJoueur ET le renvoi de la fonction caseRemplie avec pour arguments tableau, 0 et 0 vaut False
                #Alors exécuter la fonction coupIA avec pour arguments tableau, 0 et 0
            #Sinon si le renvoi de la fonction caseRemplie avec pour arguments tableau, 0 et 2 vaut False
                #Alors exécuter la fonction coupIA avec pour arguments tableau, 0 et 2
            #Sinon si le renvoi de la fonction caseRemplie avec pour arguments tableau, 2 et 2 vaut False
                #Alors exécuter la fonction coupIA avec pour arguments tableau, 2 et 2
            #Sinon si le renvoi de la fonction caseRemplie avec pour arguments tableau, 2 et 0 vaut False
                #Alors exécuter la fonction coupIA avec pour arguments tableau, 2 et 0

#Définir la fonction game
    #Appeller les variables joueur, coupJoueur et tableJeu définies en dehors de la fonction
    #Associer la valeur False à la variable coupCorrect
    #Associer la valeur False à la variable joueurGagnant
    #Tant que joueurGagnant vaut False
        #Tant que coupCorrect vaut False
            #Associer l'entier du renvoi de la fonction input("Quelle ligne voulez-vous modifier (0-2) ?:" en sautant une ligne) à la variable choiceX
            #Associer l'entier du renvoi de la fonction input("Quelle colonne voulez-vous modifier (0-2) ?:" en sautant une ligne) à la variable choiceY
            #Si choiceX est inférieure à 3 ET choiceY est inférieure à 3 ET le renvoi de la fonction caseRemplie avec pour arguments tableJeu, choiceX et choiceY est différent de True
                #Alors associer la variable coupJoueur aux index choiceX et choiceY de tableJeu
                #Associer la valeur True à la variable coupCorrect
            #Sinon
                #Afficher Veuillez saisir une valeur entre 0 et 2
            #Continuer la boucle
        #Exécuter la fonction ia avec pour argument tableJeu
        #Exécuter la fonction showTable avec pour argument tableJeu

        #Si le renvoi de la fonction isPlayerWin avec pour arguments tableJeu et O
            #Alors afficher L'IA a gagné + ratio
            #Associer la valeur True à la variable joueurGagnant
            #Sortir de la boucle
        #Sinon si le renvoi de la fonction isPlayerWin avec pour arguments tableJeu et coupJoueur
            #Alors afficher Le joueur (pseudo) a gagné ! :)
            #Associer la valeur True à la variable joueurGagnant
            #Sortir de la boucle

        #Si le renvoi de la fonction isBoardFilled avec pour argument tableJeu
            #Alors afficher Egalité !
            #Associer la valeur True à la variable joueurGagnant
            #Sortir de la boucle

        #Associer la valeur False à la variable coupCorrect
    #Tant que joueurGagnant
        #Associer le renvoi de la fontion input(Voulez-vous rejouer ?:) à la variable replay
        #Si replay vaut Oui OU replay vaut oui
            #Alors créer un tableau tableJeu avec trois listes ["-","-","-"]
            #Exécuter la fonction showTable avec pour argument tableJeu
            #Exécuter la fonction game
        #Sinon si replay vaut Non OU replay vaut non
            #Alors afficher D'accord à la prochaine
            #Sortir de la boucle
        #Sinon
            #Afficher Veuillez saisir Oui si vous voulez rejouer ou Non si vous souhaitez quitter le jeu
            #Continuer la boucle

#Exécuter la fonction game

#FIN