#DEBUT

#Créer une liste échantillonTableJeu : ["-","-","-"]

#Importer de random la fonction randint qui renvoie un nombre aléatoire entier
#Associer la valeur True à une variable caseJouable
#Associer le renvoi de la fonction input à une variable joueur1
#Associer le renvoi de la fonction input à une variable joueur2
#On créer le tableau tableJeu avec 3 listes échantillonTableJeu

#Définir une fonction showTable avec pour argument tableJeu
    #Pour chaque ligne dans TableJeu
        #Pour chaque item dans chaque ligne
            #Afficher chaque item avec un espace à la fin
        #Afficher tableJeu

#Exécuter la fonction showTable avec pour argument tableJeu

#Définir une fonction caseRemplie avec pour argument tableJeu, posx et posy
    #Si les index posx et posy de tableJeu valent "-"
        #Renvoyer False
    #Sinon
        #Renvoyer True

#Définir une fonction is_player_win avec pour argument board et player
    #Associer la valeur None à une variable win
    #Associer la valeur longueur du paramètre board à une variable n

    #On parcourt la longueur du tableau dans une suite ordonnée
        #Associer la valeur True à la variable win
        #Pour j allant de 0 à n
            #Si les index i et j de board sont différents de player
                #Associer la valeur False à la variable win
                #Sortir de la boucle
        #Si win
            #Renvoyer win

    #On parcourt la longueur du tableau dans une suite ordonnée
        #Associer la valeur True à la variable win
        #Pour j allant de 0 à n
            #Si les index j et i de board sont différents de player
                #Associer la valeur False à la variable win
                #Sortir de la boucle
        #Si win
            #Renvoyer win
    
    #Associer la valeur True à une variable win
    #On parcourt la longueur du tableau dans une suite ordonnée
        #Si les index i et j de board sont différents de player
            #Associer la valeur False à la variable win
            #Sortir de la boucle
    #Si win
        #Renvoyer win

    #Associer la valeur True à une variable win
    #On parcourt la longueur du tableau dans une suite ordonnée
        #Si les index i et n - 1 - i de board sont différents de player
            #Associer la valeur False à la variable win
            #Sortir de la boucle
    #Si win
        #Renvoyer win
    #Renvoyer False

#Définir une fonction game
    #On appelle les variables joueur1, joueur2 et tableJeu déclarées en dehors de la fonction
    #Associer le string X à la variable coupJoueur1
    #Associer le string O à la variable coupJoueur2
    #Associer le renvoi de la fonction randint 1 ou 2 à la variable premierJoueur
    #Si premierJoueur vaut 1
        #Afficher joueur1 + " vous commencez à jouer avec les X"
        #Associer la valeur joueur1 à la variable joueurTour
        #Associer la valeur coupJoueur1 à la variable coupJoueur
    #Sinon
        #Afficher joueur2 + " vous commencez à jouer avec les O"
        #Associer la valeur joueur2 à la variable joueurTour
        #Associer la valeur coupJoueur2 à la variable coupJoueur
    #Associer la valeur False à la variable coupCorrect
    #Associer la valeur False à la variable joueurGagnant
    #Tant que joueurGagnant vaut False
        #Tant que coupCorrect vaut False
            #Afficher "Tour de " + joueurTour
            #Associer la valeur int de input("Quel ligne voulez-vous modifier (0-2) ?: ") à la variable choiceX
            #Associer la valeur int de input("Quel colonne voulez-vous modifier (0-2) ?: ")
            #Si la fonction caseRemplie ayant pour paramètres tableJeu, choiceX et choiceY est différente de True
                #Associer la valeur coupJoueur aux index choiceX et choiceY de tableJeu
                #Associer la valeur True à la variable coupCorrect
        #Exécuter la fonction showTable avec pour argument tableJeu

        #Si la fonction is_player_win avec pour arguments tableJeu et coupJoueur
            #Afficher "Le joueur " + joueurTour + " a gagné ! :)"
            #Sortir de la boucle

        #Si la fonction is_board_filled avec pour argument tableJeu
            #Afficher "Egalité !"
            #Sortir de la boucle

        #Si coupJoueur vaut coupJoueur1
            #Associer la valeur coupJoueur2 à la variable coupJoueur
            #Associer la valeur joueur2 à la variable joueurTour
        #Sinon
            #Associer la valeur coupJoueur1 à la variable coupJoueur
            #Associer la valeur joueur1 à la variable joueurTour

        #Associer la valeur False à la variable coupCorrect
    #Associer la valeur input("Voulez-vous rejouer ?: ") à la variable replay
    #Si replay vaut "Oui" ou "oui"
        #Associer la valeur 3 échantillonTableJeu à la variable tableJeu
        #Exécuter la fonction showTable avec pour argument tableJeu
        #Exécuter la fonction game
    #Sinon si replay vaut "Non" ou "non"
        #Afficher "D'accord à la prochaine !"
        #Associer la valeur False à la variable joueurGagnant
    #Sinon
        #Afficher "Veuillez saisir Oui si vous voulez rejouer et Non si vous souhaitez quitter le jeu"
        #Continuer la boucle

#Exécuter la fonction game
#FIN