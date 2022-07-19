def solution(s):  # s type:string
    answer_string = ""  # type:string
    answer = 0  # type:int

    # match numeric string with integer
    num_box = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }  # type:dict

    temp = ""
    for c in s:
        # print(f"c : {c} / temp : {temp}")
        if c.isnumeric():
            answer_string += c
        else:
            temp += c
            if temp in num_box.keys():
                answer_string += num_box[temp]
                # print(f"add {temp} => {num_box[temp]}\n answer : {answer_string}")
                temp = ""  # initialize temp

    # change answer_string(type:string) to answer(type:int)
    answer = int(answer_string)
    return answer


if __name__ == "__main__":
    sample = "one4seveneight"
    answer = solution(sample)
    print(answer)

## old incomplete
# if len(temp) >= 1:
#     print(temp)
#     if temp in num_box.keys():
#         answer_string += num_box[temp]
#         print(f"add {temp} => {num_box[temp]}\n answer : {answer_string}")
#         temp = "" # initialize temp
#     else:
#         temp += c
#         continue

# if c.isnumeric():
#     answer_string += c
#     print(f"add {c}\n answer : {answer_string}")
#     continue
# else:
#     temp += c

#  model 1
"""
num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)
"""