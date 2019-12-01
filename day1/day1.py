import os


def calculate_module(mass):
    return int(int(mass) / 3) - 2


def fuel_calculation(mass):
    total_mass = 0

    while int(mass) > 0:
        mass = calculate_module(mass)
        if mass < 0:
            return total_mass
        total_mass += mass

    return total_mass


def part1(file):
    with open(file) as f:
        total_mass = 0

        for mass in f.readlines():
            total_mass += calculate_module(mass)

        print(total_mass)


def part2(file):
    with open(file) as f:
        total_mass = 0

        for mass in f.readlines():
            total_mass += fuel_calculation(mass)

        print(total_mass)


part1('day1.txt')
part2('day1.txt')
