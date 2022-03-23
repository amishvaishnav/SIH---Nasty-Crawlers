import re
import anytree as at
from anytree.exporter import JsonExporter

# extract tags from html
pattern = re.compile('</?!?[A-Z]*[a-z]*[a-z0-9]*>?')
string =  open("marketplaces/DCdutchconnectionUK.htm", "r")

tagList = re.findall(pattern, string.read())

for i in range(len(tagList)):
    tagList[i] = tagList[i].replace("<", "")
    tagList[i] = tagList[i].replace(">", "")
    # tagList[i] = tagList[i].replace("/", "")

# print(tagList)

tagList.remove("!DOCTYPE")

nodeList = []
singleton = ["!DOCTYPE", "area", "base", "br", "col", "command", "embed", "hr", "img", "input", "keygen", "link", "meta", "param", "source", "track", "wbr"]
parent = None

# make the tree
for i in range(len(tagList)):
    if tagList[i] in singleton:
        # add to current parent node
        if parent:
            nodeList.append(at.Node(tagList[i], parent=parent))
        else:
            nodeList.append(at.Node(tagList[i]))
    elif "/" in tagList[i]:
        # change parent node to parent's parent node
        parent = parent.parent
    else:
        # add to current parent node and change parent to new node
        if parent:
            nodeList.append(at.Node(tagList[i], parent=parent))
        else:
            nodeList.append(at.Node(tagList[i]))

        parent = nodeList[len(nodeList) - 1]

# save as json
# exporter = JsonExporter(indent=2, sort_keys=True)
# print(exporter.export(nodeList[0]))
# file = open("data.json", "w")

# file.write(exporter.export(nodeList[0]))

# show as tree
for pre, fill, node in at.RenderTree(nodeList[0]):
    print("%s%s" % (pre, node.name))