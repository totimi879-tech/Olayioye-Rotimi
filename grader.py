name = input("Enter Student Name: ")
math = float(input("Enter Math score: "))
english = float(input("Enter English score: "))
science = float(input("Enter Science score: "))

total = math + english + science
average = total / 3

if average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

print("\n--- Student Result ---")
print(f"Name: {name}")
print(f"Average Score: {average:.2f}")
print(f"Final Grade: {grade}")