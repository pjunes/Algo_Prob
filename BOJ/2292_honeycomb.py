def solution(N):
    temp = 1
    for i in range(1, 100000):
        temp += (i-1) * 6

        if (N <= temp):
            answer = i
            return answer

        # if temp > 1000000000:
        #     break

    return -1

if __name__ == "__main__":
    N = int(input())
    answer = solution(N)
    print(answer)