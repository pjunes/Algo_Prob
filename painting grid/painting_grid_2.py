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
    print(f"#{test_case}", end=" ")

    even_dot_flag = 0
    even_hash_flag = 0
    odd_dot_flag = 0
    odd_hash_flag = 0
    flag_sum = 0

    for i in range(n):
        temp = input()
        for j, v in enumerate(temp):
            if v == "?":
                continue

            if (i + j) % 2 == 0: # even
                if v == ".":
                    even_dot_flag = 1
                # elif v == "#":
                else:
                    even_hash_flag = 1
            else: # odd
                if v == ".":
                    odd_dot_flag = 1
                # elif v == "#":
                else:
                    odd_hash_flag = 1

            if even_hash_flag:
                if odd_hash_flag:
                    impos_flag = 1
                elif even_dot_flag:
                    impos_flag = 1
            elif even_dot_flag:
                if odd_dot_flag:
                    impos_flag = 1
            elif odd_hash_flag:
                if odd_dot_flag:
                    impos_flag = 1

            if impos_flag:
                break
    
    print(f"{out_dict[impos_flag]}")
