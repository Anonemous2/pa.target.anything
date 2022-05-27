# This script was written by Anonemous2 11/27/2020

# imports
import os
import json

# This script makes changes to a few select units AFTER the buildscript has been ran, and all units.jsons have been
# merged into /pa.

# The following units are have changes:

# Rex
# Reduced damage to 1/6th against non-orbital
def update_rex():
    # start by finding the rex ammo file
    rex_dir = find_home_dir()
    rex_dir += "/pa/units/addon/rex/rex_ammo.json"

    # attempt to open the rex_ammo.json
    with open(rex_dir, 'r') as file:
        file_data = json.load(file)
        print("DEBUG - Full file: " + json.dumps(file_data))

        # open damage value, then divide it by 6
        rex_damage = json.dumps(file_data["damage"])
        print("DEBUG - Rex damage: " + rex_damage)
        rex_damage = int(int(rex_damage) / 6)
        print("DEBUG - Rex damage: " + str(rex_damage))
        file_data["damage"] = rex_damage

        # open armor_damage_map, AT_Orbital, and set it to 6.0
        file_data["armor_damage_map"] = {"AT_Orbital": 6.0}
        print("DEBUG - Rex armor_damage_map: " + json.dumps(file_data["armor_damage_map"]))

        # attempt to update file_data
        print("DEBUG - Full file: " + json.dumps(file_data))
        file.close()
        file = open(rex_dir, 'w')
        file.write(json.dumps(file_data))
        file.close()


# Fighter
# 15% damage against non-air
def update_fighter():
    # start by finding the hummingbird ammo file
    hummingbird_dir = find_home_dir()
    hummingbird_dir += "/pa/units/air/fighter/fighter_ammo.json"

    # attempt to open the fighter_ammo.json
    with open(hummingbird_dir, 'r') as file:
        file_data = json.load(file)
        print("DEBUG - Full file: " + json.dumps(file_data))

        # open damage value, then divide it by 8
        # hummingbird_damage = json.dumps(file_data["damage"])
        # print("DEBUG - Hummingbird damage: " + hummingbird_damage)
        # hummingbird_damage = int(int(hummingbird_damage) / 8)
        # print("DEBUG - Hummingbird damage: " + str(hummingbird_damage))
        # file_data["damage"] = hummingbird_damage

        # open armor_damage_map, add AT_Air, and set it to 1.0, and all other ATs' to 0.15
        data_append = {"armor_damage_map": {"AT_Air": 1.0, "AT_Bot": 0.15, "AT_Commander": 0.15, "AT_Naval": 0.15,
                                            "AT_Orbital": 0.15, "AT_Vehicle": 0.15, "AT_Structure": 0.15}}
        file_data.update(data_append)
        print("DEBUG - Hummingbird armor_damage_map: " + json.dumps(file_data["armor_damage_map"]))

        # attempt to update file_data
        print("DEBUG - Full file: " + json.dumps(file_data))
        file.close()
        file = open(hummingbird_dir, 'w')
        file.write(json.dumps(file_data))
        file.close()


# Adv Fighter
# 15% damage against non-air
def update_adv_fighter():
    # start by finding the phoenix ammo file
    phoenix_dir = find_home_dir()
    phoenix_dir += "/pa/units/air/fighter_adv/fighter_adv_ammo.json"

    # attempt to open the fighter_adv_ammo.json
    with open(phoenix_dir, 'r') as file:
        file_data = json.load(file)
        print("DEBUG - Full file: " + json.dumps(file_data))

        # open damage value, then divide it by 8
        # phoenix_damage = json.dumps(file_data["damage"])
        # print("DEBUG - Phoenix damage: " + phoenix_damage)
        # phoenix_damage = int(int(phoenix_damage) / 8)
        # print("DEBUG - Phoenix damage: " + str(phoenix_damage))
        # file_data["damage"] = phoenix_damage

        # open armor_damage_map, add AT_Air, and set it to 1.0, and all other ATs' to 0.15
        data_append = {"armor_damage_map": {"AT_Air": 1.0, "AT_Bot": 0.15, "AT_Commander": 0.15, "AT_Naval": 0.15,
                                            "AT_Orbital": 0.15, "AT_Vehicle": 0.15, "AT_Structure": 0.15}}
        file_data.update(data_append)
        print("DEBUG - Phoenix armor_damage_map: " + json.dumps(file_data["armor_damage_map"]))

        # attempt to update file_data
        print("DEBUG - Full file: " + json.dumps(file_data))
        file.close()
        file = open(phoenix_dir, 'w')
        file.write(json.dumps(file_data))
        file.close()


