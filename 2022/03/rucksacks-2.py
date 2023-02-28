from pyprojroot import here


def get_priority(item):
    if ord(item) >= 97:
        return ord(item) - 96
    else:
        return ord(item) - 38


def find_badge(group):
    sack1, sack2, sack3 = [''.join(sorted(sack)) for sack in sorted(group, key=lambda sack: len(sack))]
    idx2, item2 = 0, sack2[0]
    idx3, item3 = 0, sack3[0]

    for idx1 in range(len(sack1)):
        item1 = sack1[idx1]

        while item2 <= item1:
            if item1 == item2:
                while item3 <= item2:
                    if item1 == item2 == item3:
                        return item1
                    idx3 += 1
                    item3 = sack3[idx3]
            idx2 += 1
            item2 = sack2[idx2]


def sum_priorities(rucksacks):
    priorities_sum = 0
    group = []

    with open(rucksacks, 'r') as rucksacks:

        for rucksack in rucksacks:
            rucksack = rucksack.strip()
            if len(group) < 3:
                group.append(rucksack)

            if len(group) == 3:
                badge = find_badge(group)
                priorities_sum += get_priority(badge)
                group = []

    return priorities_sum
    


if __name__ == "__main__":

    rucksacks = f"{here('./03/input-2.txt')}"
    result = sum_priorities(rucksacks)
    print(result)