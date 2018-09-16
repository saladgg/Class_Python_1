from Student import StudentClass
from Car import CarClass

student1 = StudentClass("Sario", "ENG", 2.80)
student2 = StudentClass("Mario", "CT", 3.02)
student3 = StudentClass("Sara", "CS", 4.30)

car1 = CarClass("Toyota", 2015, 3000000)
car2 = CarClass("Mercedez", 2018, 5000000)


print("-----------STUDENT CLASS DATA----------")
print("Is student1 on honor roll? "+str(student1.is_on_honor_roll()))
student1.student_info()
student2.student_info()
student3.student_info()


print("-----------CAR CLASS DATA----------")
print("Price of %s is: %s" %(car1.make, car1.price))
print(car1.car_info())
print(car2.car_info())

