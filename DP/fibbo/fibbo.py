def solution(memo, n):
    answer = 0

    if not memo[n] == -1:
        print(f"memo[{n}] : {memo[n]}")
        return memo[n]

    # else:
    
    answer = solution(memo, n-2) + solution(memo, n-1)
    memo[n] = answer
    return answer

if __name__ == "__main__":
    n = int(input())
    
    # memo = [-1] * (n+1)
    memo = [-1 for _ in range(n+1)]
    memo[1], memo[2] = 1, 1
    print(memo)

    answer = solution(memo, n)

    print(answer)
    print(memo)