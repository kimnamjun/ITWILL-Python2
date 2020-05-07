def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])
    p = routes[0][0] - 1
    for r in routes:
        if not r[0] <= p <= r[1]:
            answer += 1
            p = r[1]
    return answer