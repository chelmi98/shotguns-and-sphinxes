from os import getcwd , chdir

home = getcwd()

def readFile (path, name, strip = True):
    chdir(home + path)
    tmp = open(name)
    tmp2 = tmp.readlines()
    tmp.close()

    if strip:
        for i in range(len(tmp2)):
            tmp2[i] = tmp2[i].strip()
    else:
        for i in range(len(tmp2)):
            tmp2[i] = tmp2[i].rstrip()

    return tmp2

def readCnfg (path, name):
    chdir(home + path)
    tmp = open(name)
    tmp2 = tmp.readlines()
    tmp.close()
    tmp3 = {}

    for i in range(len(tmp2)):
        tmp2[i] = tmp2[i].strip()
        try:
            tmp3[tmp2[i][:tmp2[i].index('=')]] = int(tmp2[i][tmp2[i].index('=') + 1:])
        except:
            tmp3[tmp2[i][:tmp2[i].index('=')]] = tmp2[i][tmp2[i].index('=') + 1:]

    return tmp3

def getDesc(prefix,items):
    desc=[]; c=0
    while True:
        try:
            desc+=[items[prefix+str(c)]]
            c+=1
        except:
            return desc