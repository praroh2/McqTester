"""
Unless it is absolutely neccessary do not call any
function other than writeToFile.
Always set a key that isn't the default key.
"""

import json
import encrypt as e

Gkey = 'whatever'

def checkExists(PfName):
    """
    Checks if a file exists.
    """
    try:
        open(PfName)
        return True
    except:
        return False

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

def helper(PifName, PofName, Pmode):
    Lrecs = open(PifName).readlines()
    fp = open(PofName, Pmode)
    for Li in Lrecs:
        temp = Li.split('######')[:-1]
        if len(temp) != 7:
            print("Size: Invalid entry:", temp, '\n\n')
            continue
        try:
            if int(temp[-1]) not in range(1,5) or int(temp[-2]) not in range(1,5):
                print("Range: Invalid entry:", temp, '\n\n')
                continue
        except:
            print("Type: Invalid entry:", temp, '\n\n')
            continue
        Lrecord = []
        for Lj in temp:
            Lrecord.append(Lj.split('###'))
        Lrecord = e.encryptRecord(Lrecord, Gkey)
        fp.write(json.dumps(Lrecord) + '\n')

def main():
##    while True:
##        temp = setKey(input("Please enter a valid string to set as key: "))
##        if temp == 0:
##            break
##    while True:
##        LifName = input("Enter the name of the input file: ")
##        if checkExists(LifName):
##            break
##        else:
##            print('Please check the filename.')
##    LofName = input("Enter the name of the output file: ")
##    while True:
##        Lmode = input("Enter mode (a/w): ")
##        if Lmode == 'a' or Lmode == 'w':
##            break
##        else:
##            print('Please enter a valid mode.')
##    helper(LifName, LofName, Lmode)
    setKey("pizza")
    helper("abc", "randomactsofpizza.txt", "w")

main()
print('Done')
