# =====================================================
# PROJECT 5: SMART EMPLOYEE PAYROLL SYSTEM
# DEVELOPER: SOHAIB KHAN (AI ENGINEER)
# COMPANY: ELLAFA-TECH SOLUTIONS
# =====================================================

import datetime

# Professional Header
print("=" * 60)
print(f"{'ELLAFA-TECH SOLUTIONS - PAYROLL DEPARTMENT':^60}")
print("=" * 60)

# Employee Inputs
emp_name = input("Enter Employee Name: ")
emp_id = input("Enter Employee ID (e.g., ET-101): ")
designation = input("Enter Designation (Manager/Dev/Intern): ")
basic_salary = float(input("Enter Basic Monthly Salary: Rs "))

# Overtime Logic
overtime_hours = float(input("Enter Overtime Hours Worked: "))
hourly_rate = basic_salary / 160  # Assuming 160 working hours a month
overtime_pay = overtime_hours * hourly_rate

# Extra Pay
house_rent = basic_salary * 0.10
medical_allowance = basic_salary * 0.05

# Deductions
# income_tex
if basic_salary >= 50000:
    tax = basic_salary * 0.05
else:
    tax = basic_salary * 0.02
    
# Provident fund
provident_fund = basic_salary * 0.03

# Gross Salary
gross_salary = basic_salary + overtime_pay + overtime_hours + house_rent + medical_allowance
print(gross_salary)

# Net Selary 
net_salary = gross_salary - (tax + provident_fund)
print(net_salary)

# --- Professional Salary Slip Generation ---
print("\n" + "=" * 60)
print(f"{'OFFICIAL SALARY STATEMENT':^60}")
print("=" * 60)

# Employee Details Section
print(f"Employee Name : {emp_name:<20} | ID: {emp_id}")
print(f"Designation   : {designation:<20} | Date: {datetime.datetime.now().strftime('%Y-%m-%d')}")
print("-" * 60)

# Earnings Section
print(f"{'EARNINGS':<30} | {'AMOUNT':<20}")
print("-" * 60)
print(f"{'Basic Salary':<30} | Rs {basic_salary:,.2f}")
print(f"{'Overtime Pay':<30} | Rs {overtime_pay:,.2f}")
print(f"{'House Rent (10%)':<30} | Rs {house_rent:,.2f}")
print(f"{'Medical Allowance (5%)':<30} | Rs {medical_allowance:,.2f}")
print("-" * 60)
print(f"{'GROSS SALARY':<30} | Rs {gross_salary:,.2f}")

# Deductions Section
print("\n" + "-" * 60)
print(f"{'DEDUCTIONS':<30} | {'AMOUNT':<20}")
print("-" * 60)
print(f"{'Income Tax':<30} | Rs {tax:,.2f}")
print(f"{'Provident Fund (3%)':<30} | Rs {provident_fund:,.2f}")
print("-" * 60)

# Final Net Salary
print(f"{'NET TAKE-HOME SALARY':<30} | RS {net_salary:,.2f}")
print("=" * 60)
print(f"{'Note: This is a computer-generated document.':^60}")
print(f"{'Developed by: Sohaib Khan (AI Engineer)':^60}")
print("=" * 60)