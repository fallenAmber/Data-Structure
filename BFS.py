class Node:
    def __init__(self,data):
        self.data=data
        self.ad_list=[]
        self.visited=False
class BFS():
    def bfs(self,StartNode):
        queue=[]
        queue.append(StartNode)
        StartNode.visited=True
        while queue:
            actualNode=queue.pop(0)
            print(actualNode.data)
        for n in actualNode.ad_list:
            if not n.visited:
                n.visited=True
                queue.append(n)




node1=Node("A")
node2=Node("B")
node3=Node("C")
node4=Node("D")
node5=Node("E")
node1.ad_list.append(node2)
node1.ad_list.append(node3)
node2.ad_list.append(node4)
node3.ad_list.append(node5)
a=Node(node1)
a.bfs()
    