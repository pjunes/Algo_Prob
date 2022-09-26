def solution(T, n, A, m, B):
    answer = 0
    
    A_sum = [A[i] for i in range(n)]
    for i in range(1, n):
        A_sum[i] += A_sum[i-1]
    A_sum.insert(0, 0)

    B_sum = [B[i] for i in range(m)]
    for j in range(1, m):
        B_sum[j] += B_sum[j-1]
    B_sum.insert(0, 0)

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

    for A_key in A_dict.keys():
        B_key = T - A_key
        if B_dict.get(B_key, 0):
            answer += A_dict[A_key] * B_dict[B_key]

    return answer

if __name__ == "__main__":
    T = int(input()) # (-1,000,000,000 ≤ T ≤ 1,000,000,000)

    n = int(input()) # (1 ≤ n ≤ 1,000)
    A = list(map(int, input().split(' '))) # |A[_]| <= 1,000,000

    m = int(input()) # (1 ≤ m ≤ 1,000)
    B = list(map(int, input().split(' '))) # |B[_]| <= 1,000,000

    answer = solution(T, n, A, m, B)
    print(answer)