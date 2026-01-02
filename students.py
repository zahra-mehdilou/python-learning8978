number=int(input("Enter the number of students:"))
print("And now for each student first enter the full name and then enter the age:")
students={}
for i in range(number):
    name=input("Enter the name:")
    age=int(input(f"Enter the age of {name}: "))
    students[name]=age
print("Students' data :",students)
    
