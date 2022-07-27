def solution(N):
    answer = 0
    answer += N//5
    # N = N%5
    answer += (N%5)//3
    if (N%5)%3:
        return -1

    return answer

if __name__ == "__main__":
    while(True):
        N = int(input())
        answer = solution(N)
        print(answer)