def exists(Pfname):
    """
    Checks whether the given file exists.
    This file contains questions.
    """
    try:
        open(Pfname, 'r')
        return True
    except:
        print('Invalid question set\n')
        return False

def checkKey(Pkey):
    """
    Checks whether the given key is correct for the given question set.
    Not required anymore. Maybe later?
    """
    return True
    
def main(Pctrl):
    """
    Pctrl = True for new session. Old session will be reset.
    """
    print('\n#################################################################\nLogin:')
    while True:
        if Pctrl:
            Lusn = input("Enter USN: ")
            Lfile = input("Select question set: ")
            Lkey = input("Enter key: ")
            print('\n#####\nUSN:         ', Lusn)
            print('Question set:', Lfile)
            print('Key:         ', Lkey)
            corr = input("\nIs that right? You may not be able to change it later. (Y/N): ")
            if corr == "y" or corr == "Y":
                if exists(Lfile) and checkKey(Lkey):
                    return [Lusn, Lfile, Lkey]
        else:
            Lusn = input("Enter USN: ")
            Lkey = input("Enter key: ")
            print('\n#####\nUSN: ', Lusn)
            print('Key: ', Lkey)
            corr = input("Is that right? You may not be able to change it later. (Y/N): ")
            if corr == "y" or corr == "Y":
                if exists(Lusn) and checkKey(Lkey):
                    return [Lusn, Lusn, Lkey]
