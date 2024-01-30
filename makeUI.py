import tkinter as tk
import tkinter.messagebox as mbox
import tictactoe as tic

# root = tk.Tk()
# root.title("Tic Tac Toe")

# for buttons
map = [["", "", ""],
       ["", "", ""],
       ["", "", ""]]

# to keep track of the game
states = [["", "", ""],
          ["", "", ""],
          ["", "", ""]]

# starting player
player = "O"

def button_click(row, col, root):
    # starting player
    global player

    if states[row][col] == "X" or states[row][col] == "O":
        mbox.showinfo("WRONG", "Occupied!")

    else:

        map[row][col].config(text="O")
        states[row][col] = "O"
        if tic.evaluateGame(states, "X", "O") == "O":
            mbox.showinfo("Winner", "O wins")
            root.destroy()

        if all(all(element != "" for element in sublist) for sublist in states):
            mbox.showinfo("No winner", "It's a tie")
            root.destroy()

        bestmove = tic.makeMoveMax(states)

        map[bestmove[0]][bestmove[1]].config(text="X")
        states[bestmove[0]][bestmove[1]] = "X"

        if tic.evaluateGame(states, "X", "O") == "X":
            mbox.showinfo("Winner", "AI wins")
            root.destroy()

        if all(all(element != "" for element in sublist) for sublist in states):
            mbox.showinfo("No winner", "It's a tie")
            root.destroy()


# whole game


def playGame(map):

    root = tk.Tk()
    root.title("Tic Tac Toe")

    for row in range(3):
        for col in range(3):
            map[row][col] = tk.Button(height=4, width=8, fg="blue",
                                      # kommer skapa en function för varje unik knapp
                                      font=("Helvetica", "15"), command=lambda r=row, c=col, ro=root: button_click(r, c, ro))
            map[row][col].grid(row=row, column=col)

    root.mainloop()


playGame(map)
