"""The file to make and display the degree plan."""

from Course import Course

import numpy

class Graph:
    """The class that implements the degree's DAG."""
    def __init__(self):
        self.List = []                             # List of courses.
        self.mHPS = 18                             # Max credit hours per semester.
        self.matrix                                # The adjacency matrix (Will be a numpy matrix).
    def sort(self):
        minInDegree = 100                          # No courses have 100s of prereqs. 
        for course in self.List:
            curInDegree = 0                        # The in-degree of the course we're looking at.
            for j in range(0, len(self.List)):
                curInDegree += self.matrix[course.id][j]
            if (curInDegree < minInDegree):
                minInDegree = curInDegree
        assert minInDegree == 0, "Invalid plan!"  # This graph is not a DAG if this assertion fails.
        canTake = []                               # The list of courses one can take this semester.
        for course in self.List:
            curInDegree = 0
            for j in range(0, len(self.List)):
                curInDegree += self.matrix[course.id][j]
            if (curInDegree == minInDegree):
                canTake.append(course)             # If the course has minInDegree, then add it to the list.
        for course in canTake:                    # Calculate the out-degree for every course.
            curOutDegree = 0
            for i in range(0, len(canTake)):
                curOutDegree += self.matrix[i][course.id]
            course.outDegree = curOutDegree        
        canTake.sort(key = lambda course: -course.outDegree)  # Sort the list of available courses by outDegree (descending order).
        # NOTE: THIS METHOD IS INCOMPLETE AS OF YET.
        
                
                    
                
        
        