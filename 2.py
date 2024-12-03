import re


def is_valid(matches):
    if all((matches[i] < matches[i + 1] and (matches[i+1] - matches[i]) > 0 and (matches[i+1] - matches[i]) < 4) for i in range(len(matches) - 1)):
      return True 
    elif all((matches[i] > matches[i + 1] and (matches[i] - matches[i+1]) > 0 and (matches[i] - matches[i+1]) < 4) for i in range(len(matches) - 1)):
      return True
    else:
       return False    

def part1():
   total=0
   with open("2.txt") as file:
      for line in file:
         matches = list(re.findall(r'\d+', line))
         matches = [int(num) for num in matches]
         if(is_valid(matches)):
            total +=1   
   return total
  
print(part1())


def part2():
   total = 0
   with open("2.txt") as file:
      for line in file:
         matches = list(re.findall(r'\d+', line))
         matches = [int(num) for num in matches]

         if(is_valid(matches)):
            total+=1
         else:  
            for i in range(len(matches)):
               matchminusi = matches[:i] + matches[i+1:]
               if(is_valid(matchminusi)):
                  total +=1
                  break
   return total
        
print(part2())
