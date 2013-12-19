import json
import random
import sys
from cnfgutil import *
from os import getcwd , chdir

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
            if random.randint(0, 2) == 0:
                target.hp-=10
                print('You hit for '+str(10)+' damage.')
            else:
                print('You miss.')
        else:
            print('The target is dead.')


class mob():
    def __init__(self, path, name):
        stats = readCnfg(path, name)

        self.desc = getDesc('desc', stats)
        self.deaddesc = getDesc('deaddesc', stats)
        self.hp = stats['health']
        self.inventory = []
        self.dead = False

    def update(self):
        if self.hp <= 0:
            self.dead=True

    def attack(self, target):
        if not self.dead:
            if random.randint(0, 2) == 0:
                target.hp -= 10
                print('It hits for ' + str(10) + ' damage.')
            else:
                print('It misses.')

    def describe(self):
        if not self.dead:
            print self.desc[random.randint(0, len(self.desc) - 1)],
        else:
            print self.deaddesc[random.randint(0, len(self.deaddesc) - 1)],


class room():
    def __init__(self,contents):
        self.contents=contents

    def describe(self):
        pass


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
    print('')


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
    else:
        print(response[0] + ' isnt a command.')

    if timetick:
        you.location.contents[0].update()
        you.location.contents[0].attack(you)
        you.update()


if __name__ == '__main__':
    home = getcwd()
    stuff = []
    stuff += [mob(home+'//assets//mobs','mummie.txt')]
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
