"""The class wrapping a course."""

class Course(object):
    """Attributes of a course."""
    name = ""           # The course name.
    credit = 0          # The number of credit hours. 
    Id = 0              # Course identifier (not part of input).
    inDegree = 0        # The number of pre-requisites for this course. 
    outDegree = 0       # The number of courses for which this is a pre-req.
    taken = False       # Has the course been taken or not.