class BinaryTreeNode:

    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None


    def __str__(self, level=0):
        ret = "  " *level + str(self.data) + "\n"
        if self.leftchild:
            ret += self.leftchild.__str__(level+1)
        if self.rightchild:
            ret += self.rightchild.__str__(level+1)
        return ret


def printTree(Node, prefix="", is_left=True):
    if not Node:
        return

    if Node.rightchild:
        printTree(Node.rightchild, prefix + ("│    " if is_left else "    "), False)

    print(prefix + ("└── " if is_left else "┌── ") + str(Node.data))

    if Node.leftchild:
        printTree(Node.leftchild, prefix + ("     " if is_left else "│   "), True)


#Para recorrido Level Order
class Queue():

    def __init__(self):
        self.__list = []

    def __str__(self):
        return '--'.join(map(str,self.__list))


    def enqueue(self,e):
        self.__list.append(e)
        return True

    def dequeue(self):
        if self.is_empty():
            return "Error no es posible desencolar, no hay elementos"

        return self.__list.pop(0)

    def first(self):
        if self.is_empty():
            return "Error no es posible leer el primer elemento, no hay elementos"

        return self.__list[0]


    def is_empty(self):
        return len(self.__list) == 0

    def len(self):
        return len(self.__list)

def insertnodeBT(root, newvalue):

   if root is None:
    return BinaryTreeNode(newvalue)

   auxqueue = Queue()
   auxqueue.enqueue(root)

   while not auxqueue.is_empty():

    temproot = auxqueue.dequeue()

    if temproot.leftchild is None:
      temproot.leftchild = BinaryTreeNode(newvalue)
      return root
    auxqueue.enqueue(temproot.leftchild)

    if temproot.rightchild is None:
      temproot.rightchild = BinaryTreeNode(newvalue)
      return root
    auxqueue.enqueue(temproot.rightchild)

   return root

def autogenerate_bt(root,n,min,max):
  for i in range(n):
    root = insertnodeBT(root,random.randint(min,max))
  return root


#bst o de busqueda
def insertnodeBST(rootNode,value):

  if rootNode == None:
    return BinaryTreeNode(value)

  if value <= int(rootNode.data):
    rootNode.leftchild = insertnodeBST(rootNode.leftchild,value)
  else:
    rootNode.rightchild = insertnodeBST(rootNode.rightchild,value)

  return rootNode

    
def searchNodeBST(root, valuetofind):
    if root is None:
        return "el nodo con valor {} NO fue encontrado".format(valuetofind)

    print("Nodos visitados/recorrido : ",root.data)
    if root.data == valuetofind:
        return "el nodo con valor {} SI fue encontrado".format(valuetofind)
    elif valuetofind < root.data:
        return searchNodeBST(root.leftchild, valuetofind)
    else:
        return searchNodeBST(root.rightchild, valuetofind)
    

import random
def autogenerate_bst(root,n,min,max):
  for i in range(n):
    root = insertnodeBST(root,random.randint(min,max))
  return root


