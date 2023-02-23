input = open("input.txt").read().split("\n")

bitstring = 0b0000000000000000

operations = {}
for i in input:
    split = i.split("->")
    print(split)
    for p in range(len(split)-1):
        if "AND" in split:
            index = split.index("AND")
            if split[index - 1] in values and split[index + 1] in values:
                value = values[split[index - 1]] & values[split[index + 1]]
                values[split[split.index("->") + 1]] = value
        elif "NOT" in split:
            index = split.index("NOT")
            if split[index+1] in values:
                value = values[split[index+1]] ^ 65535
                values[split[split.index("->") + 1]] = value
        elif "OR" in split:
            index = split.index("OR")
            if split[index - 1] in values and split[index + 1] in values:
                value = values[split[index - 1]] | values[split[index + 1]]
                values[split[split.index("->") + 1]] = value
        elif "RSHIFT" in split:
            index = split.index("RSHIFT")
            if split[index - 1] in values:
                print(values[split[index - 1]])
                value = values[split[index - 1]] >> int(split[index + 1])
                print(value)
                values[split[split.index("->") + 1]] = value
        elif "LSHIFT" in split:
            index = split.index("LSHIFT")
            if split[index - 1] in values:
                print(values[split[index - 1]])
                value = values[split[index - 1]] << int(split[index + 1])
                print(value)
                values[split[split.index("->") + 1]] = value
        else:
            if split[0] in values:
                value = values[split[0]]
            else:
                value = int(split[0]) if split[0].isdigit() else split[0]

            values[split[split.index("->") + 1]] = value

print(values)
for i in sorted(values.keys()):
    print(f"{i}:",values[i])