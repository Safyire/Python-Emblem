from tkinter import *

flag = 0
turns = 0


def check_values():
    # Create "if statements" for when X or Y gets three in a row via row 1.
    # Include "if statement" for when X gets 3 in a row.
    # Include "if statement" for when Y gets 3 in a row.
    # In both cases, the labelTitle should change and address who won or a tie.
    # In both cases, call "disableButtons()" after a winner is declared.
    if "X" == button_0.cget("text") == button_1.cget("text") == button_2.cget("text"):
        labelTitle.config(text="Player X Won!")
        disable_buttons()
    elif "Y" == button_0.cget("text") == button_1.cget("text") == button_2.cget("text"):
        labelTitle.config(text="Player Y Won!")
        disable_buttons()

    # Create "if statements" for when X or Y gets three in a row via row 2.
    # Include "if statement" for when X gets 3 in a row.
    # Include "if statement" for when Y gets 3 in a row.
    # In both cases, the labelTitle should change and address who won or a tie.
    # In both cases, call "disableButtons()" after a winner is declared.
    elif "X" == button_3.cget("text") == button_4.cget("text") == button_5.cget("text"):
        labelTitle.config(text="Player X Won!")
        disable_buttons()
    elif "Y" == button_3.cget("text") == button_4.cget("text") == button_5.cget("text"):
        labelTitle.config(text="Player Y Won!")
        disable_buttons()

    # Create "if statements" for when X or Y gets three in a row via row 3.
    # Include "if statement" for when X gets 3 in a row.
    # Include "if statement" for when Y gets 3 in a row.
    # In both cases, the labelTitle should change and address who won or a tie.
    # In both cases, call "disableButtons()" after a winner is declared.
    elif "X" == button_6.cget("text") == button_7.cget("text") == button_8.cget("text"):
        labelTitle.config(text="Player X Won!")
        disable_buttons()
    elif "Y" == button_6.cget("text") == button_7.cget("text") == button_8.cget("text"):
        labelTitle.config(text="Player Y Won!")
        disable_buttons()

    # Create "if statements" for when X or Y gets three in a row via column 1.
    # Include "if statement" for when X gets 3 in a row.
    # Include "if statement" for when Y gets 3 in a row.
    # In both cases, the labelTitle should change and address who won or a tie.
    # In both cases, call "disableButtons()" after a winner is declared.
    elif "X" == button_0.cget("text") == button_3.cget("text") == button_6.cget("text"):
        labelTitle.config(text="Player X Won!")
        disable_buttons()
    elif "Y" == button_0.cget("text") == button_3.cget("text") == button_6.cget("text"):
        labelTitle.config(text="Player Y Won!")
        disable_buttons()

    # Create "if statements" for when X or Y gets three in a row via column 2.
    # Include "if statement" for when X gets 3 in a row.
    # Include "if statement" for when Y gets 3 in a row.
    # In both cases, the labelTitle should change and address who won or a tie.
    # In both cases, call "disableButtons()" after a winner is declared.
    elif "X" == button_1.cget("text") == button_4.cget("text") == button_7.cget("text"):
        labelTitle.config(text="Player X Won!")
        disable_buttons()
    elif "Y" == button_1.cget("text") == button_4.cget("text") == button_7.cget("text"):
        labelTitle.config(text="Player Y Won!")
        disable_buttons()

    # Create "if statements" for when X or Y gets three in a row via column 3.
    # Include "if statement" for when X gets 3 in a row.
    # Include "if statement" for when Y gets 3 in a row.
    # In both cases, the labelTitle should change and address who won or a tie.
    # In both cases, call "disableButtons()" after a winner is declared.
    elif "X" == button_2.cget("text") == button_5.cget("text") == button_8.cget("text"):
        labelTitle.config(text="Player X Won!")
        disable_buttons()
    elif "Y" == button_2.cget("text") == button_5.cget("text") == button_8.cget("text"):
        labelTitle.config(text="Player Y Won!")
        disable_buttons()

    # Create "if statement" for when X or Y gets three in a row via diagonally from left to right.
    # Include "if statement" for when X gets 3 in a row.
    # Include "if statement" for when Y gets 3 in a row.
    # In both cases, the labelTitle should change and address who won or a tie.
    # In both cases, call "disableButtons()" after a winner is declared.
    elif "X" == button_0.cget("text") == button_4.cget("text") == button_8.cget("text"):
        labelTitle.config(text="Player X Won!")
        disable_buttons()
    elif "Y" == button_0.cget("text") == button_4.cget("text") == button_8.cget("text"):
        labelTitle.config(text="Player Y Won!")
        disable_buttons()

    # Create "if statement" for when X or Y gets three in a row via diagonally from right to left.
    # Include "if statement" for when X gets 3 in a row.
    # Include "if statement" for when Y gets 3 in a row.
    # In both cases, the labelTitle should change and address who won or a tie.
    # In both cases, call "disableButtons()" after a winner is declared.
    elif "X" == button_2.cget("text") == button_4.cget("text") == button_6.cget("text"):
        labelTitle.config(text="Player X Won!")
        disable_buttons()
    elif "Y" == button_2.cget("text") == button_4.cget("text") == button_6.cget("text"):
        labelTitle.config(text="Player Y Won!")
        disable_buttons()

    # Create "if statement" for when a tie occurs.
    # Include "if statement" checking to see if all buttons are disabled.
    # Change the labelTitle to indicate a tie.
    else:
        if turns == 9:
            labelTitle.config(text="It's a tie!")


