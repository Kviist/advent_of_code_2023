class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Number:
    def __init__(self, number, coordinate):
        self.number = number
        self.coordinate = coordinate
        self.x = coordinate.x
        self.y = coordinate.y

    def append(self, number):
        self.number += number

    def value(self):
        return int(self.number)

    def index_end(self):
        return self.x + len(self.number) - 1

    def is_first_row(self):
        return self.y == 0

    def is_last_row(self, ylength):
        return self.y == ylength - 1

    def is_first_char(self):
        return self.x == 0

    def is_last_char(self, xlength):
        return self.index_end() == xlength - 1

    def adjacents(self, xlength, ylength):
        res = []

        if not self.is_first_char():
            res.append(Coordinate(self.x - 1, self.y))  # left
            if not self.is_first_row():
                res.append(Coordinate(self.x - 1, self.y - 1))  # top left
            if not self.is_last_row(ylength):
                res.append(Coordinate(self.x - 1, self.y + 1))  # bottom left

        if not self.is_last_char(xlength):
            res.append(Coordinate(self.index_end() + 1, self.y))  # right
            if not self.is_first_row():
                res.append(Coordinate(self.index_end() + 1, self.y - 1))  # top right
            if not self.is_last_row(ylength):
                res.append(Coordinate(self.index_end() + 1, self.y + 1))  # bottom right

        for i in range(self.x, self.index_end() + 1):
            if not self.is_first_row():
                res.append(Coordinate(i, self.y - 1))
            if not self.is_last_row(ylength):
                res.append(Coordinate(i, self.y + 1))

        return res

    def is_adjacent(self, other, xlength, ylength):
        return any(
            map(
                lambda coordinate: coordinate.x == other.x and coordinate.y == other.y,
                self.adjacents(xlength, ylength),
            )
        )


def find_numbers(grid):
    numbers = []

    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char.isalnum():
                if numbers and numbers[-1].index_end() == x - 1:
                    numbers[-1].append(char)
                else:
                    numbers.append(Number(char, Coordinate(x, y)))

    return numbers


def is_symbol(char):
    return not (char.isalnum() or char == ".")


def is_gear(char):
    return char == "*"


def is_adjacent_to(callback, number, grid):
    run_call = lambda coordinate: callback(grid[coordinate.y][coordinate.x])
    return any(map(run_call, number.adjacents(len(grid[0]), len(grid))))


def filter_numbers(numbers, grid, callback):
    check = lambda number: is_adjacent_to(callback, number, grid)
    return filter(check, numbers)


def sum_and_print(message, numbers):
    values = map(lambda num: int(num.number), numbers)
    print(message, sum(list(values)))


def get_adjacents(coordinate, numbers, xlength, ylength):
    res = []

    for number in numbers:
        if number.is_adjacent(coordinate, xlength, ylength):
            res.append(number)

    return res


def part_two(grid, numbers):
    total = 0

    for r_i, row in enumerate(grid):
        for c_i, char in enumerate(row):
            if is_gear(char):
                adj_nums = get_adjacents(
                    Coordinate(c_i, r_i), numbers, len(grid[0]), len(grid)
                )
                if len(adj_nums) > 1:
                    total += adj_nums[0].value() * adj_nums[1].value()

    return total


with open("../data/input") as input:
    to_char_list = lambda line: list(line.strip())
    grid = list(map(to_char_list, input.readlines()))

    numbers = find_numbers(grid[:])
    filtered = filter_numbers(numbers, grid, is_symbol)
    sum_and_print("Part one:", filtered)

    print("Part two:", part_two(grid[:], numbers))
