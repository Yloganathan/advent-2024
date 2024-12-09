import re

def is_valid(value, numbers, part2):
    if(len(numbers) == 2):
        if (value == numbers[0] * numbers[1]) or (value == numbers[0] + numbers[1]):
            return True
        if part2:
            return (value == int(f"{numbers[0]}{numbers[1]}"))
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
        if(part2):  
            return (is_valid(value, list1, True) or is_valid(value, list2, True) or is_valid(value, list3, True))
        return (is_valid(value, list1, False) or is_valid(value, list2, False))
        
    else:
        return False    

def part(part2):
    with open("7.txt") as file:
        input = [(line.rstrip()) for line in file]
        total = 0
        for calc in input:
            value = int(calc.split(':')[0])
            numbers =  [int(x) for x in calc.split(':')[1].split()]
            if is_valid(value, numbers, part2):
                total +=value
        return total

print(part(False))
print(part(True))