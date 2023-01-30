boxes = open('input.txt').read().split('\n')
print(boxes)
total_sum = 0
for box in boxes:
    length,width,height = list(map(int, box.split('x')))
    side1 = length * width
    side2 = width * height
    side3 = length * height
    total_box = 2 * (side1+side2+side3) + min(side1,side2,side3)
    total_sum += total_box

print(total_sum)