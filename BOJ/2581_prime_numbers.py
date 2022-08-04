def solution(M, N):
    answer_ar = []
    answer1 = 0
    answer2 = 0

    # num_ar_len = len(num_ar)

    prime_ar = [2]

    prime_flag = True

    for i in range(3, N+1):
        prime_flag = True
        for prime_num in prime_ar:
            if not i%prime_num:
                prime_flag = False
                break

        if prime_flag:
            prime_ar.append(i)

    for n in range(M, N+1):
        if n in prime_ar:
            answer_ar.append(n)

    if len(answer_ar) == 0:
        return -1, -1

    answer1 = sum(answer_ar)
    answer2 = answer_ar[0]

    return answer1, answer2 

if __name__ == "__main__":
    M = int(input()) 
    N = int(input())
    # M, N = 3, 3
    answer1, answer2 = solution(M, N)
    
    print(answer1)
    if not answer1 == -1:
        print(answer2)