def Sieve_of_Eratosthenes(M, N): # Sieve of Eratosthenes
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

def solution(N):
    return len(Sieve_of_Eratosthenes(N, 2*N))

if __name__ == "__main__":
    while True:
        N = int(input())
        if N == 0:
            break
        print(solution(N))