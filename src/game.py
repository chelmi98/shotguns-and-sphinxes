import random

running=True

class mob(object):
    def __init__(self,race,name,gender,maxhealth,baseattack):
        self.race=race
        self.name=name
        if name=='none':
            self.title='the '+race
        else:
            self.title=name
        self.gender=gender
        self.maxhealth=maxhealth
        self.health=maxhealth
        self.baseattack=baseattack
        self.dead=False
        self.seen=False

    def attack(self,target):
        if target.dead==False:
            if random.randint(1,3)==3:
                print('You miss '+target.title+'.')
            else:
                target.health-=self.baseattack
                print('You hit '+target.title+'.')
        else:
            print(target.title+' is already dead.')

    def update(self):
        if self.health<0 and self.dead==False:
            self.health=0
            self.dead=True
            print(self.title+' is dead.')

    def describe(self):
        if self.seen==False:
            print('You see '+self.title+'.')
            self.seen=True

you=mob('human','player','m',100,20)

mobs=[]
mobs+=[mob('beetle','none','m',50,10)]

def describe():
    for i in mobs:
        i.describe()

def tick(response):
    global running
    response=response.lower()
    response=response.split(' ')

    if response[0]=='quit':
        if confirm():
            running=False
    elif response[0]=='attack':
        you.attack(mobs[0])
        mobs[0].update()
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