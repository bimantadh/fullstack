class StudentContact:
    
    mobile = None

class StudentDetail(StudentContact):

    def __init__(self):
        self.name = None 
        self.age = None
    
    def set_name(self,name):
        self.name = name

    def get_name(self):
        return self.name

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age

    def set_attributes(self,name ,age, mobile):
        self.name = name
        self.age = age
        self.mobile = mobile


class StudentMark:

    def __init__(self):
        self.math_mark = 100
        self.science_mark = 200

    def set_marks(self, math_mark, science_mark):
        self.math_mark = math_mark
        self.science_mark = science_mark

    def get_total_marks(self):
        total = self.math_mark + self.science_mark
        return total


class Student:
    @staticmethod
    def main(name, age, mobile ,math_mark, science_mark):
        sd = StudentDetail()
        sd.set_attributes(name, age, mobile)

        sm=StudentMark()
        sm.set_marks(math_mark, science_mark)

        total=sm.get_total_marks()
        print(f"""
              Name:{sd.get_name()},
              Age: {sd.get_age()},
              Mobile: {sd.mobile},
              Marks: {total} 
              """)
        
students = [
            
            {"name":'Ram', "age":20, "mobile": 9810, "math_mark": 90 , "science_mark" : 95 },
            {"name":'Ram', "age":20, "mobile": 9810, "math_mark": 90 , "science_mark" : 95 }
]
