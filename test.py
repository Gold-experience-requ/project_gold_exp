"""import mysql.connector as m
mydb = m.connect(
  host="localhost",
  user="root",
  password="swordsaint"
)
cur = mydb.cursor()
cur.execute("create database testdb")
cur.execute("use testdb")
cur.execute("create table testtable (id int, name varchar(255))") 
cur.execute("insert into testtable (id, name) values (1, 'test')")
cur.execute("select * from testtable")
for row in cur.fetchall():
    print(row)
mydb.commit()
#test comment
#test comment from github main edit
#check 2
#last check
#test from branch
#last test from branch



print("  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  ")
print(" | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. | ")
print(" | |      __      | || |  _______     | || |     ______   | || |      __      | || |  ________    | || |  _________   | | ")
print(" | |     /  \     | || | |_   __ \    | || |   .' ___  |  | || |     /  \     | || | |_   ___ `.  | || | |_   ___  |  | | ")
print(" | |    / /\ \    | || |   | |__) |   | || |  / .'   \_|  | || |    / /\ \    | || |   | |   `. \ | || |   | |_  \_|  | | ")
print(" | |   / ____ \   | || |   |  __ /    | || |  | |         | || |   / ____ \   | || |   | |    | | | || |   |  _|  _   | | ")
print(" | | _/ /    \ \_ | || |  _| |  \ \_  | || |  \ `.___.'\  | || | _/ /    \ \_ | || |  _| |___.' / | || |  _| |___/ |  | | ")
print(" | ||____|  |____|| || | |____| |___| | || |   `._____.'  | || ||____|  |____|| || | |________.'  | || | |_________|  | | ")
print(" | |              | || |              | || |              | || |              | || |              | || |              | | ")
print(" | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' | ")
print("  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  ")
print(" ")

    clear_screen()
    print("---------------------------------------------------------")
    print("██████╗  ██████╗  ██████╗  ██████╗  █████╗  ███████╗")
    print("██╔══██╗██╔═══██╗██╔═══██╗██╔═══██╗██╔══██╗██╔════╝")
    print("██████╔╝██║   ██║██║   ██║██║   ██║███████║█████╗  ")
    print("██╔══██╗██║   ██║██║   ██║██║   ██║██╔══██║██╔══╝  ")
    print("██║  ██║╚██████╔╝╚██████╔╝╚██████╔╝██║  ██║███████╗")
    print("╚═╝  ╚═╝ ╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝")
    print("\n")
    print("             WELCOME TO THE ARCADE ZONE!")
    print("          GET READY FOR PIXELATED FUN!")
    print("\n")
    print("           > PRESS ENTER TO BEGIN <")
    print("---------------------------------------------------------")
    input() # Waits for user to press Enter
    
    print("---------------------------------------------------------")
print(" █████╗ ██████╗  ██████╗  █████╗ ██████╗  ███████╗")
print("██╔══██╗██╔══██╗██╔════╝ ██╔══██╗██╔═══██╗██╔════╝")
print("███████║██████╔╝██║      ███████║██║   ██║█████╗  ")
print("██╔══██║██╔══██╗██║      ██╔══██║██║   ██║██╔══╝  ")
print("██║  ██║██║  ██║╚██████╔╝██║  ██║██████╔╝ ███████╗")
print("╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ═════╝  ╚══════╝")
print("\n")
print("             WELCOME TO THE ARCADE ZONE!")
print("          GET READY FOR PIXELATED FUN!")
print("\n")
print("           > PRESS ENTER TO BEGIN <")
print("---------------------------------------------------------")
input() # Waits for user to press Enter"""

import tkinter as tk
from tkinter import messagebox
import random

root = tk.Tk()
root.title("Tic-Tac-Toe")

current_player = "X"  # Human is X, Computer is O
board = [""] * 9

def check_winner():
    wins = [
        (0,1,2), (3,4,5), (6,7,8),  # rows
        (0,3,6), (1,4,7), (2,5,8),  # columns
        (0,4,8), (2,4,6)            # diagonals
    ]
    for a, b, c in wins:
        if board[a] == board[b] == board[c] != "":
            return board[a]
    if "" not in board:
        return "Draw"
    return None

def computer_move():
    empty = [i for i, v in enumerate(board) if v == ""]
    if empty:
        move = random.choice(empty)
        board[move] = "O"
        buttons[move].config(text="O")
        winner = check_winner()
        if winner:
            if winner == "Draw":
                messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
            else:
                messagebox.showinfo("Tic-Tac-Toe", f"Player {winner} wins!")
            reset_board()

def on_click(i):
    global current_player
    if board[i] == "" and not check_winner():
        board[i] = "X"
        buttons[i].config(text="X")
        winner = check_winner()
        if winner:
            if winner == "Draw":
                messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
            else:
                messagebox.showinfo("Tic-Tac-Toe", f"Player {winner} wins!")
            reset_board()
        else:
            computer_move()

def reset_board():
    global board, current_player
    board = [""] * 9
    current_player = "X"
    for btn in buttons:
        btn.config(text="")

buttons = []
for i in range(9):
    btn = tk.Button(root, text="", font=("Arial", 32), width=5, height=2,
                    command=lambda i=i: on_click(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

reset_btn = tk.Button(root, text="Reset", command=reset_board)
reset_btn.grid(row=3, column=0, columnspan=3, sticky="nsew")

root.mainloop()