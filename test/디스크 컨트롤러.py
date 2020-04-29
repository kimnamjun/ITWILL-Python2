def solution(jobs):
    answer = 0
    length = len(jobs)
    jobque = list()
    time = jobs[0][0]
    jobs.sort()

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
        print()

        cur = jobque.pop(0)
        time += cur[1]
        answer += time - cur[0]

    return answer // length

solution([[0, 3], [1, 9], [2, 6]])