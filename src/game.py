running=True

def describe():
    print('You see a cat.')

def tick(response):
    response=response.lower()
    response=response.split(' ')
    print response

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