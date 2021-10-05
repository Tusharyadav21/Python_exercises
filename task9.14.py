# To input basic salary of an employee and calculate its Gross salary according to following:
base_salary = float(input("Enter the Basic salary : "))
print("Basic Salary : ",base_salary)

if(base_salary<=10000):
    HRA = 0.20*base_salary
    DA = 0.80*base_salary
    gross = base_salary+HRA+DA
elif(base_salary<=20000):
    HRA = 0.25 * base_salary
    DA = 0.90 * base_salary
    gross = base_salary + HRA + DA
else:
    HRA = 0.30 * base_salary
    DA = 0.95 * base_salary
    gross = base_salary + HRA + DA

print("HRA :",HRA)
print("DA :",DA)
print("Gross Salary :",gross)