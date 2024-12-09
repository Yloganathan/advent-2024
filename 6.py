grid_length = 0
grid_height = 0
starting_position = None
next_direction ={
    "^":">",
    ">":"v",
    "v":"<",
    "<":"^"
}

with open("6.txt") as file:
    input = [list(line.rstrip()) for line in file]
    grid_height  = len(input) 
    
    for i in range(len(input)):
        grid_length = max(grid_length, len(input[i]))
        for j in range(len(input[i])):
            if input[i][j] == '^':
                starting_position = { "x":i, "y":j}

def get_gaurd_path():
    gaurd_position = starting_position.copy()
    gaurd_direction = '^'
    gaurd_path = set()
    gaurd_path_dir = set()
    stuck_in_loop = False

    while (gaurd_position["x"] >= 0 and gaurd_position["x"] < grid_height and gaurd_position["y"] >=0 and gaurd_position["y"] < grid_length):
        new_x = gaurd_position["x"]
        new_y = gaurd_position["y"]

        match gaurd_direction:
            case '^':
                new_x -=1
            case '>':
                new_y +=1
            case 'v':
                new_x +=1
            case '<':
                new_y -=1

        if(new_x < grid_height and new_y < grid_length):
            if(input[new_x][new_y] == '#'):
                gaurd_direction = next_direction[gaurd_direction]
                # print(f'changing direction to {gaurd_direction} at {new_x}, {new_y}')
                continue
            else:
                if((new_x, new_y, gaurd_direction) in gaurd_path_dir):
                    # print(gaurd_path_dir)
                    # print(f'finding {gaurd_position}, {gaurd_direction}')
                    return gaurd_path, True
                gaurd_path_dir.add((new_x, new_y, gaurd_direction))
                gaurd_path.add((new_x, new_y))
                gaurd_position["x"] = new_x
                gaurd_position["y"] = new_y
        else: 
            break

    return gaurd_path, stuck_in_loop

def part1():
    path, loop = get_gaurd_path()
    print(loop)
    return len(path)

def part2():
    total = 0
    path, loop = get_gaurd_path()
    input_c = input.copy()
    for item in path:
       input_c[item[0]][item[1]] = '#'
       ndpath, loop = get_gaurd_path()
       input_c[item[0]][item[1]] = '.'
       if(loop):
           total +=1

    return total

print(part1())
print(part2())