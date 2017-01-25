# key points argument passing
x = 3

def func(y):
    print(y)
func(x)              # prints: 3


# key.points.assignment
x = 3
def func(x):
    x = 7           # defining a local x, not changing the global one

print func(x)
print(x)            # prints: 3


# key.points.mutable.py
x = [1, 2, 3]
def func(x):
    x[1] = 42       # this affects the caller!

func(x)
# func(x)
print(x)            # prints: [1, 42, 3]


# key.points.mutable.assignment.py
x = [1, 2, 3]

def func(x):
    x[1] = 42               # this changes the caller!
    x = 'something else'    # this points x to a new string object

func(x)
print(x)                    # still prints: [1, 42, 3]


# arguments.positional.py
def func(a, b, c):
    print (a, b, c)
func(1, 2, 3)               # prints 1 2 3


# arguments.keyword.py
def func(a, b, c):
    print(a, b, c)
func(a=1, c=2, b=3)         # prints: 1 3 2


# arguments.default.py
def func(a, b=4, c=88):
    print(a, b, c)

func(1)                      # prints: 1 4 88
func(b=5, a=7, c=9)          # prints: 7 5 9
func(42, c=9)                # prints: 42 4 9
# func(b=1, c=2, 42)         # positional argument after keyword one


# arguments.variable.positional.py
def minimum(*n):
    print(n)        # n is a tuple
    if n:             # explained after the code
        mn = n[0]
        for value in n[1:]:
            if value < mn:
                mn = value
        print(mn)

minimum(1, 3, -7, 9)        # n = (1, 3, -7, 9) - prints: -7
minimum()                   # n = () - prints: nothing


# arguments.variable.positional.unpacking.py
def func(*args):
    print(args)

values = (1, 3, -7, 9)
func(values)                # equivalent to: func((1, 3, -7, 9))
func(*values)               # equivalent to: func(1, 3, -7, 9)


# arguments.variable.keyword.py
def func(**kwargs):
    print(kwargs)
# All calls equivalent. They print: {'a': 1, 'b': 42}
func(a=1, b=42)
func(**{'a': 1, 'b': 42})
func(**dict(a=1, b=42))


# arguments.variable.db.py
def connect(**options):
    conn_params = {
        'host': options.get('host', '127.0.0.1'),
        'port': options.get('port', 5432),
        'user': options.get('user', ''),
        'pwd': options.get('pwd', ''),
    }

    print(conn_params)
    # we then connect to the db (commented out)
    # db.connect(**conn_params)

connect()
connect(host='127.0.0.42', port=5433)
connect(port=5431, user='fab', pwd='gandalf')


# arguments.all.py
def func(a, b, c=7, *args, **kwargs):
    print('a, b, c:', a, b, c)
    print('args:', args)
    print('kwargs:', kwargs)

func(1, 2, 3, *(5, 7, 9), **{'A': 'a', 'B': 'b'})
func(1, 2, 3, 5, 7, 9, A='a', B='b')                    # same as previous one


# arguments.all.kwonly.py
# def func_with_kwonly(a, c, b=42, d=256, *args, **kwargs):
#    print('a, b:', a, b)
#    print('c, d:', c, d)
#    print('args:', args)
#    print('kwargs:', kwargs)

# both calls equivalent
# func_with_kwonly(3, 42, c=0, d=1, *(7, 9, 11), e='E', f='F')
# func_with_kwonly(3, 42, *(7, 9, 11), c=0, d=1, e='E', f='F')


# arguments.defaults.mutable.py
def func(a=[], b={}):
    print(a)
    print(b)
    print('#' * 12)
    a.append(len(a))    # this will affect a's default value
    b[len(a)] = len(a)  # and this will affect b's one

func()
func()
func()

# arguments.defaults.mutable.intermediate.call.py
func()
func(a=[1, 2, 3], b={'B': 1})
func()


# arguments.defaults.mutable.no.trap.py
def func(a=None):
    if a is None:
        a = []
    # do whatever you want with `a` ...


# 