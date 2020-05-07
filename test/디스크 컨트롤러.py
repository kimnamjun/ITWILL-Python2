def solution(jobs):
    answer = 0
    length = len(jobs)
    jobque = list()
    jobs.sort()
    time = jobs[0][0]

    while jobs or jobque:
        if jobs and jobs[0][0] > time:
            time = jobs[0][0]

        while jobs:
            if jobs[0][0] <= time:
                jobque.append(jobs.pop(0))
            else:
                break
        jobque.sort(key=lambda x: x[1])

        print(f'time   : {time}')
        print(f'jobs   : {jobs}')
        print(f'jobque : {jobque}')

        cur = jobque.pop(0)
        time += cur[1]
        answer += time - cur[0]
        print(answer)
        print()

    return answer // length

# lst = [[0, 3], [1, 9], [2, 6], [3, 3], [4, 2]]
# lst = [[0, 9], [0, 4], [0, 5], [0, 7], [0, 3]]
lst = [[1, 9], [1, 4], [1, 5], [1, 7], [1, 3]]

print(solution(lst))
