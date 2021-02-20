__author__ = 'deepika'


"""
Amazon will start a new marketing
campaign targeting customers
according to their purchasing
profiles.

This campaign has 3 kinds of
messages each one targeting one
group of customers:

Message 1 - targets the 25% of
customers that spend the most at the
site

Message 2 - targets the 25% of
customers that spend the least at the
site

Message 3 - targets the rest of the
customers.

Given a list of purchases made during
a period of time, write a program that
sends the correct message to each
customer that purchased
anything during that period.

Each purchase in this list features
the customer id, the purchase
amount among other information.

The API to send messages to customers
follows below:
MessageSender.send(customerId, messageId)
"""

class Node:
    def __init__(self, id, amount):
        self.customer = id
        self.puracheAmount = amount
        self.left = None
        self.right = None

class MessageSender:
    def __init__(self):
        self.root = None
        self.size = 0

    def _insert_procedure(self, root, newNode):
        if root is None:
            return newNode

        if root.puracheAmount < newNode.puracheAmount:
            root.right = self._insert_procedure(root.right, newNode)
        else:
            root.left = self._insert_procedure(root.left, newNode)
        return root

    def registerPayment(self, cid, amount):

        newNode = Node(cid, amount)
        if self.root is None:
            self.root = newNode

        else:
            self._insert_procedure(self.root, newNode)
        self.size += 1

    def fetch_categories(self):

        result_top = []
        result_overall = []

        k = int(0.25 * self.size)
        self._fetch_top_25_util(self.root, k, result_top, result_overall)
        print("Top 25% are", result_overall[0:k] )
        print("Bottom 25% are", result_overall[self.size-k:] )
        print("Overall ", result_overall[k:self.size-k] )

    def _fetch_top_25_util(self, root, k, result_top, result_overall):
        if root is None:
            return

        self._fetch_top_25_util(root.right, k - 1, result_top, result_overall)
        #if k == 0:
        #    result_top.append((root.customer, root.puracheAmount)  )
        #else:
        result_overall.append( (root.customer, root.puracheAmount) )
        self._fetch_top_25_util(root.left, k - 1, result_top, result_overall)


m = MessageSender()
m.registerPayment(1, 10)
m.registerPayment(2, 100)
m.registerPayment(3, 300)
m.fetch_categories()
m.registerPayment(4, 20)
m.registerPayment(5, 19)
m.registerPayment(6, 5)
print("------------")
m.fetch_categories()
m.registerPayment(7, 1000)
m.registerPayment(8, 209)
print("------------")
m.fetch_categories()
"""
('Top 25% are', [])
('Bottom 25% are', [])
('Overall ', [(3, 300), (2, 100), (1, 10)])
------------
('Top 25% are', [(3, 300)])
('Bottom 25% are', [(6, 5)])
('Overall ', [(2, 100), (4, 20), (5, 19), (1, 10)])
------------
('Top 25% are', [(7, 1000), (3, 300)])
('Bottom 25% are', [(1, 10), (6, 5)])
('Overall ', [(8, 209), (2, 100), (4, 20), (5, 19)])
"""