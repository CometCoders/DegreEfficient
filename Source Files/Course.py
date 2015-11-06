"""The class wrapping a course."""

class Course(object):
    def __init__(self):
        self.name = ''           # The course name.
        self.credit = 0          # The number of credit hours. 
        self.Id = 0              # Course identifier (not part of input).
        self.inDegree = 0        # The number of pre-requisites for this course. 
        self.outDegree = 0       # The number of courses for which this is a pre-req.
        self.taken = False       # Has the course been taken or not.
        self.pre_req = []
    
    def add_name(self, n):
        self.name = n
        
    def add_credit(self, c):
        self.credit = c

    def get_name(self):
        return(self.name)

    def get_credit(self):
        return(self.credit)

    def add_Id(self, n):
        self.Id = n

    def get_Id(self):
        return(self.Id)
    
