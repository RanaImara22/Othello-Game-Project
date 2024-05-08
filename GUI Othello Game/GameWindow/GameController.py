import tkinter as tk
from GameWindow.GameBoard import GameBoard
from tkinter import messagebox
import time


class GameController:
    def __init__(self, players , depth):
        self.players = players
        self.depth = depth
        self.current_player = {'player': self.players[0], 'validMoves': []}
        self.board = None  # Initialize board attribute as None
        self.start_game()

    def copy_board(self):
        self.copyBoard = GameBoard(self, self.players)
        for i in range(8):
            for j in range(8):
                self.copyBoard.board[i][j] = self.board.board[i][j]

    
    def start_game(self ):
        self.board = GameBoard(self , self.players)
        self.current_player = {'player': self.players[0], 'validMoves': self.board.valid_moves(self.players[0])}
        self.displayValidMoves(self.current_player)
        pass

    
    def clicked(self, i = -1, j = -1 , current_player = None): 
        if not self.current_player['player'].name == "Computer"  and (i, j) not in current_player['validMoves']:
            return
        self.board.remove_valid_moves(current_player['validMoves'])
        if self.current_player['player'].name == "Computer" : self.computer_move()
        else: self.playDisk(i, j , self.current_player['player'])
        if self.board.check_end_game():
            self.show_winner()
            return
        
        if not self.switch_player(self.current_player):
            messagebox.showinfo("No Valid Move", f"No Valid Move for {self.current_player['player'].name}. Switching Player")
            if not self.switch_player(self.current_player):
                self.show_winner()

        if self.current_player['player'].name == "Computer":
            self.board.updateGUI() , time.sleep(3)  
            self.clicked(-1 , -1 , self.current_player)
            
    
    def displayValidMoves(self , current_player):
        current_player['validMoves'] = self.board.valid_moves(current_player['player'])
        if not current_player['validMoves']:
            return False
        self.board.display_valid_moves(current_player['validMoves'])
        return True
        pass
    

    def playDisk(self , i , j , player):
        self.board.add_disk(i, j, player)
        self.change_score()
        pass

    def show_winner(self):
        if self.players[0].score > self.players[1].score:
            tk.messagebox.showinfo("Winner", self.players[0].name + " is the winner")
        elif self.players[0].score < self.players[1].score:
            tk.messagebox.showinfo("Winner", self.players[1].name + " is the winner")
        else:
            tk.messagebox.showinfo("Winner", "It's a tie")

    def reset_game(self):
        self.board.reset_board()
        self.current_player = {'player': self.players[0], 'validMoves': self.board.valid_moves(self.players[0])}
        self.displayValidMoves(self.current_player)
        self.change_score()
        pass

    def switch_player(self , current_player):
        if current_player['player'] == self.players[0]:
            current_player['player'] = self.players[1]
        else:
            current_player['player'] = self.players[0]
        current_player['validMoves'] = self.board.valid_moves(current_player['player'])
        self.board.current_player_label.config(text= "Current Player: " + current_player['player'].name)
        return self.displayValidMoves(current_player)

    def change_score(self):
        self.board.player_labels[0].config(text= str(self.players[0].score))
        self.board.player_labels[1].config(text= str(self.players[1].score))

    def utilityFunc(self , board):
        for i in range(8):
            for j in range(8):
                print(board[i][j] , end = " ")
            print()
        # Black is MAX and White is MIN
        white = 0
        black = 0
        for i in range(8):
            for j in range(8):
                if (board[i][j] == 'W'):
                    white += 1
                elif (board[i][j] == 'B'):
                    black += 1
        return black - white
    
    # alphaBetaSearch(board, depth, alpha, beta, players[0])
    def alphaBetaSearch(self, child_board, depth, alpha, beta, isMaxPlayer):
        if (depth == 0):
            return self.utilityFunc(child_board), None
        
        children = self.board.valid_moves(self.players[not isMaxPlayer], child_board)
        if (isMaxPlayer):
            maxEval = -1000
            bestChild = None
            if(len(children) == 1):
                return self.utilityFunc(child_board), children[0]
            for child in children:
                childrenBoard = self.getboardCopy(child_board)
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
            if(len(children) == 1):
                return self.utilityFunc(child_board), children[0]
            for child in children:
                childrenBoard = self.getboardCopy(child_board)
                self.board.add_disk(child[0], child[1], self.players[1] , childrenBoard)
                evalutation, _ = self.alphaBetaSearch(childrenBoard, depth - 1, alpha, beta, True)
                if (minEval > evalutation):
                    minEval = evalutation
                    bestChild = child
                beta = min(beta, evalutation)
                if (beta <= alpha):
                    break
            return minEval, bestChild
        
    def getboardCopy(self , board):
        boardCopy = []
        for i in range(8):
            boardCopy.append([])
            for j in range(8):
                boardCopy[i].append(board[i][j])
        return boardCopy
            
    def computer_move(self):
        evalutation, bestMove = self.alphaBetaSearch(self.board.getBoardCopy(), self.depth, -1000, 1000, False)
        if(bestMove == None):
            tk.messagebox.showinfo("No Valid Move", f"No Valid Move for {self.current_player['player'].name}. Switching Player")
            self.switch_player(self.current_player)
            return
        self.playDisk(bestMove[0], bestMove[1], self.players[1]) 


 

