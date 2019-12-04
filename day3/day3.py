from collections import defaultdict


def read_file(name):
    with open(f"{name}") as f:
        content = f.readlines()
    return [x.strip() for x in content]


def manhattan(position):
    return abs(position[0]) + abs(position[1])


def wire_position(wire):
    x, y = 0, 0
    position = set()

    for i in range(len(wire)):
        for _ in range(int(wire[i][1:])):
            direction = wire[i][0]

            if direction == "U":
                y += 1
            elif direction == "D":
                y -= 1
            elif direction == "R":
                x += 1
            elif direction == "L":
                x -= 1
            else:
                raise RuntimeError(f"not valid direction: {direction}")

            position.add((x, y))

    return position


def crossing_distance(wire, crossing):
    x, y = 0, 0
    crossing = defaultdict(int)
    distance = 0

    for i in range(len(wire)):
        for _ in range(int(wire[i][1:])):
            direction = wire[i][0]

            if direction == "U":
                y += 1
            elif direction == "D":
                y -= 1
            elif direction == "R":
                x += 1
            elif direction == "L":
                x -= 1
            else:
                raise RuntimeError(f"not valid direction: {direction}")

            distance += 1

            if (x, y) in crossing:
                crossing[(x, y)] = distance

    return crossing


input = read_file("day3.txt")
first_wire = input[0].split(",")
second_wire = input[1].split(",")


def calculations():
    position_of_first_wire = wire_position(first_wire)
    position_of_second_wire = wire_position(second_wire)
    intersection = position_of_first_wire.intersection(position_of_second_wire)

    return min(manhattan(position) for position in intersection)


result = calculations()
print(f"Solution for part1: {result}")
