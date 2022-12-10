
from advent.daily import read_input

class Tree():
    def __init__(self, height:int) -> None:
        self.height = height
        self.visible = {
            "left" : True,
            "top" : True,
            "right" : True,
            "bottom" : True
        }
    
    def is_visible(self):
        return any(self.visible.values())
        
    def __repr__(self):
        # return f"{self.is_visible()}"
        return f"{self.height}"
    def __str__(self):
        return f"Tree with height {self.height}"


def main():
    tree_map = parse(read_input())
    calc_visible(tree_map)
    print(f"Solution 1: {count_visible(tree_map)} trees are visible")


def parse(input:str):
    tree_map = []
    for line in input.split('\n'):
        tree_row = []
        for height in line:
            tree_row.append(Tree(height))
        tree_map.append(tree_row)
    return tree_map


def calc_visible(tree_map):
    for k, tree_row in enumerate(tree_map[1:-1]):
        for i, tree in enumerate(tree_row[1:-1]):
            # left
            left_trees = tree_row[:i+1]
            tree.visible["left"] = all([n.height < tree.height for n in left_trees])
            # right
            right_trees = tree_row[i+2:]
            tree.visible["right"] = all([n.height < tree.height for n in right_trees])
            # top
            top_trees = [tree_map[l][i+1] for l in range(k+1)]  # bricht für k=0
            tree.visible["top"] = all([n.height < tree.height for n in top_trees])
            # bottom
            trees_below = [tree_map[l][i+1] for l in range(k+2, len(tree_map))]
            tree.visible["bottom"] = all([n.height < tree.height for n in trees_below])


def count_visible(tree_map):
    count = 0
    for tree_row in tree_map:
        for tree in tree_row:
            if tree.is_visible():
                count += 1
    return count

if __name__ == "__main__":
    main()