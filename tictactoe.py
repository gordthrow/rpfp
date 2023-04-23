import tkinter as tk

class TicTacToe:
    def __init__(self, master):
        self.master = master
        master.title("Tic Tac Toe")
        self.current_player = 'X'
        self.game_board = [[None]*3 for _ in range(3)]

        self.create_board()
        
    def create_board(self):
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.master, text='', font=('Arial', 50), width=3, height=1,
                                   command=lambda i=i, j=j: self.button_click(i, j))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)
            
        self.status_label = tk.Label(self.master, text=f"{self.current_player}'s turn", font=('Arial', 20))
        self.status_label.grid(row=3, column=0, columnspan=3, sticky="nsew")
        
        self.reset_button = tk.Button(self.master, text='Reset', font=('Arial', 20), command=self.reset_board)
        self.reset_button.grid(row=4, column=0, columnspan=3, sticky="nsew")
        
    def button_click(self, i, j):
        if self.game_board[i][j] is None:
            self.game_board[i][j] = self.current_player
            self.buttons[i][j].config(text=self.current_player, state=tk.DISABLED)
            winner = self.check_win()
            if winner:
                self.status_label.config(text=f"{self.current_player} wins!")
                self.disable_board()
            elif self.check_tie():
                self.status_label.config(text="Tie game!")
                self.disable_board()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                self.status_label.config(text=f"{self.current_player}'s turn")
                
    def check_win(self):
        for i in range(3):
            if self.game_board[i][0] == self.game_board[i][1] == self.game_board[i][2] != None:
                return True
            if self.game_board[0][i] == self.game_board[1][i] == self.game_board[2][i] != None:
                return True
        if self.game_board[0][0] == self.game_board[1][1] == self.game_board[2][2] != None:
            return True
        if self.game_board[0][2] == self.game_board[1][1] == self.game_board[2][0] != None:
            return True
        return False
    
    def check_tie(self):
        for i in range(3):
            for j in range(3):
                if self.game_board[i][j] is None:
                    return False
        return True
    
    def disable_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(state=tk.DISABLED)
                
    def reset_board(self):
        self.current_player = 'X'
        self.game_board = [[None]*3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text='', state=tk.NORMAL)
        self.status_label.config(text=f"{self.current_player}'s turn")
        
root = tk.Tk()
game = TicTacToe(root)
root.mainloop()