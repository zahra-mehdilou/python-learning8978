number=int(input("Enter the number of students:"))
print("And now for each student first enter the full name and then enter the score:")
students={}
for i in range(number):
    name=input("Enter the name:")
    score=int(input(f"Enter the score of {name}: "))
    while 0>score or score>20 :
        print("The score is not valid!")
        score=int(input(f"Enter the valid score of {name}: "))
    students[name]=score
print(students)
while True:
 name_score=(input("Enter the name you want to know their score:"))
 if name_score == "exit" :
     break
 if name_score in students:
     print(f"{name_score}'s score is {students[name_score]}")
 else:
   print("This name is not in the list")
