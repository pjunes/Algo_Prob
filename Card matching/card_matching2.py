def in_range(r, c):
    return (r>=0) and (r<4) and (c>=0) and (c<4)

def move(board, r, c):
    queue = list() # (r,c) max 8

    dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1] # 우좌 상하

    for dx, dy in zip(dxs, dys):
        nr = r + dy
        nc = c + dx
        if in_range(nr, nc):
            # arrow move
            queue.append((nr, nc))
            # ctrl + arrow move
            while (not board[nr][nc]) and in_range(nr + dy, nc + dx):
                nr += dy
                nc += dx
            if (nr, nc) not in queue:
                queue.append((nr,nc))
        # else:
        #     continue
    
    return queue

def queue_search(board, queue):
    queue_queue = list() # max 8*8
    for r, c in queue:
        queue_queue.append(move(board, r, c))
    return queue_queue

def min_move(board, r1, c1, r2, c2):
    cost = 0
    if r1 == r2 and c1 == c2:
        return cost

    queue = move(board, r1, c1)
    cost += 1

    for r, c in queue:
        if r == r2 and c == c2:
            return cost

    queue_queue = list()
    queue_queue.append((queue, cost+1))

    while True:
        queue, cost = queue_queue.pop(0)
        for que in queue_search(board, queue):
            for r, c in que:
                if r==r2 and c==c2:
                    return cost
            queue_queue.append((que, cost+1))

def solution(board, r, c):
    answer = 0
    root = list()
    root_rc = (r, c)

    cards = set()
    for i in range(4):
        for j in range(4):
            elem = board[i][j]
            root.append(elem)
            if elem and elem not in cards:
                cards.add(elem)

    answer_ar = list()

    # 순열생성
    import itertools
    card_permutation = itertools.permutations(cards, len(cards))

    for permutation in card_permutation:
        # init
        answer = 0
        r, c = root_rc

        # board init
        for i in range(4):
            for j in range(4):
                board[i][j] = root[4*i + j]

        for number in permutation:
            move_cost = list() # compare 2 cards

            for i in range(4):
                for j in range(4):
                    if board[i][j] == number:
                        move_cost.append((min_move(board, r, c, i, j), i, j))

            if move_cost[0][0] <= move_cost[1][0]:
                cost, r, c = move_cost[0]
                _, r2, c2 = move_cost[1]
            else:
                cost, r, c = move_cost[1]
                _, r2, c2 = move_cost[0]

            answer += cost + 1 # move + enter

            cost = min_move(board, r, c, r2, c2)
            answer += cost + 1 # move + enter

            board[r][c] = 0
            board[r2][c2] = 0

            r, c = r2, c2

        answer_ar.append(answer)

    print(answer_ar)
    return min(answer_ar)

if __name__ == "__main__":
    board = [[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]]
    r, c = 1, 0

    # board = [[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]]
    # r, c = 0, 1

    answer = solution(board, r, c)
    print(answer)
