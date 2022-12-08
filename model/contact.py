# задание к уроку 4.3

from sys import maxsize
class Contact:

    def __init__(self, firstname: object = None, lastname: object = None, mobile: object = None, id: object = None) -> object:
        self.firstname=firstname
        self.lastname=lastname
        self.mobile=mobile
        self.id = id

    def __repr__(self):
        return "%s:%s:%s:%s" % (self.id, self.lastname, self.firstname, self.mobile)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.lastname == other.lastname and self.firstname == other.firstname and self.mobile == other.mobile

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize