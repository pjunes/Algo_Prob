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

global counter

def merge_ascent_inplace(target_ar, start_1, len_1, start_2, len_2):
    ### input explanation ###
    # target_ar : ar to sort
    # start_1 : start of fisrt ar
    # len_1 : length of first ar
    # start_2 : start of second ar
    # len_2 : length fo second ar
    ### input exlpanation end ###

    # end_1 : end of first ar
    # end_2 : end of second_ar

    # first ar and second ar are connected.
    # so, {end_1} should be {start_2 - 1}
    
    global counter

    end_1 = start_1 + len_1 - 1  
    end_2 = start_2 + len_2 - 1

    # result values
    start_result = start_1 # not necessary, {start_result} == {start_1}
    len_result = len_1 + len_2

    # if already sorted -> end quickly
    if target_ar[end_1] <= target_ar[start_2]:
        return start_result, len_result

    # i : index for first ar. also mean elements sorted before i. i goes from start_1 to end_2
    # j : index for second ar. j goes from start_2 to end_2
    i = start_1  
    j = start_2  

    # main merge inplace sorting algorithm
    # while (i <= end_1) & (j <= end_2):# while (i < start_1 + len_1) & (j < start_2 + len_2):
    while (i <= end_2):
        if (j > end_2) | (i == j):
            break

        if target_ar[i] <= target_ar[j]:
            i += 1
        else:  # target_ar[i] > target_ar[j]:  # inversion
            target_ar.insert(i, target_ar.pop(j))
            counter += 1
            i += 1
            j += 1

    return start_result, len_result

def merge_sort_ascent(target_ar):
    # algorithm get 2 parts, and merge each parts into a part.
    # part means sorted subset
    # algorithm proceeds until the subset becomes a whole.
    
    queue = list()
    # element type : list
    # element overview : [index, length]
    # index : start of element
    # length : length of element
    # elements mean subset of target_ar

    # queue have information of sorted subset.
    # algorithm merges the subsets in the queue to make one.

    # merge sort starts from 1 length elements.
    for i in range(len(target_ar)):
        queue.append([i, 1])

    while(True):
        # Must have at least 2 subsets to merge.
        if len(queue) > 1: 
            # queue[n][0] means index of nth subset.
            # This condition exists to confirm that subsets pair properly.
            # When there is an odd number of subsets to be merged, one subset left.
            # The remaining subset must be sent back to the back of the queue
            if queue[0][0] < queue[1][0]: 
                target1 = queue.pop(0) # used elements are removed
                target2 = queue.pop(0)
                # def merge_ascent_inplace(target_ar, start_1, len_1, start_2, len_2)
                # make two subsets into one sorted subset
                queue.append(list(merge_ascent_inplace(target_ar, target1[0], target1[1], target2[0], target2[1])))
            else:
                queue.append(queue.pop(0)) # re: The remaining subset must be sent back to the back of the queue
        else: # len(queue) <= 1
            # queue[0] == (0,len(target_ar)):
            # one last element should be [0, len(target_ar)]
            break

if __name__ == "__main__":
    sys.stdin = open("counting inversions of the duplicated sequence\input_cnt_inv_dup_seq.txt", "r")
    T = int(input())

    for i in range(1, T + 1):
        counter = 0
        _, iter_num = map(int, input().split())
        trg_ar = list(input().split()) * iter_num
        merge_sort_ascent(trg_ar)

        print(f"#{i} {counter}")