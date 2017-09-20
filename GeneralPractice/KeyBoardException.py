__author__ = 'deepika'


def test_keyboardException():

    try:
        count = 1000000
        while count >= 0:
            count = count - 1
            print "Count is now : ", count
    except KeyboardInterrupt as ex:
        print "CAUGHT KEYBOARD EXCEPTION : ", ex
        print type(ex)
        print ex.args

test_keyboardException()