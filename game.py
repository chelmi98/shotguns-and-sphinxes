import json
import random
import sys
from os import getcwd

class player():
    def __init__(self, location):
        self.hp = 100 # hit points
        self.mp = 100 # mana points
        self.STR = 5 # used for damage and brute strength stuff
        self.DEX = 5 # used for determining if hits land, and speed
        self.INT = 5 # determines magic skill
        self.inventory = []
        self.equiped = []
        self.location = location

    def update(self):
        if self.hp <= 0:
            print('You died.')
            input('Press enter to quit.')
            sys.exit()

    def attack(self,target):
        if not target.dead:
            target.target = self
            if random.randint(0, 2) == 0:
                target.hp-=10
                print('You hit for ' + str(10) + ' damage.')
            else:
                print('You miss.')
        else:
            print('The target is dead.')


class mob():
    def __init__(self, path, name):
        stats = loadJson(path, name)

        self.desc = stats['descriptions']['alive']
        self.deaddesc = stats['descriptions']['dead']
        self.described = False

        self.hp = stats['health']
        self.basedmg = stats['attack']['basedmg']
        self.inventory = []
        self.dead = False

        self.target = None

    def update(self):
        if not self.dead:
            if self.hp <= 0:
                self.dead = True
                self.described = False
            else:
                # AI stuff goes here
                if self.target:
                    self.attack(self.target)

    def attack(self, target):
        if not self.dead:
            if random.randint(0, 2) == 0:
                target.hp -= self.basedmg
                print('It hits for %i damage.' % self.basedmg)
            else:
                print('It misses.')

    def describe(self, passive = True):
        if passive:
            if not self.described:
                self.described = True
            else:
                return

        if not self.dead:
            print self.desc[random.randint(0, len(self.desc) - 1)]
        else:
            print self.deaddesc[random.randint(0, len(self.deaddesc) - 1)]


class room():
    def __init__(self,contents):
        self.contents=contents

    def describe(self):
        pass


def readFile (path, name, strip = True):
    tmp = open(path + '\\' + name)
    tmp2 = tmp.readlines()
    tmp.close()

    if strip:
        for i in range(len(tmp2)):
            tmp2[i] = tmp2[i].strip()
    else:
        for i in range(len(tmp2)):
            tmp2[i] = tmp2[i].rstrip()

    return tmp2


def loadJson(path, name):
    f = open(path + '\\' + name)
    j = json.load(f)
    f.close()
    return j


def confirm():
    print('Are you sure?')
    if raw_input('>>> ')[0] in ('y','Y'):
        return(True)
    else:
        return(False)


def describe():
    you.location.describe()
    for i in you.location.contents:
            i.describe()


def tick(response):
    global running
    response = response.lower()
    response = response.split(' ')

    timetick = False

    if response[0] == 'quit':
        if confirm():
            running = False
    elif response[0] == 'attack':
        timetick = True
        you.attack(you.location.contents[0])
    elif response[0] == 'wait':
        timetick = True
        print('You wait for a moment before continuing.')
    else:
        print(response[0] + ' isnt a command.')

    if timetick:
        for i in you.location.contents:
            i.update()

        you.update()


if __name__ == '__main__':
    home = getcwd()
    stuff = []
    stuff += [mob(home+'//assets//mobs', 'mummie.json')]
    entry = room(stuff)
    you = player(entry)

    # prints title
    title = readFile(home+'//assets//misc', 'title.txt', False)
    for i in title:
        print(i)
    print('')

    running = True
    while running:
        describe()
        print('What would you like to do?')
        response=raw_input('>>> ')
        tick(response)
