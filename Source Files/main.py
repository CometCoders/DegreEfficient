from Course import Course
from Graph import Graph

ask1 = 'y'
List = []


"""while ask1=='y':
    name = raw_input("Enter the course name: ")
    credit = int(raw_input("Enter the credit hours: "))
    c = Course()
    c.add_name(name)
    c.add_credit(credit)
    c.Id = i
    List.append(c)
    i = i + 1
    ask1 = raw_input("Do you want to enter more? (y/n) : ")

for c in List:
    print c.get_name(), ", ", c.get_Id(), ", "

i = 0

print("Enter the pre-reqs for the following courses:\n")

for a in List:
    prereqs = raw_input(a.name + ": ")
    if (len(prereqs.split(" ")) == 1):
        for c in List:
            if (c.name == prereqs):
                a.pre_req.append(c)
    else:
        for prereq in prereqs.split(" "):
            for c in List:
                if (c.name == prereq):
                    a.pre_req.append(c)"""

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

for a in List:
    print a.name, a.credit,
    for n in a.pre_req_name:
        print n,
    print "\n"

    
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

print("\t"), 
for a in List:
    print a.name, 
print()


for a in range(0, len(List)):
    print (List[a].name + ": "),
    for b in range(0, len(List)):
        print (str(Matrix[a][b]) + "\t"),
    print "\n"

graph = Graph(List, Matrix)
graph.sort()

        
