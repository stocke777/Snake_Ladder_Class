import random
import itertools
import time

class Player:

    id_iter = itertools.count()

    def __init__(self, name):
        self.name = name
        self.id = next(self.id_iter)
        self.position = 0

    def __str__(self):
        return str(self.id) + "|" + str(self.name)


class Dice:

    def __init__(self, number_of_dice):
        self.number_of_dice = number_of_dice

    def roll_dice(self):
        return random.randrange(1, self.number_of_dice*6+1)

class Jumper:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def is_ladder(self):
        return self.start<self.end

    def is_snake(self):
        return self.start>self.end

    def __str__(self):
        return f"({self.start} : {self.end})"

class Gameboard:

    def __init__(self, jumpers, players, board_size, dice):
        self.number_of_players = len(players)
        self.jumpers = jumpers
        self.players = players
        self.board_size = board_size
        self.dice = dice
        self.result = []

    def print_result(self):
        print("Result:")
        for i, player in enumerate(self.result):
            print(i+1, player)

    def start_game(self):
        # for player in players:
        #     print(player, end = " ")
        # print()
        # for jumper in jumpers:
        #     print(jumper, end = " ")

        while len(players)>1:
            # time.sleep(1)
            dice_count = dice.roll_dice()
            player = self.players.pop(0)

            if player.position + dice_count <= self.board_size:
                if player.position + dice_count == self.board_size:
                    # print("Player {} finished at {} place".format(player.name, self.number_of_players - len(players)))
                    self.result.append(player)
                else:
                    player.position += dice_count
                    # print("Player {} reached position {}".format(player.name, player.position))
                    for jumper in self.jumpers:
                        if player.position == jumper.start:
                            player.position = jumper.end
                            # print("Player {} JUMPED to position {}".format(player.name, player.position))   
                            break
                    self.players.append(player)
            else:
                # print("Player {} need exactly {} to finish!!!".format(player.name, self.board_size - player.position))
                self.players.append(player)
        
        if self.players:
            self.result.append(players.pop())

        self.print_result()

            


#-------------------------------------------------------------#

NUMBER_OF_DICE = 2

#Players
p1 = Player("a")
p2 = Player("b")
p3 = Player("c")
p4 = Player("d")
players = [p1, p2, p3, p4]

#Jumpers
j1 = Jumper(3, 8)
j2 = Jumper(10, 12)
j3 = Jumper(18, 8)
j4 = Jumper(15, 11)
jumpers = [j1, j2, j3, j4]

#dice
dice = Dice(NUMBER_OF_DICE)

#gameboard
game = Gameboard(jumpers, players, 20, dice)
game.start_game()


