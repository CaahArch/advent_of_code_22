

import sys
import os

def read_input(file_path=None):
    if file_path is None:
        script_path = sys._getframe(1).f_globals['__file__']
        script_dir = os.path.dirname(script_path)
        file_path = script_dir + "/input.txt"

    with open(file_path, "r") as file:
        contents = file.read().strip()
    return contents