import datetime
import calendar

# === CONFIG ===
BASE_SALARY = 5_800_000
MEAL_ALLOWANCE = 650_000
PARKING_ALLOWANCE = 150_000

# === DETERMINE WORK DAYS ===
current_date = datetime.datetime.now()
current_month = current_date.month
current_year = current_date.year
days_in_month = calendar.monthrange(current_year, current_month)[1]

# Quy tắc: tháng có 31 ngày → 27 công, còn lại → 26 công
standard_work_days = 27 if days_in_month == 31 else 26

# === INPUT OVERTIME ===
overtime_hours = float(input("Enter overtime hours: "))

# === SALARY CALCULATIONS ===
hourly_rate = BASE_SALARY / (standard_work_days * 8)
overtime_salary = overtime_hours * hourly_rate * 1.3
base_salary_excluding_ot = 8 * (standard_work_days - overtime_hours / 8) * hourly_rate

print(f"Hourly Rate: {hourly_rate:,.0f}")
print(f"Base Salary (without OT): {base_salary_excluding_ot:,.0f}")
print(f"Overtime Salary: {overtime_salary:,.0f}")

# === ALLOWANCES ===
actual_meal_allowance = (MEAL_ALLOWANCE // 26) * standard_work_days
print(f"Meal Allowance: {actual_meal_allowance:,.0f}")

# === TOTAL SALARY ===
total_salary = base_salary_excluding_ot + overtime_salary + actual_meal_allowance + PARKING_ALLOWANCE
print(f"Total Salary: {total_salary:,.0f}")

# === DEDUCTIONS ===
social_insurance = BASE_SALARY * 0.08
health_insurance = BASE_SALARY * 0.015
unemployment_insurance = BASE_SALARY * 0.01

total_deductions = social_insurance + health_insurance + unemployment_insurance
net_salary = total_salary - total_deductions

# === RESULT ===
print(f"Net Salary: {net_salary:,.0f}")
