from datastrukturer import *
import algoritmer.binary_search as bs

""" 
tree = Tree(0)
tree.add(tree.root, 1)
tree.add(tree.root, 2)
tree.add(tree.root, 3)
tree.add(tree.root.branches[0], 4)
tree.add(tree.root.branches[0], 5)
tree.add(tree.root.branches[2], 6)
tree.add(tree.root.branches[2], 7)
tree.add(tree.root.branches[2].branches[0], 8)
tree.add(tree.root.branches[2].branches[1], 9)
print(tree.getDict())

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

liste = LinkedList(1, 234, 235, 363, 457, 458, 568)
print(bs.iterative(liste, 438))
print(bs.recursive(liste, 363))
