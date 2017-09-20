__author__ = 'deepika'

import unittest as unit
from mock import  Mock, patch

import MainClass as mc

class MainClassTest(unit.TestCase):
    def testSayHello(self):
        patcher = patch('MainClass.mcp').start()
        patcher.say_hello.return_value = "I will not say hello"
        mc.mainFunction()
        print "finished"


