def mark_grade(mark):
    if 100 >= mark >= 90:
        return ("A+")
    elif 90 >= mark >= 80:
        return ("A")
    elif 80 >= mark >= 70:
        return ("B+")
    elif 70 >= mark >= 60:
        return ("B")
    elif 60 >= mark >= 50:
        return ("C+")
    else:
        return ("No Grade")

mark = int(input("Enter Marks: "))
           
if mark > 50:
    print (f"Congrats! Passed with a score of {mark} and grade: {mark_grade(mark)}")
else:
    print (f"Failed! score: {mark} and grade: {mark_grade(mark)}")
    
