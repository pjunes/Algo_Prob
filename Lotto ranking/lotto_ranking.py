def solution(lottos, win_nums):
    answer = [1, 1]
    
    for v in lottos:
        if v:
            if v not in win_nums:
                answer[0] += 1
                answer[1] += 1
        else:
            answer[1] += 1
    
    if answer[0] > 6:
        answer[0] = 6
    if answer[1] > 6:
        answer[1] = 6
    
    return answer

def solution_model(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]

"""
다음과 같은 상황이 주어졌을때,
1	6개
2	5개 
3	4개 
4	3개 
5	2개 
6   0~1개

내가 처음 생각한 해결방안은 1~7로 구현한 뒤, 7이 나오면 6으로 바꾸는 방식이었다.
단점으로는 범위가 2 이상인 구획을 모두 따로 구현해야 한다는 것.
if answer[0] > 6:
    answer[0] = 6
if answer[1] > 6:
    answer[1] = 6

다른 답안에서 해결방안을 찾았다.
배열을 사용해 라벨링 후, 인덱스를 활용하는 방식이다.
rank=[6,6,5,4,3,2,1]


"""