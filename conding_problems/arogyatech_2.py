
import random

class TicTokToe:
    def __init__(self, row=None, col=None):
        self.matrix = [["" for _ in range(3)] for _ in range(3)]
        self.user_input = None

        if row==None and col==None:
            r = random.choice([i for i in range(3)])
            c = random.choice([i for i in range(3)])
            self.matrix[r][c] = "O"
            # print(f"compter has marked row={r} and col{c}")
            for obj in self.matrix:
                print(obj)
            print("now your turn, please provide row and col value: ")
            self.user_input = input()
            self.player_input(self.user_input)
        
        self.last_move = None
    
    def check_winner(self, playername):
        ...
        

    def player_input(self, playerinputl):
        ...
        # if row<0 or col<0 or row>=3 or col>=3 or self.matrix[row][col]!=-1:
        #     raise Exception("invaild input please retry")
        
        # if self.last_move and self.last_move==playername:
        #     raise Exception("it's not your turn")
        
        # self.matrix[row][col] = playername
        # if self.check_winner(playername):
        #     print(f"player {playername} win")
        #     self.last_move=None
        #     self.matrix = [[-1 for _ in range(3)] for _ in range(3)]

        


a = TicTokToe()



