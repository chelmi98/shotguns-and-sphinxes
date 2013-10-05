import random
import cnfgutil

title=cnfgutil.readFile('//assets','title.txt',False)
for i in title:
    print(i)
print('')

running = True

class mob(object):
    def __init__(self,path,name):
        stats=cnfgutil.readCnfg(path,name)

        self.desc=[]; c=0
        while True:
            try:
                self.desc+=[stats['desc'+str(c)]]
                c+=1
            except:
                break

    def describe(self):
        print(self.desc[random.randint(0,len(self.desc)-1)])

##class wep(object):
##    def __init__(self,path,name):
##        stats=cnfgutil.readCnfg(path,name)
##        self.dmg=stats['damage']
##        print(self.dmg)

class room(object):
    def __init__(self,contents):
        self.contents=contents

    def describe(self):
        for i in self.contents:
            i.describe()

bob=mob('//assets//mobs','mummie.txt')
entry=room([bob])

def describe():
    entry.describe()

def tick(response):
    global running
    response=response.lower()
    response=response.split(' ')

    if response[0]=='quit':
        if confirm():
            running=False
    else:
        print(response[0]+' isnt a command.')

def confirm():
    print('Are you sure?')
    if raw_input('>>> ')[0] in ('y','Y'):
        return(True)
    else:
        return(False)

while running:
    describe()
    print('What would you like to do?')
    response=raw_input('>>> ')
    tick(response)