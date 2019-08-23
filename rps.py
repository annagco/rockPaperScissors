import random
import time


"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class AllRockPlayer(Player):
    pass


class RandomPlayer(Player):
    def move(self):
        choice = random.choice(moves)
        return choice


class HumanPlayer(Player):
    def move(self):
        time.sleep(1)
        choice = input("Please pick: Rock, Paper or Scissors? ")
        while not self.validateChoice(choice):
            choice = input("Please pick: Rock, Paper or Scissors? ")
        return choice

    def validateChoice(self, choice):
        if ((choice == 'rock') or
           (choice == 'scissors') or
           (choice == 'paper')):
            return True

        return False


class ReflectPlayer(Player):
    def __init__(self):
        self.nextPlay = random.choice(moves)

    def move(self):
        return self.nextPlay

    def learn(self, my_move, their_move):
        self.nextPlay = their_move


class CyclePlayer(Player):
    def __init__(self):
        self.nextPlay = random.choice(moves)

    def move(self):
        return self.nextPlay

    def learn(self, my_move, their_move):
        if my_move == 'rock':
            self.nextPlay = 'paper'
        elif my_move == 'paper':
            self.nextPlay = 'scissors'
        elif my_move == 'scissors':
            self.nextPlay = 'rock'


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.scorep1 = 0
        self.scorep2 = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        time.sleep(1)
        self.compute_score(move1, move2)
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(3):
            time.sleep(1)
            print(f"Round {round}:")
            time.sleep(1)
            self.play_round()
        self.announce_winner()
        print("Game over!")

    def compute_score(self, movep1, movep2):
        if beats(movep1, movep2):
            self.scorep1 += 1
            print("Player 1 won this round!")
            time.sleep(1)
        elif beats(movep2, movep1):
            self.scorep2 += 1
            print("Player 2 won this round!")
        else:
            time.sleep(1)
            print("Draw!")
            time.sleep(1)

        print(f"Player 1 score: {self.scorep1}")
        time.sleep(1)
        print(f"Player 2 score: {self.scorep2}")

    def announce_winner(self):
        if self.scorep1 == self.scorep2:
            print("It was a draw!")
        elif self.scorep1 > self.scorep2:
            print("Player 1 is the winner!")
        else:
            print("Player 2 is the winner!")


if __name__ == '__main__':
    players = [
    AllRockPlayer(),
    RandomPlayer(),
    ReflectPlayer(),
    CyclePlayer()
    ]
    p1 = HumanPlayer()
    p2 = random.choice(players)
    game = Game(p1, p2)
    game.play_game()
