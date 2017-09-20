__author__ = 'deepika'

#Clousures:
#Inner function has access to variables even when outer function's scope has exited.
#this access of free variables by a function is called a clourse

# A clousure closes over free variable in its environment.. 

def outer_func():
    mydummyVar = "Hello world ! "

    def inner_func():
        print (mydummyVar) #Free variable as it was not defined within this scope.
    return inner_func


my_func = outer_func()
