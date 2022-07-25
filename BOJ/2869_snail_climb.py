def solution(A, B, V):
    answer = (V-A)/(A-B)
    if answer%1:
        answer = int(answer) + 2
    else:
        answer = int(answer) + 1
    return answer

if __name__ == "__main__":
    A, B, V = map(int, input().split(" ")) # 1 <= B < A <= V <= 1,000,000,000
    answer = solution(A, B, V)
    print(answer)

"""
answer = 0
h = 0
while True:
    answer += 1
    h += A
    if h >= V:
        break
    h -= B
"""