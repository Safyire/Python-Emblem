import random
import time
import math

# Init
weapon_type = 0
weapon_type_list = ["sword", "lance", "axe", "bow", "tome"]
player_hp = random.randint(40, 60)
player_str = random.randint(10, 20)
player_def = random.randint(9, 19)
enemy_hp = random.randint(40, 60)
enemy_str = random.randint(10, 20)
enemy_def = random.randint(9, 19)


def clear():
    print("\n" * 60)  # No way to clear the interpreter, apparently


def how_to_play():
    clear()
    print("Python Emblem is a \"Sit and watch\" RPG where all you\n"
          "can do is watch and pray your RNG turns out in your favor.\n\n"
          "Stat explanations:\n"
          "HP: Your total HP. Reach 0, and you're dead.\n"
          "Str (Strength): Measure of your strength.\n"
          "Def (Defense): Measure of how well you can resist the enemy's Str.\n"
          )
    input("Press enter to continue.")
    main()


def weapon_set():
    clear()
    change_weapon = 0
    cur_weapon = "Iron Sword"
    weapon_list = ["Iron Sword", "Iron Lance", "Iron Axe", "Iron Bow", "Fire Tome"]
    print("You are a", weapon_type_list[weapon_type], "user.")
    print("Your current weapon is", cur_weapon + ".")
    while not (change_weapon == "y" or change_weapon == "n"):
        change_weapon = input("Do you want to change your weapon? (y/n)\n")
        if change_weapon == "y" or change_weapon == "n":
            if change_weapon == "y":
                print("1: Iron Sword\n"
                      "2: Iron Lance\n"
                      "3: Iron Axe\n"
                      "4: Iron Bow\n"
                      "5: Fire Tome\n")
                weapon_switch = input("Which weapon? ")
                for i in range(len(weapon_list)):
                    if weapon_switch == i:
                        cur_weapon = weapon_list[i]
                        print("Your current weapon is now", cur_weapon)
            if change_weapon == "n":
                main()
        else:
            continue


def start():
    clear()
    print("Your current stats are:\n",
          "HP:", player_hp, "\n"
          "Str:", player_str, "\n"
          "Def:", player_def, "\n")
    input("Press enter to continue.")
    print("Your enemy's stats are:\n",
          "HP:", enemy_hp, "\n"
          "Str:", enemy_str, "\n"
          "Def:", enemy_def, "\n")
    input("Press enter to FIGHT!")
    clear()
    if player_str > enemy_def:
        damage = player_str - enemy_def
        print("You attack the enemy for", damage, "damage.")
    else:
        damage = 0
        print("You attack the enemy for 0 damage.", "Wow, you're bad.")
    enemy_hp_current = enemy_hp
    enemy_hp_current = enemy_hp_current - damage
    print("¡Uf! Enemy has", str(enemy_hp_current) + "/" + str(enemy_hp), "HP left.")
    input("Press enter to continue.")


def main():
    clear()
    print("Welcome to Python Emblem! Choose an option.")
    menu_mode = 0
    while menu_mode <= 1 or menu_mode >= 3:
        try:
            menu_mode = int(input("1: How to play\n2: Choose weapon\n3: Start\n"))
            if 1 <= menu_mode <= 3:
                break
            else:
                clear()
                print("Invalid input. Choose an option.")
                continue
        except ValueError:
            print("Invalid input. Choose an option.")
    if menu_mode == 1:
        how_to_play()
    elif menu_mode == 2:
        weapon_set()
    else:
        start()


main()
