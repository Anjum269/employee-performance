def assign_grade(avg):
    if avg >= 90:
        return "S"
    elif avg >= 80:
        return "A"
    elif avg >= 65:
        return "B"
    elif avg >= 50:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "F"

def main(test_mode=False):
    if test_mode:
        # Default values for Jenkins
        name = "Test Employee"
        emp_id = "EMP001"
        department = "IT"
        score1, score2, score3 = 85, 90, 80
    else:
        name = input("Enter Employee Name: ")
        emp_id = input("Enter Employee ID: ")
        department = input("Enter Department: ")
        score1 = float(input("Enter Work Efficiency Score: "))
        score2 = float(input("Enter Communication Score: "))
        score3 = float(input("Enter Task Completion Score: "))

    average = (score1 + score2 + score3) / 3
    grade = assign_grade(average)

    print("\n--- Employee Performance Report ---")
    print("Name:", name)
    print("Employee ID:", emp_id)
    print("Department:", department)
    print("Average Score:", round(average, 2))
    print("Grade:", grade)

if __name__ == "__main__":
    main(test_mode=True)   # Jenkins-safe execution
