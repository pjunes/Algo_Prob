def solution(N, prime_ar):
    if N == 1:
        return 1

    for prime_num in prime_ar:
        if N%prime_num == 0:
            print(prime_num)
            solution(N//prime_num, prime_ar)
            break

    return 1

def prime_numbers_until_the_number(N): # return ar [int] # N >= 3
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

    return prime_ar

# def solution(N):
#     if N == 1:
#         return 1

#     prime_ar = prime_numbers_between_two_numbers(3, N)

#     for prime_num in prime_ar:
#         if N%prime_num == 0:
#             print(prime_num)
#             solution(N//prime_num)
#             break
        

#     return 1

# def prime_numbers_between_two_numbers(M, N): # return ar [int]
#     answer_ar = []

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

if __name__ == "__main__":
    N = int(input())

    prime_ar = prime_numbers_until_the_number(N)
    
    solution(N, prime_ar)