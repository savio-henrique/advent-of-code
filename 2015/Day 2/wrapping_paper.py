boxes = open('input.txt').read().split('\n')
sum_paper = 0
sum_ribbon = 0
#Part 1#
for box in boxes:
    length,width,height = list(map(int, box.split('x')))
    side1 = length * width
    side2 = width * height
    side3 = length * height
    total_box = 2 * (side1+side2+side3) + min(side1,side2,side3)
    sum_paper += total_box
#Part 1#
#Part 2#
    if height == max(height,width,length):
        total_ribbon = 2 * (length + width)
    elif width == max(height,width,length):
        total_ribbon = 2 * (height + length)
    else:
        total_ribbon = 2 * (height + width)
    total_ribbon += length * width * height
    sum_ribbon += total_ribbon
#Part 2#
print(sum_paper) #Part 1 Solution
print(sum_ribbon) #Part 2 Solution