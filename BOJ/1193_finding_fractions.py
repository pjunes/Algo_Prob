def solution(N):
    temp = 0 # 탐색한 floor의 포함되는 element의 총 합을 저장하는 변수

    i = 0
    while True:
        i += 1
        temp += i
        if N <= temp:
            remainder = N + i - temp # N번째 element가 floor에서 몇 번째 있는지 저장하는 변수
            break

    if i%2: # i%2 == 1
        upper = i - remainder + 1
        lower = remainder
    else: # i%2 == 0
        upper = remainder
        lower = i - remainder + 1
    return f"{upper}/{lower}"

def solution2(N):
    upper = 1
    lower = 0
    turn_flag = True
    inc_upper_flag = True
    for i in range(N):
        if turn_flag:
            if upper == 1:
                lower += 1
                inc_upper_flag = True
            else: # lower == 1
                upper += 1
                inc_upper_flag = False
            
            if upper + lower == 2:
                turn_flag = True
            else:
                turn_flag = False
            continue

        if inc_upper_flag:
            upper += 1
            lower -= 1
            if lower == 1:
                turn_flag = True
        else:
            upper -= 1
            lower += 1
            if upper == 1:
                turn_flag = True
    return f"{upper}/{lower}"

if __name__ == "__main__":
    # N = int(input())
    # answer = solution(N)
    # answer2 = solution2(N)
    # print(answer)
    # print(answer2)
    for i in range(1, 10001):
        if not solution(i) == solution2(i):
            print(f"error!! i = {i}")

"""
upper_inc = False

upper = 1
lower = 0

cnt = 1
for i in range(1, N): # 1, 2, 3, ... i는 층(대각)을 의미
    if upper == 1:
        upper_inc = True
        lower += 1
    else:
        upper_inc = False
        upper += 1

    for j in range(i-1): # 1층 (1) 2층 (2) 3층 (3) : (N) N은 층에 속한 원소의 개수 의미
        cnt += 1
        if upper_inc:
            upper += 1
            lower -= 1
        else:
            upper -= 1
            lower += 1
        print(f"{cnt} : {upper}/{lower}") 
"""