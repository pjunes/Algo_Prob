# prob

# There are sequences A0, A1, ⋯, AN-1 of length N.
# Consider the sequences B0, B1, ⋯, and BNK-1 of length N*K in which the sequence A is copied K times.
# for all 0 ≤ i ≤ N - 1 and 0 ≤ k ≤ K - 1, B(k⋅N+i) = A(i)
# Write a program to find the remainder of dividing the number of inversions in sequence B by 109 + 7.

# Here, the inversion number means the number of pairs of two integers (i, j) where 0 ≤ i < j ≤ NK – 1 and Bi > Bj.
# In the first line, two integers N, K (1 ≤ N ≤ 2000, 1 ≤ K ≤ 109) are given with a space between them.
# In the second line, N integers between 1 and 2000, A0, A1, ⋯, AN-1, are given with one space in between.
# For each test case, the remainder of dividing the number of inversions of the sequence B defined in the problem by 109 + 7 is output.

# sample_input

# 3
# 4 1
# 1 2 3 4
# 4 2
# 1 5 4 1
# 3 141592653
# 5 8 9

# expected output

# #1 0
# #2 11
# #3 652469608

import sys

if __name__ == "__main__":
    sys.stdin = open("counting inversions of the duplicated sequence\input_cnt_inv_dup_seq.txt", "r")
    T = int(input())

    for t in range(1, T + 1):
        # inversion_cnt : type int, counter for number of inversion.
        inversion_cnt = 0
        # repeated_cnt : type int, counter for number of repeated number.
        repeated_cnt = 0

        # raw_len : type int, a length of unit array
        # dup_num : type int, a number of the unit array is repeated
        raw_len, dup_num = map(int, input().split())
        # raw_ar : type list[int], a unit array.
        raw_ar = list(map(int, input().split()))

        # print(f"case : {raw_len} {dup_num}\n{raw_ar}")

        if raw_len == 1:
            print(f"#{t} {inversion_cnt}") # inversion_cnt == 0
            continue

        # count inversion of unit array
        # using algorithms inspired by bubble sort
        for i in range(raw_len-1):
            for j in range(i+1, raw_len):
                if raw_ar[i] > raw_ar[j]:
                    inversion_cnt += 1
                # elif raw_ar[i] == raw_ar[j]:
                #     repeated_cnt += 1

        if dup_num == 1:
            print(f"#{t} {inversion_cnt}")
            continue

        # count repeated number of unit
        unit_dict = dict()
        for v in raw_ar:
            if v in unit_dict:
                unit_dict[v] += 1
            else:
                unit_dict[v] = 0
        repeated_cnt = sum(unit_dict.values())

        # print(f"unit array inversion_cnt : {inversion_cnt}")
        # print(f"unit array repeated_cnt : {repeated_cnt}")

        

        inversion_cnt *= dup_num

        inversion_cnt += int(raw_len*(raw_len - 1)/2 - repeated_cnt) * int(dup_num*(dup_num - 1)/2)
        
        inversion_cnt %= 10**9 + 7

        print(f"#{t} {inversion_cnt}")