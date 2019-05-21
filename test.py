import cmdWrapper


def func(args):
    print(args)


wrapper = cmdWrapper.Wrapper('my test wrapper')
wrapper.add_int('int1')
wrapper.bind(func)
wrapper.show()
