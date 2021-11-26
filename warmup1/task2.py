
# puzzle https://adventofcode.com/2019/day/4
# (link przypięty na kanale o AOC)
#
import numpy as np
in_a = 357253
in_b = 892942

solutions = 0

for i in range(in_a, in_b):
    digit_list = np.array([0]*10)
    prev = 0
    found_not_incr = False
    phrase = str(i)
    repeating = False
    # print(phrase)
    for j, d in enumerate(phrase):
        # print(j,d)
        if j!=0 and int(phrase[j-1]) > int(d):
            found_not_incr = True
            break
        if j != 0 and phrase[j-1] == d:
            repeating = True
            if digit_list[int(d)]==0:
                digit_list[int(d)] +=1
            digit_list[int(d)] += 1
    if repeating and not found_not_incr and np.any(digit_list==2):
        solutions +=1
        print(phrase)
