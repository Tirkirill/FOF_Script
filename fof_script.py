import random

text:str = "\"BotList\"\n{"

rand_names: str = [
    "VIP Sex Energy VIP", 
    "HekI/Ita }I{pET kaLLLLL", 
    "#~PaP[ER]~Ph[a]Nt0m~#",
    "FapToBbIu^", 
    "TaTaPuH", 
    "Ha_KoJleHu_OJleHu", 
    "XuJIuGan", 
    "BeJIuKuu*", 
    "6u6JIuk", 
    "4ekHyTbIu*", 
    "PyLu_Ot_BaByLu"
    "X.A.K.E.R",
    "CCCP/KilleR"
]

for i in range(25):

    bot_rotation_speed:int = random.randint(1, 10)
    bot_shoot_delay:int    = random.randint(1, 10)
    bot_aim_trailing:int   = random.randint(1, 10)
    bot_strafe:int         = random.randint(1, 10)
    bot_force_team:int     = random.randint(1, 4)
    bot_aggression:int     = random.randint(1, 10)
    bot_name:int           = random.choice(rand_names) + "   " + str(random.randint(1, 1000))
    bot_start_weapon: int  = 7 # Динамит

    text += "\n \"preset\" \n  {"
    text += "\n    \"bot_rotation_speed\"\t\t \"{0}\"".format(bot_rotation_speed)
    text += "\n    \"bot_shoot_delay\"\t\t \"{0}\"".format(bot_shoot_delay)
    text += "\n    \"bot_aim_trailing\"\t\t \"{0}\"".format(bot_aim_trailing)
    text += "\n    \"bot_strafe\"\t\t \"{0}\"".format(bot_strafe)
    text += "\n    \"bot_force_team\"\t\t \"{0}\"".format(bot_force_team)
    text += "\n    \"bot_aggression\"\t\t \"{0}\"".format(bot_aggression)
    text += "\n    \"bot_name\"\t\t \"{0}\"".format(bot_name)
    text += "\n    \"bot_equipment\"\t\t \"{0},{1},{2},{3}\"".format(bot_start_weapon, -1, -1, -1)
    text += "\n  }"

text += "\n}"

my_file = open("new_script.txt", "w")
my_file.write(text)
my_file.close()