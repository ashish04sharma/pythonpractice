# Simple interest and compound interest

principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest (% per year): "))
time = float(input("Enter time (years): "))

simple_interest = (principal * rate * time) / 100
amount = principal * (1 + rate / 100) ** time
compound_interest = amount - principal

print("Simple Interest:", round(simple_interest, 2))
print("Compound Interest:", round(compound_interest, 2))
