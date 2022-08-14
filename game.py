import time
from player import ComputerPlayer, HumanPlayer, AIPlayer


class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # single list to represent 3*3 board
        self.CurrentWinner = None  # keep track of winner

    def printBoard(self):
        # getting the rows

        for row in [self.board[i * 3: (i + 1) * 3] for i in range(3)]:
            print("|" + "|".join(row) + "|")

    @staticmethod
    def print_board_nums():
        # | 1 | 2 | 3 |   (tells us what number corresponds to what box)
        number_board = [[str(i) for i in range((j * 3 + 1), ((j+1) * 3 + 1))] for j in range(0, 3)]
        for row in number_board:
            print("|" + "|".join(row) + "|")
        print("")

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
        # moves = []
        # for (i, spot) in enumerate(self.board):
        #    # ['x', 'o', 'x'] --> [(0, 'x'), (1, 'o'), (2, 'x')]
        #    if spot == ' ':
        #        moves.append(i)
        # return moves

    def make_move(self, square, letter):
        if letter == 'O':
            self.board[square] = 'O'
            if self.winner(square, letter):
                self.CurrentWinner = 'O'
        else:
            self.board[square] = 'X'
            if self.winner(square, letter):
                self.CurrentWinner = 'X'

    def winner(self, square, letter):
        # win if 3 in a row
        row_index = square // 3
        row = self.board[row_index * 3: (row_index + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        # check column
        column_index = square % 3
        column = [self.board[column_index + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # check diagonal
        diagonal1 = self.board[0:9:4]
        diagonal2 = self.board[2:7:2]
        if all([spot == letter for spot in diagonal1]):
            return True
        elif all([spot == letter for spot in diagonal2]):
            return True

        return False

    def empty_squares(self):
        return " " in self.board

    def num_empty_squares(self):
        return self.board.count(' ')


def play(game, x_player, o_player, print_game=True):
    # game returns winner
    if print_game:
        game.print_board_nums()

    letter = 'O'  # starting move

    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        game.make_move(square, letter)

        if game.CurrentWinner:
            if print_game:
                game.printBoard()
                print("")
                print(letter + ' wins!')
                return letter

        if print_game:
            print(letter + f" makes move to square {square + 1}")
            print('')
            game.printBoard()
            print('')
        letter = 'O' if letter == 'X' else 'X'
        # print(game.board)

        # tiny break
        time.sleep(0.8)

    if print_game:
        print("It's a tie!")


if __name__ == '__main__':
    x = AIPlayer('X')
    o = HumanPlayer('O')
    t = TicTacToe()
    play(t, x, o, print_game=True)



