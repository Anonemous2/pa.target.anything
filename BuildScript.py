#This script was written by Anonemous2 11/26/2020

#import os subprocess module
import os
#import json module
import json
from json.decoder import JSONDecodeError


def main():
    # starts by asking for correct directory to media PA
    # use default, then ask if the user wants to change it.
    media_dir = "C:/Program Files (x86)/Steam/steamapps/common/Planetary Annihilation Titans/media"
    print("Is the following directory correct? (y/n): " + media_dir)
    user_input = str(input())
    if (user_input.lower()) == "n":
        while user_input.lower() != "y":
            print("Enter new media directory: ")
            media_dir = str(input())
            media_dir = media_dir.replace('\\', '/')
            print("Is the following directory correct? (y/n): " + media_dir)
            user_input = str(input())
    # setup unit mod folder
    # find current directory
    home_dir = os.path.dirname(os.path.realpath(__file__))
    home_dir = home_dir.replace('\\', '/')
    print(home_dir)
    # create the units dir
    create_dir("/pa", home_dir)
    create_dir("/pa/units", home_dir)

    # start creating modified units
    # must create a list off all unit jsons first
    print("---Find---")
    # create a list of files
    found_files = []
    print("The following files have been found:")
    for root, dirs, files in os.walk(media_dir + "/pa/units"):
        for name in files:
            file = os.path.join(root, name)
            file = file.replace('\\', '/')
            #print(file)
            found_files.append(file)
    json_files = remove_other(found_files)
    update_weapons(json_files, media_dir)
    # use remove_other method
    found_files = []
    for root, dirs, files in os.walk(media_dir + "/pa_ex1/units"):
        for name in files:
            file = os.path.join(root, name)
            file = file.replace('\\', '/')
            # print(file)
            found_files.append(file)
    # use remove_other method
    json_files = remove_other(found_files)
    update_weapons(json_files, media_dir)

def update_weapons(json_files, media_dir):
    print("--Weapon Update--")
    # find current directory to save changes to it
    save_path = os.path.dirname(os.path.realpath(__file__))
    save_path = save_path.replace('\\', '/')
    total = len(json_files)
    index = 0
    while index < total:
        try:
            with open(json_files[index]) as file:
                file_data = json.load(file)
            #print(file_data)
            if "target_layers" in file_data:
                print("Weapon json: " + json_files[index])
                # save old Weapon target Layers
                file_data_pretarget = json.dumps(file_data["target_layers"])
                file_data_pretarget = file_data_pretarget.split(",")
                print(file_data_pretarget)
                # override old target layers
                file_data["target_layers"] = ["WL_LandHorizontal","WL_Seafloor","WL_WaterSurface","WL_Air",
                                              "WL_Underwater","WL_Orbital"]

                # create target prorities
                target_pri = ""
                index_1 = 0
                while index_1 < len(file_data_pretarget):
                    if index_1 == 0:
                        target_pri = str(get_target_pri(file_data_pretarget[index_1]))
                    else:
                        target_pri += " | " + str(get_target_pri(file_data_pretarget[index_1]))
                    index_1 += 1
                # check if they already exist
                if "target_priorities" not in file_data:
                    data_append = {"target_priorities": [target_pri]}
                    file_data.update(data_append)
                else:
                    # if they do exist, add brackets to append, and strip target_priorities
                    data_to_append = file_data["target_priorities"]
                    print("LLL4")
                    updated_data = json.dumps(data_to_append)
                    updated_data = updated_data.replace('"','')
                    updated_data = updated_data[updated_data.find('[') + 1:-1]
                    updated_data = updated_data.split(',')
                    updated_data.append(target_pri)
                    print(updated_data)
                    file_data["target_priorities"] = updated_data
                    print(file_data)


                # save to new directory
                new_dir_save = json_files[index]
                new_dir_save = new_dir_save.replace(media_dir, "")
                file_name = new_dir_save[new_dir_save.rfind('/') + 1:]
                # attempt to create directories
                # loop through file until no more sub directories exist
                pulled_dir = ""
                dir_end_index = new_dir_save.find('/')
                while dir_end_index != -1:
                    new_dir = new_dir_save[:dir_end_index]
                    try:
                        os.mkdir(save_path + pulled_dir + new_dir)
                    except OSError as error:
                        print(error)
                    pulled_dir += new_dir + "/"
                    new_dir_save = new_dir_save[(dir_end_index + 1):]
                    dir_end_index = new_dir_save.find('/')
                final_dir = save_path + pulled_dir + file_name
                print(final_dir)
                new_file = open(final_dir, "w+")
                print(json.dumps(file_data))
                new_file.write(json.dumps(file_data))
                new_file.close()
            else:
                if "damage" in file_data:
                    print("Ammo json: " + json_files[index])
                    # save to new directory
                    new_dir_save = json_files[index]
                    new_dir_save = new_dir_save.replace(media_dir, "")
                    file_name = new_dir_save[new_dir_save.rfind('/') + 1:]
                    # attempt to create directories
                    # loop through file until no more sub directories exist
                    pulled_dir = ""
                    dir_end_index = new_dir_save.find('/')
                    while dir_end_index != -1:
                        new_dir = new_dir_save[:dir_end_index]
                        try:
                            os.mkdir(save_path + pulled_dir + new_dir)
                        except OSError as error:
                            print(error)
                        pulled_dir += new_dir + "/"
                        new_dir_save = new_dir_save[(dir_end_index + 1):]
                        dir_end_index = new_dir_save.find('/')
                    final_dir = save_path + pulled_dir + file_name
                    print(final_dir)
                    new_file = open(final_dir, "w+")
                    print(json.dumps(file_data))
                    new_file.write(json.dumps(file_data))
                    new_file.close()
        except UnicodeDecodeError as error:
            print(error)
        except JSONDecodeError as error:
            print(error)
        index += 1

def remove_other(found_files):
    json_files = []

    for file in found_files:
        if file.find('.json') != -1:
            json_files.append(file)
    print("--Final--")
    #for item in json_files:
        #print(item)
    print(json_files)
    return json_files

def create_dir(new_dir,home_dir):
    print("--Create Dir--")
    final_dir = home_dir + new_dir
    try:
        os.mkdir(final_dir)
    except OSError as error:
        print(error)

def get_target_pri(file_data_pretarget):
    if file_data_pretarget.find("WL_LandHorizontal") != -1:
        print("This unit used to shoot Land")
        return "Land"
    if file_data_pretarget.find("WL_WaterSurface") != -1:
        print("This unit used to shoot Naval")
        return "Naval"
    if file_data_pretarget.find("WL_Seafloor") != -1:
        print("This unit used to shoot Seafloor")
        return "Amphibious"
    if file_data_pretarget.find("WL_Underwater") != -1:
        print("This unit used to shoot Underwater")
        return "Sub"
    if file_data_pretarget.find("WL_Air") != -1:
        print("This unit used to shoot Air")
        return "Air"
    if file_data_pretarget.find("WL_Orbital") != -1:
        print("This unit used to shoot Orbital")
        return "Orbital"
    if file_data_pretarget.find("Orbital") != -1:
        print("This unit used to shoot Orbital")
        return "Orbital"


main()

#end of program
print("---END---")