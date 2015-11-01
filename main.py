from Course import Course

ask = 'y'
c = Course()
List = []
i = 0

while ask=='y':
    name = raw_input("Enter the course name: ")
    credit = int(raw_input("Enter the credit hours: "))
    c.add_name(name)
    c.add_credit(credit)
    List.append(c)
    i = i + 1
    ask = raw_input("Do you want to enter more? (y/n) : ")

for j in range (0,i):
    print List[j].get_name(), ", ", List[j].get_credit(), ", ",j
