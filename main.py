print("This line will be printed.")
x = 1
if x == 1:
    # indented four spaces
    print("x is 1.")

# Create a variable savings
savings = 100

# Create a variable growth_multiplier
growth_multiplier = 1.1

# years
# years = input("Over how many years? ")
years = 7

# Calculate result
result = float(savings) * float(growth_multiplier) ** float(years)

# Print out result
print(result)

x = ["a", "b", "c", "d"]
print(x)
x[1] = "r"
print(x)
x[2:] = ["s", "t"]
print(x)