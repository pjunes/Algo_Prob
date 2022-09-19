def solution():
    answer = 0

    ### take input ###

    # n : the number of coins
    # k : target value
    # (1 ≤ n ≤ 100, 1 ≤ k ≤ 10,000)
    n, k = map(int, input().split(' '))
    # n, k = 3, 10

    # coin values (cv_ar)
    cv_ar = [0] * n
    for i in range(n):
        cv_ar[i] = int(input())
    # cv_ar = [1, 2, 5]

    ### end ###
    
    ### sort cv_ar ###

    # 오름차순 정렬
    for i in range(n):
        for j in range(i+1, n):
            if cv_ar[i] > cv_ar[j]:
                cv_ar[i], cv_ar[j] = cv_ar[j], cv_ar[i]

    ### end ###

    ### generate memo ###

    # memo[k] : f(k)
    # memo = [-1 for _ in range(k+1)]

    memo = [[-1 for _ in range(k+1)] for _ in range(n+1)]
    # 세로축 : cv_ar의 idx
    # 가로축 : k

    # algorithm의 동작을 위해 k=0 일 때의 값을 1로 설정
    # 0원에서 한 코인만을 사용해 k원을 만들었을 경우의 수를 의미
    for i in range(n):
        memo[i][0] = 1

    ### end ###

    # print(f"cv_ar : {cv_ar}\n")
    # print(f"set_ar : {set_ar}\n")

    answer = find_case(memo, cv_ar, n, k)

    return answer

# def for_loop(memo, cv_ar, k):
#     answer = 0

#     if not memo[k] == -1:
#         return memo[k]

#     for v in cv_ar:
#         pass

#     return answer

# k : k target value
# n : 사용한 코인의 개수
def find_case(memo, cv_ar, n, k):
    answer = 0
    ### debuging ###
    # print(f"n({n}), k({k})", end = " ")

    # check range
    # if not (n > 0 and k > 0):
    #     return 0

    # check memo
    if not memo[n][k] == -1:
        # print(f"return {memo[n][k]}")
        return memo[n][k]

    if n == 1:
        if k%cv_ar[n-1] == 0:
            # print(f"return 1")
            return 1
        else:
            # print(f"return 0")
            return 0

    # answer += find_case(memo, cv_ar, n-1, k)

    # print()

    for i in range(k//cv_ar[n-1]+1):
        answer += find_case(memo, cv_ar, n - 1, k - i * cv_ar[n-1])

    ### debuging ###
    # print(f"n({n}), k({k}) : answer({answer})")
    
    return answer

if __name__ == "__main__":
    answer = solution()
    print(answer)