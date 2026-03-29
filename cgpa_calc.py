# --- The CGPA Calculator ---
num_courses = int(input("How many courses did you take? "))
total_points = 0

# This "for" loop asks you a question for every course
for i in range(1, num_courses + 1):
    score = float(input(f"Enter score for Course {i}: "))
    total_points += score

average = total_points / num_courses

if average >= 70:
    status = "First Class"
elif average >= 60:
    status = "Second Class Upper"
elif average >= 50:
    status = "Second Class Lower"
else:
    status = "Pass/Third Class"

print("\n--- Results ---")
print(f"Average: {average:.2f}")
print(f"Status: {status}")