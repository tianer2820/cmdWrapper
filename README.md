# cmdWrapper
cmdWrapper is a very simple python gui lib based on wxpython. It allows programmers to create simple gui wrappers for their command line program.


### What is this
Having a gui makes your app looks better and makes it more user friendly, however, makeing a GUI is difficult and time consuming. CmdWrapper lets you create simple gui wrappers for command line apps.

### What it looks like
![test1.py](/screen_shots/test1.png)
![test2.py](/screen_shots/test2.png)

### How to use
Here is a example of how to use this lib: 
```
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
```
What the lib is doing is just getting inputs from the user. By adding different "entries", you can get different types of data. See more exmaples in [examples](/examples)
