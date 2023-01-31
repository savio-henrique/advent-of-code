import hashlib as hl

#Part 1#
input = "yzbqklnj"
num = 1
hashcode = hl.md5(f"{input}{num}".encode()).hexdigest()

# while hashcode[:5] != "00000":
#     num += 1
#     hashcode = hl.md5(f"{input}{num}".encode()).hexdigest()
#Part 1#
#Part 2#
while hashcode[:6] != "000000":
    num += 1
    hashcode = hl.md5(f"{input}{num}".encode()).hexdigest()
#Part 2#
print(num) #Part 1 and 2 Solution

#Part 1 Solution: 282749#
#Part 2 Solution: 9962624#
