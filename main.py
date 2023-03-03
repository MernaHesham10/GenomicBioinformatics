### Single Read ###

# Read file txt, and Removing the new line characters
def GettingSingleReadLines(readFile):
    with open(readFile) as lines:
        outputLines = [line.rstrip() for line in lines]
        
    # print('Single Read File_txt Output Lines: ', outputLines)

    return outputLines


# Function to Split Single Read Lines to Get Sequences Length, and Sequences
def SplittingSingleReadLines(fileLines):
    sequenceLength = int(fileLines[0])

    lineIndex = 0
    forwardList = []
    backwardList = []

    for lineIndex in range(len(fileLines)):
        if lineIndex >= 1:
            forwardList.append(
                fileLines[lineIndex][0:sequenceLength - 1])
            backwardList.append(
                fileLines[lineIndex][1:sequenceLength])

    #print('Single Read Lines For First List: ', forwardList)
    #print('Single Read Lines For Second List: ', backwardList)

    return forwardList, backwardList


def CreatingSingleReadsDictionary(forwardList, backwardList):
    # Create Dictionary With Keys[First Read List] With Empty Values As List
    readsDictionary = {readsDicKey: list() for readsDicKey in
                                      forwardList}

    # Filling Dictionary With Values[Second Read List]
    lineIndex = 0
    for lineIndex in range(len(forwardList)):
        readsDictionary[forwardList[lineIndex]].append(
            backwardList[lineIndex])

    #print('Single Reads Dictionary = ', readsDictionary)

    return readsDictionary


def GettingStartEndReads(readsDict):
    readsDictKeys = list(readsDict.keys())
    readsDictValues = list(readsDict.values())

    j = 0
    i = 0
    readsDictValuesTemp = []

    for i in readsDictValues:
        for j in i:
            readsDictValuesTemp.append(j)

    startRead = [keysIndex for keysIndex in readsDictKeys if keysIndex not in readsDictValuesTemp]

    #print('Single Reads Dictionary Start Read = ', singleReadFile_readsDictionaryStartSeq)

    i = 0
    j = 0

    # jj  = singleReadFile_reads Dictionary Values Index Of Index
    jj = 0
    endRead = []

    for i in readsDictKeys:
        for j in readsDictValues:
            for jj in j:
                if jj not in readsDictKeys:
                    endRead = jj

    #print('Single Reads Dictionary End Read = ', endRead)

    return startRead, endRead


def CalculatingSingleReadPath(forwardList, backwardList, readsDict, startSeq, endSeq):
    readsPath = []
    startSeqStr = startSeq[0]
    readsPath.append(startSeqStr)

    i = 0
    lineIndex = 0
    for lineIndex in range(len(readsDict)):
        if not endSeq:
            readsDictLastVal = backwardList[-1]

            if startSeqStr != readsDictLastVal:
                forwardList[lineIndex] = startSeqStr

                if (len(readsDict[forwardList[lineIndex]]) > 1):

                    for i in range(len(
                            readsDict[forwardList[lineIndex]])):
                        readsPath.append(
                            readsDict[forwardList[lineIndex]][
                                i])
                    startSeqStr = \
                    readsDict[forwardList[lineIndex]][len(
                        readsDict[forwardList[lineIndex]]) - 1]

                else:
                    readsPath.append(
                        readsDict[forwardList[lineIndex]][0])
                    forwardList[lineIndex] = readsDict[
                        forwardList[lineIndex]]
                    startSeqStr = \
                    forwardList[lineIndex][0]

        else:
            if startSeqStr != endSeq[0]:
                forwardList[lineIndex] = startSeqStr

                if (len(readsDict[forwardList[lineIndex]]) > 1):

                    for i in range(len(
                            readsDict[forwardList[lineIndex]])):
                        readsPath.append(
                            readsDict[forwardList[lineIndex]][
                                i])
                    startSeqStr = \
                    readsDict[forwardList[lineIndex]][len(
                        readsDict[forwardList[lineIndex]]) - 1]

                else:
                    readsPath.append(
                        readsDict[forwardList[lineIndex]][0])
                    forwardList[lineIndex] = readsDict[
                        forwardList[lineIndex]]
                    startSeqStr = \
                    forwardList[lineIndex][0]

    #print('Single Reads Path List = ', readsPath)

    return readsPath