# Spinner
# 25% damage against non-air
def update_spinner():
    # start by finding the spinner ammo file
    spinner_dir = find_home_dir()
    spinner_dir += "/pa/units/land/aa_missile_vehicle/aa_missile_vehicle_ammo.json"

    # attempt to open the aa_missile_vehicle_ammo.json
    with open(spinner_dir, 'r') as file:
        file_data = json.load(file)
        print("DEBUG - Full file: " + json.dumps(file_data))

        # open armor_damage_map, add AT_Air, and set it to 1.0, and all other ATs' to 0.25
        data_append = {"armor_damage_map": {"AT_Air": 1.0, "AT_Bot": 0.25, "AT_Commander": 0.25, "AT_Naval": 0.25,
                                            "AT_Orbital": 0.25, "AT_Vehicle": 0.25, "AT_Structure": 0.25}}
        file_data.update(data_append)
        print("DEBUG - Spinner armor_damage_map: " + json.dumps(file_data["armor_damage_map"]))

        # attempt to update file_data
        print("DEBUG - Full file: " + json.dumps(file_data))
        file.close()
        file = open(spinner_dir, 'w')
        file.write(json.dumps(file_data))
        file.close()

# Stinger
# 25% damage against non-air
def update_stinger():
    # start by finding the spinner ammo file
    spinner_dir = find_home_dir()
    spinner_dir += "/pa/units/land/bot_aa/bot_aa_tool_weapon.json"

    # attempt to open the aa_missile_vehicle_ammo.json
    with open(spinner_dir, 'r') as file:
        file_data = json.load(file)
        print("DEBUG - Full file: " + json.dumps(file_data))

        # open armor_damage_map, add AT_Air, and set it to 1.0, and all other ATs' to 0.25
        data_append = {"armor_damage_map": {"AT_Air": 1.0, "AT_Bot": 0.25, "AT_Commander": 0.25, "AT_Naval": 0.25,
                                            "AT_Orbital": 0.25, "AT_Vehicle": 0.25, "AT_Structure": 0.25}}
        file_data.update(data_append)
        print("DEBUG - Spinner armor_damage_map: " + json.dumps(file_data["armor_damage_map"]))

        # attempt to update file_data
        print("DEBUG - Full file: " + json.dumps(file_data))
        file.close()
        file = open(spinner_dir, 'w')
        file.write(json.dumps(file_data))
        file.close()

# Galata
# 25% damage against non-air
def update_galata():
    # start by finding the galata ammo file
    galata_dir = find_home_dir()
    galata_dir += "/pa/units/land/air_defense/air_defense_ammo.json"

    # attempt to open the air_defense_ammo.json
    with open(galata_dir, 'r') as file:
        file_data = json.load(file)
        print("DEBUG - Full file: " + json.dumps(file_data))

        # open armor_damage_map, add AT_Air, and set it to 1.0, and all other ATs' to 0.25
        data_append = {"armor_damage_map": {"AT_Air": 1.0, "AT_Bot": 0.25, "AT_Commander": 0.25, "AT_Naval": 0.25,
                                            "AT_Orbital": 0.25, "AT_Vehicle": 0.25, "AT_Structure": 0.25}}
        file_data.update(data_append)
        print("DEBUG - Galata armor_damage_map: " + json.dumps(file_data["armor_damage_map"]))

        # attempt to update file_data
        print("DEBUG - Full file: " + json.dumps(file_data))
        file.close()
        file = open(galata_dir, 'w')
        file.write(json.dumps(file_data))
        file.close()


# Flak
# 25% damage against non-air
def update_flak():
    # start by finding the galata ammo file
    flak_dir = find_home_dir()
    flak_dir += "/pa/units/land/air_defense_adv/air_defense_adv_ammo.json"

    # attempt to open the air_defense_adv_ammo.json
    with open(flak_dir, 'r') as file:
        file_data = json.load(file)
        print("DEBUG - Full file: " + json.dumps(file_data))

        # open armor_damage_map, add AT_Air, and set it to 1.0, and all other ATs' to 0.25
        data_append = {"armor_damage_map": {"AT_Air": 1.0, "AT_Bot": 0.25, "AT_Commander": 0.25, "AT_Naval": 0.25,
                                            "AT_Orbital": 0.25, "AT_Vehicle": 0.25, "AT_Structure": 0.25}}
        file_data.update(data_append)
        print("DEBUG - Flak armor_damage_map: " + json.dumps(file_data["armor_damage_map"]))

        # attempt to update file_data
        print("DEBUG - Full file: " + json.dumps(file_data))
        file.close()
        file = open(flak_dir, 'w')
        file.write(json.dumps(file_data))
        file.close()


