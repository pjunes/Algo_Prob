# there is grid size n x m.
# each square should be colored black or white.
# some colors of squares are already decided.
# program make judgement about the grid could be colored with all adjacent squres different color.

# sample_input
# 3
# 3 6
# #.????
# ?#????
# ???.??
# 1 5
# ##????
# 3 3
# .#.
# #?#
# .#.

# sample_output
# #1 possible
# #2 impossible
# #3 possible

import sys

sys.stdin = open("painting grid\painting_grid_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    impos_flag = 0
    out_dict = {0:"possible", 1:"impossible"}
    n, m = map(int, input().split())
    print(f"#{test_case}")

    # method 1.
    # whole grid
    # index i, index j
    # i + j == even vs odd

    # method 2. -- my choice
    # even grid / odd grid

    grid_odd = list()
    grid_even = list()

    for i in range(n):
        temp = input()
        for j, v in enumerate(temp):
            if (i + j) % 2 == 0:
                grid_even.append(v)
            else:
                grid_odd.append(v)

    print(grid_even)
    print(grid_odd)
    
    # if "#" in grid_even:
    #     if "#" in grid_odd:
    #         impos_flag = 1
    #     elif "." in grid_even:
    #         impos_flag = 1
    # elif "." in grid_even:
    #     if "." in grid_odd:
    #         impos_flag = 1
    #     elif "#" in grid_even:
    #         impos_flag = 1
    # elif "#" in grid_odd:
    #     if "#" in grid_even:
    #         impos_flag = 1
    #     elif "." in grid_odd:
    #         impos_flag = 1
    # elif "." in grid_odd:
    #     if "." in grid_even:
    #         impos_flag = 1
    #     elif "#" in grid_odd:
    #         impos_flag = 1

    if "#" in grid_even:
        if "#" in grid_odd:
            impos_flag = 1
        elif "." in grid_even:
            impos_flag = 1
    elif "." in grid_even:
        if "." in grid_odd:
            impos_flag = 1
    elif "#" in grid_odd:
        if "." in grid_odd:
            impos_flag = 1
    
    print(f"{out_dict[impos_flag]}")
