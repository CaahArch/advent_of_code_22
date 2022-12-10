
from pprint import pprint
from advent.day8.treehouse import * 

test_input = """30373
25512
65332
33549
35390"""

visible = [[True, True, True, True, True],
 [True, True, True, False, True],
 [True, True, False, True, True],
 [True, False, True, False, True],
 [True, True, True, True, True]]

def test_visible():
    tree = Tree(3)
    tree.visible["right"] = True
    assert tree.is_visible()
    
    tree = Tree(3)
    tree.visible["right"] = False
    tree.visible["left"] = False
    tree.visible["top"] = False
    tree.visible["bottom"] = False
    assert not tree.is_visible()

def test_parse():
    tree_map = parse(test_input)
    pprint(tree_map)

def test_calc_visible():
    tree_map = parse(test_input)
    calc_visible(tree_map)
    pprint(tree_map)
    assert [[x.is_visible() for x in y] for y in tree_map] == visible
    


def test_count_visible():
    tree_map = parse(test_input)
    calc_visible(tree_map)
    pprint(tree_map)
    assert count_visible(tree_map) == 21