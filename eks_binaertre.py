""" 
EKSEMPEL binærtre

I dette eksemplet har jeg bare latt brukeren skrive inn
tallene som skal inn i binærtreet, så kan de velge
hvilken order den skal bruke.
Klarte egentlig ikke å finne på et eksempel.
"""
from datastrukturer import BinaryTree, levelorder, preorder, inorder, postorder

treee = BinaryTree()  # lager et nytt binærtre
inp = ""  # input

# tekst som sier hva du skal gjøre
print("type numbers to add to tree (stop to stop)")
while inp != 'stop':  # stopper da input er "stop"
    inp = input("> ")  # endrer input
    try:
        x = int(inp)  # gjør input til int
        treee.append(x)  # legger x inn i treet

    except ValueError:  # kommer hit hvis input ikke tall
        continue  # fortsetter while løkken

# -----

inp = ""  # resetter input

# tekst som sier hva du skal gjøre
print("write order to see tree in order (stop to stop)\norders:\nlevel\npre\nin\npost")
while inp != 'stop':  # stopper hvis input er "stop"
    inp = input("> ")  # endrer input

    if inp == 'level':  # ser om input er "level"
        result = levelorder.recursive(treee.root, 0)  # levelorder result
    elif inp == 'pre':  # ser om input er "pre"
        result = preorder.recursive(treee.root)  # preorder result
    elif inp == 'in':  # ser om input er "in"
        result = inorder.recursive(treee.root)  # inorder result
    elif inp == 'post':  # ser im input er "post"
        result = postorder.recursive(treee.root)  # postorder result

    if inp != 'stop':  # ser om input er "stop"
        print(result)  # printer result
