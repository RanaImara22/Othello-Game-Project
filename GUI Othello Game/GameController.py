import tkinter as tk
from Board import GameBoard
from tkinter import messagebox
import time

from BoardController import BoardController
from Player import Player


class GameController:
    def __init__(self, players , depth):
        self.players = players
        self.depth = depth
        self.current_player = False
        self.current_valid_moves = []
        self.board = None
        self.start_game()


    def start_game(self ):
        self.board = GameBoard(self , self.players)
        self.displayValidMoves()
        pass

    def check_end_game(self):
        if self.board.check_end_game():
            self.show_winner()
            return True
        return False
    
    def clicked(self, i = -1, j = -1): 
        if not self.players[self.current_player].name == "Computer":
            for move in self.current_valid_moves:
                if move[0] == (i, j):
                    self.board.remove_valid_moves(self.current_valid_moves)
                    BoardController.flip_cells(move[0], move[1], self.players, self.current_player, self.board)
                    self.board.change_score(self.players)
                    if(self.switch_player()) :
                        if(self.players[self.current_player].name == "Computer") : self.computer_turn(True)
                    else : 
                        if(not self.switch_player()): 
                            self.show_winner()
                            return
                        break
        else : 
            self.computer_turn(True)
    
    def computer_turn(self , update = True):
        if(update) : self.board.updateGUI() , time.sleep(1)
        self.computer_move()
        self.board.remove_valid_moves(self.current_valid_moves)
        self.board.change_score(self.players)
        if(not self.switch_player()):
            if(not self.switch_player()): 
                self.show_winner() 
                return
            self.computer_turn(False)

    def displayValidMoves(self):
        self.current_valid_moves = BoardController.valid_moves(self.players , self.current_player , self.board , False)
        if not self.current_valid_moves:
            tk.messagebox.showinfo("No Valid Move", f"No Valid Move for {self.players[self.current_player].name}. Switching Player")
            return False
        self.board.display_valid_moves(self.current_valid_moves)
        return True
    

    def show_winner(self):
        if self.players[0].score > self.players[1].score:
            tk.messagebox.showinfo("Winner", self.players[0].name + " is the winner")
        elif self.players[0].score < self.players[1].score:
            tk.messagebox.showinfo("Winner", self.players[1].name + " is the winner")
        else:
            tk.messagebox.showinfo("Winner", "It's a tie")

    def reset_game(self):
        self.board.reset_board()
        self.current_player = False
        self.board.remove_valid_moves(self.current_valid_moves)
        self.displayValidMoves()
        self.board.change_current_player_label(self.players[self.current_player])
        pass

    def switch_player(self):
        self.current_player = not self.current_player
        self.valid_moves = BoardController.valid_moves(self.players , self.current_player , self.board , False)
        self.board.change_current_player_label(self.players[self.current_player])
        return self.displayValidMoves()


    def utilityFunc(self , board):
        # Black is MAX and White is MIN
        white = 0
        black = 0
        for i in range(8):
            for j in range(8):
                if (board[i][j] == 'W'):
                    white += 1
                elif (board[i][j] == 'B'):
                    black += 1
        return white - black
    
    # alphaBetaSearch(board, depth, alpha, beta, players[0])
    def alphaBetaSearch(self, child_board, depth, alpha, beta, isMaxPlayer):
        if (depth == 0): return self.utilityFunc(child_board), None
        children = BoardController.valid_moves(self.players, not isMaxPlayer, child_board , True)
        if(len(children) == 0):  return self.utilityFunc(child_board), None
        if (isMaxPlayer):
            maxEval = -1000
            bestChild = None
            for child in children:
                childrenBoard = self.board.copy_board(child_board , True)
                BoardController.flip_cells(child[0], child[1], self.players, 0, childrenBoard, True)
                evalutation, _ = self.alphaBetaSearch(childrenBoard, depth - 1, alpha, beta, False)
                if (maxEval < evalutation):
                    maxEval = evalutation
                    bestChild = child
                alpha = max(alpha, evalutation)
                if (beta <= alpha):
                    break
            return maxEval, bestChild
        else:
            minEval = 1000
            bestChild = None
            for child in children:
                childrenBoard = self.board.copy_board(child_board , True)
                BoardController.flip_cells(child[0], child[1], self.players, 0, childrenBoard, True)
                evalutation, _ = self.alphaBetaSearch(childrenBoard, depth - 1, alpha, beta, True)
                if (minEval > evalutation):
                    minEval = evalutation
                    bestChild = child
                beta = min(beta, evalutation)
                if (beta <= alpha):
                    break
            return minEval, bestChild
                    
    def computer_move(self):
        evalutation, bestMove = self.alphaBetaSearch(self.board.copy_board(self.board.buttons , False), self.depth, -1000, 1000, False)
        if(bestMove != None):
            BoardController.flip_cells(bestMove[0], bestMove[1], self.players, self.current_player, self.board)



    