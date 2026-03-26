#Student Grading System

name = input("please, enter your name: ").lower()
grade = int(input("please, enter your grade (1, 2 o 3): "))

#ask for notes 
note_1 = float(input("enter your note_1: "))
note_2 = float(input("enter your note_2: "))
note_3 = float(input("enter your note_3: "))

#calculate average
average = (note_1 + note_2 + note_3)/3

#evaluate status
if average >= 3:
    status =  "approved"

else:
    status = "reproved"

#show report
print("\n--- student report ---")
print("name:" , name)
print("grade:" , grade)
print("average:" , round (average, 2))
print("status:" , status)

