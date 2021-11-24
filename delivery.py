import heapq


class Edge():
    def __init__(self, weight, startVertex, targetVertex):
        self.weight = weight
        self.startVertex = startVertex
        self.targetVertex = targetVertex


import heapq


class Node():
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.adjacencyList = []
        self.minDistance = float("inf")
        self.predecessor = None

    def __lt__(self, other):
        selfPriority = self.minDistance
        otherPriority = other.minDistance
        return selfPriority < otherPriority

    def calculateShortestPath(self):
        q = []
        startVertex = self
        startVertex.minDistance = 0
        heapq.heappush(q, (startVertex.minDistance, startVertex))
        while q:
            currentVertex = heapq.heappop(q)[1]
            for edge in currentVertex.adjacencyList:
                u = edge.startVertex
                v = edge.targetVertex
                newDistance = u.minDistance + edge.weight
                if newDistance < v.minDistance:
                    v.predecessor = u
                    v.minDistance = newDistance
                    heapq.heappush(q, (v.minDistance, v))

    def getShortestPathTo(self, targetVertex):
        print("shortest path to vertex is:", targetVertex.minDistance)
        node = targetVertex
        path = []
        while node is not None:
            path.append(node.name)
            node = node.predecessor
        path.reverse()
        return path


nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")
nodeD = Node("D")
nodeE = Node("E")
nodeF = Node("F")
nodeG = Node("G")
nodeH = Node("H")
nodeI = Node("I")
nodeJ = Node("J")
nodeK = Node("K")
nodeL = Node("L")
nodeM = Node("M")
nodeN = Node("N")
nodeO = Node("O")
nodeP = Node("P")
nodeQ = Node("Q")
nodeR = Node("R")
nodeS = Node("S")
nodeT = Node("T")

edge1 = Edge(5, nodeA, nodeE)
edge2 = Edge(2, nodeA, nodeC)
edge3 = Edge(4, nodeA, nodeD)
edge4 = Edge(5, nodeA, nodeB)
edge5 = Edge(3, nodeB, nodeC)
edge6 = Edge(3, nodeB, nodeG)
edge7 = Edge(4, nodeB, nodeF)
edge8 = Edge(3, nodeC, nodeD)
edge9 = Edge(3, nodeC, nodeI)
edge10 = Edge(9, nodeC, nodeH)
edge11 = Edge(1, nodeD, nodeK)
edge12 = Edge(2, nodeD, nodeJ)
edge13 = Edge(6, nodeE, nodeK)
edge14 = Edge(3, nodeE, nodeD)
edge15 = Edge(8, nodeH, nodeO)
edge16 = Edge(4, nodeH, nodeM)
edge17 = Edge(5, nodeH, nodeL)
edge18 = Edge(1, nodeH, nodeG)
edge19 = Edge(5, nodeI, nodeD)
edge20 = Edge(3, nodeI, nodeO)
edge21 = Edge(2, nodeJ, nodeP)
edge22 = Edge(9, nodeJ, nodeR)
edge23 = Edge(2, nodeJ, nodeO)
edge24 = Edge(4, nodeK, nodeP)
edge25 = Edge(1, nodeK, nodeJ)
edge26 = Edge(2, nodeL, nodeM)
edge27 = Edge(5, nodeL, nodeF)
edge28 = Edge(2, nodeM, nodeN)
edge29 = Edge(4, nodeN, nodeS)
edge30 = Edge(5, nodeN, nodeQ)
edge31 = Edge(8, nodeO, nodeT)
edge32 = Edge(4, nodeO, nodeN)
edge33 = Edge(9, nodeQ, nodeL)
edge34 = Edge(3, nodeR, nodeP)
edge35 = Edge(4, nodeR, nodeT)
edge36 = Edge(1, nodeT, nodeS)

nodeA.adjacencyList = [edge1, edge2, edge3, edge4]
nodeB.adjacencyList = [edge5, edge6, edge7]
nodeC.adjacencyList = [edge8, edge9, edge10]
nodeD.adjacencyList = [edge11, edge12]
nodeE.adjacencyList = [edge13, edge14]
nodeH.adjacencyList = [edge15, edge16, edge17, edge18]
nodeI.adjacencyList = [edge19, edge20]
nodeJ.adjacencyList = [edge21, edge22, edge23]
nodeK.adjacencyList = [edge24, edge25]
nodeL.adjacencyList = [edge26, edge27]
nodeM.adjacencyList = [edge28]
nodeN.adjacencyList = [edge29, edge30]
nodeO.adjacencyList = [edge31, edge32]
nodeQ.adjacencyList = [edge33]
nodeR.adjacencyList = [edge34, edge35]
nodeT.adjacencyList = [edge36]

nodeA.calculateShortestPath()
nodeA.getShortestPathTo(nodeT)