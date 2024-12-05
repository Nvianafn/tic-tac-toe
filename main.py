import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        
        # Inisialisasi variabel permainan
        self.current_player = "X"
        self.board = [""] * 9
        self.buttons = []
        
        # Frame untuk status
        status_frame = tk.Frame(self.window)
        status_frame.pack(pady=5)
        
        self.status_label = tk.Label(
            status_frame,
            text=f"Giliran Player {self.current_player}",
            font=('Arial', 14)
        )
        self.status_label.pack()
        
        # Frame untuk papan permainan
        game_frame = tk.Frame(
            self.window,
            bg='gray'
        )
        game_frame.pack(pady=5)
        
        # Membuat grid 3x3
        for i in range(3):
            for j in range(3):
                button = tk.Button(
                    game_frame,
                    text="",
                    font=('Arial', 20, 'bold'),
                    width=6,
                    height=2,
                    command=lambda row=i, col=j: self.button_click(row, col)
                )
                button.grid(row=i, column=j, padx=2, pady=2)
                self.buttons.append(button)
        
        # Tombol reset
        reset_button = tk.Button(
            self.window,
            text="Reset Game",
            font=('Arial', 12),
            command=self.reset_game
        )
        reset_button.pack(pady=10)
        
        # Mengatur ukuran minimum window
        self.window.minsize(300, 400)
    
    def button_click(self, row, col):
        index = row * 3 + col
        
        # Cek apakah kotak masih kosong
        if self.board[index] == "":
            self.board[index] = self.current_player
            self.buttons[index].config(
                text=self.current_player,
                state="disabled",
                disabledforeground="black"
            )
            
            # Cek pemenang
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} Menang!")
                self.disable_all_buttons()
            # Cek seri
            elif "" not in self.board:
                messagebox.showinfo("Game Over", "Permainan Seri!")
                self.disable_all_buttons()
            else:
                # Ganti pemain
                self.current_player = "O" if self.current_player == "X" else "X"
                self.status_label.config(text=f"Giliran Player {self.current_player}")
    
    def check_winner(self):
        # Kombinasi menang
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Baris
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Kolom
            [0, 4, 8], [2, 4, 6]              # Diagonal
        ]
        
        # Cek setiap kombinasi
        for combo in win_combinations:
            if (self.board[combo[0]] == self.board[combo[1]] == 
                self.board[combo[2]] == self.current_player):
                # Highlight kombinasi pemenang
                for index in combo:
                    self.buttons[index].config(bg='light green')
                return True
        return False
    
    def disable_all_buttons(self):
        for button in self.buttons:
            button.config(state="disabled")
    
    def reset_game(self):
        # Reset variabel
        self.current_player = "X"
        self.board = [""] * 9
        self.status_label.config(text=f"Giliran Player {self.current_player}")
        
        # Reset tombol
        for button in self.buttons:
            button.config(
                text="",
                state="normal",
                bg='SystemButtonFace'
            )
    
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()