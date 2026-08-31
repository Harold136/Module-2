while True:
    student_last_name = input("What is your last name ")
    if student_last_name == "ZZZ":
        break
    student_first_name = input("What is your first name ")
    gpa = input("what is your gpa ")

    value = float(gpa)

    if value >= 3.5:
        print(student_last_name, student_first_name, "you have made the deans list")
    elif value >= 3.25:
        print(student_first_name, student_last_name, "has made honoroll")
    else:
        print(student_first_name,student_last_name, "has not made either deans list or honor roll")
    
      
    