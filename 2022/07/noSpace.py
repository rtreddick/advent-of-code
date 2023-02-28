from typing import Optional, Dict


class File:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size


class FileTree:
    def __init__(self, name: str, parent: Optional['FileTree'], dirs: Dict[str, 'FileTree'], files: Dict[str, 'File']):
        self.name = name
        self.parent = parent
        self.dirs = dirs
        self.files = files
        self.size = 0

    def _getChild(self, dir: str):
        return self.dirs.get(dir)

    def _getFile(self, file: str):
        return self.files.get(file)

    def _mkChild(self, dir: str):
        if self._getChild(dir) is None:
            self.dirs.update({dir: FileTree(dir, self, {}, {})})

    def _mkFile(self, file: str, size: int):
        if self._getFile(file) is None:
            self.files.update({file: File(file, size)})

    def _calcSizes(self):
            sizeFiles = sum([file.size for file in self.files.values()]) if self.files else 0
            sizeDirs = sum([dir._calcSizes() for dir in self.dirs.values()]) if self.dirs else 0
            self.size = sizeFiles + sizeDirs
            return self.size


class FileSystem:
    def __init__(self):
        self.root = FileTree('/', None, {}, {})
        self.pwd = self.root
        self.size = 0

    def _cd(self, dir: str):
        if dir == '/':
            self.pwd = self.root
        elif dir == '..' and self.pwd is not self.root:
            self.pwd = self.pwd.parent
        else:
            child = self.pwd._getChild(dir)
            if child is not None:
                self.pwd = child

    @classmethod
    def fromTerminalOutput(cls, terminalOutput):

        with open(terminalOutput, 'r') as terminalOutput:
            terminalLines = [line.strip() for line in terminalOutput.readlines()]

        # initialize empty file system
        fileSystem = FileSystem()

        # build file tree
        for line in terminalLines:

            # change directory
            if line.startswith('$ cd'):
                dir = line.replace('$ cd ', '')
                fileSystem._cd(dir)

            # make directory
            elif line.startswith('dir'):
                dir = line.replace('dir ', '')
                fileSystem.pwd._mkChild(dir) # type: ignore

            # make file
            elif line[0].isdigit():
                size, file = line.split(' ')
                fileSystem.pwd._mkFile(file, int(size)) # type: ignore
        
        # calculate recursive sizes
        fileSystem.root._calcSizes()
        
        return fileSystem


def sumSizes(fileTree: FileTree, maxSize=100000):
    sizesSum = 0
    
    if fileTree.size <= maxSize:
        sizesSum += fileTree.size

    sizesDirs = [sumSizes(dir) for dir in fileTree.dirs.values()]
    sizesSum += sum(sizesDirs) if sizesDirs else 0
    
    return sizesSum


def freeUpSpace(fileTree: FileTree, totalSpace=70000000, spaceNeeded=30000000, targetDelete=None):
    if targetDelete == None:
        freeSpace = totalSpace - fileTree.size
        targetDelete = spaceNeeded - freeSpace

    if fileTree.size >= targetDelete:
        sizesDirs = [freeUpSpace(dir, targetDelete=targetDelete) for dir in fileTree.dirs.values()]
        return min([fileTree.size, *sizesDirs])

    return float('inf')


if __name__ == '__main__':

    terminalOutput = './07/input-1.txt'
    fileSystem = FileSystem.fromTerminalOutput(terminalOutput)
    print(sumSizes(fileSystem.root), freeUpSpace(fileSystem.root))

