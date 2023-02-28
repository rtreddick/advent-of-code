

def buildTuple(string):
    return tuple(map(int, string.split('-')))

def sortBySize(*tuples):
    return sorted([*tuples], key=lambda tuple: tuple[1]-tuple[0])

def countPairs(sections):
    count = 0

    with open(sections, 'r') as lines:
        for line in lines:
            small, large = sortBySize(*map(buildTuple, line.strip().split(',')))
            if small[0] >= large [0] and small[1] <= large[1]:
                count += 1

    return count


if __name__ == "__main__":

    sections = './04/input-1.txt'
    result = countPairs(sections)
    print(result)