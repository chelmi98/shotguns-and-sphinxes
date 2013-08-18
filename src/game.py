import random

running=True

class mob(object):
    def __init__(self,race,name,gender,maxhealth,baseattack):
        self.race=race
        self.name=name
        self.gender=gender
        self.maxhealth=maxhealth
        self.health=maxhealth
        self.baseattack=baseattack
        self.dead=False
        self.seen=False

    def attack(self,target):
        if target.dead==False:
            if random.randint(1,2)==2:
                target.health-=self.baseattack
                print('You hit the '+target.race+'.')
            else:
                print('You miss the '+target.race+'.')
        else:
            print('The '+target.race+' is already dead.')

    def update(self):
        if self.health<0 and self.dead==False:
            self.health=0
            self.dead=True
            print('The '+self.race+' is dead.')

    def describe(self):
        if self.seen==False:
            print('You see a '+self.race)
            self.seen=True

you=mob('human','player','m',100,20)

mobs=[]
mobs+=[mob('beetle','none','m',50,10)]

def describe():
    for i in mobs:
        i.describe()

def tick(response):
    response=response.lower()
    response=response.split(' ')
    if response[0]=='attack':
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
    if response=='quit':
        if confirm():
            running=False
    else:
        tick(response)