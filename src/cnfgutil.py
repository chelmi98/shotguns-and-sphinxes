import os

home=os.getcwd()

def readFile(path,name):
    os.chdir(home+path)
    tmp=open(name)
    tmp2=tmp.readlines()
    tmp.close()
    tmp3={}

    for i in range(len(tmp2)):
        tmp2[i]=tmp2[i].strip()
        print(tmp2[i])
        tmp3[tmp2[i][:tmp2[i].index('=')]]=tmp2[i][tmp2[i].index('=')+1:]

    return tmp3
