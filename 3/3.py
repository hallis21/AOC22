# with open("inp.txt", "r") as f:
#     sum = 0
#     # scores is a dict that has all lower case letters from z to z, with a score from 1 to 26
#     for l in f:
#         first_half = set(l[:len(l)//2])
#         second_half = set(l[len(l)//2:])
#         res = first_half.intersection(second_half)
#         sum += scores[res.pop()]
        
#     print(sum)

# PART 2
# scores = {chr(i): i - 96 for i in range(97, 123)}
# scores2 = {chr(i): i - 38 for i in range(65, 91)}
# scores = z = {**{chr(i): i - 96 for i in range(97, 123)}, **{chr(i): i - 38 for i in range(65, 91)}}
# result = 0
# with open("inp.txt", "r") as f:
    # Read three lines at once
    # for l1, l2, l3 in zip(*[f]*3):
    #     # Split the lines into sets
    #     l1 = set(l1.strip())
    #     l2 = set(l2.strip())
    #     l3 = set(l3.strip())
    #     # Find the intersection of the three sets
    #     res = l1.intersection(l2, l3)
    #     # Print the result
    #     result += scores[res.pop()]
    # print(result)

# Part 2 one liner
print(sum([{**{chr(i): i - 96 for i in range(97, 123)}, **{chr(i): i - 38 for i in range(65, 91)}}[set(x.strip()).intersection(set(y), set(z)).pop()] for x,y,z in zip(*[open("inp.txt")]*3)]))
