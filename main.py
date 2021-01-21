salary = int(input("Enter annual salary pay:"))
raise_p = int(input("Enter pay raise percentage:"))
years = int(input("Enter duration of years:"))

raise_p = raise_p / 100 + 1

while years > 0:
    new_salary = salary * raise_p
    years -= 1
    salary = new_salary
    print(new_salary)