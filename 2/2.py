# with open("inp.txt", "r") as f:
    # results = 0
    # score_table = {"A":{"A":4, "B":8, "C":3}, "B":{"A":1, "B":5, "C":9}, "C":{"A":7, "B":2, "C":6}}
    # for line in f:
    #     bits = line.split()
    #     # Part 1
    #     translate = {"X": "A", "Y": "B", "Z": "C"}
    #     bits[1] = translate[bits[1]]
    #     results += score_table[bits[0]][bits[1]]

# 'On' soulution
res = 0
res_table = {"A":{"X":3,"Y":4, "Z":8}, "B":{"X":1,"Y":5,"Z":9}, "C":{"X":2,"Y":6,"Z":7}}
[res := res +res_table[x[0]][x[2]] for x in open("inp.txt", "r").readlines()]
print(res)
