def solution():
    answer = 0

    ### take input ###

    # n : the number of coins, 1 ≤ n ≤ 100
    # k : target value, 1 ≤ k ≤ 10,000
    n, k = map(int, input().split(' '))

    # coin values (cv_ar), 100,000보다 작거나 같은 자연수
    cv_ar = [0 for _ in range(n)]
    for i in range(n):
        cv_ar[i] = int(input())

    ### end ###

    ### generate memo ###
    # 흔히 쓰이는 memo의 용도로 사용되지 않음.

    # memo[k] : f(k)
    memo = [0 for _ in range(k+1)]

    # algorithm의 동작을 위해 k=0 일 때의 값을 1로 설정
    # 0원에서 한 코인만을 사용해 k원을 만들었을 경우의 수를 의미
    memo[0] = 1

    ### end ###

    answer = for_loop(memo, cv_ar, k)

    return answer

def for_loop(memo, cv_ar, k):
    answer = 0

    for v in cv_ar:
        for i in range(1, k+1):
            if i - v >= 0:
                memo[i] += memo[i-v]

    answer = memo[k]

    return answer

if __name__ == "__main__":
    answer = solution()
    print(answer)