def solution(N):
    answer = 0
    quotient_N5 = N//5
    # remainder_N5 = N%5
    for i in range(quotient_N5, -1, -1):
        if (N-5*i)%3:
            continue
        else:
            answer += i + (N-5*i)//3
            return answer

    return -1

if __name__ == "__main__":
    N = int(input())
    answer = solution(N)
    print(answer)

    # while(True):
    #     N = int(input())
    #     answer = solution(N)
    #     print(answer)