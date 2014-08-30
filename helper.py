import encrypt as e
import json, random, copy

def askQ(Precord, Pkey):
    """
    Decrypts the contents of the question, displays it and takes input.
    """
    global Gscore, Gtotal
    print('\n#################################################################\n')
    Lrecord = e.decryptRecord(Precord, Pkey)

    Lscore = int(Lrecord[6][0])
    
    print('\n\nQuestion:')
    for Li in Lrecord[0]:
        print(Li)
    print('\nOption 1:')
    for Li in Lrecord[1]:
        print(Li)
    print('\nOption 2:')
    for Li in Lrecord[2]:
        print(Li)
    print('\nOption 3:')
    for Li in Lrecord[3]:
        print(Li)
    print('\nOption 4:')
    for Li in Lrecord[4]:
        print(Li)
    
    while True:
        Lsel = input("\nEnter choice: ")
        if Lsel == '1' or Lsel == '2' or Lsel == '3' or Lsel == '4':
            if int(Lsel) == int(Lrecord[5][0]):
                Gscore += Lscore
            Gtotal += Lscore
            return 0
        elif Lsel == '0':
            Lconf = input('Are you sure that you want to answer this question later? (Y/N): ')
            if Lconf == 'Y' or Lconf == 'y':
                return 1
        else:
            print('Enter a number in the range 0-4.\n0 to answer the question later')

    
def main(Pqs, Pkey, Pusn, Pno):
    """

    """
    global Gscore, Gtotal
    
    if Pno:
        Gscore = 0
        Gtotal = 0
    else:
        temp = Pqs.pop()
        Gscore = int(temp[0])
        Gtotal = int(temp[1])

    random.shuffle(Pqs)
    
    while len(Pqs) > 0:
        temp = copy.deepcopy(Pqs[-1])
        Lstat = askQ(temp, Pkey)
        if Lstat == 0:
            Pqs.pop()
        elif Lstat == 1:
            Pqs.insert(0, Pqs.pop())

        fp = open(Pusn, "w")
        for Li in Pqs:
            temp = json.dumps(Li) + '\n'
            fp.write(temp)
        fp.write(json.dumps([str(Gscore), str(Gtotal)]))
        fp.close()
        
    if len(Pqs) == 0:
        print('\n#################################################################\nDone\n\nScore =', Gscore, '/', Gtotal, '(', Gscore*100.0/Gtotal, '% )')
