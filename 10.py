

def find_incremental_path(grid, my_position, current_value, grid_length, grid_height):
    step = int(grid[my_position[0]][my_position[1]])
    if current_value == 8 and step == 9:
        return 1
    else:
        left = (my_position[0],my_position[1] - 1) if my_position[1]-1 >=0 else None
        right = (my_position[0],my_position[1] + 1) if my_position[1]+1 < grid_length else None
        top = (my_position[0] - 1,my_position[1]) if my_position[0]-1 >=0 else None
        bottom = (my_position[0] + 1,my_position[1]) if my_position[0]+1 < grid_height else None

    path_count = 0
    for neighbor in [left, right, top, bottom]:
        if neighbor and int(grid[neighbor[0]][neighbor[1]]) == step + 1:
                path_count += find_incremental_path(grid, neighbor, step, grid_length, grid_height)
    return path_count


with open("10.txt") as file:
    total = 0
    input = [list(line.rstrip()) for line in file]
    grid_height  = len(input) 
    grid_length = 0
    for i in range(len(input)):
        grid_length = max(grid_length, len(input[i]))
        for j in range(len(input[i])):
            if input[i][j] == '0':
                reached_9s = []
                total += find_incremental_path(input, (i,j), 0, grid_length, grid_height)
    print(total)