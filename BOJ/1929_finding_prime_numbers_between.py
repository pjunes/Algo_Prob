"""
def solution(M, N):
    answer_ar = []

    prime_ar = [2]

    prime_flag = True

    for i in range(3, N+1):
        prime_flag = True
        for prime_num in prime_ar:
            if not i%prime_num:
                prime_flag = False
                break

        if prime_flag:
            prime_ar.append(i)

    for n in range(M, N+1):
        if n in prime_ar:
            answer_ar.append(n)

    # if len(answer_ar) == 0: # 조건에 맞는 수가 없는 경우는 주어지지 않는다.
    #     return []

    return answer_ar

if __name__ == "__main__":
    M, N = map(int, input().split(" "))
    answer_ar = solution(M, N)

    for answer in answer_ar:
        print(answer)
"""