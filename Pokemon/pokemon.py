def solution(nums):  # nums type:list with int / always have even elements
    answer = 0

    # num_counter = dict()
    # dict[key] = dict.get(key, 0) + 1
    # 사용하여 list(array)의 원소의 개수 count
    # for n in nums:
    #     num_counter[n] = num_counter.get(n, 0) + 1

    # 문제의 요지는 원소의 개수 count가 아니라 key의 수 이므로.
    # set(nums)
    # 주어진 list를 set으로 바꾼 뒤, len(set(nums))와 같은 방식으로 answer를 구할 수 있다.

    # if len(num_counter.keys()) > int(len(nums)/2):
    #     answer = int(len(nums)/2)
    # else:
    #     answer = len(num_counter.keys())

    # min을 사용해 더 작은 값을 간결하게 가져오기.
    # answer = min(int(len(nums)/2), len(num_counter.keys()))
    answer = min(int(len(nums)/2), len(set(nums)))
    
    return answer

if __name__ == "__main__":
    sample = [3, 1, 2, 3]
    answer = solution(sample)
    print(answer)