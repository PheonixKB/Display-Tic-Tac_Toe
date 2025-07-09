import tkinter as tk
from tkinter import messagebox
def is_winner(board):
    winner=[[0,1,2],[3,4,5],[6,7,8],
            [0,3,6],[1,4,7],[2,5,8],
            [0,4,8],[2,4,6]]
    for line in winner:
        a,b,c=line
        if board[a]==board[b]==board[c]!=" ":
            return board[a]
    if " " not in board:
        return 'Draw'
    return None
class TicTacToe:
    clicked=False
    def __init__(self,root):
        self.root=root
        self.root.title('Tic-Tac-Toe')
        self.board=[" "]*9
        self.buttons=[]
        self.scores={'X':0,'O':0,"Draw":0}
        for i in range(9):
            btn=tk.Button(root,text=" ",font=('Helvetica',20),height=3,width=6,command=lambda idx=i:self.player(idx))
            btn.grid(row=i//3,column=i%3)
            self.buttons.append(btn)
        restart = tk.Button(root, text="Restart", font=('Helvetica',14),
                            command=self.reset, width=18)
        restart.grid(row=3, column=0, columnspan=3, pady=10)

    def player(self,idx):
        if self.board[idx]!=' ':
            return
        if not TicTacToe.clicked:
            self.make_moves(idx,'X')
            TicTacToe.clicked=True
        elif TicTacToe.clicked:
            self.make_moves(idx,'O')
            TicTacToe.clicked=False
        self.game_over()
    
    def make_moves(self,idx,player):
        self.board[idx]=player
        self.buttons[idx]['text']=player
    def game_over(self):
        result=is_winner(self.board)
        if result=='Draw':
            msg="Its a Draw"
            self.scores['Draw']+=1
            self.reset()
        elif result is None:
            return None
        elif result=='X':
            msg='X wins'
            self.scores['X']+=1
        elif result=='O':
            msg='O wins'
            self.scores['O']+=1
        else:
            return False
        messagebox.showinfo("Tic-Tac-Toe", msg)
        again = messagebox.askyesno(title='Tic-Tac-Toe',message=f"{self.scores}\n\nPlay again?")
        if again:
            self.reset()
        else:
            self.disable_buttons()
    
    def reset(self):
        self.board=[' ']*9
        for btn in self.buttons:
            btn.config(text=' ',state='normal')
        TicTacToe.clicked=False
    def disable_buttons(self):
        for btn in self.buttons:
            btn.config(state="disabled")
if __name__ == "__main__":
    root = tk.Tk()
    TicTacToe(root)
    root.mainloop()
