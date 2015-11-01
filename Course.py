class Course(object):
    name = ''
    credit = 0
    Id = 0
    inDegree = 0
    outDegree = 0

    def add_name(self, n):
        self.name = n
    def add_credit(self, c):
        self.credit = c
    def get_name(self):
        return(self.name)
    def get_credit(self):
        return(self.credit)


c = Course()
print c.Id
d = Course()
print d.Id
