# --------------------------------------№1--------------------------------------#
time_in_seconds = int(input("Enter the time in seconds: "))
hours = time_in_seconds // 3600
minutes = (time_in_seconds // 60) - (hours * 60)
seconds = (time_in_seconds % 60)
print(f"{hours:02}:{minutes:02}:{seconds:02}")
# --------------------------------------№2--------------------------------------#
n = input("Enter the number: ")
total = 0
for i in range(1, 4):
    total += int(n * i)

print(total)
# --------------------------------------№3--------------------------------------#
num_init = int(input("Enter the positive integer: "))
max_number = 0
num = num_init
while num_init > 0:
    last_number = num_init % 10
    if last_number > max_number:
        max_number = last_number
        if max_number == 9:
            break
    num_init //= 10

print(max_number)

def num_max(num):
    if num < 10:
        return num
    else:
        m = num_max(num // 10)
        return m if m > num % 10 else num % 10
print(num_max(1293))

# --------------------------------------№4--------------------------------------#
firm_revenue = int(input("Enter firm revenue: "))
company_costs = int(input("Enter company costs: "))
firm_result = firm_revenue - company_costs
print(firm_result)
if firm_result < 0:
    print("The company worked at a loss")
else:
    print("The company worked in profit!")
    profitability_of_proceeds = firm_result / firm_revenue
    print(f"Profit margin was {profitability_of_proceeds:.2f}")
    number_of_employees = int(input("Enter number of employees: "))
    profit_per_employee = firm_result / number_of_employees
    print(f"Firm profit in per employee was {profit_per_employee:.2f}")
# --------------------------------------№5--------------------------------------#
a = int(input("Enter the result of the first day: "))
b = int(input("Enter the result you want to achieve: "))
total = a
days = 1
while total < b:
    total += total * 0.1
    days += 1
print(days)
print(f"{total:.2f}")

