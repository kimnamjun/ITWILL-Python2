def solution(n):
    answer = ''
    cnt = 0
    while cnt < 100:
        print(n, 3 ** cnt)
        x = 3 ** (cnt + 1)
        if n // x <= 3 ** cnt:
            answer += '1'
        elif n // x <= 3 ** cnt * 2:
            answer += '2'
        else:
            answer += '4'

        cnt += 1
        n -= 3 ** cnt
        if n <= 0:
            break

    return answer[::-1]

for i in range(1, 21):
    print(f'{i} : {solution(i)}')
    print()
