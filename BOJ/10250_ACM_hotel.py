def solution(H, N):
    room = ((N-1)//H) + 1
    floor = (((N-1)%H) + 1) * 100

    return floor + room

if __name__ == "__main__":
    testcase_num = int(input())
    for testcase in range(testcase_num):
        H, _, N = map(int, input().split(" "))
        answer = solution(H, N)
        print(answer)