class Node(object):
    def __init__(self, char: str):
        self.char = char
        self.children = list()
        self.tag = None
        self.counter = 1  # number of words having this character


def add(root, emotic: str, tag: str):
    node = root
    for char in emotic:
        in_child = False
        # is the character in any of the children of that node?
        for child in node.children:
            if child.char == char:
                child.counter += 1
                node = child  # the current node now is the child
                in_child = True
                break

        # the character not in any of the children
        # create a new child
        if not in_child:
            new_node = Node(char)
            node.children.append(new_node)

            node = new_node
    node.tag = tag  # this is the last character in the word, specify its tag
