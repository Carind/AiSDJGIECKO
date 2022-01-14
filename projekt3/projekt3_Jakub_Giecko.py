from enum import Enum
from typing import Dict, List, Any, Optional


class EdgeType(Enum):
    directed = 1
    undirected = 2

class Vertex:
    data: Any
    index: int

    def __init__(self,data: Any,index: int):
        self.data=data
        self.index=index

class Edge:
    source: Vertex
    destination: Vertex
    weight: Optional[float]

    def __init__(self,source: Vertex,destination: Vertex):
        self.source=source
        self.destination=destination

    def __init__(self,source: Vertex,destination: Vertex, weight: float=1):
        self.source=source
        self.destination=destination
        self.weight=weight


class Graph:
    adjacencies: Dict[Vertex, List[Edge]] = {}
    lastIndex: int = 0

    def __init__(self):
        self.adjacencies= {}
        self.lastIndex = 0

    def create_vertex(self, data: Any) -> Vertex:
        newVertex=Vertex(data,self.lastIndex)
        self.adjacencies[newVertex]=[]
        self.lastIndex += 1
        return newVertex

    def createEdge(self, a, b):
        self.adjacencies[a].append(Edge(a,b))

    def add_directed_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        self.adjacencies[source].append(Edge(source,destination,weight))

    def add_undirected_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        self.adjacencies[source].append(Edge(source, destination, weight))
        self.adjacencies[destination].append(Edge(destination, source, weight))

    def add(self, edge: EdgeType, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        if edge == 1:
            self.add_directed_edge(source,destination,weight)
        elif edge == 2:
            self.add_undirected_edge(source,destination,weight)

    def __str__(self):
        out:str=""
        for item in self.adjacencies.keys():
            out+=str(item.data)
            out+=": "
            for edge in self.adjacencies[item]:
                out+=str(edge.destination.data)
                out+=" "
            out+=" | "
        return out

    def getVertex(self,value):
        for vertex in self.adjacencies.keys():
            if vertex.data == value:
                return vertex

    def getAdjacencyMatrix(self):
        x = len(self.adjacencies.keys())
        out:int=[[0 for i in range(x)] for j in range(x)]
        i = 0
        j = 0
        for item in self.adjacencies.keys():
            i+=1
            for edge in self.adjacencies[item]:
                j+=1
                out[edge.source.index][edge.destination.index]=1
        return out

def multiplySqareMatrices(A,B):
    x: int = len(A)
    out: int = [[-1 for i in range(x)] for j in range(x)]
    res: int = 0
    for i in range(x):
        for j in range(x):
            for k in range(x):
                res+=A[i][k]*B[k][j]
            out[i][j]=res
            res=0
    return out

def paths_count(g: Graph, a: Any, b: Any) -> int:
    v_a = g.getVertex(a).index
    v_b = g.getVertex(b).index
    matrix=g.getAdjacencyMatrix()
    out=matrix[v_a][v_b]
    for i in range(1,len(g.adjacencies.keys())):
        matrix = multiplySqareMatrices(matrix,g.getAdjacencyMatrix())
        out += matrix[v_a][v_b]

    matrix = multiplySqareMatrices(matrix,g.getAdjacencyMatrix())
    if(matrix[v_a][v_b]!=0):
        return-1

    return out

print()
print("-1 oznacza nieskończoność")
print()

test: Graph = Graph()
test.create_vertex("a")
test.create_vertex("b")
test.create_vertex("c")

test.createEdge(test.getVertex("a"),test.getVertex("b"))
test.createEdge(test.getVertex("b"),test.getVertex("c"))
test.createEdge(test.getVertex("a"),test.getVertex("c"))

print(test)

print(paths_count(test,"a","c"))

test2: Graph = Graph()
test2.create_vertex("a")
test2.create_vertex("b")
test2.create_vertex("c")
test2.create_vertex("d")

test2.createEdge(test2.getVertex("a"),test2.getVertex("b"))
test2.createEdge(test2.getVertex("a"),test2.getVertex("d"))
test2.createEdge(test2.getVertex("a"),test2.getVertex("a"))
test2.createEdge(test2.getVertex("b"),test2.getVertex("c"))
test2.createEdge(test2.getVertex("c"),test2.getVertex("d"))
test2.createEdge(test2.getVertex("b"),test2.getVertex("d"))

print(test2)

print(paths_count(test2,"a","d"))

test3: Graph = Graph()
test3.create_vertex("a")
test3.create_vertex("b")
test3.create_vertex("c")
test3.create_vertex("d")
test3.create_vertex("e")

test3.createEdge(test3.getVertex("a"),test3.getVertex("d"))
test3.createEdge(test3.getVertex("a"),test3.getVertex("e"))
test3.createEdge(test3.getVertex("b"),test3.getVertex("c"))
test3.createEdge(test3.getVertex("b"),test3.getVertex("d"))
test3.createEdge(test3.getVertex("c"),test3.getVertex("d"))
test3.createEdge(test3.getVertex("c"),test3.getVertex("e"))
test3.createEdge(test3.getVertex("d"),test3.getVertex("e"))

print(test3)

print(paths_count(test3,"b","e"))
