data = list()
for _ in range(int(input())):
    data.append(int(input()))

if len(data) < 3:
    print(sum(data))

else:
    tab1 = [data[0], data[1]]
    tab2 = [0, data[0] + data[1]]
    tab3 = [0, 0]

    for idx2, val in enumerate(data[2:]):
        idx = idx2 + 2
        tab1.append(data[idx] + tab3[idx - 1])
        tab2.append(data[idx] + max(tab1[idx - 1], tab3[idx - 1]))
        tab3.append(max(tab1[idx-1], tab2[idx-1]))

    print(max(tab1[-1], tab2[-1], tab3[-1]))