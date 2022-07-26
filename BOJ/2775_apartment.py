def solution(k, n):
    answer = 0

    prev = [0] * n
    curr = [0] * n

    for i in range(n):
        curr[i] = i+1

    for i in range(k):
        for j in range(n):
            prev[j] = curr[j]

        for j in range(n):
            curr[j] = sum(prev[:j+1])
    
    answer = curr[n-1]

    return answer

if __name__ == "__main__":
    T = int(input())
    for test_case in range(T):
        k = int(input()) # k층
        n = int(input()) # n호
        answer = solution(k, n)
        print(answer)