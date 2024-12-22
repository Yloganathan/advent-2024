from functools import lru_cache
import re
parts  = [int(p) for p in re.split(r'\s+', open("11.txt").read())]

print(parts)

@lru_cache
def blink_once(number):
    output = []
    str_num = str(abs(number))
    if number == 0:
        output.append(1)
    elif (len(str_num) % 2) == 0:
        mid = int(len(str_num)/2)
        output.append(int(str_num[:mid]))
        output.append(int(str_num[mid:]))
    else:
        output.append(number * 2024)
    return output

@lru_cache(None)
def blink(number, max_blink):
    if(max_blink == 1):
        return len(blink_once(number))
    return sum([blink(out_item, max_blink - 1) for out_item in blink_once(number)])


def part1(parts):
    count = 0
    for part in parts:
        count += blink(part, 75)
   
    print (count)

part1(parts)