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


def window_pos_init():
    window_width = 350
    window_height = 150
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (window_width / 2)
    y = (screen_height / 2) - (window_height / 2)
    root.geometry('%dx%d+%d+%d' % (window_width, window_height, x, y))


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
    clear_window()
    label_title.config(height=10, text="Python Emblem is a \"Sit and watch\" RPG where all you\n"
                                       "can do is watch and pray your RNG turns out in your favor.\n\n"
                                       "Stat explanations:\n"
                                       "HP: Reach 0, and you're dead.\n"
                                       "Str: Your strength.\n"
                                       "Def: How well you can resist and defend the enemy's Str.\n")
    htp_close_button = tk.Button(root, text="Close").grid(row=2)
    htp_close_button.config(command=lambda: button_clicked(htp_close_button))


def change_weapon():
    clear_window()
    print("change_weapon")


def fight():
    clear_window()
    print("fight")


def main():
    window_pos_init()
    window_init()


main()

root.mainloop()
