class Person:
    def __init__ (self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def set_details(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get_details(self):
        print("Name:", str(self.name)+ "\nAge:",str(self.age)+ "\nGender:",str(self.gender))


class Student(Person):
    def __init__(self, name, age, gender, student_id, course, grades):
        super().__init__(name,age,gender)
        self.student_id = student_id
        self.course = course
        self.grades =  grades

    def set_student_details(self, student_id, course):
        self.student_id = student_id
        self.course = course
    
    def add_grade(self, grades):
        (self.grades).append(grades)
        print("New grade list for",self.name,":",self.grades)

    def calculate_average_grades(self):
        total = 0
        number = 0
        if self.grades != [""]:
            for counter in self.grades:
                total = total + int(counter)
                number = number + 1
            print(total/number)
        else:
            print(0)
    
    def get_mentor(self):
        pass

class Professor(Person):
    def __init__(self, name, age, gender, staff_id, department, salary):
        super().__init__(name,age,gender)
        self.staff_id = staff_id
        self.department = department 
        self.salary = salary

    def set_professor_details(self, staff_id, department, salary):
        self.staff_id = staff_id
        self.department = department 
        self.salary = salary

    def give_feedback(self, student, feedback):
        print("Feedback for", student.name,":",feedback)
    
    def increase_salary(self,percentage):
        self.salary = self.salary * (1+(percentage/100))
        print("New salary is for ",self.name,":", self.salary)

    def get_professor_summary(self):
        print("Name:", str(self.name)+ "\nAge:",str(self.age)+ "\nGender:",str(self.gender)+"\nStaff_id:",str(self.staff_id) +"\nDepartment:",str(self.department)+"\nSalary",str(self.salary))

    def mentor_student(self, student):
        print("Professor",self.name,"is now mentoring student",student.name,"on",student.course)

class Administrator(Person):
    def __init__(self, name, age, gender, admin_id, office, years_of_service):
        super().__init__(name,age,gender)
        self.admin_id = admin_id
        self.office = office
        self.years_of_service = years_of_service

    def set_admin_details(self, admin_id, office, years_of_service):
        self.admin_id = admin_id
        self.office = office
        self.years_of_service = years_of_service
    
    def increment_service_years(self):
        self.years_of_service = self.years_of_service + 1
        print("Years of service for",self.name,":",self.years_of_service)
    
    def get_admin_summary(self):
        print("Name:", str(self.name)+ "\nAge:",str(self.age)+ "\nGender:",str(self.gender)+"\nAdmin_id:",str(self.admin_id) +"\nOffice:",str(self.office)+"\nYears of service",str(self.years_of_service))


student1 = Student("Tom",12,"Male","123456789","Maths",[4,6,9,8,8,9])
student2 = Student("John",12,"Male","987654321","English",[1,3,4,8,8,9])

professor1 = Professor("Mike",20,"Male","0001","Maths",40000)
professor2 = Professor("Bob",20,"Male","0002","English",40000)

administrator1 = Administrator("Smith",30,"Male","246810","Room 1",10)

student1.add_grade(2)
student2.add_grade(3)
professor1.give_feedback(student1,"Well done")
professor2.give_feedback(student2,"Well done")
professor1.increase_salary(10)
professor2.increase_salary(10)
administrator1.increment_service_years()