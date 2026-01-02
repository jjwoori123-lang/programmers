def solution(info, n, m):
    global answer
    answer = n
    visit = set()
    def dfs(x, a, b):
        global answer
        visit.add((x, a, b))
        if a >= n or b >= m: return
        if a >= answer: return 
        if a < answer and x == len(info):
            answer = a
            return
        if (x+1, a + info[x][0], b) not in visit: dfs(x+1, a + info[x][0], b)
        if (x+1, a, b + info[x][1]) not in visit: dfs(x+1, a, b + info[x][1])    
    dfs(0,0,0)
    if answer !=n:return answer
    elif answer >= n:return -1