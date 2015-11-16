"""The file to make and display the degree plan."""

from Course import Course

class Graph:
    """The class that implements the degree's DAG."""
    def __init__(self, List, matrix):
        self.List = List                                    # List of courses.
        self.mHPS = 18                                      # Max credit hours per semester.
        self.matrix = matrix                                # The adjacency matrix.
        self.ListBySem = []                                 # List of courses, grouped by semester.

    def sort(self):
        """Produces a list of courses to take, grouped by semester."""
        # Only barebones topological sort for now. No support for max hours.
        firstZero = False                                   # We want to run at least once after the matrix has all zeros.
        while (not self.done() or not firstZero):           # Will stop when we see the matrix full of zeros for the second time.
            if (self.done() and not firstZero):             # Saw all zeros for the first time.
                firstZero = True                            # So the next time won't be the first time anymore.
            canTake = []                                    # The list of courses we can take in a given semester. 
            for i in range(0, len(self.matrix)):            # Iterate through all courses to see which ones can be taken.
                if (self.List[i].beenTaken()):              # If course i has been taken ...
                    continue                                # ... then look at the next one.
                print self.List[i].get_name(), ' can be taken - ',  # For debugging.
                canTakeThis = True                          # Assume that course i can be taken.
                for j in range(0, len(self.matrix)):        # Look at all the courses to see which ones are a prereq of i.
                    if (self.matrix[i][j] != 0):            # If any of the prereqs has not been taken already ...
                        canTakeThis = False                 # ... then this one cannot be taken.
                        break                               # No need to look at any other prereqs. 
                print(canTakeThis),                                 # For debugging.
                x = int(raw_input("Press 1 to continue: "))         # For debugging.
                if (canTakeThis):                           # If course i can be taken ...
                    self.List[i].take()                     # ... then take it ...
                    canTake.append(self.List[i])            # ... and add it to the list of courses to take in this semester.
            for j in range(0, len(canTake)):                # Now, for every course we can take in this semester ...
                for i in range (0, len(self.matrix)):       # ... iterate through the list of courses, ...
                    self.matrix[i][canTake[j].get_Id()] = 0 # ... and remove it as a prereq for each one. 
            self.ListBySem.append(canTake)                  # Add this semester's courses to the bigger list. 
        for i in range(0, len(self.ListBySem)):             # For 
            for j in range(0, len(self.ListBySem[i])):      # Debugging
                print(self.ListBySem[i][j].get_name()),     # (---)
            print("")

    def done(self):
        """Checks to see if we're done adding courses to ListBySem or not. Returns True if the matrix has all 0s."""
        print(self.matrix)
        print(len(self.matrix))
        for i in range(0, len(self.matrix)):
            for j in range(0, len(self.matrix)):
                if (self.matrix[i][j] != 0):
                    return False
        return True
                        
        
        
