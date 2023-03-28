class Students:

    def __init__(self, name, age, grade):
        self.grade = grade
        self.name = name
        self.age = age

    def personality(self):
        if self.grade > 5:
            print("Good")
        else:
            print("Bad")


s1 = Students("surya", 21, 6)
s2 =Students("satya",22,5)
s1.personality()
print(s1.grade)
print(s1.name)


