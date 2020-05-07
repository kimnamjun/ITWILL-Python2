for _ in range(int(input())):
    n = int(input())
    sticker = list()
    sticker.append(list(map(int, input().split())))
    sticker.append(list(map(int, input().split())))

    tab = [[sticker[0][0]], [sticker[1][0]], [0]]

    for i in range(1, n):
        tab[0].append(sticker[0][i] + max(tab[1][i-1], tab[2][i-1]))
        tab[1].append(sticker[1][i] + max(tab[0][i-1], tab[2][i-1]))
        tab[2].append(max(tab[0][i-1], tab[1][i-1]))

    print(max(tab[0][-1], tab[1][-1], tab[2][-1]))