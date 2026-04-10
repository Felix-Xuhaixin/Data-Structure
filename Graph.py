"""
undirected Graph
directed Graph
weighted Graph

BFS : Breadth First Search
DFS : Depth First Search

adjacency list

adjacency matrix

"""

class Graph:

    def __init__(self,directed = False):
        self.directed = directed
        self.adj_list = dict()


    def __repr__(self):
        graph_str = "" 
        for node, neighbors in self.adj_list.items():
            graph_str += f"{node} -> {neighbors}\n"
        return graph_str
    
    def add_node(self, node):
        if node not in self.adj_list:
            self.adj_list[node] = set()
        else:
            raise ValueError('Node exists already')
        
    def remove_node(self,node):
        if node not in self.adj_list:
            raise ValueError("Node does not exists")
        
        for neighbors in self.adj_list.values():
            neighbors.discard(node)

    def add_edge (self, from_node, to_node, weight = None):
        if from_node not in self.adj_list:
           self.add_node(from_node)

        if to_node not in self.adj_list:
           self.add_node(to_node)


        if weight is None:
            self.adj_list[from_node].add(to_node)
            if not self.directed: # directed graph need more connection
                self.adj_list[to_node].add(from_node)
            
        else:
            self.adj_list[from_node].add((to_node,weight))
            if not self.directed: # Undirected Graph need to add the both way
                self.adj_list[to_node].add((from_node,weight))

    
    def remove_edge(self, from_node, to_node):
        if from_node in self.adj_list:
            if to_node in self.adj_list[from_node]:
                self.adj_list[from_node].remove(to_node)
            else:
                raise ValueError('Edge does not exists')
        
            if not self.directed:
                if to_node in self.adj_list[from_node]:
                    self.adj_list[from_node].remove(to_node)
    
        else:
            raise ValueError('Edge does not exists')
        

    def get_neighbors(self, node):
        return self.adj_list.get(node,set())
           
        
    def has_node(self, node):
        return node in self.adj_list

    def has_edge(self, from_node , to_node):
        if from_node in self.adj_list:
            return to_node in self.adj_list[from_node]
        return False
    

    def get_nodes(self):
        return list(self.adj_list.keys())
    
    def get_edges(self):
        edges = []
        for from_node, neighbors in self.adj_list.items():
            for to_node in neighbors:
                edges.append((from_node,to_node))
        

    def bfs(self,start):
        # visited = set()
        # queue = [start]
        # order = []

        # while queue:
        #     node = queue.pop(0)
        #     if node not in visited:
        #         visited.add(node)
        #         order.append(node)
        #         neighbors = self.get_neighbors(node)
        pass

if __name__ == "__main__":
    myGraph = Graph()
    myGraph.add_edge('A','B',10)
    myGraph.add_edge('B','C',6)
    myGraph.add_edge('A','C',19)
    myGraph.add_edge('D','E',18)
    myGraph.add_edge('C','D',13)
    myGraph.add_edge('E','F',115)


    print(myGraph.__repr__)
                






            

    


        
        




