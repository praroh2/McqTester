import json

def main(Pfile):
    temp = open(Pfile).readlines()
    Ltemp = []
    for Li in temp:
        Ltemp.append(json.loads(Li))
    return Ltemp
