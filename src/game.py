import random
import cnfgutil

title=cnfgutil.readFile('//assets','title.txt',False)
for i in title:
    print(i)
print('')

running = True

def confirm():
    print('Are you sure?')
    if raw_input('>>> ')[0] in ('y','Y'):
        return(True)
    else:
        return(False)

def getDesc(prefix,items):
    desc=[]; c=0
    while True:
        try:
            desc+=[items[prefix+str(c)]]
            c+=1
        except:
            return desc

class player(object):
    def __init__(self):
        self.health=100
        self.mp=100
        self.str=5 #used for damage and brute strength stuff
        self.dex=5 #used for determining if hits land, and speed
        self.int=5 #determines magic skill
        self.backpack=[]

    def update(self):
        if self.health<=0:
            print('You died.')
            input('press enter to close the program')
            exit()

    def attack(self,target):
        if not target.dead:
            if random.randint(0,2)==0:
                target.health-=10
                print('You hit for '+str(10)+' damage.')
            else:
                print('You miss.')
        else:
            print('The target is dead.')

class mob(object):
    def __init__(self,path,name):
        stats=cnfgutil.readCnfg(path,name)

        self.desc=getDesc('desc',stats)
        self.deaddesc=getDesc('deaddesc',stats)
        self.health=stats['health']
        self.dead=False

    def update(self):
        if self.health<=0:
            self.dead=True

    def attack(self,target):
        if not self.dead:
            if random.randint(0,2)==0:
                target.health-=10
                print('It hits for '+str(10)+' damage.')
            else:
                print('It misses.')

    def describe(self):
        if not self.dead:
            print self.desc[random.randint(0,len(self.desc)-1)],
        else:
            print self.deaddesc[random.randint(0,len(self.deaddesc)-1)],

class room(object):
    def __init__(self,contents):
        self.contents=contents

    def describe(self):
        for i in self.contents:
            i.describe()

you=player()
stuff=[]
stuff+=[mob('//assets//mobs','mummie.txt')]
entry=room(stuff)

def describe():
    entry.describe()
    print('')

def tick(response):
    global running
    response=response.lower()
    response=response.split(' ')

    timetick=False

    if response[0]=='quit':
        if confirm():
            running=False
    elif response[0]=='attack':
        timetick=True
        you.attack(entry.contents[0])
    else:
        print(response[0]+' isnt a command.')

    if timetick:
        entry.contents[0].update()
        entry.contents[0].attack(you)
        you.update()

while running:
    describe()
    print('What would you like to do?')
    response=raw_input('>>> ')
    tick(response)