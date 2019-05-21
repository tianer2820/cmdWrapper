import cmdWrapper


# define a call back function
def func(args):
    print(args)


# initiallize a Wrapper object
wrapper = cmdWrapper.Wrapper('my test wrapper')

# add different entries
wrapper.add_int('int1')
wrapper.add_int('int2')
wrapper.add_float('float1')
wrapper.add_open_file('open1')
wrapper.add_save_file('open2')

# bind our functions to the wrapper
wrapper.bind(func)

# show it
wrapper.show()
