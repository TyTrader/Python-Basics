x = 'Tyson is awesome'  # This is a global variable


def myfunc():
    x = 'tyso is not awesome'  # This is a local variable defined within the myfunc() function
    print('who told you that ' + x)


myfunc()

print('news is that ' + x)
