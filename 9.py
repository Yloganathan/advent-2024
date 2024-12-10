import re

input = []
with open("9.txt") as file:
    input = file.read()

def get_file_shape_from_disk_info(input):
    file_id = 0
    file_size_first_pass = []
    free_spaces = []
    for i in range(len(input)):
        if(i% 2): 
            free_spaces.append((len(file_size_first_pass), int(input[i])))
            for j in range(int(input[i])):
                file_size_first_pass.append('.') 
            
        else: # even number is size of file
            for j in range(int(input[i])):
                file_size_first_pass.append(file_id)
            file_id +=1
    return file_size_first_pass, file_id -1, free_spaces

def part1():
    total = 0
    file_size_first_pass = get_file_shape_from_disk_info(input)

    while(True):
        try:
            index = file_size_first_pass.index('.')
            last_value = file_size_first_pass.pop()
            file_size_first_pass[index]=last_value
        except ValueError:
            break

    for index, value in enumerate(file_size_first_pass):
        total += (index * value )

    return total


print(part1())