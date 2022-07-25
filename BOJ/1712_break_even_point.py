def solution(A, B, C):
    if C <= B:
        return -1
    return int(A / (C - B)) + 1

if __name__ == "__main__":

    A, B, C = map(int, input().split(" "))
    answer = solution(A, B, C)
    print(answer)



    # temp = A / (C - B)
    # if temp%1:
    #     answer = int(temp) + 1
    # else:
    #     answer = int(temp)
    # answer = int(temp) + 1
    # return answer