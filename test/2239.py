idx = ((0,1,2,9,10,11,18,19,20),
       (3,4,5,12,13,14,21,22,23),
       (6,7,8,15,16,17,24,25,26),
       (27,28,29,36,37,38,45,46,47),
       (30,31,32,39,40,41,48,49,50),
       (33,34,35,42,43,44,51,52,53),
       (54,55,56,63,64,65,72,73,74),
       (57,58,59,66,67,68,75,76,77),
       (60,61,62,69,70,71,78,79,80))

# cell 번호에 맞는 box 번호를 반환
def box(cell):
    for i in range(9):
        if cell in idx[i]:
            return i

# cell에 들어갈 수 있는 번호 리스트를 반환
def find(board, cell):
    num = set()
    for i in range(cell // 9, cell // 9 + 9):
        num.add(board[i])
    for i in range(cell % 9, 81, 9):
        num.add(board[i])
    for i in idx[box(cell)]:
        num.add(board[i])
    num.remove('0')
    return sorted(list(num), reverse=True)

def play(board, start):
    print(start)
    for i in range(start, 64):
        if board[i] == '0':
            for j in find(board, i):
                board = board[:i] + str(j) + board[i+1:]
                play(board, i)

brd = str()
for i in range(9):
    brd += input()

answer = play(brd, 0)
print(answer)