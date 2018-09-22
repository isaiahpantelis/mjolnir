# from pprint import pformat
from typing import List


class Node:

    def __init__(self, value=None, parent=None, children=[], leaf=False, depth=0):

        self.value = value
        self.parent = parent
        self.children = children
        self.leaf = leaf
        self.depth = depth

    def __eq__(self, other):

        if (self.label == other.label and
            self.parent == other.parent and
            self.children == other.children and
            self.leaf == other.leaf and
                self.depth == other.depth):
            return True
        else:
            return False

    def __repr__(self):
        # return pformat(f"label > '{self.label}' | parent > {self.parent} | children > {self.children}")
        return f"(value: '{self.value}' | parent: {self.parent} | children: {self.children} | leaf: {self.leaf}) | depth: {self.depth}"

# ----------------------------------------------------------------------------------------------------------------------


class LabeledTree(dict):

    def __init__(self, root: Node):

        super(LabeledTree, self).__init__()

        self['root'] = root

# ----------------------------------------------------------------------------------------------------------------------

    def add(self, section: List[str]):

        # print(f'-- Adding {section}')

        nparts = len(section)

        for k in range(0, nparts):

            part = section[k]
            node_key = '_'.join(section[:k+1])

            # print(f'   Adding section {part}')
            # Find all the nodes at depth k
            knodes = [label for label in self if self[label].depth == k]
            # print(f'      nodes at depth {k} = {knodes}')

            if node_key not in knodes:

                if k == 0:
                    parent = 'root'
                else:
                    parent = '_'.join(section[:k])

                if k == nparts - 1:
                    leaf = True
                else:
                    leaf = False

                self[node_key] = Node(value=part, parent=parent, children=[], leaf=leaf, depth=k)
                self[parent].children.append(node_key)

# ----------------------------------------------------------------------------------------------------------------------
