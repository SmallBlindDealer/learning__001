
from abc import ABC, abstractmethod
import random
from typing import List
from collections import deque
class Player:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.position = 0

class Snake:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        

class Ladder:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Dice:
    def __init__(self, total_dices):
        self.total_dices = total_dices
    
    def roll(self):
        return random.randint(self.total_dices, 6*self.total_dices)

class Board:
    def __init__(self, size):
        self.size = size
        self.snakes = {}
        self.ladders = {}

    def add_snake(self, start, end):
        self.snakes[start] = Snake(start, end)
    
    def add_ladder(self, start, end):
        self.ladders[start] = Ladder(start, end)
    
class GameController:
    def __init__(self, board: Board, players: deque[Player]):
        self.board = board
        self.players = players
        self.dice = Dice(1)
    
    def play(self):
        while True:
            player = self.players.popleft()
            dice_value = self.dice.roll()
            print(f"{player.name} rolled a dice and got {dice_value}")
            new_position = player.position + dice_value
            
            if new_position > self.board.size:
                print(f"{player.name} needs {self.board.size - player.position} to win")
                self.players.append(player)
                continue
            
            elif new_position in self.board.snakes:
                snake = self.board.snakes[new_position]
                print(f"{player.name} got bitten by a snake at {new_position} and moved to {snake.end}")
                new_position = snake.end
            
            elif new_position in self.board.ladders:
                ladder = self.board.ladders[new_position]
                print(f"{player.name} climbed a ladder at {new_position} and moved to {ladder.end}")
                new_position = ladder.end
            # else:
            #     print(f"{player.name} moved to {new_position}")
            
            player.position = new_position

            if new_position == self.board.size:
                print(f"{player.name} won the game")
                return
            
            self.players.append(player)
        
    

if __name__=="__main__":
    board = Board(100)
    board.add_snake(24, 5)
    board.add_snake(45, 20)
    board.add_snake(74, 34)
    board.add_snake(95, 17)
    board.add_ladder(5, 41)
    board.add_ladder(25, 69)
    board.add_ladder(35, 92)
    board.add_ladder(47, 87)

    players = deque([Player("1", 1),Player("2", 2),Player("3", 3),Player("4", 4)])

    gameController = GameController(board, players)
    gameController.play()




    

