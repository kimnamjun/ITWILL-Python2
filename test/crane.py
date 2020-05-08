def solution(k, room_number):
    answer = [room_number[0]]
    sec = [[room_number[0], room_number[0]]]
    for n in room_number[1:]:
        chk = True
        left = mid = 0
        right = len(sec)-1
        while left <= right and chk:
            mid = (left + right) // 2
            if n < sec[mid][0]:
                right = mid - 1
            elif n > sec[mid][1]:
                left = mid + 1
            else:
                sec[mid][1] += 1
                n = sec[mid][1]
                chk = False
                if mid != len(sec)-1 and sec[mid][1] == sec[mid+1][0] - 1:
                    sec[mid][1] = sec[mid+1][1]
                    sec.pop(mid+1)
        if chk:
            p = mid
            if n > sec[mid][0]:
                p = mid + 1
            if mid < len(sec)-1 and n > sec[mid+1][0]:
                p = mid + 2
            sec.insert(p, [n, n])

            if p < len(sec)-1 and sec[p][1] == sec[p+1][0] - 1:
                sec[p][1] = sec[p+1][1]
                sec.pop(p+1)
            if p > 0 and sec[p-1][1] + 1 == sec[p][0]:
                sec[p-1][1] = sec[p][1]
                sec.pop(p)
        answer.append(n)
    return answer


k = 10
room_number = [6,3,1,4,1,3,1,5]
print(solution(k, room_number))