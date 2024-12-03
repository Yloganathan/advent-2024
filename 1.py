import re



left = []
right = []
with open("1.txt") as file:
    for line in file:
        matches = list(re.findall(r'\d+', line))
        left.append(int(matches[0]))
        right.append(int(matches[1]))


def part1(): 
   total=0
   left.sort()
   right.sort()
   for i in range(len(left)):
      total = total + abs(left[i] - right[i])
   return total

def part2():
   total = 0
   for entry in left:
      count =  right.count(entry)
      total = total + (count * entry)
   return total

print(part1())
print(part2())
