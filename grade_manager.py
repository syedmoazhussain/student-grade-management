def calculate_average(grades):
    return sum(grades) / len(grades)

def get_result(average):
    if average >= 85:
        return "Excellent"
    elif average >= 70:
        return "Good"
    elif average >= 50:
        return "Pass"
    else:
        return "Fail"

grades = []

print("Enter 5 student grades:")
for i in range(5):
    grade = float(input(f"Grade {i + 1}: "))
    grades.append(grade)

average = calculate_average(grades)
result = get_result(average)

print("\n--- Academic Report ---")
print(f"Average: {average:.2f}")
print(f"Result: {result}")
