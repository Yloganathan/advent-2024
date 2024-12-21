import re
parts  = [int(p) for p in re.split(r'\s+', open("11.txt").read())]

print(parts)

def blink_once(input):
    output = []
    for number in input:
        str_num = str(abs(number))
        if number == 0:
            output.append(1)
        elif (len(str_num) % 2) == 0:
            mid = int(len(str_num)/2)
            output.append(int(str_num[:mid]))
            output.append(int(str_num[mid:]))
        else:
            output.append(number * 2024)
    # print(output)
    return output

def blink(input, max_blink):
    output = None
    while max_blink > 0:
        output = blink_once(input)
        input = output
        max_blink -= 1
    return output

def part1(parts):
    output = blink(parts, 25)
    print (len(output))

part1(parts)