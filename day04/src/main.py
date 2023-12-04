class Row:
    def __init__(self, row):
        self.row = row

    def values(self):
        return list(map(int, self.row.strip().replace("  ", " 0").split(" ")))


class Card:
    def __init__(self, index, winning: Row, yours: Row):
        self.index = index
        self.winning = winning.values()
        self.yours = yours.values()

    def win_count(self):
        return len(list(filter(lambda x: x in self.winning, self.yours)))

    def score(self):
        if not (count := self.win_count()):
            return 0

        return pow(2, count - 1)


def line_to_card(input):
    index, line = input
    parts = line.split(":")[1].split("|")
    return Card(index, Row(parts[0]), Row(parts[1]))


def get_copies(cards):
    res = [1] * len(cards)

    for card in cards:
        for i in range(card.win_count()):
            res[card.index + i + 1] += res[card.index]

    return res


with open("../data/input") as input:
    cards = list(map(line_to_card, enumerate(input.readlines())))
    scores = list(map(Card.score, cards[:]))
    print("Part 1:", sum(scores))

    copies = get_copies(cards[:])
    print("Part 2:", sum(copies))
