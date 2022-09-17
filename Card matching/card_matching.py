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
    cost = 1
    queue = move(board, r1, c1)

    for r, c in queue:
        if r==r2 and c==c2:
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

def find_card(board, r1, c1):
    cost = 0
    
    if board[r1][c1]:
        return cost, r1, c1

    cost += 1
    queue = move(board, r1, c1)

    for r, c in queue:
        if board[r][c]:
            return cost, r, c

    queue_queue = list()
    queue_queue.append((queue, cost+1))

    while True:
        queue, cost = queue_queue.pop(0)
        for que in queue_search(board, queue):
            for r, c in que:
                if board[r][c]:
                    return cost, r, c
            queue_queue.append((que, cost+1))

def solution(board, r, c):
    answer = 0
    flag = True

    while flag:

        cost, r, c = find_card(board, r, c)
        answer += cost + 1 # move + enter

        number = board[r][c]

        for i in range(4):
            for j in range(4):
                if i == r and j == c:
                    continue
                if board[i][j] == number:
                    r2, c2 = i, j

        cost = min_move(board, r, c, r2, c2)
        answer += cost + 1 # move + enter

        board[r][c] = 0
        board[r2][c2] = 0

        r, c = r2, c2

        flag = False
        for i in range(4):
            for j in range(4):
                if board[i][j]:
                    flag = True

    return answer

if __name__ == "__main__":
    board = [[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]]
    r, c = 1, 0

    board = [[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]]
    r, c = 0, 1

    answer = solution(board, r, c)
    print(answer)

    # move test
    # print(move(board, 1, 2))


    # test
    # cost = 1
    # queue = [1, 2, 3]

    # test = list()

    # test.append((queue, cost))
    # print(test)
    # cost += 1
    # print(test)

    # print(min_move(board, 0, 0, 3, 3))
    # print(find_card(board, 2, 1))