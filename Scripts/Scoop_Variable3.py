a=20
def fonction1():
    global a
    a=40
    print(a)

def fonction2():
    print(a)

fonction1()
fonction2()


