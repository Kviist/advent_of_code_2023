class Game:
    def __init__(self, line):
        self.line = line

    def game_number(self):
        return int(self.line.split(":")[0].replace("Game ", ""))

    def get_rounds(self):
        rounds = self.line.split(":")[1].split(";")
        return map(lambda x: Round(x), rounds)


class Round:
    def __init__(self, line):
        self.red, self.green, self.blue = 0, 0, 0
        self.process_round(line)

    def process_round(self, line):
        for part in line.split(","):
            count, color = part.strip(" \n\t").split(" ")
            self.set_count(color, int(count))

    def set_count(self, color, count):
        if color == "red":
            self.red = count
        elif color == "green":
            self.green = count
        elif color == "blue":
            self.blue = count

    def is_over(self, other: "Round"):
        return (
            self.red < other.red or self.green < other.green or self.blue < other.blue
        )

    def power(self):
        return self.red * self.green * self.blue


def is_possible(game):
    return not any(limit.is_over(round) for round in game.get_rounds())


def find_minimum_power(game):
    current = Round("0 red, 0 green, 0 blue")

    for round in game.get_rounds():
        current.red = max(current.red, round.red)
        current.blue = max(current.blue, round.blue)
        current.green = max(current.green, round.green)

    return current.power()


with open("../data/input.txt") as input:
    games = list(map(lambda x: Game(x), input.readlines()))

    limit = Round("12 red, 13 green, 14 blue")
    possible_games = list(filter(is_possible, games))
    possible_game_numbers = map(lambda game: game.game_number(), possible_games)

    minimum_powers = map(find_minimum_power, games)

    print(sum(possible_game_numbers))  # part one
    print(sum(minimum_powers))  # part two
