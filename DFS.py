class DFS :

    def dfs(G, u):
        res = {}
        for node in G:
            res[node] = [False, -1, -1]
        time = 1
        stack = []
        stack.append(u)
        while len(stack) >= 1:
            current = stack[len(stack)-1]
            if not res[current][0] :
                res[current][0] = True
                res[current][1] = time
                time += 1
                for neighbour in G[current] :
                    if not res[neighbour][0] :
                        stack.insert(0,neighbour)
            stack.pop()

        return res
                
    def printResult(list):
        print(list)

