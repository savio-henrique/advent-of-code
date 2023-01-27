input = open('input.txt','r')
input = input.read()

floor = 0
#Part 1#
position = None
for i in range(len(input)):
    if input[i] == '(':
        floor +=1
    elif input[i] == ')':
        floor -=1
#Part 1#
#Part 2#
    if floor == -1:
        position = i+1 if position == None else position
# Part 2#
print(floor) #Part 1 Solution
print(position) #Part 2 Solution