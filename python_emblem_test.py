import random
import time
import math

weapon_type = 0
weapon_type_list = ["sword", "lance", "axe", "bow", "tome"]
player_hp = random.randint(30, 50)
player_str = random.randint(10, 20)
player_def = random.randint(9, 19)
player_spd = random.randint(5, 30)
player_skl = random.randint(3, 15)
player_luk = random.randint(1, 9)
enemy_hp = random.randint(30, 50)
enemy_str = random.randint(10, 20)
enemy_def = random.randint(9, 13)
enemy_spd = random.randint(5, 29)
enemy_skl = random.randint(3, 15)
enemy_luk = random.randint(0, 3)


def clear():
    print("\n" * 60)  # Shout-outs to Python and PyCharm for not implementing a simple clear console function


def how_to_play():
    clear()
    print("Python Emblem is a \"Sit and watch\" RPG where all you\n"
          "can do is watch and pray your RNG turns out in your favor.\n\n"
          "Stat explanations:\n"
          "HP: Your total HP. Reach 0, and you're dead.\n"
          "Atk (Attack): Measure of your strength.\n"
          "Def (Defense): Measure of how well you can resist the enemy's Atk.\n"
          "Spd (Speed): If your speed is ≥ 5 than the enemy's, you attack twice in a row!\n"
          "Skl (Skill): How well you can land hits.\n"
          "Luk (Luck): How well you can dodge attacks.\n\n"
          "Your damage is calculated by (your Atk - enemy Def).\n"
          "Your chances of landing a hit is determined by ((your Skl - enemy Luk) * 10)%.\n\n"
          "Keep playing and level up!\n"
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
          "Def:", player_def, "\n"
          "Spd:", player_spd, "\n"
          "Skl:", player_skl, "\n"
          "Luk:", player_luk, "\n")
    print("Your enemy's stats are:\n",
          "HP:", enemy_hp, "\n"
          "Str:", enemy_str, "\n"
          "Def:", enemy_def, "\n"
          "Spd:", enemy_spd, "\n"
          "Skl:", enemy_skl, "\n"
          "Luk:", enemy_luk, "\n")
    input("Press enter to FIGHT!")
    clear()
    enemy_hp_current = enemy_hp
    while True:
        if player_str > enemy_def:
            if player_spd - enemy_spd >= 5:  # Double
                damage = int((player_str - enemy_def) * 2)
                print("You attack the enemy for", damage/2, "damage.\n"
                      "You doubled the enemy! Dealt another", damage/2, "damage.")
            else:
                damage = int(player_str - enemy_def)
                print("You attack the enemy for", damage, "damage.")
        else:
            damage = 0
            print("You attack the enemy for 0 damage.", "Wow, you're bad.")
        enemy_hp_current -= damage
        if enemy_hp_current < 0:
            print("Enemy has 0/" + str(enemy_hp), "left. The enemy falls!")
            break
        else:
            print("Enemy has", str(enemy_hp_current) + "/" + str(enemy_hp), "HP left.")
            input("Press enter to continue.")
            time.sleep(0.25)
            print("\n")


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
