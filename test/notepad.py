a=[1,2,3,4,5,6,7,9]

c = 0
left = 0
right = len(a) - 1
find = 8

while c < 100:
    c += 1

    mid = (left + right) // 2
    if a[mid] < find:
        left = mid + 1
    elif a[mid] > find:
        right = mid - 1
    else:
        print(f'find index is {mid}')
        break
    if c == 99:
        print('not found find')
