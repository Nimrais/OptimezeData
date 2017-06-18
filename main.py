from tree import Tree
import string
from pprint import pprint
NLayers = 5 #max number of Layers in req
def refactorReq(req):
    refReq = []
    for i in req:
        if(i):
            splited = i.split('[')
            ref = []
            for j in splited:
                if ']' in j:
                    ref.append(j[:len(j)-1:])
                else:
                    ref.append(j)
            refReq.append(ref)
    return refReq


def optimize_data(template, data):
    dic = data.copy()
    pieces = string.Formatter().parse(template)
    requestes = []
    for req in pieces:
        requestes.append(req[1])
    requestes = refactorReq(requestes)
    tree = Tree()
    tree.build(data)
    for req in requestes:
        tree.request(req,tree.nodes())
    newtree = Tree()
    newtree.buildColor(tree,tree.colorOut())
    return newtree.buildDict()

def main():
    template = template = (
        'Python version: {languages[python][latest_version]}\n'
        'Python site: {languages[python][site]}\n'
        'Rust version: {languages[rust][latest_version]}\n'
    )
    data = {
        'languages': {
            'python': {
                'latest_version': '3.6',
                'site': 'http://python.org',
            },
            'rust': {
                'latest_version': '1.17',
                'site': 'https://rust-lang.org',
            },
        },
        'users': {
            "Vasia":{
                'age': '2',
                'town': 'Kiev',
            }
        },
        'animals': ['cow', 'penguin'],
    }
    print("Original data:")
    print(data)
    new_data = optimize_data(template, data)
    print("Optimized data:")
    print(new_data)
if __name__ == '__main__':
    main()












