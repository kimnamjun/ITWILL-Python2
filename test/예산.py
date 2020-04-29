def solution(budgets, M):
    budgets.sort()
    left = 0
    right = budgets[-1]

    while left <= right:
        mid = (left + right) // 2
        budgets2 = [x if x < mid else mid for x in budgets]
        total = sum(budgets2)

        if total == M:
            return mid
        elif total < M:
            left = mid + 1
        else:
            right = mid - 1
    return right
