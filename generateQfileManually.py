"""
Unless it is absolutely neccessary do not call any
function other than writeToFile.
Always set a key that isn't the default key.
"""

import json
import encrypt as e

Gkey = 'whatever'

def setKey(Pkey):
    """
    Global key is set. Do not use default.
    """
    global Gkey
    if type(Pkey) == str:
        for Li in Pkey:
            if Li not in 'abcdefghijklmnopqrstuvwxyz':
                print('Invalid key')
                return 1
        Gkey = Pkey
        print('\n\nKey set to: ', Pkey, '\n\nDo not forget this key. It will not be displayed again.\n\n')
        return 0
    else:
        print('Invalid key')
        return 1
    
def getNLines(Pn, Pval):
    """
    Reads n lines of ip and returns a list of strings.
    """
    temp = []
    for Li in range(Pn):
        temp.append(input(Pval + ", Line " + str(Li + 1) + ": "))
    return temp

def createRecord():
    """
    Reads questions, options and other data.
    """
    Lrecord = []

    for Li in ['Question', 'Option1', 'Option2', 'Option3', 'Option4']:
        Ls = "\nEnter the number of lines of " + Li + ": "
        while True:
            try:
                Ln = int(input(Ls))
                break
            except:
                print('Please enter a number')
        Lrecord.append(getNLines(Ln, Li))

    for Li in ['Correct answer', 'Score']:
        while True:
            try:
                Ln = int(input("\nEnter " + Li + ": "))
                if Ln in range(1,5):
                    Lrecord.append([str(Ln)])
                else:
                    print("Please enter a number in range 1-4")
                    continue
                break
            except:
                print('Please enter a number in range 1-4')
    return e.encryptRecord(Lrecord, Gkey)

def writeToFile(Pfile, Pmode = 'a'):
    """
    Write records into Pfile as json data.
    """

    if Pmode != 'a' and Pmode != 'w':
        print('Mode should be \'a\' or \'w\' only')
        return 1
    print('\n###############\n')
    while True:
        temp = setKey(input("Please enter a valid string to set as key: "))
        if temp == 0:
            break

    Lcount = 0
    fp = open(Pfile, Pmode)
    while True:
        LrecordString = json.dumps(createRecord()) + '\n'
        temp = fp.write(LrecordString)
        Lcount += 1
        while True:
            Lin = input('Add another record? (Y/N): ')
            if Lin == 'Y' or Lin == 'y' or Lin == 'N' or Lin == 'n':
                break
        if Lin == 'N' or Lin == 'n':
            break
    print(Lcount, "records created")
    return 0

writeToFile('randomactsofpizza', 'w')
