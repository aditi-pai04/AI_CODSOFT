#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class AlphaBeta:
    def __init__(self):
        self.c=0
        self.play_tic_tac_toe()
    def print_board(self,board):
        for row in board:
            print(" | ".join(row))
            print("-" * 10)

    def is_winner(self,board, player):
        # Check rows
        for row in board:
            if all(cell == player for cell in row):
                return True

        # Check columns
        for col in range(3):
            if all(board[row][col] == player for row in range(3)):
                return True

        # Check diagonals
        if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
            return True

        return False

    def is_board_full(self,board):
        return all(cell != ' ' for row in board for cell in row)

    def get_empty_cells(self,board):
        return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

    def minimax(self,board, depth, alpha, beta, maximizing_player):
        self.c+=1
        if self.is_winner(board, 'X'):
            return -1
        if self.is_winner(board, 'O'):
            return 1
        if self.is_board_full(board):
            return 0

        if maximizing_player:
            max_eval = float('-inf')
            for i, j in self.get_empty_cells(board):
                board[i][j] = 'O'
                eval = self.minimax(board, depth + 1, alpha, beta, False)
                board[i][j] = ' '
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = float('inf')
            for i, j in self.get_empty_cells(board):
                board[i][j] = 'X'
                eval = self.minimax(board, depth + 1, alpha, beta, True)
                board[i][j] = ' '
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval

    def get_best_move(self,board):
        best_val = float('-inf')
        best_move = None
        alpha = float('-inf')
        beta = float('inf')

        for i, j in self.get_empty_cells(board):
            board[i][j] = 'O'
            move_val = self.minimax(board, 0, alpha, beta, False)
            board[i][j] = ' '

            if move_val > best_val:
                best_move = (i, j)
                best_val = move_val

            alpha = max(alpha, best_val)

        return best_move

    def play_tic_tac_toe(self):
        board = [[' ' for _ in range(3)] for _ in range(3)]
        player_turn = True  # True for 'X', False for 'O'

        while True:
            self.print_board(board)

            if player_turn:
                row, col = map(int, input("Enter your move (row and column): ").split())
                if board[row][col] == ' ':
                    board[row][col] = 'X'
                else:
                    print("Invalid move. Try again.")
                    continue
            else:
                print("Computer's move:")
                row, col = self.get_best_move(board)
                board[row][col] = 'O'

            if self.is_winner(board, 'X'):
                self.print_board(board)
                print("You win!")
                break
            elif self.is_winner(board, 'O'):
                self.print_board(board)
                print("Computer wins!")
                break
            elif self.is_board_full(board):
                self.print_board(board)
                print("It's a tie!")
                break

            player_turn = not player_turn
        print(self.c)

if __name__ == "__main__":
    object1=AlphaBeta()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




