class Student :
    def __init__(self,name ,age ,marks):
        self.name= name
        self.age  = age
        self.marks = marks


st1= Student('Ankit', 20, 100)
st2= Student('Bishal',40,15)


print (st1.name)
print (st2.age)
print (f"{st1.name} marks is {st2.marks}\n")


print (st2.name)
print (st1.age)
print (st2.marks)