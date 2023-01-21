# задание к уроку 4.3

from sys import maxsize
class Contact:

    def __init__(self, firstname = None, lastname = None, all_phones_from_homepage = None, id = None, homephone = None, mobilephone = None, workphone =None):
        self.firstname=firstname
        self.lastname=lastname
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.id = id
        self.all_phones_from_homepage = all_phones_from_homepage

    def __repr__(self):
        return "%s:%s:%s:%s" % (self.id, self.lastname, self.firstname, self.mobile)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.lastname == other.lastname and self.firstname == other.firstname and self.mobile == other.mobile

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize