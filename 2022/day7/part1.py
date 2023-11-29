import pathlib
from typing import List, Optional


class File:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    def __str__(self, indent: int = 0) -> str:
        indentStr = "  " * indent
        return f"{indentStr}File: {self.name}, Size: {self.size}"

class Directory:
    def __init__(self, name: str, parent):
        self.name = name
        self.parent: Optional[Directory] = parent
        self.dirs: List[Directory] = []
        self.files: List[File] = []
    
    def __str__(self, indent: int = 0) -> str:
        indentStr = "  " * indent
        string = f"{indentStr}Dir: {self.name}"
        for d in self.dirs:
            string += f"\n{d.__str__(indent+1)}"
        for f in self.files:
            string += f"\n{f.__str__(indent+1)}"
        return string

def getDirectorySize(dir: Directory) -> int:
    size = sum(f.size for f in dir.files)
    size += sum(getDirectorySize(d) for d in dir.dirs)
    return size

def run(inputPath: pathlib.Path):
    root = Directory("/", None)
    allDirs: List[Directory] = []

    cwd = root
    for command in [c.strip().split() for c in inputPath.open().readlines()]:
        if command[0] == "$":
            if command[1] == "cd":
                if command[2] == "/":
                    cwd = root
                elif command[2] == "..":
                    cwd = cwd.parent
                else:
                    print(cwd)
                    print(command)
                    cwd = next(d for d in cwd.dirs if d.name == command[2])
        elif command[0] == "dir":
            newDir = Directory(command[1], cwd)
            allDirs.append(newDir)
            cwd.dirs.append(newDir)
        else:
            cwd.files.append(File(command[1], int(command[0])))

    print(root)

    totalSize = 0
    for d in allDirs:
        dirSize = getDirectorySize(d)
        if dirSize <= 100000:
            totalSize += dirSize

    print(totalSize)