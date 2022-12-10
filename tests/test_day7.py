
from advent.day7.direcories import * 

commands = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

def test_parse():
    tree = parse(commands)
    tree.show(data_property="file_size")
    for dir, size in zip(('a', 'e', 'd', '/'), 
                    (94269, 584, 24933642, 23352670)):
        data_dict = tree.get_node(dir).data
        assert data_dict.file_size == size

def test_calc_size():
    tree = parse(commands)
    calc_size(tree.get_node('/'), tree)
    tree.show(data_property="dir_size")
    
    for dir, size in zip(('a', 'e', 'd', '/'), 
                    (94853, 584, 24933642, 48381165)):
        data_dict = tree.get_node(dir).data
        error = data_dict.file_size + data_dict.dir_size - size
        assert error == 0 