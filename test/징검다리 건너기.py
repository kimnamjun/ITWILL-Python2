def solution(stones, k):
    values = sorted(list(set(stones)))
    left = mid = 0
    right = len(values) - 1

    while left <= right:
        mid = (left + right) // 2
        stone = [s - values[mid] for s in stones]

        maxi = dist = 0
        for s in stone:
            if s <= 0:
                dist += 1
            else:
                maxi = max(maxi, dist)
                dist = 0
        maxi = max(maxi, dist)
        print(mid, maxi)
        print(stone)

        if k < maxi:
            right = mid - 1
        else:
            left = mid + 1
    return values[right]


stones01 = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
stones02 = [1,2,3,4,5,6,7,8,9]
stones03 = [4, 8, 10, 6, 4, 2, 8, 4, 10, 2]

print(solution(stones03, 3))