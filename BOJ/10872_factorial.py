def solution(N):
    if N < 1:
        return 1 # N
    return N * solution(N-1)

if __name__ == "__main__":
    N = int(input())
    answer = solution(N)
    print(answer)