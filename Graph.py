
graph = {'A':['B','C','D'],
            'B':['E'],
            'C':['F','G'],
            'D':['H'],
            'E':['I'],
            'F':['J']}

def dfs(graph,source):
    if source is None or source not in graph: #Find the value source in graph
        return 'Invalid input'
    
    path=[] #camino
    Queue = [source] #fila first in - first out

    while (len(Queue) != 0):
        s = Queue.pop() # delete the last item
        if s not in path:
            path.append(s) #map the graph
        
        if s not in graph:
            continue
        
        for neighbor in graph[s]:
            Queue.append(neighbor) #appende the node neighbor in Queque
    
    return " ".join(path)

search=dfs(graph,'A')
print(search)