# L Fighter
# 15% damage against non-air
def update_l_fighter():
    # start by finding the galata ammo file
    l_fighter_dir = find_home_dir()
    l_fighter_dir += "/pa/units/air/l_fighter/l_fighter_ammo.json"

    # attempt to open the l_fighter_ammo.json
    with open(l_fighter_dir, 'r') as file:
        file_data = json.load(file)
        print("DEBUG - Full file: " + json.dumps(file_data))

        # open armor_damage_map, add AT_Air, and set it to 1.0, and all other ATs' to 0.25
        data_append = {"armor_damage_map": {"AT_Air": 1.0, "AT_Bot": 0.15, "AT_Commander": 0.15, "AT_Naval": 0.15,
                                            "AT_Orbital": 0.15, "AT_Vehicle": 0.15, "AT_Structure": 0.15}}
        file_data.update(data_append)
        print("DEBUG - Legion Fighter armor_damage_map: " + json.dumps(file_data["armor_damage_map"]))

        # attempt to update file_data
        print("DEBUG - Full file: " + json.dumps(file_data))
        file.close()
        file = open(l_fighter_dir, 'w')
        file.write(json.dumps(file_data))
        file.close()


# L Adv Fighter
# 15% damage against non-air
def update_l_adv_fighter():
    # start by finding the galata ammo file
    l_fighter_adv_dir = find_home_dir()
    l_fighter_adv_dir += "/pa/units/air/l_fighter_adv/l_fighter_adv_ammo.json"

    # attempt to open the l_fighter_ammo.json
    with open(l_fighter_adv_dir, 'r') as file:
        file_data = json.load(file)
        print("DEBUG - Full file: " + json.dumps(file_data))

        # open armor_damage_map, add AT_Air, and set it to 1.0, and all other ATs' to 0.25
        data_append = {"armor_damage_map": {"AT_Air": 1.0, "AT_Bot": 0.15, "AT_Commander": 0.15, "AT_Naval": 0.15,
                                            "AT_Orbital": 0.15, "AT_Vehicle": 0.15, "AT_Structure": 0.15}}
        file_data.update(data_append)
        print("DEBUG - Legion Adv Fighter armor_damage_map: " + json.dumps(file_data["armor_damage_map"]))

        # attempt to update file_data
        print("DEBUG - Full file: " + json.dumps(file_data))
        file.close()
        file = open(l_fighter_adv_dir, 'w')
        file.write(json.dumps(file_data))
        file.close()


# L Bot AA
# 25% damage against non-air
def update_l_aa_bot():
    # start by finding the l_bot_aa ammo file
    l_bot_aa_dir = find_home_dir()
    l_bot_aa_dir += "/pa/units/land/l_bot_aa/l_bot_aa_ammo.json"

    # attempt to open the l_bot_aa_ammo.json
    with open(l_bot_aa_dir, 'r') as file:
        file_data = json.load(file)
        print("DEBUG - Full file: " + json.dumps(file_data))

        # open armor_damage_map, add AT_Air, and set it to 1.0, and all other ATs' to 0.25
        data_append = {"armor_damage_map": {"AT_Air": 1.0, "AT_Bot": 0.25, "AT_Commander": 0.25, "AT_Naval": 0.25,
                                            "AT_Orbital": 0.25, "AT_Vehicle": 0.25, "AT_Structure": 0.25}}
        file_data.update(data_append)
        print("DEBUG - Legion AA Bot armor_damage_map: " + json.dumps(file_data["armor_damage_map"]))

        # attempt to update file_data
        print("DEBUG - Full file: " + json.dumps(file_data))
        file.close()
        file = open(l_bot_aa_dir, 'w')
        file.write(json.dumps(file_data))
        file.close()


