__author__ = 'deepika'

"""
We want to create a simple job scheduler that runs tasks after a specified amount of time. It should implement an interface like this:
interface JobScheduler {
  void schedule(Runnable task, long delayMs);
}

I learnt the difference between wait and sleep.
+ I also learnt that I don't know how to use heapq map
"""

import time
import heapq
import thread
import threading


class Job:
    def __init__(self, task, delayMs):
        self.task = task
        self.delayMs = delayMs
        self.absoluteTimestamp = None

class JobScheduler:

    def consumer():
        while True:
            with self.lock:
                if len(self.heap) == 0:
                    wait()
                elif self.heap[0].absoluteTimestamp < time.time() * 1000:
                    wait(time.time() * 1000 - self.heap[0].absoluteTimestamp)
                else:
                    job = heapq.pop(self.heap)
                    job.start()

    def __init__(self):
        # datastructure for heapify
        self.heap = []
        t1 = Thread(target = self.consumer)
        t1.start()
        self.lock = threading.lock()


    def schedule(self, job):
        # 1.) Find the absolute time.
        current_time = time.time() * 1000
        absolute_time = current_time + job.delayMs

        job.absoluteTimestamp = absolute_time

        # 2.) Put it on the Proprity Queue and heapify

        with self.lock:
            heapq.heappush(self.heap, job)
            notify_all()


t1 = Thread
j1 = Job(t1, 100)
j2 = Job(t2, 5)
j3 = Job(t3, 2)



js = JobScheduler()
js.schedule(j1)
js.schedule(j2)
js.schedule(j3)

