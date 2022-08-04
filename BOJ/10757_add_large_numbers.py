def solution(A, B):
    answer = 0

    answer = A + B

    return answer

if __name__ == "__main__":
    A, B = map(int, input().split(" "))
    answer = solution(A, B)
    print(answer)