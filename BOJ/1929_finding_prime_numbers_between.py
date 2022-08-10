def solution(M, N): # Sieve of Eratosthenes
    isPrime_flags = [False,False] + [True]*(N-1)
    primes = []
    answer_ar = []

    for n in range(2,N+1):
      if isPrime_flags[n]:
        primes.append(n)
        for i in range(2*n, N+1, n):
            isPrime_flags[i] = False

    for p in primes:
        if p > M:
            answer_ar.append(p)
    
    return answer_ar

if __name__ == "__main__":

    M, N = map(int, input().split(" "))

    answer_ar = solution(M, N)

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

"""
def prime_numbers_until_the_number(N):
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

def solution(M, N, prime_ar):
    answer_ar = [n for n in range(M, N+1)]
    # print(f"initial answer_ar : {answer_ar}")

    for p in prime_ar:
        for n in answer_ar:
            if n == p:
                continue
            if n%p == 0:
                # print(f"remove {n} / p : {p}, n : {n}, n%p : {n%p}")
                answer_ar.remove(n)

    return answer_ar

def solution(M, N):
    answer_ar = [n for n in range(M, N+1)]

    pre_answer_ar = [n for n in range(3, M+1)]
    prime_ar = [2]

    idx = 0
    pop_flag = False
    # while_flag = True
    while True:
        for p in prime_ar:
            if pop_flag:
                continue
            if pre_answer_ar[idx]%p == 0:
                print(pre_answer_ar.pop(idx))
                # pre_answer_ar.pop(idx)
                pop_flag = True
        pop_flag = False
        idx += 1
        if idx == len(pre_answer_ar):
            break
            
        pass

    print(pre_answer_ar)

    return answer_ar
"""