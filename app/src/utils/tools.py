# utils methods
import os


def exists_path(path):
    if os.path.exists(path):
        return True
    else:
        return False


def breakln(lines=10):
    print(lines*'-')
