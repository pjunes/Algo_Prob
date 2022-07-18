def solution(s): # s : string
    answer_string = ""
    answer = 0 # answer : int

    num_box = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

    temp = ""
    for c in s:
        print(f"c : {c} / temp : {temp}")
        if len(temp) >= 1:
            print(temp)
            if temp in num_box.keys():
                answer_string += num_box[temp]
                print(f"add {temp} => {num_box[temp]}\n answer : {answer_string}")
                temp = "" # initialize temp
            else:
                temp += c
                continue

        if c.isnumeric():
            answer_string += c
            print(f"add {c}\n answer : {answer_string}")
            continue
        else:
            temp += c

    answer = int(answer_string)
    return answer

if __name__ == "__main__":
    sample = "one4seveneight"
    answer = solution(sample)
    print(answer)