# L Adv Bot AA
# 25% damage against non-air
def update_l_aa_bot_adv():
    # start by finding the l_bot_aa ammo file
    l_bot_aa_adv_dir = find_home_dir()
    l_bot_aa_adv_dir += "/pa/units/land/l_bot_aa_adv/l_bot_aa_adv_ammo.json"

    # attempt to open the l_bot_aa_ammo.json
    with open(l_bot_aa_adv_dir, 'r') as file:
        file_data = json.load(file)
        print("DEBUG - Full file: " + json.dumps(file_data))

        # open armor_damage_map, add AT_Air, and set it to 1.0, and all other ATs' to 0.25
        data_append = {"armor_damage_map": {"AT_Air": 1.0, "AT_Bot": 0.25, "AT_Commander": 0.25, "AT_Naval": 0.25,
                                            "AT_Orbital": 0.25, "AT_Vehicle": 0.25, "AT_Structure": 0.25}}
        file_data.update(data_append)
        print("DEBUG - Legion Adv AA Bot armor_damage_map: " + json.dumps(file_data["armor_damage_map"]))

        # attempt to update file_data
        print("DEBUG - Full file: " + json.dumps(file_data))
        file.close()
        file = open(l_bot_aa_adv_dir, 'w')
        file.write(json.dumps(file_data))
        file.close()


# L AA Defense
# 25% damage against non-air
def update_l_air_defense():
    # start by finding the l_air_defense ammo file
    l_air_defense_dir = find_home_dir()
    l_air_defense_dir += "/pa/units/land/l_air_defense/l_air_defense_ammo.json"

    # attempt to open the l_air_defense_ammo.json
    with open(l_air_defense_dir, 'r') as file:
        file_data = json.load(file)
        print("DEBUG - Full file: " + json.dumps(file_data))

        # open armor_damage_map, add AT_Air, and set it to 1.0, and all other ATs' to 0.25
        data_append = {"armor_damage_map": {"AT_Air": 1.0, "AT_Bot": 0.25, "AT_Commander": 0.25, "AT_Naval": 0.25,
                                            "AT_Orbital": 0.25, "AT_Vehicle": 0.25, "AT_Structure": 0.25}}
        file_data.update(data_append)
        print("DEBUG - l_air_defense armor_damage_map: " + json.dumps(file_data["armor_damage_map"]))

        # attempt to update file_data
        print("DEBUG - Full file: " + json.dumps(file_data))
        file.close()
        file = open(l_air_defense_dir, 'w')
        file.write(json.dumps(file_data))
        file.close()


# L Adv AA Defense
# 25% damage against non-air
def update_l_air_defense_adv():
    # start by finding the l_air_defense_adv ammo file
    l_air_defense_adv_dir = find_home_dir()
    l_air_defense_adv_dir += "/pa/units/land/l_air_defense_adv/l_air_defense_adv_ammo.json"

    # attempt to open the l_air_defense_adv_ammo.json
    with open(l_air_defense_adv_dir, 'r') as file:
        file_data = json.load(file)
        print("DEBUG - Full file: " + json.dumps(file_data))

        # open armor_damage_map, add AT_Air, and set it to 1.0, and all other ATs' to 0.25
        data_append = {"armor_damage_map": {"AT_Air": 1.0, "AT_Bot": 0.25, "AT_Commander": 0.25, "AT_Naval": 0.25,
                                            "AT_Orbital": 0.25, "AT_Vehicle": 0.25, "AT_Structure": 0.25}}
        file_data.update(data_append)
        print("DEBUG - l_air_defense_adv armor_damage_map: " + json.dumps(file_data["armor_damage_map"]))

        # attempt to update file_data
        print("DEBUG - Full file: " + json.dumps(file_data))
        file.close()
        file = open(l_air_defense_adv_dir, 'w')
        file.write(json.dumps(file_data))
        file.close()


# Lynx
# 25% damage against non-orbital, non-air
def update_lynx():
    # start by finding the anti_orbital_armor ammo file
    lynx_dir = find_home_dir()
    lynx_dir += "/pa/units/l_addon/anti_orbital_armor/lynx_ammo.json"

    # attempt to open the lynx_ammo.json
    with open(lynx_dir, 'r') as file:
        file_data = json.load(file)
        print("DEBUG - Full file: " + json.dumps(file_data))

        # open armor_damage_map, add AT_Air, and set it to 1.0, set AT_Orbital to 2.0, and all other ATs' to 0.25
        data_append = {"armor_damage_map": {"AT_Air": 1.0, "AT_Bot": 0.25, "AT_Commander": 0.25, "AT_Naval": 0.25,
                                            "AT_Orbital": 2.0, "AT_Vehicle": 0.25, "AT_Structure": 0.25}}
        file_data.update(data_append)
        print("DEBUG - Lynx armor_damage_map: " + json.dumps(file_data["armor_damage_map"]))

        # attempt to update file_data
        print("DEBUG - Full file: " + json.dumps(file_data))
        file.close()
        file = open(lynx_dir, 'w')
        file.write(json.dumps(file_data))
        file.close()


