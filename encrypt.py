"""
Implements a modified version of Caesar shift.
It is not very secure.
"""

import transformation as tr

def decryptRecord(Precord, Pkey):
    """
    Takes an encrypted record and returns a decrypted one.
    """
    Lrecord = []
    for Li in Precord:
        temp = []
        for Lj in Li:
            temp.append(decrypt(Lj, Pkey))
        Lrecord.append(temp)
    return Lrecord

def encryptRecord(Precord, Pkey):
    """
    Takes a record, and returns an encrypted record.
    """
    Lrecord = []
    for Li in Precord:
        temp = []
        for Lj in Li:
            temp.append(encrypt(Lj, Pkey))
        Lrecord.append(temp)
    return Lrecord

def rstr(Pstr):
    """
    Reverse a string
    """
    Lt = ''
    for Li in range(len(Pstr)-1, -1, -1):
        Lt += Pstr[Li]
    return Lt

def encrypt(Pstr, Pkey):
    """
    Encrypts a string Pstr based on key Pkey.
    """
    for Li in Pkey:
        temp = ''
        for Lj in Pstr:
            try:
                temp += tr.Gtrans[Li][Lj]
            except:
                temp += Lj
        Pstr = temp
    return Pstr
    

def decrypt(Pstr, Pkey):
    """
    Decrypts a string Pstr based on key Pkey.
    """
    Pkey = rstr(Pkey)
    for Li in Pkey:
        temp = ''
        for Lj in Pstr:
            try:
                temp += tr.Gitrans[Li][Lj]
            except:
                temp += Lj
        Pstr = temp
    return Pstr
