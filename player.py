import math
import random


class Player:
    def __init__(self, letter):
        #  letter is x or o
        self.letter = letter

    def get_move(self, game):
        pass


class ComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        move = random.choice(game.available_moves())
        return move


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_move = False
        val = None
        while not valid_move:
            user_move = (input(self.letter + "'s turn to move. Input move (1-9): "))
            try:
                val = int(user_move) - 1
                if val not in game.available_moves():
                    raise ValueError
                valid_move = True
            except ValueError:
                print("Invalid move. Try again")

        return val


class AIPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            move = random.choice(game.available_moves())
        else:
            move = self.minimax(game, self.letter)['position']
        return move

    def minimax(self, state, player):
        max_player = self.letter
        other_player = 'X' if player == 'O' else 'O'

        # check if the previous move was a winner
        if state.CurrentWinner == other_player:
            return {'position': None,
                    'score': 1 * (1 + state.num_empty_squares()) if other_player == max_player else -1 *
                        (1 + state.num_empty_squares())

                    }

        elif not state.empty_squares():  # no empty squares
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}  # each score should maximize (be larger)
        else:
            best = {'position': None, 'score': math.inf}  # each score should minimize (be smaller)

        for possible_move in state.available_moves():
            #  step 1: make a move, try that spot
            state.make_move(possible_move, player)
            #  step 2: recurse using minimax to simulate a game after making that move
            sim_score = self.minimax(state, other_player)
            #  step 3: undo the move
            state.board[possible_move] = ' '
            state.CurrentWinner = None
            sim_score['position'] = possible_move
            #  step 4: update the dictionaries if necessary
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score

        return best
