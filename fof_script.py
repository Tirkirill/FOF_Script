import random
from CONSTS import WEAPONS, BOT_NAMES

text:str = "\"BotList\"\n{"

weapons:list[str] = [40, 41, 42]

for i in range(25):

    bot_rotation_speed:int = random.randint(1, 10)
    bot_shoot_delay:int    = random.randint(1, 10)
    bot_aim_trailing:int   = random.randint(1, 10)
    bot_strafe:int         = random.randint(1, 10)
    bot_force_team:int     = random.randint(1, 4)
    bot_aggression:int     = random.randint(1, 10)
    bot_name:int           = random.choice(BOT_NAMES) + "   " + str(random.randint(1, 1000))
    bot_start_weapon:int   = 26
    bot_start_weapon_2:int = 6
    bot_start_weapon_3:int = -1
    bot_start_weapon_4:int = -1

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

text += "\n}"

my_file = open("new_script.txt", "w")
my_file.write(text)
my_file.close()