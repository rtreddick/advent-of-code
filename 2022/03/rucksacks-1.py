from pyprojroot import here


# A-Z unicode points 65 to (65+25)
# a-z unicode points 97 to (97+25)

# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.

# time complexity: O(nlog(n)) due to sort


def get_priority(item):
    if ord(item) >= 97: return ord(item) - 96
    else: return ord(item) - 38


def find_dup_item(rucksack):
    splitIdx = len(rucksack) // 2
    compartment1, compartment2 = sorted(rucksack[:splitIdx]), sorted(rucksack[splitIdx:])
    idx2, item2 = 0, compartment2[0]

    for idx1 in range(len(compartment1)):
        item1 = compartment1[idx1]

        while item2 <= item1:
            if item1 == item2: return item1
            idx2 += 1
            item2 = compartment2[idx2]


def sum_priorities(rucksacks):
    priorities_sum = 0

    with open(rucksacks, 'r') as rucksacks:
        for rucksack in rucksacks:
            dup_item = find_dup_item(rucksack)
            priorities_sum += get_priority(dup_item)       

    return priorities_sum

if __name__ == "__main__":

    rucksacks = f"{here('./03/input-1.txt')}"
    result = sum_priorities(rucksacks)
    print(result)