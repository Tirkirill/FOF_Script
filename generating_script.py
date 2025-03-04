import random
from CONSTS import WEAPONS, BOT_NAMES, NO_WEAPON, RANDOM_WEAPON

def get_weapon_info(weapon:str) -> tuple[int, bool]:

    """
    Получает на вход строку weapon 
    Возвращает номер оружия и нужно ли получать новое оружие заново каждый раз
    
    :param weapon: может быть название оружия либо значения CONSTS.NO_WEAPON, CONSTS.RANDOM_WEAPON
    :return: Кортеж(номер оружия, нужно ли получать новое случайное оружие для каждого бота)
    
    """

    if weapon == NO_WEAPON:
        return -1, False
    
    if weapon == RANDOM_WEAPON:
        return -1, True
    
    return WEAPONS[weapon], False

def get_current_weapon(bot_weapon:int, weapon_is_random:bool, WEAPONS_list:list[str]) -> int:

    """
    Возвращает номер оружия
    
    :param bot_weapon: номер оружия
    :param weapon_is_random: нужно ли получать случайное оружие
    :param WEAPONS_list: список возможного оружия
    :return: номер оружия
    
    """

    if weapon_is_random:
        res = random.choice(WEAPONS_list)
    else:
        res = bot_weapon

    return res

def generate_script_file(
        start_weapon1:str, 
        start_weapon2:str, 
        start_weapon3:str, 
        start_weapon4:str):

    """
    Создает файл скрипта
    
    :param start_weapon1: может быть название оружия либо значения CONSTS.NO_WEAPON, CONSTS.RANDOM_WEAPON
    :param start_weapon2: может быть название оружия либо значения CONSTS.NO_WEAPON, CONSTS.RANDOM_WEAPON
    :param start_weapon3: может быть название оружия либо значения CONSTS.NO_WEAPON, CONSTS.RANDOM_WEAPON
    :param start_weapon4: может быть название оружия либо значения CONSTS.NO_WEAPON, CONSTS.RANDOM_WEAPON
    
    """

    text:str = "\"BotList\"\n{"

    bot_weapon1, weapon1_is_random = get_weapon_info(start_weapon1)
    bot_weapon2, weapon2_is_random = get_weapon_info(start_weapon2)
    bot_weapon3, weapon3_is_random = get_weapon_info(start_weapon3)
    bot_weapon4, weapon4_is_random = get_weapon_info(start_weapon4)
    
    WEAPONS_list:list[str] = []
    if weapon1_is_random or weapon2_is_random or weapon3_is_random or weapon4_is_random:
        WEAPONS_list = list(WEAPONS.values())

    for i in range(25):

        bot_rotation_speed:int = random.randint(1, 10)
        bot_shoot_delay:int    = random.randint(1, 10)
        bot_aim_trailing:int   = random.randint(1, 10)
        bot_strafe:int         = random.randint(1, 10)
        bot_force_team:int     = random.randint(1, 4)
        bot_aggression:int     = random.randint(1, 10)
        bot_name:int           = random.choice(BOT_NAMES) + "   " + str(random.randint(1, 1000))

        bot_start_weapon:int =   get_current_weapon(bot_weapon1, weapon1_is_random, WEAPONS_list)
        bot_start_weapon_2:int = get_current_weapon(bot_weapon2, weapon2_is_random, WEAPONS_list)
        bot_start_weapon_3:int = get_current_weapon(bot_weapon3, weapon3_is_random, WEAPONS_list)
        bot_start_weapon_4:int = get_current_weapon(bot_weapon4, weapon4_is_random, WEAPONS_list)

        text += "\n \"preset\" \n  {"
        text += "\n    \"bot_rotation_speed\"\t\t \"{0}\"".format(bot_rotation_speed)
        text += "\n    \"bot_shoot_delay\"\t\t \"{0}\"".format(bot_shoot_delay)
        text += "\n    \"bot_aim_trailing\"\t\t \"{0}\"".format(bot_aim_trailing)
        text += "\n    \"bot_strafe\"\t\t \"{0}\"".format(bot_strafe)
        text += "\n    \"bot_force_team\"\t\t \"{0}\"".format(bot_force_team)
        text += "\n    \"bot_aggression\"\t\t \"{0}\"".format(bot_aggression)
        text += "\n    \"bot_name\"\t\t \"{0}\"".format(bot_name)
        text += "\n    \"bot_equipment\"\t\t \"{0},{1},{2},{3}\"".format(
            bot_start_weapon, 
            bot_start_weapon_2, 
            bot_start_weapon_3, 
            bot_start_weapon_4
        )
        text += "\n  }"

    my_file = open("new_script.txt", "w")
    my_file.write(text)
    my_file.close()