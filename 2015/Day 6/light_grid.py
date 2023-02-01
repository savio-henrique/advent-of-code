instructions = open("input.txt").read().split("\n")

#Part 1#
def part1():
    grid = [[False for x in range(1000)] for x in range(1000)]
    def toggle(grid, start: tuple, finish: tuple):
        for line in range(start[0] - 1, finish[0]):
            for column in range(start[1] - 1, finish[1]):
                if grid[line][column] == True:
                    grid[line][column] = False
                elif grid[line]:
                    grid[line][column] = True

    def turnOn(grid, start: tuple, finish: tuple):
        for line in range(start[0] - 1, finish[0]):
            for column in range(start[1] - 1, finish[1]):
                if not grid[line][column]:
                    grid[line][column] = True

    def turnOff(grid, start: tuple, finish: tuple):
        for line in range(start[0] - 1, finish[0]):
            for column in range(start[1] - 1, finish[1]):
                if grid[line][column]:
                    grid[line][column] = False

    def countLights(grid):
        counter = 0
        for line in grid:
            for column in line:
                if column:
                    counter += 1
        return counter

    for line in instructions:
        splitted = line.split(' ')
        splitted.pop(-2)
        start = tuple(map(int,splitted[-2].split(",")))
        finish = tuple(map(int,splitted[-1].split(",")))
        if "turn on" in line:
            turnOn(grid,start,finish)
        elif "turn off" in line:
            turnOff(grid, start, finish)
        elif "toggle" in line:
            toggle(grid, start, finish)

    print("The total of turned on lights is:",countLights(grid),"lights.") #Part 1 Solution

part1()
# Part 1#
# Part 2#
def part2():
    grid = [[0 for x in range(1000)] for x in range(1000)]
    def toggle(grid, start: tuple, finish: tuple):
        for line in range(start[0] - 1, finish[0]):
            for column in range(start[1] - 1, finish[1]):
                grid[line][column] += 2

    def turnOn(grid, start: tuple, finish: tuple):
        for line in range(start[0] - 1, finish[0]):
            for column in range(start[1] - 1, finish[1]):
                grid[line][column] += 1

    def turnOff(grid, start: tuple, finish: tuple):
        for line in range(start[0] - 1, finish[0]):
            for column in range(start[1] - 1, finish[1]):
                if grid[line][column] > 0:
                    grid[line][column] -= 1

    def countBrightness(grid):
        counter = 0
        for line in grid:
            for column in line:
                counter += column
        return counter

    for line in instructions:
        splitted = line.split(' ')
        splitted.pop(-2)
        start = tuple(map(int,splitted[-2].split(",")))
        finish = tuple(map(int,splitted[-1].split(",")))
        if "turn on" in line:
            turnOn(grid,start,finish)
        elif "turn off" in line:
            turnOff(grid, start, finish)
        elif "toggle" in line:
            toggle(grid, start, finish)

    print('The total brightness of the grid is:',countBrightness(grid),".") #Part 1 Solution

part2()
# Part 2#