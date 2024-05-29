import random
import const


def generate_random_number(min, max) -> int:
    return random.randint(min, max)

def generate_spawn_height(player_y) -> int:
    max: int = 0
    min: int = 0
    print(player_y, (((player_y + const.get_size()) - (3*const.get_size()))))
    if ((player_y + const.get_size()) == const.get_ground_height()) or (((player_y + const.get_size()) - (3*const.get_size())) <= player_y): #haben die selbe hoehe
        max = 3
        min = 0
    elif ((player_y + const.get_size()) > const.get_ground_height() and (((player_y + const.get_size()) - (3*const.get_size())) > player_y )):# spieler ist höher oder gleich 3 blöcke
        max = 6
        min = 3
    elif ((player_y + const.get_size()) > const.get_ground_height() and (((player_y + const.get_size()) - (6*const.get_size())) > player_y )):# spieler ist höher oder gleich 6 blöcke
        max = 9
        min = 6
    elif ((player_y + const.get_size()) > const.get_ground_height() and (((player_y + const.get_size()) - (9*const.get_size())) > player_y )):# spieler ist höher oder gleich 9 blöcke
        max = 12
        min = 9
    elif ((player_y + const.get_size()) > const.get_ground_height() and (((player_y + const.get_size()) - (12*const.get_size())) > player_y )):# spieler ist höher oder gleich 12 blöcke --> fehler!
        print("Spieler ist zu hoch! Fehler!")
    else:
        print("Spieler ist unter dem boden! Fehler!")
        exit(0)

    is_valid:bool = True
    while is_valid:
        spawn_height = generate_random_number(min, max)
        print(f"spawnheight: {spawn_height}")
        if spawn_height == 0:
            is_valid = True
            spawn_height = generate_random_number(min, max)
        else:
            is_valid = False
            height:int = const.get_ground_height() - (spawn_height * const.get_size())
            return height
