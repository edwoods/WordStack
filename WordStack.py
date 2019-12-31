import re

def transposeStack(stackWords):
    result = []

    for col,value in enumerate(stackWords[0]):
        newWord = ""
        for row in range(0, len(stackWords)):
            x = len(stackWords[row])
            if len(stackWords[row]) <= col:
                break

            char = stackWords[row][col]
            if char == ' ':
                break

            newWord += char

        result.append(newWord)

    print(result)
    return result

def FormatAllWords():
    wordFile = open("words.txt",'r')
    words = wordFile.readlines()
    wordFile.close()

    # words = [x[:-1] for x in words]   # remove the carriage return

    words3orMore = []
    for word in words:
        x = len(word)
        if len(word) < 3:
            x = 0
        else:
            words3orMore.append(word)

    words3orMore.sort(key=WordLen)

    wordFile = open("words3.txt",'w')
    wordFile.writelines(words3orMore)
    wordFile.close()

#-------------------------------------------------------
def lookForWords(stack, words):
    for isw, sw in enumerate(stack):
        for word in words:
            if len(word) > len(sw):
                break

            ichar = sw.find(word)
            if ichar == -1:
                continue
            else:
               print(isw, ' ', ichar, ' ', sw + " " + word)

        # elif word in sw:
            #     print(sw + " " + word)

    # try reversed stack words
    for isw, sw in enumerate(stack):
        sw = sw[::-1]
        for word in words:
            if len(word) > len(sw):
                break

            ichar = sw.find(word)
            if ichar == -1:
                continue
            else:
                print(isw, ' ', ichar, ' ', sw + " " + word)

def LoadStack(MainWin):
    # read the word stack
    wordFile = open("word stack.txt", 'r')
    MainWin.stack = wordFile.readlines()
    wordFile.close()

    MainWin.stack = [x[:-1] for x in MainWin.stack]  # remove the carriage return
    MainWin.stack = [x.strip() for x in MainWin.stack if x.strip()]  # remove empty lines

    MainWin.stack2 = transposeStack(MainWin.stack)

    MainWin.nRows = len(MainWin.stack)
    MainWin.nCols = len(MainWin.stack[0])

    # put the letters on the display
    for iword, word in enumerate(MainWin.stack):
        row = 14 - iword
        for iltr, letter in enumerate(word[::]):
            MainWin.SetButton(row, iltr, letter, [255,0,0])
            x = 0


def SolveWordStack(MainWin):
    # read the word stack
    wordFile = open("word stack.txt", 'r')
    stack = wordFile.readlines()
    wordFile.close()

    stack = [x[:-1] for x in stack]   # remove the carriage return
    stack2 = transposeStack(stack)

    wordFile = open("words3.txt", 'r')
    words = wordFile.readlines()
    wordFile.close()

    words = [x[:-1] for x in words]   # remove the carriage return

    lookForWords(stack, words)
    lookForWords(stack2, words)

    # for sw in stack:
    #     for word in words:
    #         if len(word) > len(sw):
    #             break
    #         elif word is sw:
    #             print(sw + " " + word)
    #
    # # try reversed stack words
    # for sw in stack:
    #     sw = sw[::-1]
    #     for word in words:
    #         if len(word) > len(sw):
    #             break
    #         elif word is sw:
    #             print(sw + " " + word)


# wordFile = open("words.txt",'r')
# words = wordFile.readlines()
# wordFile.close()
#
# words3orMore = [];
# for word in words:
#     x = len(word)
#     if len(word) < 4:
#         x = 0
#     else:
#         words3orMore.append(word)
#
# wordFile = open("words3.txt",'w')
# wordFile.writelines(words3orMore)
# wordFile.close()

def WordLen(word):
    return len(word)

#-------------------------------------------------------------
# FormatAllWords()
# SolveWordStack()
