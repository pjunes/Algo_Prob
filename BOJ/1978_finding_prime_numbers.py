def solution(num_ar):
    answer = 0
    num_ar_len = len(num_ar)

    prime_ar = [2]

    prime_flag = True

    for i in range(3, 1001):
        prime_flag = True
        for prime_num in prime_ar:
            if not i%prime_num:
                prime_flag = False
                break

        if prime_flag:
            prime_ar.append(i)

    for n in num_ar:
        if n in prime_ar:
            answer += 1

    return answer

if __name__ == "__main__":
    N = int(input())
    num_ar = list(map(int, input().split(" ")))
    # N = 4
    # num_ar = list(map(int, "1 3 5 7".split(" ")))
    answer = solution(num_ar)
    print(answer)