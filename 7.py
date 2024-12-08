import re

def is_valid(value, numbers):
    if(len(numbers) == 2):
        if (value == numbers[0] * numbers[1]) or (value == numbers[0] + numbers[1]) or (value == int(f"{numbers[0]}{numbers[1]}")):
            return True
        return False
    elif(len(numbers) > 2):
        mul = numbers[0] * numbers[1]
        add = numbers[0] + numbers[1]
        combined = int(f"{numbers[0]}{numbers[1]}")
        list1 = [add]
        list2 = [mul]
        list3 = [combined]
        for i in range(2, len(numbers)):
            list1.append(numbers[i])
            list2.append(numbers[i])
            list3.append(numbers[i])
        return (is_valid(value, list1) or is_valid(value, list2) or is_valid(value, list3))
        
    else:
        return False    

def part2():
    with open("7.txt") as file:
        input = [(line.rstrip()) for line in file]
        total = 0
        for calc in input:
            value = int(calc.split(':')[0])
            numbers =  [int(x) for x in calc.split(':')[1].split()]
            if is_valid(value, numbers):
                total +=value
        return total

print(part2())