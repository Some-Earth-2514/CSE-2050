"""
p1 = Person('jake', 'jas14034')
p1.name
'jake'
p1.netid
'jas14034'
print(p1)
"Person: 'jake', 'jas14034'"
"""


class Person:
    def __init__(self, name, netid):
        self.name = name
        self.netid = netid

    def __repr__(self):
        return f"Person: {self.name}, {self.netid}"


# inheritance implementation
class Employee(Person):
    def __init__(self, name, netid, office):
        # method 1 (Second best, gets harder to maintain)
        Person.__init__(self, name, netid)
        self.office = office

        # method 2 (THE BEST way, although it gets complicated real fast)
        super().__init__(self, name, netid, office)
        self.office = office

        # method 3 (THE WORST way, copy-pasting code is bad, don't reuse code within files)
        self.name = name
        self.netid = netid
        self.office = office

    def assign_office(self, office):
        self.office = office
