# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
        
#     def get_descriptive_name(self):

#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model

#         return long_name.title()

# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())        


# class Employee:
#     def __init__(self,name , surname , gender , date_birth ):
#         self.name = name
#         self.surname = surname
#         self.gender = gender
#         self.date_birth = date_birth


#     def __str__(self):
#         return f'{self.name} {self.surname} {self.gender} {self.date_birth}'

# empl = Employee("sadyr","japarov", "male", "5 mart")
# empl2 = Employee("sadyrov","japar", "male", "10 mart")

# print(empl)
# print(empl2)




class Human:
    def __init__(self, name, age, favorite_lesson):
        self.name = name
        self.age = age
        self.favorite_lesson = favorite_lesson
    def __str__(self):
        return f'{self.name} {self.age}'

 
class Teacher(Human):
    def __init__(self, name , age , favorite_lesson , salary ,speciality, ):
        self.salary = salary
        self.speciality = speciality
        super().__init__(name, age, favorite_lesson)
    def __str__(self):
        return f' {self.name} {self.age} {self.speciality} {self.salary}'


class Student(Human):
    def __init__(self , name , age , favorite_lesson , grade):
        self.grade = grade
        super().__init__(name, age, favorite_lesson)
    def __str__(self):
     return f'{self.name} {self.age} {self.favorite_lesson} {self.grade}'

salam = Human('MUKHAMED ' ,30, 'Matic')
aleikum = Teacher('MUKHAMED' , 30 , 'Matic' 'Man' , 25000 , 'Teacher')
salami = Student('MUKHAMED',30, 'Matic', 5)

print(salam)
print(aleikum)
print(salami)