# TODO
# jump를 구현하거나
# prev를 구현하기

def solution(s):
    answer = 0
    trg_value = 0
    hist = list()

    s_len = len(s)
    s_node_len = 1
    s_node = ""

    c_node = "" # comparison node
    p_node = "" # previous node

    # r_cnt = 0 # repeatition conter
    r_flag = False # repeatition flag

    while s_node_len <= int(s_len / 2):
        # initialize : new node_len
        trg_value = s_len

        print(f"initial trg_value : {trg_value}") # debugging

        pass

        for i in range(0, s_len, s_node_len):

            print(f"i : {i}") # debugging

            s_node = s[i : i+s_node_len]

            # initialize : comparison
            # r_cnt = 0
            r_flag = False

            for j in range(i+s_node_len, s_len, s_node_len):
                c_node = s[j : j+s_node_len]

                print(f"s_node : {s_node}\nc_node : {c_node}")

                if s_node == c_node:
                    # r_cnt += 1
                    r_flag = True
                    
                    print(f"trg_value : {trg_value} -> ", end="")
                    trg_value -= s_node_len
                    print(f"{trg_value}")
                    continue
                    
                else:
                    break
                # end of if

                pass
            # end of for

            if r_flag:
                print(f"trg_value : {trg_value} -> ", end="")
                trg_value += 1
                print(f"{trg_value}")
            else:
                pass

            p_node = s_node
            
        # end of for

        hist.append(trg_value)
        s_node_len += 1

        pass
    # end of while

    answer = min(hist)
    print(hist)
    return answer

if __name__ == "__main__":
    print(solution("abcabcabcabcdededededede"))


# def solution(s):
#     # answer : min length of result
#     # answer = 0
#     # result : result of compression
#     result = ""
#     # result_hist : history of len(result)
#     result_len_hist = list()

#     # s_len : length of input {s}
#     s_len = len(s)
#     # node_len : unit length of compression
#     node_len = 1
    
#     # prev : value(s_node) previously used inside the for loop
#     # prev = None
#     # r_cnt : Count the number of repeated node.
#     r_cnt = 0
#     # jump_cnt : Count the number of needed jump
#     jump_cnt = 0

#     while node_len <= int(s_len / 2):
#         ### initialize
#         result = ""

#         for i in range(s_len):
#             ### initialize
#             r_cnt = 0

#             ## jump stage
#             if jump_cnt:
#                 # print("jump")
#                 jump_cnt -= 1
#                 continue

#             # exclude the remainder
#             if i + node_len > s_len:
#                 # print(f"i{i} + node_len{node_len} < s_len{s_len}") # debugging
#                 result += f"{s[i : ]}"
#                 continue

#             ### case start.
#             ## set start point and s_node

#             # s_node : compression unit
#             s_node = s[i : i + node_len]

#             # compare s_node with next node
#             for j in range(i+node_len, s_len, node_len):
#                 if s[j : j+node_len] == s_node:
#                     r_cnt += 1
#                 else:
#                     break

#             if r_cnt:
#                 result += f"{r_cnt + 1}{s_node}"
#             else:
#                 result += f"{s_node}"

#             # jump stage setting
#             # python에서는 for 문의 i 값을 바꿔줘도 loop의 횟수가 변하지 않기 때문에
#             # 건너 뛰어야 할 경우를 구현, jump stage
#             jump_cnt = node_len - 1 + r_cnt * node_len

# #             print(f"""
# # node_len : {node_len}
# # s_node   : {s_node}
# # i        : {i}
# # r_cnt    : {r_cnt}
# # jump_cnt : {jump_cnt}
# # """)

#         # end of for
#         # print(result)
#         result_len_hist.append(len(result))
        
#         node_len += 1
#     # end of while

#     # print(min(result_len_hist))
#     # return answer
#     return min(result_len_hist)

# if __name__ == "__main__":
#     print(solution("aabbaccc"))


# # grave
# """
#     # for c in s:
#     #     # case start.
#     #     # Every points can be the start point. regardless of node_len

#     #     # case 1. pattern == node
#     #     if c == prev or not r_cnt:
#     #         r_cnt += 1
#     #     else:
#     #         result += f"{r_cnt if r_cnt > 1 else None}{prev}"
#     #         r_cnt = 0
#     #     prev = c

    

#             # jump_cnt *= node_len

#             # string comparison in python is nothing special.
#             # if s_node == prev or not r_cnt:
#             #     r_cnt += 1
#             # else:
#             #     result += f"{r_cnt if r_cnt > 1 else None}{prev}"
#             #     r_cnt = 0
#             # prev = s_node

# """

# # debugging
# #             print(f"""
# # node_len : {node_len}
# # s_node   : {s_node}
# # i        : {i}
# # """)

# #             print(f"""
# # node_len : {node_len}
# # s_node   : {s_node}
# # i        : {i}
# # r_cnt    : {r_cnt}
# # jump_cnt : {jump_cnt}
# # """)