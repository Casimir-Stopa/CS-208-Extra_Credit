# CS-208-Extra_Credit

This program has constructors for Python classes of students, professors, courses, classes, and majors. It also tells you what an object of that class contains using ``__str__``. I could not get any other magic methods working.

The student class take a name, ID number, year, GPA, major, advisor, and current classes.
```
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
```

The professor class take a name, department, whether or not they are tenured, whether or not they are a chair, and their advisees.
```
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
```

The course class take the name of the course, the department it's in, the course number, the prerequisites to take it, how often it is taught, and the professors who usually teach it.

```
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
```

The classes class takes the name of the class, the department it's in, the course number, the term it is being taught in, the days that there are classes, the period of the class, and the professor teaching it

```
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
```

The major class takes the name of the department, the chair of the department, the professors in the department, and the requirements to get the major
```
class major:
    def __init__(self, department, chair, profs, *requirements):
        self.department = department
        self.chair = chair
        self.profs = profs
        self.requirements = requirements
    def __str__(self):
        return(f'The major in {self.department} is chaired by the {self.chair}. The courses are taught by {self.profs}. Completing the major requires {self.requirements}')
```
Here is an example of objects you can make and the result of printing these objects
```
student1 = student("Bill", "Cypher", 133773, 'Junior', 3.55, "PS", "Steve Stove", "Important class", "Cool class", "sad class")

prof1 = professor("Steve", "Stove", "ENVS", True, False, 'Billy Bob', 'Robby Rob')

course1 = course("Intro to intros", "Study Studies" "", 101, "None", "every fall and spring", "L. Erna")

class1 = classes('The Human Mind', 'PSYCH', 150, 'Fall 2023', 'MWF', '3', 'Beather Boffmann')

major1 = major('Computer Science', 'A. Gore', 'A. Gore, C. Sharp, P. Tonn', 'CS 141', 'CS 142', 'CS 208', 'CS 220', 'CS 292', 'CS 332')
    
```
```
print(student1):
This is Bill Cypher, their ID number is 133773, they are a Junior, their GPA is 3.55, they are a(n) PS major, their advisor is Steve Stove. They are currently taking ('Important class', 'Cool class', 'sad class')

print(prof1):
This is Steve Stove, they are in the ENVS department, they are tenured, but are not a department chair, their advisee(s) is/are ('Billy Bob', 'Robby Rob')

print(course1):
Intro to intros: Study Studies 101. Prerequisites: None. Course taught every fall and spring. Classes will be taught by ('L. Erna',)

print(class1):
The Human Mind: PSYCH 150. Fall 2023. MWF 3. Beather Boffmann

print(major1):
The major in Computer Science is chaired by the A. Gore. The courses are taught by A. Gore, C. Sharp, P. Tonn. Completing the major requires ('CS 141', 'CS 142', 'CS 208', 'CS 220', 'CS 292', 'CS 332')
```

I also created a function. Since the assignment was to create classes with various magic methods, this does not seem like it will get me anything more from the assignment, but since I have it I might as well show it.

The function is called canDoHonors and checks if a student's GPA is high enough to do an honors project. If it is, then it say how far the student's GPA can drop and still do an honors project. If it is too low, then it says how high their grade needs to go up to do one.

```
honorsGPA = 3.3
def canDoHonors(GPA):
    if GPA >= honorsGPA:
        return print((f'This student has a GPA high enough to do an honors project. Their GPA cannot drop by more than {round((GPA - honorsGPA), 2)} to do one'))
    else: return print((f'This student has a GPA that is too low to do an honors project. Their GPA must rise by at least {round((GPA - honorsGPA), 2)} to do one'))
```
```   
student1 = student("Bill", "Cypher", 133773, 'Junior', 3.55, "PS", "Steve Stove", "Important class", "Cool class", "sad class")
student2 = student("Sandy", "Stove", 133773, 'Sophmore', 2.86,"ENVS", "Steve Stove", "Green Oaks")

canDoHonors(student1.GPA):
This student has a GPA high enough to do an honors project. Their GPA cannot drop by more than 0.25 to do one

canDoHonors(student2.GPA):
This student has a GPA that is too low to do an honors project. Their GPA must rise by at least -0.44 to do one
```

To do something like this using magic methods as asked, I belieive I would need to using magic methods like ``__gt__`` and compare a given student's GPA to the GPA needed to do an honors project. What I do not understand is how to tell the method to look at the GPA part of the student object, and what you would need to give the method in order to give the desired output. Same goes for other magic methods I tried to impement like adding a class to a student's current schedule using ``__add__``. 
