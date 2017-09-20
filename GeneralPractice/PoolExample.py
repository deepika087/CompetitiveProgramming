__author__ = 'deepika'

import multiprocessing
class Solver(object):
    def __init__(self):
        print "Called init function of solver"

    def __call__(self, *args, **kwargs):
        print "In call function solver class"
        print args


pool=multiprocessing.Pool(4)
result = pool.apply_async(Solver(), args=("abc", "pqr", "lmn"))
result.get()
