typeList = type ([1, 1])
typeDic = type ({1: 1})
maxnum = 100000000000000000000000000000000000000000000000000000000000000000


#
'''
in this class. I relese Tree as orgraph,where nodes is list like this elem where
elem[0]`s data, which node consists
elem[1]`s number, which vertex takes when it is added to Tree
elem[2]`s list os sons of vertex, list of numbers which uses like ref on another node
'''
class Tree (object):
    def __init__(self):
        self._color = set ()  # nodes that take part in out
        self._nodes = [] # list of all nodes
        self._len = 0 #number of nodes
        self._colored = [] # colored list
        self._heads = []
        #'''our graph is composed, from different connects Componets => if we know ref on head of component we know all
        #component
        #'''

    def addVer(self, name):
        node = [name, self._len, []]#creates node
        self._len += 1#
        self._nodes.append (node)
        return node[1]

    def __len__(self):
        return self._len

    def setLink(self, i, j):
        self._nodes[i][2].append (j)

    def __str__(self):
        return str (self._nodes)

    def build(self, dic, father=None):
        '''
        We can see that this functions
        updates Tree with information in a list
        cause we have bijection Trees -> Dicts Dicts -> Trees
        '''
        if (father == None):
            layer = list (dic.keys ())
            for name in layer:
                num = self.addVer (name)
                self._heads.append (num)
                if type (dic[name]) == typeDic:
                    self.build (dic[name], num)
                else:
                    self._nodes[len (self) - 1][2] = dic[name]
        else:
            layer = list (dic.keys ())
            for name in layer:
                num = self.addVer (name)
                self._nodes[father][2].append (num)
                if type (dic[name]) == typeDic:
                    self.build (dic[name], num)
                else:
                    self._nodes[len (self) - 1][2] = dic[name]

    def request(self, req, nodes):
        if len (req) > 1:
            # nodes is preposition where is req[0], on start its all list of nodes
            prepositon = [node for node in nodes if req[0] == node[0]]
            # req[1] son of req[1] => find that node which have son with name req[1]
            num = None

            for head in prepositon:
                if type (head[2]) == typeList:
                    for node in head[2]:
                        if self.nodes ()[node][0] == req[1]:
                            num = head[1]
            self.switchColor (num)
            prepositon = []
            for i in self.nodes ()[num][2]:
                prepositon.append (self._nodes[i])
            self.request (req[1::], prepositon)
        else:
            prepositon = [node for node in nodes if req[0] == node[0]][0]
            self.switchColor (prepositon[1])

    def switchColor(self, i):
        if not self.nodes ()[i] in self._colored:
            self._colored.append (self.nodes ()[i])

    def colorOut(self):
        return self._colored

    def nodes(self):
        return self._nodes

    def heads(self):
        return self._heads

    def componentBuildDict(self, i):
        '''
        Really something like python magic 
        we call creates in reccursive way
        and after got list that based on Tree
        That functions build dict of one compoent of Connectivty
        '''
        if not (type(self.nodes ()[i][2]) == typeList):
            name = self.nodes ()[i][0]
            value = self.nodes ()[i][2]
            return {name: value}
        else:
            out = {}
            for j in self.nodes ()[i][2]:
                out.update (self.componentBuildDict (j))
            return {self.nodes ()[i][0]: out}

    def buildDict(self):
        '''
        If we have dicts for all commponet of connectivity
        we can merge them and will take all dic cause our graph
        is Forest
        '''
        out = {}
        for i in self.heads():
            out.update (self.componentBuildDict(i))
        return out

    def buildColor(self, tree, colored):  # takes colored vertex and builds new Tree base on them
        TNheads = []
        for node in colored:
            if node[1] in tree.heads():
                TNheads.append(node)
        for node in TNheads:
            self.addBranchColor(tree, node[1], colored)

    def addBranchColor(self, tree, index, colored, father=None):

        if father == None:
            assert index in tree.heads (), "Not Head"
            num = self.addVer(tree[index][0])
            self._heads.append(num)
            for i in tree[index][2]:
                if tree[i] in colored:
                    self.addBranchColor(tree,i,colored,num)
        else:
            num = self.addVer(tree[index][0])
            self._nodes[father][2].append(num)
            if (type(tree[index][2]) == typeList):
                for i in tree[index][2]:
                    if tree[i] in colored:
                        self.addBranchColor(tree,i,colored,num)
            else:
                self._nodes[num][2] = tree[index][2]
    def __getitem__(self, item):
        return self._nodes[item]

    def clearColor(self):
        self._colored = []


DATA = {
    'user': {
        'python': 3.6,
        'Nikola': 1998,
    },
    'lan':{
        'first' :{
            'mom': 'ukr',
            'fat': 'rus'
        },
        'second' : 'eng'
    }
}


def main():
    newtree = Tree ()
    tree = Tree ()
    dic = DATA
    tree.build (dic)
    tree.request (['lan', 'first','mom'], tree.nodes ())
    tree.request(['user','python'],tree.nodes ())
    newtree.buildColor(tree,tree.colorOut())
if __name__ == "__main__":
    main ()
