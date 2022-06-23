import sys

sys.stdin = open("one dimensional garden\one_D_garden_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, D = map(int, input().split())

    sprayer_range = 2*D + 1

    if N % sprayer_range:
        remainder = 1
    else:
        remainder = 0

    print(f"#{test_case} {N // sprayer_range + remainder}")
