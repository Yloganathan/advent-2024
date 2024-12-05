import re


def transpose(lines):    
    transposed = zip(*lines)
    return ["".join(row) for row in transposed]

def diagonal_transpose(strings):
    result = diagonal_transpose2(strings, 'LTOR')
    result.extend(diagonal_transpose2(strings, 'RTOL'))
    return result

def diagonal_transpose2(strings, direction):
    max_length = len(strings)
    result = []
    if(direction == 'LTOR'):
        for xaxis in range(max_length):
            value = ''
            i = xaxis
            j = 0
            while i >=0:
                value += strings[i][j]
                i -=1
                j +=1
            result.append(value)
        for xaxis in range(1, max_length):
            value = ''
            i = xaxis
            j = max_length - 1

            while i < max_length:
                value += strings[i][j]
                i +=1
                j -=1
            result.append(value)
    else:
        for yaxis in range(max_length):
            value = ''
            i = 0
            j = yaxis
            while j < max_length:
                value += strings[i][j]
                i +=1
                j +=1
            result.append(value)
        for xaxis in range(1, max_length):
            value = ''
            i = xaxis
            j = 0
            while i < max_length:
                value += strings[i][j]
                i +=1
                j +=1
            result.append(value)
    return result

def part1():
    total = 0
    with open("4.txt") as file:
        input = [line for line in file]
        output = input.copy()
        output.extend(transpose(input))
        output.extend(diagonal_transpose(input))
        for line in output:
            matches = re.findall("(?=(XMAS|SAMX))", line)
            total += len(matches)
    return total

def part2():
    total = 0
    with open("4.txt") as file:
       input = [line for line in file]
       for i in range(len(input)):
        if(i != 0 and i != len(input)-1):
            matches  = re.finditer(r'A', input[i])
            for match in matches:
                previous = input[i-1]
                next = input[i+1]
                positionOfA = match.start()
                if(positionOfA == len(input[i])-1 ): #if it is last letter, continue
                    continue
                topleft = previous[match.start() - 1]
                topright = previous[match.start() + 1]
                bottomleft = next[match.start() - 1]
                bottomright = next[match.start() + 1] if match.start() + 1 < len(next) else None
                
                if(((topleft and topleft == 'M' and bottomright and bottomright == 'S') or 
                (topleft and topleft == 'S' and bottomright and bottomright == 'M'))
                and
                ((bottomleft and bottomleft == 'M' and topright and topright == 'S') or 
                (bottomleft and bottomleft == 'S' and topright and topright == 'M'))):
                    total +=1
    return total



print(part1())
print(part2())



