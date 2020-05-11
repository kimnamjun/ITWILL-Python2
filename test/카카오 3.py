def solution(gems):
    left = dict()
    right = dict()
    for idx, gem in enumerate(gems):
        if gem not in right:
            right[gem] = idx
    gems2 = list(reversed(gems[:max(right.values())+1]))
    for idx, gem in enumerate(gems2):
        if gem not in left:
            left[gem] = idx
    return [len(gems2)-max(left.values()), max(right.values())+1]



answer = [[3,7],[1,3],[1,1],[1,5]]
gems = [['A','B','B','A','A','C','D','A'],
        ['A','B','C','A','B'],
        ['A','A','A'],
        ['A','B','C','B','D']]
for i in range(4):
    print(f'기대값 : {answer[i]} / 결과값 : {solution(gems[i])}')
    print(gems[i])
    print()