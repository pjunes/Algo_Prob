"""
첫째 줄에 T(-1,000,000,000 ≤ T ≤ 1,000,000,000)가 주어진다. 
다음 줄에는 n(1 ≤ n ≤ 1,000)이 주어지고, 
그 다음 줄에 n개의 정수로 A[1], …, A[n]이 주어진다. 
다음 줄에는 m(1 ≤ m ≤ 1,000)이 주어지고, 
그 다음 줄에 m개의 정수로 B[1], …, B[m]이 주어진다. 
각각의 배열 원소는 절댓값이 1,000,000을 넘지 않는 정수이다.
"""

def solution(T, n, A, m, B):
    answer = 0

    # print(f"T : {T}\nn : {n}\nA : {A}\nm : {m}\nB : {B}")

    ### prefix sum ###
    
    A_sum = [A[i] for i in range(n)]
    for i in range(1, n):
        A_sum[i] += A_sum[i-1]
    A_sum.insert(0, 0)

    B_sum = [B[i] for i in range(m)]
    for j in range(1, m):
        B_sum[j] += B_sum[j-1]
    B_sum.insert(0, 0)
    
    ### end ###

    # print(f"A_sum : {A_sum}\nB_sum : {B_sum}")

    A_dict = dict()
    B_dict = dict()

    for start in range(n):
        for end in range(start+1, n+1):
            key = A_sum[end] - A_sum[start]
            A_dict[key] = A_dict.get(key, 0) + 1

    for start in range(m):
        for end in range(start+1, m+1):
            key = B_sum[end] - B_sum[start]
            B_dict[key] = B_dict.get(key, 0) + 1

    # print(A_dict)
    # print(B_dict)

    for A_key in A_dict.keys():
        B_key = T - A_key
        if B_dict.get(B_key, 0):
            answer += A_dict[A_key] * B_dict[B_key]

    return answer
"""
    # T = int(input()) # (-1,000,000,000 ≤ T ≤ 1,000,000,000)

    # n = int(input()) # (1 ≤ n ≤ 1,000)
    # A = list(map(int, input().split(' '))) # |A[_]| <= 1,000,000

    # m = int(input()) # (1 ≤ m ≤ 1,000)
    # B = list(map(int, input().split(' '))) # |B[_]| <= 1,000,000

    # A.insert(0, 0)
    # B.insert(0, 0)

    # grid = [[-1 for _ in range(n+1)] for _ in range(m+1)]

    # ### 초기값 설정 ###
    # for i in range(1, n+1):
    #     grid[i][0] = grid[i-1][0] + A[i]
    # for j in range(1, m+1):
    #     grid[0][j] = grid[0][j-1] + B[j]
    
    # for i in range(1, n+1):
    #     for j in range(1, m+1):
    #         grid[i][j] = grid[i-1][j] + grid[i][j-1] - grid[i-1][j-1]
"""

if __name__ == "__main__":
    T = int(input()) # (-1,000,000,000 ≤ T ≤ 1,000,000,000)

    n = int(input()) # (1 ≤ n ≤ 1,000)
    A = list(map(int, input().split(' '))) # |A[_]| <= 1,000,000

    m = int(input()) # (1 ≤ m ≤ 1,000)
    B = list(map(int, input().split(' '))) # |B[_]| <= 1,000,000

    # T = 5
    # n = 4
    # A = [1, 3, 1, 2]
    # m = 3
    # B = [1, 3, 2]

    answer = solution(T, n, A, m, B)
    print(answer)