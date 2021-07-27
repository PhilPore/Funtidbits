import sys
from collections import defaultdict, deque
'''There are n cities connected by some number of flights. 
You are given an array flights where flights[i] = [fromi, toi, pricei] 
indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, 
return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.'''

def findCheapestPrice(n,flights, src, dst, k):
    '''adj list first because  you gotta keep track of crap somehow'''

#scrap it all. Change it to a bfs state space search that runs k+1 times

#messed up, internet helped out because I was stuck. 
# The reason why is because you kept going back and forth with values. 
#Its better to keep a cost of traveling to each node. Ifi t gets cheaper then the route is valid.
#If its not then its not worth the exploration. You seemed to be on the right track when you were trying to make the 
#explored dictionary
    plane_graph = defaultdict(list)
    trip_costs = [float('inf') for i in range(n)]

    trip_costs[src] = 0 #because it costs zero to get there
    for flight in flights: #set up adj list.
        plane_graph[flight[0]].append([flight[1], flight[2]])
    
    frontier = deque([(src, 0)]) #our starting point. We can build the list to have (location, cost)
    for i in range(k+1): #bfs, we want the shallowest find.
        for f_nodes in range(len(frontier)): #explore the depth.
            node, old_cost = frontier.popleft() #we get the location, cost of the frontier
            for neibor in plane_graph[node]:
                if trip_costs[neibor[0]] > old_cost+neibor[1]: 
                    #if the trip cost is less than the new trip cost then its not worth exploring 
                    trip_costs[neibor[0]] = old_cost+neibor[1]
                    frontier.append((neibor[0], trip_costs[neibor[0]]))
        #print(trip_costs)
    #print(trip_costs)
    return -1 if trip_costs[dst] == float('inf') else trip_costs[dst]

   
'''
    while frontier:
        node = frontier.pop(0)
        if node[1] < k+1:
            if node[0][0] == dst:
                #print(node)
                temp_min = min(temp_min, node[0][1])
                continue
            cost = node[0][1]
            for new_nei in adjlist[node[0][0]]:
                if new_nei[0] not in explored:
                    frontier.append([[new_nei[0],new_nei[1]+cost], node[1]+1])
            explored.append(node[0][0])
    return temp_min if temp_min < sys.maxsize else -1
'''



'''
try
10
[[3,4,4],[2,5,6],[4,7,10],[9,6,5],[7,4,4],[6,2,10],[6,8,6],[7,9,4],[1,5,4],
[1,0,4],[9,7,3],[7,0,5],[6,5,8],[1,7,6],[4,0,9],[5,9,1],[8,7,3],[1,2,6],[4,1,5],
[5,2,4],[1,9,1],[7,8,10],[0,4,2],[7,2,8]]
6
0
7


3
[[0,1,100],[1,2,100],[0,2,500]]
0
2
1
'''
        
print(findCheapestPrice(3,[[0,1,100],[1,2,100],[0,2,500]],0,2,1))
'''print(findCheapestPrice(n = 10, flights = [[3,4,4],[2,5,6],[4,7,10],[9,6,5],[7,4,4],[6,2,10],[6,8,6],[7,9,4],[1,5,4],
[1,0,4],[9,7,3],[7,0,5],[6,5,8],[1,7,6],[4,0,9],[5,9,1],[8,7,3],[1,2,6],[4,1,5],
[5,2,4],[1,9,1],[7,8,10],[0,4,2],[7,2,8]]
, src = 6, dst = 0, k = 7))'''

'''print(findCheapestPrice(4,
[[0,1,1],[0,2,5],[1,2,1],[2,3,1]],
0,
3,
1))'''
