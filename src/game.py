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

        self.name = stats['name']
        self.gender = stats['gender']
        self.mobtype = stats['type']
        self.health = stats['health']
        self.atkbase = stats['baseatk']
        self.atktype = stats['atktype']
        self.atkrange = stats['range']
        self.hitdesc = stats['hitdesc0']
        self.missdesc = stats['missdesc0']

bob=mob('//assets//mobs','mummie.txt')

class wep(object):
    def __init__(self,path,name):
        stats=cnfgutil.readCnfg(path,name)
        self.dmg=stats['damage']
        print(self.dmg)

def describe():
    pass

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