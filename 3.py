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


#duh! took so long to learn that each line cannot be processed by itself, its all one line
def part2():
    total =0
    parts  = re.split(r'(don\'t\(\)|do\(\))', open("3.txt").read())
    skipTillDo = False
    for part in parts:
        if part == 'don\'t()':
            skipTillDo = True
        elif part =='do()':
            skipTillDo = False
        else:
            if(skipTillDo):
                continue
            matches = re.findall(r'mul\((\d+),(\d+)\)', part)
            for match in matches:
                result = int(match[0]) * int(match[1])
                total += result
    return total

print(part2())

