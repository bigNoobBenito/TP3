import random
player_life = 20
def fight():
    global player_life, difficulty
    difficulty = random.randint(1,6)
    player_strengh = random.randint(1,10)
    if difficulty > player_strengh:
        player_life -= difficulty
        print(" vous avez gagne ")
    else:
        player_life += difficulty
        print(" vous avez perdu ")

def go_away():
    player_life -= 1

