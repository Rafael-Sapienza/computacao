user_input = 'abc'

# List of variable names
variable_names = ['var1', 'var2', 'var3', 'var4', 'var50']

# Create separate variables and set them to the value 3
for var_name in variable_names:
    globals()[var_name] = 3

# Accessing the values
for var_name in variable_names:
    print(f"{var_name}: {globals()[var_name]}")

globals()['var1'] = 2

print(globals()['var1'])