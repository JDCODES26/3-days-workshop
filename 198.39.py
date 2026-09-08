hours = float(input("Enter hours worked: "))
rate = float(input("Enter hourly rate: "))

if hours > 40:
    regular_salary = 40 * rate
    overtime = hours - 40
    overtime_salary = overtime * rate * 1.5
    salary = regular_salary + overtime_salary
else:
    salary = hours * rate

print("Salary =", salary)