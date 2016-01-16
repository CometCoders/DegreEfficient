"""The file containing the Course class"""

class Course(object):
    """Blueprint for each course."""
    def __init__(self):
        self.name = ''           # The course name.
        self.credit = 0          # The number of credit hours. 
        self.Id = 0              # Course identifier (not part of input).
        self.inDegree = 0        # The number of pre-requisites for this course. 
        self.outDegree = 0       # The number of courses for which this is a pre-req.
        self.taken = False       # Has the course been taken or not.
        self.pre_req = []
        self.pre_req_name = []
        self.notBefore = 1       # We can take this course 'not before' <semester number>. 
        
    def add_name(self, n):
        self.name = n
        
    def add_credit(self, c):
        self.credit = c

    def get_name(self):
        return self.name

    def get_credit(self):
        return self.credit

    def add_Id(self, n):
        self.Id = n

    def get_Id(self):
        return(self.Id)

    def take(self):
        self.taken = True

    def beenTaken(self):
        return self.taken

    def toString(self):
        if (len(self.name) == 2): 
            return "[ " + self.name + " ] "# + "(" + str(self.inDegree) + ", " + str(self.outDegree) + ") "
        elif (len(self.name) == 3):
            return "[" + self.name  + " ]"# + "(" + str(self.inDegree) + ", " + str(self.outDegree) + ") "
        else:
            return "[" +  self.name + "]"# + "(" + str(self.inDegree) + ", " + str(self.outDegree) + ") "

    @staticmethod
    def cmpByOutDegree(a, b):
        if (a.outDegree < b.outDegree):
            return -1
        elif (a.outDegree > b.outDegree):
            return 1
        else:
            return 0

    @staticmethod
    def cmpByCredit(a, b):
        if (a.credit < b.credit):
            return -1
        elif (a.credit > b.credit):
            return 1
        else:
            return 0
    
