import fileinput

DIRECTIONS = {
    'U': (0, -1),
    'D': (0, 1),
    'L': (-1, 0),
    'R': (1, 0),
}


def parse(line):
    solution = dict()
    x, y = 0, 0
    steps = 0
    for token in line.split(','):
        (dx, dy), n = DIRECTIONS[token[0]], int(token[1:])
        for i in range(n):
            x, y, steps = x + dx, y + dy, steps + 1
            solution.setdefault((x, y), steps)
    return solution


lines = list(fileinput.input("day3.txt"))
first_wire = parse(lines[0])
second_wire = parse(lines[1])
x = set(first_wire) & set(second_wire)
# Part 1 solution:
print(min(sum(map(abs, p)) for p in x))
# Part 2 solution:
print(min(first_wire[k] + second_wire[k] for k in x))
