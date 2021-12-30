from typing import List

class BranchAndBound:
    def __init__(self,matrix):
        self.node = Node(matrix)
        self.queue=[]
        self.solution=[0]
    
    def branch_bound(self):
        self.node.reduce_row()
        self.node.reduce_col()
        for i in range(1,len(self.node.graph)):
            self.queue.append(i)
        self.branch_rec(self.node,(self.queue),self.solution)
        #start from src 0(first row)
        # 0 1 2 3 
        #0
        #1
        #2
        #3
    def branch_rec(self,node,queue,solution):
        print("==========================")
        if(len(solution)<len(node.graph)):
            for i in queue:
                x=0
                node_child= Node([x[:] for x in node.graph],node.cost,node)
                node_child.ignore_dot(i,x)
                node_child.intersect_cost(x,i)
                if(len(solution)>0):                
                    node_child.ignore_row(solution[-1])
                    x=solution[-1]
                else:                
                    node_child.ignore_row(0)
                node_child.ignore_col(i)
                print("-----------------------------")
                node_child.reduce_row()
                node_child.reduce_col()
                node_child.print_matrix()
                node.next.append(node_child) 
            minCost = node.next[0]
            idx = []
            for i in range(len(node.next)):
                if(node.next[i].cost<=minCost.cost):
                    minCost=node.next[i]
                    idx.append(i)
            for nextNode in ((node.next)):
                print(i)
                if(nextNode.cost>minCost.cost):
                    node.next.remove(nextNode)

            for i in range(len(node.next)):  
                solution1 = solution[:]
                solution1.append(queue[i])
                queue1=queue[:]
                queue1.pop(i)          

                print(queue1,solution1)
                self.branch_rec(node.next[i],queue1,solution1)
        else:
            print("Solution :",solution)
            print("Cost :",node.cost)

class Node: 
    #graph : graf yang dipakai tree untuk dihitung
    #val bisa cost, bisa time;
    def __init__(self,graph,cost=0,parent=None):
        self.graph=graph
        self.cost = cost
        self.parent=parent
        self.next=[]

    def add_child(self,node):
        self.next.append(node)

    def reduce_row(self):
        for i in self.graph:
            mini = self.min_skip_minus(i)
            if(mini>0):
                self.cost+=mini
                for j in range(len(i)):
                    i[j]-=mini

    def reduce_col(self):
        for i in range(len(self.graph)):
            mini = self.min_skip_minus([row[i] for row in self.graph ])
            if(mini>0):
                self.cost+=mini
                for j in range(len(self.graph[i])):
                    self.graph[j][i]-=mini

    def ignore_dot(self,x,y):
        if(self.graph[x][y]>0):
            self.graph[x][y]*=-1
            
        if(self.graph[x][y]==0):
            self.graph[x][y]=-1

    def intersect_cost(self,x,y):
        if(self.graph[x][y]>0):
            self.cost+=self.graph[x][y]

    def ignore_row(self,number):
        for i in range(len(self.graph)):
            if(self.graph[number][i]>-1):
                self.graph[number][i]*=-1
            if(self.graph[number][i]==0):
                self.graph[number][i]=-1

    def ignore_col(self,number):
        for i in range(len(self.graph[0])):
            if(self.graph[i][number]>-1):
                self.graph[i][number]*=-1
            if(self.graph[i][number]==0):
                self.graph[i][number]=-1

    def min_skip_minus(self,arr:List):
        arr1=[]
        mini=-1
        for i in range(len(arr)):
            if(arr[i]>=0):
                arr1.append(arr[i])
        if(len(arr1)>0):
            mini=arr1[0]
            for i in range(len(arr1)):
                if(mini>arr1[i]):
                    mini=arr1[i]
        return mini

    def print_matrix(self):
        for i in range(len(self.graph)):
            print("[",end="")
            for j in range(len(self.graph[i])):
                comma=""
                if(j<len(self.graph[i])-1):
                    comma=", "
                if(self.graph[i][j]>-1):
                    print(self.graph[i][j],end=comma)
                else:
                    print("∞",end=comma)
            print("]")
        print("Cost :",self.cost)
   