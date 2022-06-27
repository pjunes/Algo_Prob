import sys

sys.stdin = open("candy dispensing\candy_dispensing_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    A, B, K = map(int, input().split())

    A_hist = list()

    for i in range(K):
        if A >= B:
            A, B = A - B, 2*B
        else:
            A, B = 2*A, B - A

        if A in A_hist:
            break
        else:
            A_hist.append(A)

    if len(A_hist) < K:
        index = (K+1) % len(A_hist)
        result = min(A_hist[index], A+B - A_hist[index])
    else:
        result = min(A, B)


    print(f"#{test_case} {result}")

    # a,b,k = map(int,input().split())
    # c = a+b
    # n = 1
    # for i in range(31,-1,-1):
    #     n *= n
    #     if k & (1<<i):
    #         n*=2
    #     n %= c
    # a = (a*n)%c
    # b = c-a
    # print("#{} {}".format(test_case, min(a,b)))