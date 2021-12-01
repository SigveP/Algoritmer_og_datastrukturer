from datastrukturer import BinaryTree, levelorder, preorder, inorder, postorder

treee = BinaryTree()
inp = ""

print("type numbers to add to tree (stop to stop)")
while inp != 'stop':
    inp = input("> ")
    try:
        x = int(inp)
        treee.append(x)

    except ValueError:
        continue

# -----

inp = ""

print("write order to see tree in order (stop to stop)\norders:\nlevel\npre\nin\npost")
while inp != 'stop':
    inp = input("> ")

    if inp == 'level':
        result = levelorder.recursive(treee.root, 0)
    elif inp == 'pre':
        result = preorder.recursive(treee.root)
    elif inp == 'in':
        result = inorder.recursive(treee.root)
    elif inp == 'post':
        result = postorder.recursive(treee.root)

    if inp != 'stop':
        print(result)