def CalculatingSingleReadAssembleGenome(readsPath):
    i = 0
    assemblyStr = ''
    assemblyList = []
    assemblyList.append(readsPath[0])
    for i in range(len(readsPath)):
        if i >= 1:
            assemblyList.append(
                readsPath[i][
                    len(readsPath[0]) - 1])

    assemblyStr = ''.join(assemblyList)

    return assemblyStr


def CalculatingSingleReadAlgorithm(readsFile):
    fileLines = GettingSingleReadLines(readsFile)

    forwardList, backwardList = SplittingSingleReadLines(fileLines)

    readsDict = CreatingSingleReadsDictionary(forwardList, backwardList)
    # print('Graph: ', readsDict)

    readsDictStartRead, readsDictEndRead = GettingStartEndReads(readsDict)
    # print('Start Node: ', readsDictStartRead)
    # print('End Node: ', readsDictEndRead)

    readsPathList = CalculatingSingleReadPath(forwardList, backwardList, readsDict, readsDictStartRead, readsDictEndRead)

    assemblyStr = CalculatingSingleReadAssembleGenome(readsPathList)

    print('*** Single Read assembly Genome ***\n', assemblyStr )
    #print(assemblyStr == 'TTAGTACACGTCAATTAGCCTTATTGCAAGAGTAAGGCTGTCGGCGTGCTTATGTTCTCTCACAGAGCCCTGAGGGAGGTGACAAGGCAGACAGCAGCCTAAGAGCGCTATAAGCGGTTATATGCGCTGTTTTGTTTCCCTACATGGATAGCCATATGACCAAAAGGTCTAGCCGACGGTATTTCATGGACAAAAGGTTCGTGATGTAGCAGGTGTTGACTTGTTCATGGACAAGGCCAAGTTTCTCGCAAGATGGACCCGTGCATGGGTAGCCATGTAGACGGGCATTAAGCAAATGGGCCCATGTCCATCTTCGGAGGACGACAGTTGTGCCTCATACTGCCATGGCGTGCCCACCTTTGCATGCAAAAACTAGTACGCGAAAATCTCCAATCTGAACGTTGCGTCAAAACAAACTTTGCTGTGAACGAATGCTGTGCTTTGGCACTCCGCACAACCATTGTGGGCGAACGGTCAGGAAAACGCACGAAGCTGTCGCTGTGGGCTAGGTACTGTGGGCATATACGGATGAGGAGAAGGTATCCATGACTTACCATGAAAAAGTAATGAAGCACAGGGTGGAAGAGCTAACTTTCCTATTGCCCACAGTGTTGGCAGTGGGGGCCAATTGCCACTTCTCGCACTACACATTTGATGTTAGCAGCCTTCTCGAAAGTGGGCGACAATGCCACATGTCCTGCTGCATTTCAATCCCGGTACAGTATTTGTTCCTATAATCTATTAAGTTAAGCTTTAGACATGAGATTAGGTATGCTCACTTGACGACACTTGCCGATGTACGCTCCAGGTGTTACGCTAACTTATTATCAGTCGAGGGAGCAGCGTTGGCCTGTGCGAGGGCAAGTCGGCTGAAAAAAAACTACACACTCTTCCGCATATCCGCGACTGCACTCATAAACTATACAAAGGCCGCGCAGGAGCAGCAATAATCAATTAGGCACAGAGATAAGTTGTCGACGGTAACTCTTTCATCGGCAACTATGGCACGCAAATTTATAATCAGGACCAGCTGGTGCTATCCATGGACTGAACCTAAATGTCAAATAGAGCCTAGGCTTGGGACGCGGGATTCCCGTTCGCGCCGTGCTAAAGCAAGGAAGCTTTCTGTGAGAGAGTGAAAAAACACGCATGGGATTCTAAAAAACTAAGTCAAAGTTTATTGGTGCTAGTCGACTAAACATGCGGAGAGTAGTTGTAAATTTCATCCACAATAGCCTTGTACTGTTGTGTCCACACGGGGTTGGAGATAATAGTTAGGCTTAGGACGAAGCCAGTACGAACGCGACTCACCCCGGAGTGTGTACCTAATTGACAGACGAAATCGCTCTAATTCTGGGACCGATGCAGGGGCCCGTATTGATCCGCTCTGCACAAATCCCGACTTGAAAATAATGCCTATATAACCAACGAGACCAATTGAGGGAAGTTTTGAGCCTCCGCGCGCCAACTCGAACTGTCGAAAATTATCGTCCCGCAAAGCTGGTCGCTAGTGTTCGGTTGGGGAGTTGTGAATCACAGAGACGTGTAAGTGTTAGTTCGAGACTGCAAGGGCCCACAACGTAAAATTACTTCTTGCTATCGGGGGGAAAATACTAGACAGGGGCCGAGTCATTCGAGTATTCCTTCGAAACGGCGTTGTGACATCACCGGTACTTAAATGAAGCAATCAATCGACGCCAGTGCGTAAACACTAACCTAGGCTCAGCTACTTCCATTTTTTGCCAATCCTTAGTTTCCATCACCGCGCAAGTAATGCCCGGTTGTTGTACGGCCCAGAAGCCACGTCCCAACGACATGCTCCGTGAATGTTACGGCAGTGACTTAGAACGCAACGAACGTAAAGTATCACATTGTGGCCGCACGAAAATGCTACAACTGCCAATATGTAGATAACATAAGCTTACTCTAGGGCGCACACGCTACTAGCCCGATGTCTGTTGTTCAATCCCCGAGGGACAGGAGGAAACCGCTATTGGATGGCCTTCGTGTCAGATCGAGCATGCGGAGGTTGTAGCTTGCCTCGGCACTGTGATGCTTTACCGAGTGTAAAAGTCGGCATTGACTCAGAGCTGCTAACACGGAAGTCCGGTTACCACACCATCTTGTAATACAAGTTAAACAACTGAGGGGTTAGGCGTTACCGATCGGTGACATTTACGTGCAACTTTATTCTCTGCAAGTGCAAGTGCAAACCTACGATCAGTCTTTATTTGCTCCTT')


