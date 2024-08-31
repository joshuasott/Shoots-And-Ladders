import random


class player(object):
    turnnumber = ''
    wins = 0
    square = 0

    def __init__(self, turnnumber):
        self.turnnumber = turnnumber


players = [player(1), player(2), player(3), player(4)]

# Key = square that modifies position, value = where you go if you land on the key
shoots_And_Ladders = {16: 6, 48: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78,
                      1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 80: 100, 71: 91}

# Amount of games to simulate
simnumb = 10000


def run():
    global simnumb
    global sim
    sim = 0
    while sim < simnumb:
        for player in players:
            roll = random.randint(1, 6)
            player.square += roll
            check_Value = checks(player)
            if check_Value == 0 or check_Value == 3:
                continue
            elif check_Value == 1:
                break
            elif check_Value == 2:
                player.square -= roll
    results()


'''
Takes in a player after they have moved and checks if
Their position must be modified (returns 0 if a shoot or
ladder is hit, and 2 if the finish line is over shot)
and if the game has been won (returns 1)
'''


def checks(player):
    try:
        # Move from a shoot or ladder
        player.square = shoots_And_Ladders[player.square]
        # Check if game is done
        if player.square == 100:
            reset(player)
            return 1
        return 0
    except KeyError:
        if player.square == 100:
            reset(player)
            return 1
        elif player.square > 100:
            return 2
    return 3


'''
Takes in the winner of the previous game and
resets the board for the next simulation
'''


def reset(winner):
    global sim
    sim += 1
    winner.wins += 1
    for player in players:
        player.square = 0


# Prints results once the simulation is finished
def results():
    for player in players:
        print(f"Player {player.turnnumber} won {player.wins}")


run()
