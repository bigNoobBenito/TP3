import random
numero_combat = 0
player_life = 20
playing = True
difficulty = random.randint(1, 6)
nombre_victoires_consecutives = 0
combat_statut = "aucun"
def fight():
    global player_life, difficulty, nombre_victoires, nombre_defaites, combat_statut, nombre_victoires_consecutives
    nombre_victoires = 0
    nombre_defaites = 0
    player_strengh = random.randint(1,10)
    print(f"Voici le resultat de votre lance de dés qui definit votre force à ce moment {player_strengh}")
    if difficulty < player_strengh:
        player_life += difficulty
        print(f" vous avez gagne, voci votre niveau de vie {player_life} et votre nombre de victoires est {nombre_victoires_consecutives} ")
        nombre_victoires += 1
        nombre_victoires_consecutives +=1
        combat_statut = "victoire"
    else:
        player_life -= difficulty
        print(f" vous avez perdu, voci votre niveau de vie {player_life} et le nombre de monstreb que vous avez battu {nombre_victoires}")
        nombre_defaites += 1
        nombre_victoires_consecutives = 0
        combat_statut = "défaite"

def go_away():
    player_life -= 1
def rules():
    print("Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.  Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire.  Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.\n La partie se termine lorsque les points de vie de l’usager tombent sous 0.\n L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie.")
while playing:
    if player_life <= 0:

    choice =int(input(f"Vous tombez face à face avec un adversaire de difficulté : {difficulty} \n Que voulez-vous faire ? \n 1.Combattre cet adversaire \n 2.Contourner cet adversaire et aller ouvrir une autre porte \n 3. Afficher les règles du jeu \n Quitter la partie"))
    if choice == 1:
        numero_combat += 1
        fight()