### Paired Read ###

def GettingPairedReadLines(readsFile):
    readsFile = open(readsFile).readlines()
    txtLines = readsFile[0].split(" ")
    txtLines_Length = int(txtLines[0])
    txtLines_gapValue = int(txtLines[1])
    readsForward = []
    readsBackward = []

    for i in readsFile[1:]:
        txtLinesContent = i.strip().split("|")
        readsForward.append(txtLinesContent[0])
        readsBackward.append(txtLinesContent[1])

    return txtLines_Length, txtLines_gapValue, readsForward, readsBackward


def CreatingPairedReadsDictionary(forwardMers, backwardMers):
    pairedDict = {}
    for i in range(0, len(forwardMers), 2):
        pairedDict[(forwardMers[i], backwardMers[i])] = (forwardMers[i + 1], backwardMers[i + 1])
    return pairedDict


def CalculatingPairedReadPath(start, end, pairedDict, index):
    if index == 'Forward':
        index = 0
    elif index == 'Backward':
        index = 1

    seq = start[index]
    for i in range(len(pairedDict)):
        if pairedDict.get(start) == None:
            return seq
        else:
            seq += pairedDict.get(start)[index][-1]
            start = pairedDict.get(start)
    return seq


def CalculatingPairedReadAssembleGenome(prefix, suffix, length, gap):
    return prefix + suffix[len(suffix) - (length + gap):]


def GettingForwardBackwardRead(reads):
    length = len(reads[0]) - 1
    mers = []
    for read in reads:
        for i in range(len(read) - length + 1):
            mers.append(read[i: length + i])
    return mers


def CheckingPairedReadPath(readsDict):
    endRead = 0

    for i in readsDict.keys():
        checkingKeyAndValue = False

        for j in readsDict.values():
            if (j == i):
                checkingKeyAndValue = True
                break
        if not checkingKeyAndValue:
            startRead = i
            break

    for j in readsDict.values():
        checkingKeyAndValue = False
        for i in readsDict.keys():
            if (j == i):
                checkingKeyAndValue = True
                break
        if not checkingKeyAndValue:
            endRead = j
            break

    return startRead, endRead


