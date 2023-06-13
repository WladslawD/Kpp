import tkinter as tk
from tkinter import messagebox


class Board:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(self.master, width=300, height=300)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.handle_click)
        self.draw_board()

        self.current_player = "X"
        self.game_over = False
        self.board = [["", "", ""], ["", "", ""], ["", "", ""]]

    def draw_board(self):
        for i in range(3):
            self.canvas.create_line(0, i * 100, 300, i * 100)
            self.canvas.create_line(i * 100, 0, i * 100, 300)
        

    def handle_click(self, event):
        if self.game_over:
            return
        row = event.y // 100
        col = event.x // 100
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.canvas.create_text(col * 100 + 50, row * 100 + 50, text=self.current_player, font=("Helvetica", 60))
            if self.check_for_winner():
                self.canvas.unbind("<Button-1>")
                messagebox.showinfo("Game Over", self.current_player + " wins!")
                self.game_over = True
            elif self.check_for_tie():
                self.canvas.unbind("<Button-1>")
                messagebox.showinfo("Game Over", "Tie game!")
                self.game_over = True
            else:
                self.switch_players()


    def switch_players(self):
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"

    def check_for_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        return False

    def check_for_tie(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "":
                    return False
        return True


class Game:
    def __init__(self):
        self.root = tk.Tk()
        self.board = Board(self.root)
        self.root.mainloop()


if __name__ == "__main__":
    game = Game()
