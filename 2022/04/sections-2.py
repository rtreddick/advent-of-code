

def buildTuple(string):
    return tuple(map(int, string.split('-')))

def sortByStart(*tuples):
    return sorted([*tuples], key=lambda tuple: tuple[0])

def countPairs(sections):
    count = 0

    with open(sections, 'r') as lines:
        for line in lines:
            first, second = sortByStart(*map(buildTuple, line.strip().split(',')))
            if second[0] <= first[1]:
                count += 1

    return count


if __name__ == "__main__":

    sections = './04/input-1.txt'
    result = countPairs(sections)
    print(result)