def CalculatingPairedReadAlgorithm(readFile):
    txtLines_length, txtLines_gapValue, readsForward, readsBackward = GettingPairedReadLines(readFile)

    forwardMers = GettingForwardBackwardRead(readsForward)

    backwardMers = GettingForwardBackwardRead(readsBackward)

    readsDict = CreatingPairedReadsDictionary(forwardMers, backwardMers)
    #print('Graph: ', readsDict)

    startRead, endRead = CheckingPairedReadPath(readsDict)
    #print('Start Node: ', startRead)
    #print('End Node: ', endRead)

    forwardList = CalculatingPairedReadPath(startRead, endRead, readsDict, 'Forward')
    backwardList = CalculatingPairedReadPath(startRead, endRead, readsDict, 'Backward')
    assemblyStr = CalculatingPairedReadAssembleGenome(forwardList, backwardList, txtLines_length, txtLines_gapValue)

    print('*** Paired Read assembly Genome ***\n', assemblyStr)
    #print(assemblyStr == 'CACCAAGGGGGTCGTGCACGGGCCGTTGCCTACCATTGTGTACGTCGCGTTAAACATATCCCTATAGACAATAGTCTGGTATCGAAGGGTAGTCAGCTGTTACGGATTGCCCCAATAAGCGGAGCCGAAGATATCCGTTCCAATAAGCGGAGCCGAAGATATCCGTTACACAGATGGCCAATAAGCGGAGCCGAAGATATCCGTTACCTTATCAACCAATAAGCGGAGCCGAAGATATCCGTTACCCCAGTCCAGAAGCCTCCTTCGTTAAATCTAATACTTTCGTCCTGACCGTGCATAATTAGGTGAGTATGATGGCGATGGTAGGTGAGTCTAATAACACAAGATGCACCCCCAATAAGCGGAGCCGAAGATATCCGTTACACTTCCAATAAGCGGAGCCGAAGATATCCGTTACCCCAATAAGCGGAGCCGAAGATATCCGTTACTCGGACCGGCGGCAGATAAAACCTACCCCTCAATGGAGAACTTCGCCCGGTAGTATGACCGCGCAAGGTTTTCCAATAAGCGGAGCCGAAGATATCCCAATAAGCGGAGCCGAAGATATCCGTTACCGTTACACAGAAATAGTCATGGCACTTTGCACGCCAATAAGCGGAGCCGAAGATATCCGTTACTGGGCTGACGAGTTTTTTCTTTCTAAGCGGGAAGCCAATAAGCGGAGCCGAAGATATCCGTTACAGCATACAAGACACATCTGCATTTACCAATAAGCGGAGCCGAAGATATCCGTTACAACCACTGGGTACGCTGTAAGTGGACTCGTAACGACTGAGTGAGAGTTTAACTGGTGGCTATGGTGGATCGACAACTGAGTTGGAACGTTCTTTGTAGGCAGGCACCGACCGACGATCTGGTTTATCGGCCATACAGGAATCCAGATCTTCATGACTATTCTAAACCCTCCTGTATCCCAAGGGCCCAGGCGGCATGTGCAGTCCAATAAGCGGAGCCGAAGATATCCGTTACCCTGGGGCCCTCAGTATTTTTTTAATGTGGACATCTGGATCGCTAGCGGACCCAATAAGCGGAGCCGAAGATATCCGTTACGTAAACGTCGTCTTTTCGCCAGATTCTTGTGCCTGTTGTAACGTTTAATAACGGATTTATCGAAAGAACGCAGGAAGTGTCAAGAACCTGCGGGAACAAACACGATAAAATACGCGCCCGGCGAAGCGAATTAGCAAGTCTGCATCTCCAATGCAGAGCCTTGAGCAAAGGTTATCCACTGCCGCCAATAAGCGGAGCCGAAGATATCCGTTACACATCACGGAGCCCACGCTACATCCAACGCCCGACAAGGGATAATGCAAGGTTCGAGTTACGACAAATCGCAACGGGGTATCTTCCGGTGGGCCACCCTCCAAAAATACGGCTACGAGAGAGTAGGGCCCTAAAAATCACTCCCCCTACATCTTCCTCGTTCGCG')



if __name__ == '__main__':
    print('What Do You Want To Do?\n 1.Single Read\n 2.Paired Read\n\n')
    userReadTypeInput = int(input('Enter Number Of Your Choice: '))

    if userReadTypeInput == 1:
        CalculatingSingleReadAlgorithm('SingleReadsInput.txt')


    elif userReadTypeInput == 2:
        CalculatingPairedReadAlgorithm('ReadPairsInput.txt')

    else:
        print("Please Select From Menu")