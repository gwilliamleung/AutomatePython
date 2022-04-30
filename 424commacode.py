spam = ['apples','bananas', 'tofu', ' cats']
def commaCode(someList):
    commaList = ''
    for i in range(len(someList)):
        if i == (int(len(someList)-1)):
            commaList+= 'and'+ someList[i]
        else:
            commaList+= someList[i]+ ', '
    print(commaList)

commaCode(spam)

