#tuple is for read only
mytuple=(1,2,3)
#Applying Uniform Cost Search Al
mygraph={
    "S":[("A",2),("B",3),("D",5)],
    "A":[("C",4)],
    "B":[("D",4)],
    "C":[("G",2),("D",1)],
    "D":[("G",5)]
}
def path_cost(path):
    total_cost=0
    for(node,cost) in path:
        total_cost=total_cost+cost
    return total_cost,path[-1][0]

def myucs(mygraph,start,goal):
    visited=[]
    queue=[[(start,0)]]
    while queue:
        queue.sort(key=path_cost)
        path=queue.pop(0)
        node=path[-1][0]
        if node not in visited:
            visited.append(node)
            if node == goal:
                return path
            else:
                neighbour_nodes= mygraph.get(node,[])
                for (node2,cost) in neighbour_nodes:
                    new_path=path.copy()
                    new_path.append((node2,cost))
                    queue.append(new_path)
        else:
            continue
answer_path=myucs(mygraph,"S" ,"G")
print(answer_path)
