def solution(id_list, report, k):
    answer = []
    board = dict()
    rep_cnt = dict()
    ban_list = list()
    for id in id_list:
        board[id] = set()
    for r in report:
        v, key = r.split() # v : reporter / k : target
        board[key].add(v)
    for id in id_list:
        if len(board[id]) >= k:
            ban_list.append(id)
    for id in ban_list:
        for rep in board[id]:
            rep_cnt[rep] = rep_cnt.get(rep, 0) + 1
    for id in id_list:
        if id in rep_cnt.keys():
            answer.append(rep_cnt[id])
        else:
            answer.append(0)
            
    return answer

def solution_ideal(id_list, report, k):
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer