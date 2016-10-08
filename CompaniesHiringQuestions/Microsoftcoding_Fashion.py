"""
Microsoft coding challenge

You are a member of the proud Xorthol race, a species whose members choose friends entirely based on their hat collections.

A group of Xortholian freshman have just moved into their dorms and are having trouble finding a best friend. Each refuses to make friends with any Xortholian who owns a hat they find distasteful.

Your task is to find pairs of Xortholians such that each Xortholian in a pair won't find any distasteful hat owned by their new best friend.

Fortunately for you, Xortholians are picky to the point that they'll find most other Xortholians to be distasteful. As a result, they'll go along with the first (and likely only) potential friend they can find. This order is given in the input: the first Xortholian in the list will take the first possible friend in list order, then the second Xortholian will take the first possible friend from the remaining other Xortholians, and so on.

There will always be a solution.

Input definition

Each input file for this problem will contain between 150 and 300 lines (inclusive).

In particular, for each i in 0 <= i <= 50:

Lines 3 * i will have the name of a Xortholian.
Lines (3 * i) + 1 will contain a space-separated list of adjectives that describe the Xortholian's hats.
Lines (3 * i) + 2 will contain a space-separated list of adjectives the Xortholian finds distasteful.
There will be between 50 and 100 triples (inclusive). Each Xortholian will have a unique name.

Output definition

Your output should contain i lines, i.e. one line for each of the given Xortholian names.

Each line should contain a Xortholian's name, a space, and the Xortholian's new best friend's name.

Lines should be alphabetically ordered. Each Xortholian will appear twice: once in their own line as the first name, and once as a new best friend.

Example input

Aba
soft red
hard brown
Bab
hard orange
soft violet
Cen
thick yellow
quaint indigo
D'id
hard green
plaid blue
Example output

Aba Cen
Bab D'id
Cen Aba
D'id Bab__author__ = 'deepika'

"""

class Record:
    def Record(self, hate, liking):
        self.hate = hate
        self.liking = liking

if __name__=="__main__":
    lines = [line.rstrip('\r\n') for line in open('/Users/deepika/Desktop/MicrosoftExam/_4/PracticeInput.txt')]

    trueMapping = dict()

    for i in range(0, len(lines) + 1, 3):
        name = lines[i]
        hate = lines[i+1]
        liking = lines[i+2]

        trueMapping[name] = Record(hate, liking)

