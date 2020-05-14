def solution(stones, k):
    answer = 0
    stones_values = sorted(list(set(stones)))
    left = 0
    right = len(stones_values) - 1

    yes = 0
    no = len(stones_values)

    cnt = 0
    while cnt < 100:
        cnt += 1

        mid = (left + right) // 2
        stones2 = [s - stones_values[mid] for s in stones]

        length = 0
        max_length = 0
        for s in stones2:
            if s < 0:
                length += 1
            elif length != 0:
                max_length = max(max_length, length)
                length = 0
        max_length = max(max_length, length)
        if max_length >= k:
            no = mid
            right = mid - 1
        else:
            yes = mid
            left = mid + 1
        if no - yes == 1:
            return yes


    return answer