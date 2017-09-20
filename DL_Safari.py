import theano
from theano import tensor as T, function

import numpy as np

def simpleFunction():
    X=T.matrix('x')
    Y=X**2
    F = function([X], [Y])
    print X
    print Y
    print F

    x=np.ones((2,2))*3
    y=F(x)
    print "========"
    print x
    print y

def simpleFunctionWithDerivative():
    X=T.matrix('x')
    Y=X**2
    Z = T.grad(Y.sum(), X)
    F = function([X], [Y, Z])

    x=np.ones((2,2))*3
    y, z =F(x)
    print "========"
    print x
    print y
    print z

simpleFunctionWithDerivative()

