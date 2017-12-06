import tkinter as tk
import random
import time

# Game setup
weapon_type = 0
weapon_type_list = ["sword", "lance", "axe", "bow", "tome"]
player_hp = random.randint(20, 30)
player_str = random.randint(6, 10)
player_def = random.randint(2, 6)
enemy_hp = random.randint(17, 27)
enemy_str = random.randint(5, 9)
enemy_def = random.randint(1, 5)
# Tkinter layout setup
root = tk.Tk()
root.title("Python Emblem")
# TODO: Replace the placeholder favicon
root.iconbitmap("favicon.ico")
label_title = tk.Label(root, text="Welcome to Python Emblem!", width=50, height=2)
how_to_play_button = tk.Button(root, text="How to Play")
change_weapon_button = tk.Button(root, text="Change Weapon")
fight_button = tk.Button(root, text="Fight!")
quit_button = tk.Button(root, text="Quit")


def global_buttons():
    global label_title
    global how_to_play_button
    global change_weapon_button
    global fight_button
    global quit_button


def window_init():
    global_buttons()
    label_title.grid(row=0)
    how_to_play_button.grid(row=1)
    how_to_play_button.config(command=lambda: button_clicked("how_to_play_button"))
    change_weapon_button.grid(row=2)
    change_weapon_button.config(command=lambda: button_clicked("change_weapon_button"))
    fight_button.grid(row=3)
    fight_button.config(command=lambda: button_clicked("fight_button"))
    quit_button.grid(row=4)
    quit_button.config(command=lambda: quit())  # It's not a bug, it's a feature!


def clear_window():
    global_buttons()
    how_to_play_button.grid_forget()
    change_weapon_button.grid_forget()
    fight_button.grid_forget()
    quit_button.grid_forget()


def button_clicked(button):
    if button == "how_to_play_button":
        return how_to_play()
    if button == "change_weapon_button":
        return change_weapon()
    if button == "fight_button":
        return fight()
    else:
        print("button_clicked function error")


def how_to_play():
    # TODO: WIP
    print("how_to_play")
    return 0


def change_weapon():
    # TODO: WIP
    print("change_weapon")
    return 0


def fight():
    # TODO: WIP
    print("fight")
    return 0


def main():
    window_init()


main()

root.mainloop()
