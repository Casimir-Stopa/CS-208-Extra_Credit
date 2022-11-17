#Write a series of Python classes to model students, professors, course, classes, and majors.
#Implement as many of the magic methods as make sense for your model.
#Submit a git repo with a readme describing how to use your classes.
#I will leave the specifics up to you but you should implement things like
#add/drop class, get_advisor/advisee, course requirements, major requirements.
#Note that a class is a specific term offering of a course which is a more general description.
# The standard for 10% extra credit would be a barebones model with a readme ~100-150 lines of code.
#20% would include a full demo and documentation ~500+ lines of code.


class student:
    def __init__(self, firstName, lastName, IDnum, year, GPA, major, advisor, *currClasses):
        self.name = firstName + " " + lastName
        self.IDnum = IDnum
        self.year = year
        self.GPA = GPA
        self.major = major
        self.advisor = advisor
        self.currClasses = currClasses

    def __str__(self):
        return(f'This is {self.name}, their ID number is {self.IDnum}, they are a {self.year}, their GPA is {self.GPA}, they are a(n) {self.major} major, their advisor is {self.advisor}. They are currently taking {self.currClasses}')


class professor:
    def __init__(self, firstName, lastName, department, istenured, ischair, *advisees):
        self.name = firstName + " " + lastName
        self.department = department
        self.istenured = istenured
        self.ischair = ischair
        self.advisees = advisees
    def __str__(self):
        if self.istenured == True and self.ischair == True:
            return(f'This is {self.name}, they are in the {self.department} department, they are tenured, and are a department chair, their advisee(s) is/are {self.advisees}')
        if self.istenured == True and self.ischair == False:
            return(f'This is {self.name}, they are in the {self.department} department, they are tenured, but are not a department chair, their advisee(s) is/are {self.advisees}')
        else:
            return(f'This is {self.name}, they are in the {self.department} department, they are not tenured, their advisee(s) is/are {self.advisees}')


class course:
    def __init__(self, name, department, number, prerequisites, frequency, *profs):
        self.name = name
        self.department = department
        self.number = number
        self.prerequisites = prerequisites
        self.frquency = frequency
        self.profs = profs
    def __str__(self):
        return(f'{self.name}: {self.department} {self.number}. Prerequisites: {self.prerequisites}. Course taught {self.frquency}. Classes will be taught by {self.profs}')

class classes:
    def __init__(self, name, department, number, term, days, period, prof):
        self.name = name
        self.department = department
        self.number = number
        self.term = term
        self.days = days
        self.period = period
        self.prof = prof
    def __str__(self):
        return(f'{self.name}: {self.department} {self.number}. {self.term}. {self.days} {self.period}. {self.prof}')

class major:
    def __init__(self, department, chair, profs, *requirements):
        self.department = department
        self.chair = chair
        self.profs = profs
        self.requirements = requirements
    def __str__(self):
        return(f'The major in {self.department} is chaired by the {self.chair}. The courses are taught by {self.profs}. Completing the major requires {self.requirements}')

honorsGPA = 3.3
def canDoHonors(GPA):
    if GPA >= honorsGPA:
        return print((f'This student has a GPA high enough to do an honors project. Their GPA cannot drop by more than {round((GPA - honorsGPA), 2)} to do one'))
    else: return print((f'This student has a GPA that is too low to do an honors project. Their GPA must rise by at least {round((GPA - honorsGPA), 2)} to do one'))



student1 = student("Bill", "Cypher", 133773, 'Junior', 3.55, "PS", "Steve Stove", "Important class", "Cool class", "sad class")
student2 = student("Sandy", "Stove", 133773, 'Sophmore', 2.86,"ENVS", "Steve Stove", "Green Oaks")

prof1 = professor("Steve", "Stove", "ENVS", True, False, 'Billy Bob', 'Robby Rob')

course1 = course("Intro to intros", "Study Studies" "", 101, "None", "every fall and spring", "L. Erna")

class1 = classes('The Human Mind', 'PSYCH', 150, 'Fall 2023', 'MWF', '3', 'Beather Boffmann')

major1 = major('Computer Science', 'A. Gore', 'A. Gore, C. Sharp, P. Tonn', 'CS 141', 'CS 142', 'CS 208', 'CS 220', 'CS 292', 'CS 332')
    
print(student1)
print(prof1)
print(course1)
print(class1)
print(major1)
canDoHonors(student1.GPA)
canDoHonors(student2.GPA)
