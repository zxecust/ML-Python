x = 50

def func():
    global x
    print('x is',x)
    x = 2
    print('Changed global x to ',x)

func()
print('Valve of x is ',x)