# Storm
# 25% damage against non-air
def update_storm():
    # start by finding the spinner ammo file
    storm_dir = find_home_dir()
    storm_dir += "/pa/units/land/tank_flak/tank_flak_ammo.json"

    # attempt to open the tank_flak_ammo.json
    with open(storm_dir, 'r') as file:
        file_data = json.load(file)
        print("DEBUG - Full file: " + json.dumps(file_data))

        # open armor_damage_map, add AT_Air, and set it to 1.0, and all other ATs' to 0.25
        data_append = {"armor_damage_map": {"AT_Air": 1.0, "AT_Bot": 0.25, "AT_Commander": 0.25, "AT_Naval": 0.25,
                                            "AT_Orbital": 0.25, "AT_Vehicle": 0.25, "AT_Structure": 0.25}}
        file_data.update(data_append)
        print("DEBUG - Storm armor_damage_map: " + json.dumps(file_data["armor_damage_map"]))

        # attempt to update file_data
        print("DEBUG - Full file: " + json.dumps(file_data))
        file.close()
        file = open(storm_dir, 'w')
        file.write(json.dumps(file_data))
        file.close()


# Atlas
# 100% damage against non-orbital, non-air
def update_atlas():
    # start by finding the anti_orbital_armor ammo file
    atlas_dir = find_home_dir()
    atlas_dir += "/pa/units/land/titan_bot/titan_bot_ammo_stomp.json"

    # attempt to open the titan_bot_ammo_stomp.json
    with open(atlas_dir, 'r') as file:
        file_data = json.load(file)
        print("DEBUG - Full file: " + json.dumps(file_data))

        # open armor_damage_map, set all to 1.0
        data_append = {"armor_damage_map": {"AT_Air": 1.0, "AT_Bot": 1.0, "AT_Commander": 1.0, "AT_Naval": 1.0,
                                            "AT_Orbital": 1.0, "AT_Vehicle": 1.0, "AT_Structure": 1.0}}
        file_data.update(data_append)
        print("DEBUG - Atlas armor_damage_map: " + json.dumps(file_data["armor_damage_map"]))

        # attempt to update file_data
        print("DEBUG - Full file: " + json.dumps(file_data))
        file.close()
        file = open(atlas_dir, 'w')
        file.write(json.dumps(file_data))
        file.close()

# Umbrela
# Revert change
def update_umbrela():
    # start by finding the anti_orbital_armor ammo file
    atlas_dir = find_home_dir()
    atlas_dir += "/pa/units/orbital/ion_defense/ion_defense_tool_weapon.json"

    # attempt to open the titan_bot_ammo_stomp.json
    with open(atlas_dir, 'r') as file:
        file_data = json.load(file)
        print("DEBUG - Full file: " + json.dumps(file_data))

        # override old target layers
        file_data["target_layers"] = ["WL_Orbital"]

        # attempt to update file_data
        print("DEBUG - Full file: " + json.dumps(file_data))
        file.close()
        file = open(atlas_dir, 'w')
        file.write(json.dumps(file_data))
        file.close()

# Tola
# Revert change
def update_tola():
    # start by finding the anti_orbital_armor ammo file
    atlas_dir = find_home_dir()
    atlas_dir += "/pa/units/orbital/l_ion_defense/l_ion_defense_tool_weapon.json"

    # attempt to open the titan_bot_ammo_stomp.json
    with open(atlas_dir, 'r') as file:
        file_data = json.load(file)
        print("DEBUG - Full file: " + json.dumps(file_data))

        # override old target layers
        file_data["target_layers"] = ["WL_Orbital"]

        # attempt to update file_data
        print("DEBUG - Full file: " + json.dumps(file_data))
        file.close()
        file = open(atlas_dir, 'w')
        file.write(json.dumps(file_data))
        file.close()

# Other Methods
# Find Home Dir
def find_home_dir():
    home_dir = os.path.dirname(os.path.realpath(__file__))
    home_dir = home_dir.replace('\\', '/')
    print(home_dir)
    return home_dir

update_rex()
update_fighter()
update_adv_fighter()
update_spinner()
update_stinger()
update_galata()
update_flak()
update_l_fighter()
update_l_adv_fighter()
update_l_aa_bot()
update_l_aa_bot_adv()
update_l_air_defense()
update_l_air_defense_adv()
update_lynx()
update_storm()
update_atlas()
update_umbrela()
update_tola()