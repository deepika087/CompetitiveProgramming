
#First class functions allow us to treat functions like any other objects.
# for example we can pass them, return them
def html_tag(msg1):

    def wrap_text(msg2):
        print " Main msg is : ", msg1, " Your msg is : ", msg2

    return wrap_text

print_main = html_tag('h1')
print_main('Deepika')
print_main('anand')
# print_main() Wrong

# A clousure is an inner function such that it remembers the values set in outer functions. Even if the outer function
# has finshed executing.
# A clousre closes free variables in their environment.closure take advantage of first class functions.

def outer_func(msg):
    message = msg #Message is a free variable

    def inner_func():
        print " Message is : ", message
    return inner_func

hi_func = outer_func('Hi')
hello_func = outer_func('Hello')

hi_func()
hello_func()

#Clousre example 2
def logger(func):

    def log_func(*args):
        print " Running {} with argument {}".format(func.__name__, args)
        #print ( " Calling function ")
        print func(*args)
    return log_func

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

add_logger = logger(add)
sub_logger = logger(sub)

add_logger(3,3)
sub_logger(4,3)



def decorator_function(input_function):
    def wrapper_function():
        print "Executing sample line before function {}".format(input_function.__name__)
        input_function()
    return wrapper_function

def decorator_function1(input_function):
    def wrapper_function(*args, **kwargs):
        print "Custom sample line before function {}".format(input_function.__name__)
        input_function(*args, **kwargs)
    return wrapper_function

@decorator_function1 #Same as saying  display = decorator_function(display)
def display():
    print " Display function"

@decorator_function1
def specialDisplay(name, age):
    print "Special display with name {} and age {}".format(name,age)

@decorator_function
def my_display():
    print " Custom display"

#print " Lets's see", commenting the lines prints nothing
display()
my_display()
specialDisplay('john', 100)

#from functools import wraps - to preserve the original functions

#the inside function of wrapper function will be decorated with @wraps(Thefunctionyouwanttopreserve)

