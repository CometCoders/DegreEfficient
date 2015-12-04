from Course import Course
from Graph import Graph

ask1 = 'y'
List = []

f = open("Sample.txt", 'r')

i = 0
lines = []
for line in f:
    lines.append(line)
    i = i + 1

for j in range(0, len(lines)):
    l = lines[j]
    parts = []
    pres = []
    parts = l.split(", ")
    if(len(parts) > 2):
        pres = parts[2].split(": ")
        t = len(pres)-1
        pres[t] = pres[t].rstrip()
    else:
        pres = []
    c = Course()
    c.name = parts[0]
    c.credit = int(parts[1])
    c.Id = j
    for p in pres:
        c.pre_req_name.append(p)
    List.append(c)

for a in List:
    if(len(a.pre_req_name) > 0):
        for name in a.pre_req_name:
            for c in List:
                if(c.name == name):
                    a.pre_req.append(c)

"""
STUFF FOR DEBUGGING.
for a in List:
    print a.name, a.credit,
    for n in a.pre_req_name:
        print n,
    print "\n"
"""

    
Matrix = []

for i in range(0, len(List)):
    Matrix.append([])
    for j in range(0, len(List)):
        Matrix[i].append(0)

for a in List:
    i = a.Id
    j = 0
    for b in a.pre_req:
       j = int(b.Id)
       Matrix[i][j] = 1

"""
print("\t"), 
for a in List:
    print a.name, 
print()

MORE STUFF FOR DEBUGGING.

for a in range(0, len(List)):
    print (List[a].name + ": "),
    for b in range(0, len(List)):
        print (str(Matrix[a][b]) + "\t"),
    print "\n"
"""

graph = Graph(List, Matrix)
graph.sort()
graph.display()

        
