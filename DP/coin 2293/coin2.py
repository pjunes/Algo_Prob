def solution():
    answer = 0

    ### take input ###

    # n : the number of coins
    # k : target value
    n, k = map(int, input().split(' '))
    # n, k = 3, 10

    # coin values (cv_ar)
    cv_ar = [0] * n
    for i in range(n):
        cv_ar[i] = int(input())
    # cv_ar = [1, 2, 5]

    ### end ###
    
    ### sort cv_ar ###
    for i in range(n):
        for j in range(i+1, n):
            if cv_ar[i] < cv_ar[j]:
                cv_ar[i], cv_ar[j] = cv_ar[j], cv_ar[i]
    ### end ###

    # print(f"cv_ar : {cv_ar}\n")

    answer = recursion(cv_ar, k, 0, 0, 0)

    return answer

# index : index of cv_ar
# cum : cumulated value
def recursion(cv_ar, k, index, cum, answer):
    # cnt : 현재 index의 coin을 몇 개 사용할 것인지.
    cnt = 0

    ### debug
    # print(f"k : {k}, index : {index}, cum : {cum}, answer : {answer}")
    ###
    
    while True:
        # temp : 축적된 가치 + 현재 코인 * cnt
        temp = cum + (cv_ar[index] * cnt)

        # print(f"cnt : {cnt}, temp : {temp}")

        ### temp와 cnt를 사용하지 않게 개선 가능
        ### loop마다 그냥 cum에 cv_ar[index] 더해주면 됨.

        # temp == k 라면 조건 만족.
        if temp == k:
            ###
            # print(f"temp == k")

            # 기존의 답에 1 추가 (경우의 수 1 추가)
            return answer + 1

        # temp > k 라면 조건 불만족.
        elif temp > k:
            ###
            # print(f"temp > k")

            # 기존의 답 그대로 return (경우의 수 그대로)
            return answer

        # temp < K
        else:
            # print(f"temp < k")
            cnt += 1
            # 다음 코인이 있다면,
            if (index + 1) < len(cv_ar):
                # print(f"index + 1 < n")
                answer += recursion(cv_ar, k, index+1, temp, answer)
            # 없다면
            else:
                return answer

if __name__ == "__main__":
    answer = solution()
    print(answer)