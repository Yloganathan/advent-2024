import re


def part1():
    total =0
    with open("3.txt") as file:
        for line in file:
            matches = re.findall(r'mul\((\d+),(\d+)\)', line)
            for match in matches:
                result = int(match[0]) * int(match[1])
                total += result
    return total

print(part1())



def part2():
    total =0
    with open("3.txt") as file:
        for line in file:
            # print(line)
            matches = re.findall(r'mul\((\d+),(\d+)\)', line)
            for match in matches:
                result = int(match[0]) * int(match[1])
                total += result
    return total

print(part1())

