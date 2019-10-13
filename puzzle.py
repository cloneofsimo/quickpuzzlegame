from collections import defaultdict
n = 5
n2 = n*n

class Node:
    def __init__(self,str,parity):
        self.parity = -parity
        self.state = str
    def expandchild(self):
        self.childnodes = []


        for x in range(n2-1):
            r = list(self.state)
            if r[x] == 'n':
                if self.parity == 1:
                    if x+n < 25 and r[x+n] == 'n':
                        r[x] = 'a'
                        r[x+n] = 'a'
                        self.childnodes.append(Node(''.join(r),self.parity))
                else:
                    if x+1 not in [5,10,15,20] and r[x+1] == 'n':
                        r[x] = 'b'
                        r[x+1] = 'b'
                        self.childnodes.append(Node(''.join(r),self.parity))

    def Iswinningstate(self):
        self.expandchild()
        if len(self.childnodes) == 0:
            return 0
        else:
            pr = 1
            while self.childnodes:
                child = self.childnodes.pop()
                pr *= child.Iswinningstate()

            if 1-pr == 1:
                print(self.state)
            return 1-pr

M = Node('nnnnnnnnnnnnnnnnnnnnnnnnn',1)

print(M.Iswinningstate())
