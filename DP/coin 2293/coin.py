def solution():
    answer = 0

    # 동전의 개수, 목표 값
    n, k = map(int, input().split(' '))

    # 동전의 가치
    coin_values = [0] * n # 100,000 이하의 자연수를 가지는 크기 n인 배열
    for i in range(n):
        coin_values[i] = int(input())

    # memo
    memo = [0] * (k+1)
    for i in range(k+1):
        memo[i] = -1

    answer = recursion(memo, coin_values, n, k)

    print(memo)

    return answer

# for v in coin_values:
#     memo[v] = 1

# main algorithm
# 기반 정보 memo, coin_values, n, k
# value
def recursion(memo, coin_values, n, value): 
    if not memo[value] == -1:
        return memo[value]

    if value < 0:
        return 0

    # n = len(coin_values)

    queue = [0] * n
    for i in range(n):
        queue[i] = value - coin_values[i]

    cnt = 0
    for v in queue:
        cnt += recursion(memo, coin_values, n, v)
    
    if (value in coin_values):
        cnt += 1

    """
    # if (value in coin_values):
    #     if (cnt == 0):
    #         memo[value] = 1
    #         return 1
    #     else:
    #         cnt += 1

    # if (cnt == 0) and (value in coin_values):
    #     # cnt = 1
    #     # memo[value] = cnt
    #     memo[value] = 1
    #     # return memo[value]
    #     # return cnt
    #     return 1
    # elif (value in coin_values):
    #     cnt += 1
    """
    
    memo[value] = cnt
    # return memo[value]
    return cnt


    # queue = [0] * n
    # for i in range(n):
    #     queue[i] = value - coin_values[i]
    #     if queue[i] < 0:
    #         return 0
    #     elif queue[i] == 0:
    #         return 1
    #     else:
    #         recursion(memo, coin_values, n, queue[i])

if __name__ == "__main__":
    answer = solution()
    print(answer)
