"""The file to make and display the degree plan."""

from Course import Course

class Graph:
    """The class that implements the degree's DAG."""
    def __init__(self, List, matrix):
        self.List = List                            # List of courses.
        self.mHPS = 18                              # Max credit hours per semester.
        self.matrix = matrix                        # The adjacency matrix.
        self.ListBySem = []                         # List of courses, grouped by semester.

    def sort(self):
        """Produces a list of courses to take, grouped by semester."""
        # Only barebones topological sort for now. No support for max hours.
        firstZero = False                           # We want to run at least once after the matrix has all zeros.
        while (not self.done() or not firstZero):
            if (self.done() and not firstZero):
                firstZero = True
            canTake = []
            for i in range(0, len(self.matrix)):
                if (self.List[i].beenTaken()):
                    continue
                print self.List[i].get_name(), ' can be taken - ', 
                canTakeThis = True
                for j in range(0, len(self.matrix)):
                    if (self.matrix[i][j] != 0):
                        canTakeThis = False
                        break
                print(canTakeThis), 
                x = int(raw_input("Press 1 to continue: "))
                if (canTakeThis):
                    self.List[i].take()             
                    canTake.append(self.List[i])
            for j in range(0, len(canTake)):
                for i in range (0, len(self.matrix)):
                    self.matrix[i][canTake[j].get_Id()] = 0
            self.ListBySem.append(canTake)
        for i in range(0, len(self.ListBySem)):
            for j in range(0, len(self.ListBySem[j])):
                print(self.ListBySem[i][j].get_name())

    def done(self):
        """Checks to see if we're done adding courses to ListBySem or not."""
        print(self.matrix)
        print(len(self.matrix))
        for i in range(0, len(self.matrix)):
            for j in range(0, len(self.matrix)):
                if (self.matrix[i][j] != 0):
                    return False
        return True
                        
        
        
