#hier stehen alle constanten des spiels:
window_height:int = 600
window_width:int = 800

def get_window_height() -> int:
    return window_height

def get_window_width() -> int:
    return window_width




vel:int = 3 #gibt die geschwindigkeit des hintergrundes und der hindernisse an

def get_vel() -> int:
    return vel

player_val:int = 7

def get_player_vel() -> int:
    return player_val

ground_height:int = get_window_height() - 62

def get_ground_height() -> int:
    return ground_height



size:int = 50

def get_size() -> int:
    return size



spawn_height:int = get_ground_height() - get_size()

def get_spawn_height() -> int:
    return spawn_height


