# scoping level 1
def my_function():
    test = 1                        # this is defined in the local scope of the function
    print('my_function:', test)

test = 0                            # this is defined in the global scope
my_function()
print ('global:', test)


# scoping level 2
def outer():
    test = 1                        # outer scope

    def inner():
        test = 2                    # inner scope
        print('inner:', test)
    inner()
    print('outer:', test)

test = 0                            # global scope
outer()
print('global:', test)


# scoping level 2 nonlocal
def outer():
    test = 1                        # outer scope

    def inner():
        # nonlocal test
        test = 2                    # nearest enclosing scope
        print('inner: ', test)
    inner()
    print('outer: ', test)
test = 0                            # global scope
outer()
print('global: ', test)


# scoping level 3 global
def outer():
    test = 1                        # outer scope

    def inner():
        global test
        test = 2                    # global scope
        print('inner:', test)
    inner()
    print('outer:', test)
test = 0                            # global scope
outer()
print('global:', test)
