from pyprojroot import here


key = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',
    'X': 'lose',
    'Y': 'draw',
    'Z': 'win'
}

moveGuide = {
    ('rock', 'lose'): 'scissors',
    ('rock', 'draw'): 'rock',
    ('rock', 'win'): 'paper',
    ('paper', 'lose'): 'rock',
    ('paper', 'draw'): 'paper',
    ('paper', 'win'): 'scissors',
    ('scissors', 'lose'): 'paper',
    ('scissors', 'draw'): 'scissors',
    ('scissors', 'win'): 'rock'
}

movePts = {
    'rock': 1,
    'paper': 2,
    'scissors': 3
}

wins = {
    ('scissors', 'rock'),
    ('rock', 'paper'),
    ('paper', 'scissors')
}

def rps(strategyGuide, winPts=6, drawPts=3):
    
    with open(strategyGuide, 'r') as lines:
        totalScore = 0
        for line in lines:
            code1, code2 = line.replace('\n', '').split(' ')
            opp, me = key[code1], moveGuide[(key[code1], key[code2])] # type: ignore
            totalScore += movePts[me]
            if opp == me: totalScore += drawPts
            elif (opp, me) in wins: totalScore += winPts

        return totalScore
            


if __name__ == "__main__":

    path = f"{here('./02/rps.txt')}"
    # path = f"{here('./20221201-01/test.txt')}"
    totalScore = rps(path)
    print(totalScore)