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
max_score=max(students, key=students.get)
print (f" 😇 {students[max_score]} is the highest score and belongs to {max_score} ")
min_score=min(students, key=students.get)
print (f" ☹️ {students[min_score]} is the lowest score and belongs to {min_score} ")
while True:
 name_score=(input("Enter the name you want to know their score:"))
 if name_score == "exit" :
     break
 if name_score in students:
     print(f"{name_score}'s score is {students[name_score]}")
 else:
   print("This name is not in the list")
