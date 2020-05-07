from itertools import permutations
from copy import deepcopy


def action(cmd):
    if cmd == 1:  # up
        for col in range(n):
            i = 0
            while i < n-1:
                if board[i][col] == board[i+1][col]:
                    board[i][col] *= 2
                    for idx in range(i+1, n-1):
                        board[idx][col] = board[idx+1][col]
                    board[n-1][col] = 0
                i += 1

    elif cmd == 2:  # down
        for col in range(n):
            i = n-1
            while i > 0:
                if board[i-1][col] == board[i][col]:
                    board[i][col] *= 2
                    for idx in range(i-1, 0, -1):
                        board[idx][col] = board[idx-1][col]
                    board[0][col] = 0
                i -= 1

    elif cmd == 3:  # left
        for row in board:
            i = 0
            while i < n-1:
                if row[i] == row[i+1]:
                    row[i] *= 2
                    for idx in range(i+1, n-1):
                        row[idx] = row[idx+1]
                    row[n-1] = 0
                i += 1

    elif cmd == 4:  # right
        for row in board:
            i = n-1
            while i > 0:
                if row[i-1] == row[i]:
                    row[i] *= 2
                    for idx in range(i-1, 0, -1):
                        row[idx] = row[idx-1]
                    row[0] = 0
                i -= 1


def large():
    ret = 0
    for row in board:
        ret = max(ret, max(row))
    return ret


ans = 0
original_board = list()
n = int(input())
for _ in range(n):
    original_board.append(list(map(int, input().split())))

lst = [1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4]
perm = permutations(lst, 5)
for p in perm:
    board = deepcopy(original_board)
    for i in range(5):
        action(p[i])
        ans = max(ans, large())
    print(p, ans)

print(ans)