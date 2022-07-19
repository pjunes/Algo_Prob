def solution(nums):  # nums type:list with int / always have even elements
    answer = 0

    num_counter = dict()

    for n in nums:
        num_counter[n] = num_counter.get(n, 0) + 1

    if len(num_counter.keys()) > int(len(nums)/2):
        answer = int(len(nums)/2)
    else:
        answer = len(num_counter.keys())
    
    return answer


    

if __name__ == "__main__":
    sample = [3, 1, 2, 3]
    answer = solution(sample)
    print(answer)