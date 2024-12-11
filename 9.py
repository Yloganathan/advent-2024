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
    file_size_first_pass, _, _ = get_file_shape_from_disk_info(input)

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

def get_free_spaces(memory_array):
    consecutive_free_space = []
    start_index = None
    for i in range(len(memory_array)):
        if memory_array[i] == '.':
            if start_index is None:
                start_index = i
        else:
            if start_index is not None:
                length = i - start_index
                consecutive_free_space.append((start_index, length))
                start_index = None
    if start_index is not None:
        consecutive_free_space.append((start_index, len(memory_array) - start_index))
    return consecutive_free_space

def part2():
    total = 0
    file_size_first_pass, maxFileId, free_spaces = get_file_shape_from_disk_info(input)

    while(maxFileId >0):
        size_of_file = file_size_first_pass.count(maxFileId)
        occurance = file_size_first_pass.index(maxFileId)
        for i in range(len(free_spaces)):
            if(free_spaces[i][1] >= size_of_file and free_spaces[i][0] < occurance):
                file_size_first_pass = [ '.' if char == maxFileId  else char for char in file_size_first_pass]
                for j in range(size_of_file):
                    file_size_first_pass[free_spaces[i][0] + j] = maxFileId
                # re-eval free space
                free_spaces = get_free_spaces(file_size_first_pass)
                break
        maxFileId -=1

    for index, value in enumerate(file_size_first_pass):
        total += ((index * value ) if value != '.' else 0)

    return total

# print(part1())
print(part2())