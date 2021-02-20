__author__ = 'deepika'

from kazoo.client import KazooClient
import thread
import time

zoo_path = '/MyPath'

def create_path():
    zk.ensure_path(zoo_path)

def create_child(num):
    zk.ensure_path(zoo_path + '/NodeChild' + str(num))
    return

def delete_child(num):
    zk.delete(zoo_path + '/NodeChild' + str(num))
    return

zk = KazooClient(hosts='localhost:2181')
zk.start()

create_path()

#apply watch and then start thread


def modify_child_in_path(threadName):

    print "inside thread: ", threadName
    k = 1
    while k < 10:
        print "creating child k : ", k
        create_child(k)
        k = k + 1
        time.sleep(1)

    k = 9
    while k > 0:
        print "deleting child k : ", k
        delete_child(k)
        k = k - 1
        time.sleep(1)

def watch_path(threadName):

    print "inside thread: ", threadName

    @zk.ChildrenWatch(zoo_path)
    def child_watch_func(children):
        print "Inside watch function"
        print "List of Children %s" % children


thread.start_new_thread( watch_path, ("Thread-2", ) )
time.sleep(5)
print "Starting modify path call"
thread.start_new_thread( modify_child_in_path, ("Thread-1", ) )

time.sleep(10000)

print "END"
