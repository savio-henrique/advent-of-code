input = open("input.txt").read()

#Part 1#
x = 0
y = 0
#Part 1#
#Part 2#
pos_claus = (x,y)
pos_robot = (x,y)
#Part 2#
visited_houses = list()
for i in range(len(input)):
# Part 1#
    if (x,y) not in visited_houses:
        visited_houses.append((x, y))
    if input[i] == "^":
        y+=1
    elif input[i] =="v":
        y-=1
    elif input[i] =="<":
        x-=1
    elif input[i] ==">":
        x+=1
#Part 1#
#Part 2#
    if i % 2:
        temp = (x, y)
        print(temp)
        x, y = pos_robot
        pos_claus = temp
    else:
        temp = (x, y)
        print(temp)
        x, y = pos_claus
        pos_robot = temp
#Part 2#

print(len(visited_houses))