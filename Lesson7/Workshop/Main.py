from Lesson7.Workshop.Athlete import Athlete
from Lesson7.Workshop.Student import Student
from Lesson7.Workshop.StudentAthlete import StudentAthlete


# Polymorphism
def introduce_person(person):
    person.introduce()


s = Student("Anna")
a = Athlete("Anna")
sa = StudentAthlete("Mike")

s.introduce()
a.introduce()
sa.introduce()

print()
print()

introduce_person(s)
introduce_person(a)
introduce_person(sa)