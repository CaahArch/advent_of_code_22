from treelib import Tree,Node

from advent.daily import read_input

class dir_data():
    def __init__(self):
        self.dir_size = 0
        self.file_size = 0


def main():
    commands = read_input()
    dirs = parse(commands)
    calc_size(dirs.get_node(dirs.root), dirs)
   
    result = 0
    for d in dirs.all_nodes_itr():
        size = d.data.dir_size + d.data.file_size
        if size <= 100000:
            result += size

    dirs.show()
    print(f"Solution 1: {result}")
    # TODO too high


def parse(input:str) -> Tree:
    tree = Tree()
    last_dir = None
    for line in input.split('\n'):
        if line.startswith('$'):
            if line == "$ ls":
                continue
            elif line == "$ cd ..":
                last_dir = tree.parent(last_dir.identifier)
            elif line.startswith("$ cd"):
                _, _, dirname = line.split(' ')
                last_dir = tree.create_node(dirname, parent=last_dir, data=dir_data())
        else:
            size, _ = line.split(' ')
            if size != "dir":
                last_dir.data.file_size += int(size)
    return tree

    
def calc_size(node: Node, tree: Tree):
    # print(f"Calcuating size of {node.tag}...")
    if node.is_leaf():
        # print(f"Reached leaf {node.tag} with size {node.data.file_size}")
        return node.data.file_size

    for child in tree.children(node.identifier):
        node.data.dir_size += calc_size(child, tree)
        # print(f"Added child {child.tag}, new dir_size of {node.tag} is {node.data.dir_size}")
    
    return node.data.dir_size + node.data.file_size


if __name__ == "__main__":
    main()