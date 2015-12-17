"""The file to make and display the degree plan."""

from Course import Course
import sys

# Edit inDegrees of remaining courses after each semester.

class Graph:
    """The class that implements the degree's DAG."""
    def __init__(self, List, matrix):
        self.List = List                                                # List of courses.
        self.mHPS = 18                                                  # Max credit hours per semester.
        self.matrix = matrix                                            # The adjacency matrix.
        self.ListBySem = []                                             # List of courses, grouped by semester.

    def sort(self):
        """Produces a list of courses to take, grouped by semester."""
        firstZero = False                                               # We want to run at least once after the matrix has all zeros.
        while (not self.done() or not firstZero):                       # Will stop when we see the matrix full of zeros for the second time.
            if (self.done() and not firstZero):                         # Saw all zeros for the first time.
                firstZero = True                                        # So the next time won't be the first time anymore.
            canTake = []                                                # The list of courses we can take in a given semester. 
            for i in range(0, len(self.matrix)):                        # Iterate through all courses to see which ones can be taken.
                if (self.List[i].beenTaken()):                          # If course i has been taken ...
                    continue                                            # ... then look at the next one.
                canTakeThis = True                                      # Assume that course i can be taken.
                for j in range(0, len(self.matrix)):                    # Look at all the courses to see which ones are a prereq of i.
                    if (self.matrix[i][j] != 0):                        # If any of the prereqs has not been taken already ...
                        canTakeThis = False                             # ... then this one cannot be taken.
                        break                                           # No need to look at any other prereqs. 
                if (canTakeThis):                                       # If course i can be taken ...
                    canTake.append(self.List[i])                        # ... add it to the list of courses to take in this semester.
            canTake.sort(Course.cmpByOutDegree, None, False)            # Sort the list by outDegree. Take the highest ones first.
            creditHours = 0                                             # The number of credit hours to be taken in this semester.
            toBeTaken = []                                              # The list of courses to actually be taken in this semester.
            while (creditHours <= self.mHPS):                           # While we haven't exceeded the max # of credit hours we can take ...
                if (len(canTake) != 0):                                 # While we still have courses that we can possible take ...
                    course = canTake.pop()                              # Remove another course from the course list. 
                else:
                    break
                creditHours += course.credit                            # Update the number of hours.
                if (creditHours > self.mHPS):                           # If we went over ...
                    creditHours -= course.credit                        # ... take the update back ...
                    break                                               # ... and break.
                toBeTaken.append(course)                                # Else add it to the list of courses to be taken this semester.
                course.take()                               
            for j in range(0, len(toBeTaken)):                          # Now, for every course we can take in this semester ...
                for i in range (0, len(self.matrix)):                   # ... iterate through the list of courses, ...
                    self.matrix[i][toBeTaken[j].get_Id()] = 0           # ... and remove it as a prereq for each one. 
            self.ListBySem.append(toBeTaken)                            # Add this semester's courses to the bigger list.
            print("")

    def done(self):
        """Checks to see if we're done adding courses to ListBySem or not. Returns True if the matrix has all 0s."""
        for i in range(0, len(self.matrix)):
            for j in range(0, len(self.matrix)):
                if (self.matrix[i][j] != 0):
                    return False
        return True

    def display(self):
        """Displays ListBySem on the console. Primitive graphics output."""
        maxCIAS = 0                                                     # The [max]imum number of Courses In Any Semester.
        for List in self.ListBySem:                                     # Check ever semester's List in ListBySem ...
            if (len(List) > maxCIAS):                                   # ... and update the maxCIAS value.
                maxCIAS = len(List)
        graphWidth = maxCIAS * 18                                       # _[____ ____](_,_)
        semester = 1
        for List in self.ListBySem:                                     # For every semester's course list.
            print("\t   |")                                             # Blank preceding line.
            print("Semester " + str(semester) + " |"),
            blanksBWCourses = graphWidth - len(List) * 18
            blanksBWCourses /= (len(List) + 1)                          # Blanks between each course.
            for course in List:
                for i in range(0, blanksBWCourses):
                    print(""),
                print(course.toString()),
            print("\n\t   |")                                           # Blank succeeding line.
            semester += 1
        sys.stdout.write("\t   |"),
        endline = ""
        for i in range(0, graphWidth):
            endline += "_"
        print(endline)
