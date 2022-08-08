# def prime_numbers_until_the_number(N):
#     prime_ar = [2]

#     prime_flag = True

#     for i in range(3, N+1):
#         prime_flag = True
#         for prime_num in prime_ar:
#             if not i%prime_num:
#                 prime_flag = False
#                 break

#         if prime_flag:
#             prime_ar.append(i)

#     return prime_ar

# def solution(M, N, prime_ar):
#     answer_ar = [n for n in range(M, N+1)]
#     # print(f"initial answer_ar : {answer_ar}")

#     for p in prime_ar:
#         for n in answer_ar:
#             if n == p:
#                 continue
#             if n%p == 0:
#                 # print(f"remove {n} / p : {p}, n : {n}, n%p : {n%p}")
#                 answer_ar.remove(n)

#     return answer_ar

def solution(M, N):
    answer_ar = [n for n in range(M, N+1)]
    prime_ar = [2]
    # print(f"initial answer_ar : {answer_ar}")

    idx = 0
    while True:
        temp = prime_ar[idx]
        while True:
            for n in range(len(answer_ar)):
                if answer_ar[n] % prime_ar[idx] == 0:
                    answer_ar.pop(n)

        pass

    # for p in prime_ar:
    #     for n in answer_ar:
    #         if n == p:
    #             continue
    #         if n%p == 0:
    #             # print(f"remove {n} / p : {p}, n : {n}, n%p : {n%p}")
    #             answer_ar.remove(n)

    return answer_ar

if __name__ == "__main__":

    M, N = map(int, input().split(" "))

    # prime_ar = prime_numbers_until_the_number(N) # N 이하의 모든 소수를 포함하는 ar return.
    # print(f"prime_ar : {prime_ar}")

    answer_ar = solution(M, N)
    # print(f"answer_ar : {answer_ar}")

    for answer in answer_ar:
        print(answer)

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