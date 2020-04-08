# local to local scope
def spam():
    eggs = 99
    bacon()
    print(eggs)
    #print(ham) ham is undefined

def luncheon():
    global eggs
    eggs = 43 # since global eggs is called, eggs in this changes global variable
    honey = 77
    print(eggs)
    print(honey)

def bacon():
    ham = 101
    eggs = 0

spam()

# global variable to local scope
eggs = 42
honey = 101
luncheon()
print(eggs)
print(honey)
