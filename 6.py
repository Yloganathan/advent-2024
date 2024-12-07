import re

def part1():
    gaurd_path = []
    grid_length = 0
    grid_height = 0
    gaurd_position = None
    gaurd_direction = '^'
    next_direction ={
        "^":">",
        ">":"v",
        "v":"<",
        "<":"^"
    }

    with open("6.txt") as file:
        input = [line for line in file]
        grid_height  = len(input) 
        
        for i in range(len(input)):
            grid_length = max(grid_length, len(input[i]))
            for j in range(len(input[i])):
                if input[i][j] == '^':
                    gaurd_position = { "x":i, "y":j}

        while (gaurd_position["x"] < grid_height -1 and gaurd_position["y"] < grid_length -1):
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
                    gaurd_path.append((new_x +1, new_y+1))
                    gaurd_position["x"] = new_x
                    gaurd_position["y"] = new_y

    return len(set(gaurd_path))


def part2():
    gaurd_path = []
    grid_length = 0
    grid_height = 0
    gaurd_position = None
    gaurd_direction = '^'
    next_direction ={
        "^":">",
        ">":"v",
        "v":"<",
        "<":"^"
    }

    with open("6.txt") as file:
        input = [line for line in file]
        grid_height  = len(input) 
        
        for i in range(len(input)):
            grid_length = max(grid_length, len(input[i]))
            for j in range(len(input[i])):
                if input[i][j] == '^':
                    gaurd_position = { "x":i, "y":j}
                    print(gaurd_position)

        while (gaurd_position["x"] < grid_height -1 and gaurd_position["y"] < grid_length -1):
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
                    gaurd_path.append((new_x +1, new_y+1))
                    gaurd_position["x"] = new_x
                    gaurd_position["y"] = new_y

    return len(set(gaurd_path))

print(part1())