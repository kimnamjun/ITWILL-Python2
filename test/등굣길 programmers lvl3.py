# 틀리다는 것을 알지만 일단 돌려봄
def solution(m, n, puddles):
    if (m == 1 or n == 1) and puddles:
        return 0

    tab = list()
    for _ in range(n):
        tab.append([0] * m)
    tab[0][0] = 1

    for p in puddles:
        print(p[0])
        print(p[1])
        tab[p[0]-1][p[1]-1] = -1

    for c in range(n):
        for r in range(m):
            if c and r and tab[c][r] != -1:
                tab[c][r] = tab[c-1][r] + tab[c][r-1]


    print(tab)
    return tab[-1][-1] % 1000000007

print(solution(4,3,[[2,3]]))