left_side = []
right_side = []

# read "13.in"
lines = open("13.in").readlines()

def parse_line(line, first=True):
    ret = []
    i = 0
    while True:
        c = line[i]
        i += 1
        if c == ',': continue
        if c == '[':
            n, ii = parse_line(line[i:], first=False)
            ret.append(n)
            i += ii
        elif c == ']':
            return ret, i
        else:
            # Get int starting at i            
            ret.append(int(line[i-1:].split(",")[0].replace("]", "")))
        if i >= len(line): break
    if first:
        return ret[0]
    return ret, i



# Read two and two lines, and skip the thrird
for i in range(0, len(lines), 3):
    left_side.append(parse_line(lines[i].strip()))
    right_side.append(parse_line(lines[i+1].strip()))


def compare(left, right):

    if isinstance(left, int) and isinstance(right, int):
        if left == right:
            return 0
        elif left > right:
            return -1
        else:
            return 1
    # print(left, right)
    if isinstance(left, list) and isinstance(right, list):
        for i in range(len(left)):
            if i >= len(right):
                return -1
            ret = compare(left[i], right[i])
            if ret != 0:
                return ret
        if len(left) < len(right):
            return 1
    if isinstance(left, list) and isinstance(right, int):
        return compare(left, [right])
    if isinstance(left, int) and isinstance(right, list):
        return compare([left], right)
    return 0

all_lines = right_side + left_side
all_lines.remove([])
all_lines.insert(0, [])
all_lines.append([[2]])
all_lines.append([[6]])
sorted_lines = []
# Sort all elements in all lines by using the compare function
while len(all_lines) > 0:
    min_line = all_lines[0]
    min_index = 0
    for i in range(1, len(all_lines)):
        if compare(all_lines[i], min_line) < 0:
            min_line = all_lines[i]
            min_index = i
    sorted_lines.append(min_line)
    # checj if min line is [[2]]
    all_lines.pop(min_index)
sorted_lines.reverse()
print("\n".join([str(x) for x in sorted_lines]))

# Find [[2]] in the list
for i in range(len(sorted_lines)):
    if sorted_lines[i] == [[2]]:
        print(i+1)
    if sorted_lines[i] == [[6]]:
        print(i+1)