def disable_buttons():
    # Disable all buttons.
    button_0.config(state="disabled")
    button_1.config(state="disabled")
    button_2.config(state="disabled")
    button_3.config(state="disabled")
    button_4.config(state="disabled")
    button_5.config(state="disabled")
    button_6.config(state="disabled")
    button_7.config(state="disabled")
    button_8.config(state="disabled")


def button_clicked(button):
    global turns
    global flag
    if flag == 0:
        # Configure the button to show a letter, a color, and be disabled.
        button.config(text="X", bg="red", state="disabled")
        flag = 1
    else:
        # Configure the button to show a letter, a color, and be disabled.
        button.config(text="Y", bg="blue", state="disabled")
        flag = 0
    turns += 1
    check_values()


root = Tk()
root.title("TicTacToe")
root.iconbitmap("favicon.ico")

# Create a label and give it a text value. Call the label: labelTitle.
labelTitle = Label(root, text="Welcome to TicTacToe!")

# Create button_0. Give it a width of 10 and height of 5.
button_0 = Button(root, width=10, height=5)

# Configure button_0 and pass it the following argument: command=lambda: buttonClicked(button_0)
button_0.config(command=lambda: button_clicked(button_0))

# Repeat for buttons 1 through 8 using the same naming convention.
button_1 = Button(root, width=10, height=5)
button_1.config(command=lambda: button_clicked(button_1))

button_2 = Button(root, width=10, height=5)
button_2.config(command=lambda: button_clicked(button_2))

button_3 = Button(root, width=10, height=5)
button_3.config(command=lambda: button_clicked(button_3))

button_4 = Button(root, width=10, height=5)
button_4.config(command=lambda: button_clicked(button_4))

button_5 = Button(root, width=10, height=5)
button_5.config(command=lambda: button_clicked(button_5))

button_6 = Button(root, width=10, height=5)
button_6.config(command=lambda: button_clicked(button_6))

button_7 = Button(root, width=10, height=5)
button_7.config(command=lambda: button_clicked(button_7))

button_8 = Button(root, width=10, height=5)
button_8.config(command=lambda: button_clicked(button_8))

# Add labelTitle to the grid.
labelTitle.grid(row=0, columnspan=3)

# Add buttons 0 through 8 to the grid.
button_0.grid(row=1, column=0)
button_1.grid(row=1, column=1)
button_2.grid(row=1, column=2)
button_3.grid(row=2, column=0)
button_4.grid(row=2, column=1)
button_5.grid(row=2, column=2)
button_6.grid(row=3, column=0)
button_7.grid(row=3, column=1)
button_8.grid(row=3, column=2)

root.mainloop()
