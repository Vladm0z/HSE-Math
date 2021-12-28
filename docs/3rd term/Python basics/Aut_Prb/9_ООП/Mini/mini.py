class Student:
    def __init__(self, name, surname, grades=[3,4,5]):
        self.name = name
        self.surname = surname
        self.fullname = str(name) + ' ' + str(surname)
        self.grades = grades

    def greeting(self):
        return 'Hello, I am Student'

    def mean_grade(self):
        return sum(self.grades)/len(self.grades)

    def is_otlichnik(self):
        if sum(self.grades)/len(self.grades) >= 4.5:
            return 'YES'
        return 'NO'
    
    def __add__(self, other):
        return '{0} is friends with {1}'.format(self.name, other.name)
    
    def __str__(self):
        return self.fullname

class OddNumberError(Exception):
    def __init__(self, number, message='The given number is odd'):
        self.number = number
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return 'Your number is: {0} -> {1}'.format(self.number, self.message)
    
number = int(input("Enter number: "))
if not number%2 == 0:
    raise OddNumberError(number)
