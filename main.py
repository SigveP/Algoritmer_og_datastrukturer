from random import randint
from datastrukturer import *
from datastrukturer.sortering import insertionsort

"""
liste = LinkedList()
liste.append(1)
liste.append(3)
liste.append(2)
print(liste)
liste.insert(0, 23)
liste.insert(1, 13)
liste.insert(4, 90)
print(liste)
liste.pop(1)
liste.pop(3)
print(liste)

stack = Stack(3, 1, 5, 7, 2, 34, 21, 5)
print(stack.list)
stack.push(14)
print(stack.list)
for i in range(4):
    stack.pop()
print(stack.list)
 """
""" 
test = Queue(1, 7, 13, 63, 12, 53, 14)
print(test.peek())
test.enqueue(100)
print(test.peek())
test.dequeue()
test.dequeue()
test.dequeue()
test.dequeue()
print(test.peek())
print(test)
 """
""" 
ht = HashTable()
ht.add(141, "tekst 1")
ht.add(298, "tekst 2")
ht.add(8, "tekst 3")
ht.add(16, "tekst 4")
ht.add(249, "tekst 5")
ht.add('23OIFe23', "tekst 6")
ht.add('noe', "tekst 7")
ht.add('minnepinne', "tekst 8")
ht.add('potet', "tekst 9")
ht.add('nokkel', "tekst 10")
print(ht.table[0])
ht[8] = 'o87VHEfe3'
print(ht.table[0])
print(ht['potet'])
print(ht[8])
print(ht['minnepinne'])
 """
""" 
liste = LinkedList(1, 234, 235, 363, 457, 458, 568)
print(binarysearch.iterative(liste, 458))
print(binarysearch.recursive(liste, 363))
 """
""" 
from datastrukturer.maler.nodes import TreeNode
tree = BinaryTree(1)
tree.root.left = TreeNode(2)
tree.root.left.left = TreeNode(4)
tree.root.left.right = TreeNode(5)
tree.root.right = TreeNode(3)
print(preorder.iterative(tree.root))  # 1 2 4 5 3 
print(preorder.recursive(tree.root))  # 1 2 4 5 3 
print(inorder.iterative(tree.root))  # 4 2 5 1 3 
print(inorder.recursive(tree.root))  # 4 2 5 1 3 
print(postorder.iterative(tree.root))  # 4 5 2 3 1
print(postorder.recursive(tree.root))  # 4 5 2 3 1
 """
l = [randint(111, 999) for i in range(20)]
print(l)
print(insertionsort.iterative(l))
