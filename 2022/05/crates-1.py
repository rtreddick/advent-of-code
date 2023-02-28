import re


class Move:
    def __init__(self, qty, source, dest):
        self.qty = qty
        self.source = source
        self.dest = dest

    @classmethod
    def fromTuple(cls, tuple, stacks):
        qty, source, dest = tuple
        return Move(
            int(qty),
            stacks[int(source) - 1],
            stacks[int(dest) - 1]
        )

    def move(self):
        for _ in range(self.qty):
            crate = self.source.pop()
            self.dest.append(crate)


def moveCrates(instructions):

    with open(instructions, 'r') as lines:
        instructions = lines.readlines()
        
        # initialize stacks
        levels = [[stack[idx:idx+3].strip('[]').strip() for idx in range(0, len(stack), 4)] for stack in instructions[:8]]
        stacks = [[] for _ in range(len(levels[0]))]

        for level in reversed(levels):
            for stack, crate in enumerate(level):
                if crate:
                    stacks[stack].append(crate)

        # list moves
        moveTuples = [re.findall('(\d+)', move) for move in instructions[10:]]

        # execute moves
        for moveTuple in moveTuples:
            Move.fromTuple(moveTuple, stacks).move()

        # return top crate from each stack
        return ''.join([stack[-1] for stack in stacks])


if __name__ == "__main__":

    instructions = f'./05/input-1.txt'
    topCrates = moveCrates(instructions)
    print(topCrates)