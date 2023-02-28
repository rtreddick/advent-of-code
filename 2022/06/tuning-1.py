

def tuning(path, markerLen):

    with open(path, 'r') as fp:
        signal = fp.readline()

        for markerIdx in range(markerLen - 1, len(signal)):
            markerSet = set([signal[idx] for idx in range(markerIdx - markerLen + 1, markerIdx + 1)])
            if len(markerSet) == markerLen:
                return markerIdx + 1


if __name__ == '__main__':

    path = './06/input-1.txt'
    marker = tuning(path, 14)
    print(marker)