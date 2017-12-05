import tkinter
import random

# Init
weapon_type = 0
weapon_type_list = ["sword", "lance", "axe", "bow", "tome"]
player_hp = random.randint(40, 60)
player_str = random.randint(10, 20)
player_def = random.randint(9, 19)
enemy_hp = random.randint(40, 60)
enemy_str = random.randint(10, 20)
enemy_def = random.randint(9, 19)
root = tkinter.Tk()


def window_init():
    root.title("Python Emblem")
    # TODO: Replace the placeholder favicon
    root.iconbitmap("favicon.ico")
    label_title = tkinter.Label(root, text="Welcome to Python Emblem!")
    how_to_play_button = tkinter.Button(root, text="How to play")
    change_weapon_button = tkinter.Button(root, text="Change weapon")
    fight_button = tkinter.Button(root, text="Fight!")
    label_title.grid(row=0, column=0)
    how_to_play_button.grid(row=1, column=0)
    change_weapon_button.grid(row=2, column=0)
    fight_button.grid(row=3, column=0)


def main():
    window_init()


main()

root.mainloop()
