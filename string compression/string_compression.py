# 의문점 1.
# 같은 압축 단위를 가져도 최소 길이가 다를 수 있을까?

def solution(s):
    # answer : min length of result
    answer = 0
    # result : result of compression
    result = ""

    # s_len : length of input {s}
    s_len = len(s)
    # node_len : unit length of compression
    node_len = 1
    
    # prev : value(s_node) previously used inside the for loop
    prev = None
    # r_cnt : Count the number of repeated node.
    r_cnt = 0
    # jump_cnt : Count the number of needed jump
    jump_cnt = 0

    while node_len <= int(s_len / 2):

        for i in range(s_len):
            # initialize
            r_cnt = 0

            # jump stage

            # case start.
            # set start point and s_node

            # Every points can be the start point. regardless of node_len
            if i + node_len > s_len:
                # debugging
                # print(f"i{i} + node_len{node_len} < s_len{s_len}")
                continue

            # s_node : compression unit
            s_node = s[i : i+node_len]

            # debugging
#             print(f"""
# node_len : {node_len}
# s_node   : {s_node}
# i        : {i}
# """)

            for j in range(i+node_len, s_len, node_len):
                if s[j : j+node_len] == s_node:
                    r_cnt += 1
                else:
                    break

            # jump_cnt *= node_len

            # string comparison in python is nothing special.
            # if s_node == prev or not r_cnt:
            #     r_cnt += 1
            # else:
            #     result += f"{r_cnt if r_cnt > 1 else None}{prev}"
            #     r_cnt = 0
            # prev = s_node

            print(f"""
node_len : {node_len}
s_node   : {s_node}
i        : {i}
r_cnt    : {r_cnt}
""")

            # jump stage setting
            # python에서는 for 문의 i 값을 바꿔줘도 loop의 횟수가 변하지 않기 때문에
            # 건너 뛰어야 할 경우를 구현, jump stage
            jump_cnt = r_cnt * node_len

        # end of for

        
        node_len += 1
    # end of while




    # return answer
    return result

if __name__ == "__main__":
    print(solution("aabbaccc"))


# grave
"""
    # for c in s:
    #     # case start.
    #     # Every points can be the start point. regardless of node_len

    #     # case 1. pattern == node
    #     if c == prev or not r_cnt:
    #         r_cnt += 1
    #     else:
    #         result += f"{r_cnt if r_cnt > 1 else None}{prev}"
    #         r_cnt = 0
    #     prev = c

"""