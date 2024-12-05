from collections import defaultdict
from math import floor
import re

parts  = re.split(r'\n\n', open("5.txt").read())
rules = parts[0]
input = parts[1]
rule_dict = defaultdict(list)
for rule in re.split(r'\n', rules):
    rule_part = rule.split('|')
    rule_dict[rule_part[0]].append(rule_part[1])

def do_they_pass(line_items):
    clear = True
    for i in range(0, len(line_items)):
        cannot_be_ahead = rule_dict.get(line_items[i])
        if(cannot_be_ahead and any(num in line_items and line_items.index(num) < i for num in cannot_be_ahead)):
            print('nope')
            clear = False
            break
        else:
            clear = True
    return clear

def modify_to_pass(line_items, wasModified = False):
    for i in range(0, len(line_items)):
        cannot_be_ahead = rule_dict.get(line_items[i])
        if cannot_be_ahead:
            for num in cannot_be_ahead:
                if num in line_items and line_items.index(num) < i:
                    del line_items[line_items.index(num)]
                    line_items.append(num)
                    return modify_to_pass(line_items, True)
     
    return wasModified

def part1():
    total = 0
    for line in re.split(r'\n', input):
        line_items = line.split(',')
        if do_they_pass(line_items):
            middle = floor(len(line_items)/2)
            total += int(line_items[middle]) 
            
    return total

def part2():
    total = 0
    for line in re.split(r'\n', input):
        line_items = line.split(',')
        if modify_to_pass(line_items):
            middle = floor(len(line_items)/2)
            total += int(line_items[middle]) 
            
    return total

print(part1())
print(part2())
