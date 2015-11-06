from Course import Course

ask1 = 'y'
List = []
i = 0

while ask1=='y':
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
                    a.pre_req.append(c)


Matrix = [[]]

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
        

        
