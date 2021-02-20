__author__ = 'deepika'

class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        contacts = []
        for item in accounts:
            contacts.append(item[0])

        by_email = dict(lambda: [])
        for item in accounts:


