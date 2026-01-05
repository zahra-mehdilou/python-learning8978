number=int(input("Enter the number of students:"))
print("And now for each student first enter the full name and then enter the score:")
students={}
for i in range(number):
    name=input("Enter the name: ")
    char_length=len(name)
    while char_length<3 or char_length>30:
        print("❗️Your entered name is not valid! The number of characters should be between 3 and 30!")
        name=input("Enter a valid name: ")
        char_length=len(name)
    score=float(input(f"Enter the score of {name}: "))
    while score<0 or score>20 :
        print("❗️The score is not valid!")
        score=float(input(f"Enter the valid score of {name}: "))
    students[name]=score 
first=True
for name,score in students.items():
    if first==True:
        max_score=score
        max_name=name
        min_score=score
        min_name=name
        first=False
    else:
        if max_score<=score:
           max_score=score
           max_name=name
        if min_score>=score:
           min_score=score
           min_name=name
print(students)
print(f"😍 The highest score is {max_score} and belongs to {max_name} ")
print(f"😒 The lowest score is {min_score} and belongs to {min_name} ")
while True:
 name_score=(input("Enter the name you want to know their score:"))
 if name_score == "exit" :
     break
 if name_score in students:
     print(f"{name_score}'s score is {students[name_score]}")
 else:
   print("This name is not in the list")


